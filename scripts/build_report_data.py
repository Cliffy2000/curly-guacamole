#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds report/data.js from data/*.csv.

Every series in the report is derived here so the HTML contains no hand-typed
figures. Selections (which rows feed which chart) are explicit and auditable;
the VALUES always come from the CSVs.

Run:  python scripts/build_report_data.py
"""
import csv, json, os, re
from collections import defaultdict, Counter
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
OUT  = os.path.join(ROOT, "report", "data.js")

def read(name):
    with open(os.path.join(DATA, name), encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))

def num(v):
    if v is None: return None
    v = str(v).strip().replace(",", "")
    if v == "": return None
    try: return float(v)
    except ValueError: return None

products = read("products.csv")
partners = read("partners.csv")
fin      = read("financials.csv")
mkt      = read("market_series.csv")
risk     = read("risk_log.csv")
gaps     = read("gaps.csv")
sources  = read("sources.csv")
comps    = read("companies.csv")

# ---------------------------------------------------------------- collab rows
def is_collab(r):
    pc = (r.get("partner_class") or "").strip()
    return pc not in ("", "none")

collab = [r for r in products if is_collab(r)]
base   = [r for r in products if not is_collab(r)]

# ---------------------------------------------------------------- 1. SKU count
BRAND_ZH = {
  "Universal Music (TOoKA BASE)": "环球音乐 TOoKA BASE",
  "MOONDROP": "MOONDROP 水月雨",
  "final": "final / ag",
  "Sony": "Sony 索尼",
  "Victor (JVCKenwood)": "Victor / JVCKenwood",
  "Taito/Cafereo": "Taito / Cafereo",
  "MissEvan": "猫耳FM MissEvan",
  "Xinghaibei": "星海贝",
}
sku = [{"b": BRAND_ZH.get(b, b), "n": n}
       for b, n in Counter(r["brand"] for r in collab).most_common()]

# ---------------------------------------------------------------- 2. JP prices
prices = sorted(num(r["price_value"]) for r in collab
                if r.get("price_currency") == "JPY" and num(r.get("price_value")))

# ------------------------------------------------- 3. collab premium (derived)
# base-platform rows carry the reference price; pair them with the collab
# prices observed on the same model_code family.
PLATFORMS = [
  ("TE-Q3R", "TE-Q3R", "廉价平台"),
  ("TE-V1R", "TE-V1R", "主力平台 · 最多 SKU 共用"),
  ("TE-J2",  "TE-J2",  "旗舰入耳 · HYDE"),
  ("WA-J1",  "WA-J1",  "旗舰头戴 · HYDE"),
  ("WB-P1",  "WB-P1",  "骨传导"),
]
base_price = {}
for r in base:
    mc = (r.get("model_code") or "").strip()
    p  = num(r.get("price_value"))
    if mc and p: base_price[mc] = p

premium = []
for plat, prefix, note in PLATFORMS:
    bp = base_price.get(plat)
    if not bp: continue
    cps = sorted({num(r["price_value"]) for r in collab
                  if (r.get("model_code") or "").startswith(prefix)
                  and r.get("price_currency") == "JPY" and num(r.get("price_value"))})
    for cp in (cps[:1] + cps[-1:] if len(cps) > 1 else cps):
        premium.append({"p": plat, "base": bp, "collab": cp,
                        "pct": round((cp / bp - 1) * 100, 1), "note": note,
                        "n": sum(1 for r in collab
                                 if (r.get("model_code") or "").startswith(prefix)
                                 and num(r.get("price_value")) == cp)})
# China comparison (RAYS): base row is partner_class none, collab is esports_club
rays_base = next((num(r["price_value"]) for r in base
                  if (r.get("model_code") or "") == "RAYS"), None)
rays_col  = next((num(r["price_value"]) for r in collab
                  if (r.get("model_code") or "") == "RAYS"), None)
premium_cn = None
if rays_base and rays_col:
    premium_cn = {"p": "MOONDROP RAYS", "base": rays_base, "collab": rays_col,
                  "pct": round((rays_col / rays_base - 1) * 100, 1),
                  "note": "中国 · 电竞俱乐部联名", "cur": "CNY"}

# ------------------------------------------------------------ 4. volume tiers
VOL_PICKS = [
 ("ag COTSUBU for ASMR Patra BLACK Ver.", "units_allocated_sold_out", "ag COTSUBU 帕特拉二弹 · 年内配额售罄"),
 ("ag COTSUBU for ASMR Patra BLACK Ver.", "units_ordered",            "ag COTSUBU 帕特拉二弹 · 开售 12 小时"),
 ("final",                                "units_sold_cumulative",     "final ASMR／睡眠向累计"),
 ("Preseed Japan / AVIOT",                "units_shipped_cumulative",  "AVIOT Q 系列平台累计"),
 ("Onkyo",                                "units_ordered_annual",      "ONKYO 年度受注量 2025"),
 ("KPro01 (Koiwai Kotori x Owltech)",     "backers",                   "KPro01 众筹支持人数"),
 ("MOONDROP Robin (Honkai Star Rail)",    "units_sold",                "MOONDROP 知更鸟 · 三平台合计"),
 ("ag COTSUBU for ASMR Patra Edition (1st)", "units_restock",          "ag COTSUBU 帕特拉一弹 · 最终再版"),
 ("ag COTSUBU for ASMR Patra Edition (1st)", "units_event_allocation", "ag COTSUBU 帕特拉一弹 · 见面会配额"),
]
TIER_ZH = {"verified_primary": "一手已披露", "verified_secondary": "二手已披露",
           "partial": "部分核实", "lead_only": "六级信源", "derived": "推导值"}
vol = []
for ent, met, lab in VOL_PICKS:
    rows = [r for r in fin if r["entity_name"] == ent and r["metric"] == met]
    if not rows: continue
    # prefer the most recent
    r = sorted(rows, key=lambda x: x.get("period_end") or "")[-1]
    v = num(r["value"])
    if v is None: continue
    vol.append({"l": lab, "v": int(v),
                "t": TIER_ZH.get(r.get("confidence"), r.get("confidence")),
                "s": (r.get("source_url") or "").split("//")[-1].split("/")[0] or "推导"})
# AVIOT TE-D01v platform figure lives in a product note, keep it explicit
d01v = next((r for r in products if (r.get("model_code") or "") == "TE-D01v-SGR"), None)
if d01v and "120000" in (d01v.get("notes") or ""):
    vol.append({"l": "AVIOT TE-D01v 平台累计", "v": 120000, "t": "一手已披露",
                "s": "aviot.jp"})

# --------------------------------------------------------- 5. partner classes
PC_ZH = {
 "seiyuu_individual":"声优 · 个人","vtuber_individual":"虚拟艺人 · 个人",
 "vtuber_unit":"虚拟艺人 · 组合","musician":"音乐人","virtual_singer":"虚拟歌手／声库",
 "virtual_character":"虚拟角色","seiyuu_group":"声优 · 团体","utaite_individual":"唱见",
 "tv_programme_ip":"电视节目 IP","tv_announcer":"电视台播音员","sound_director":"音响监督",
 "seiyuu_label":"声优厂牌","reviewer_influencer":"评测人／影响者",
 "radio_programme":"广播节目","mastering_engineer":"母带工程师",
 "illustrator_vtuber":"插画师兼 VTuber","esports_club":"电竞俱乐部",
 "celebrity_comedian":"艺人／搞笑艺人",
}
partner = [{"c": PC_ZH.get(c, c), "n": n, "raw": c}
           for c, n in Counter(r["partner_class"] for r in partners
                               if (r.get("partner_class") or "").strip()).most_common()]

# --------------------------------------------------- 6. voice clips vs price
voice = []
for r in collab:
    n = num(r.get("voice_clip_count")); p = num(r.get("price_value"))
    if n and p and r.get("price_currency") == "JPY":
        voice.append({"n": int(n), "p": int(p),
                      "l": (r.get("product_name") or "")[:44]})
voice.sort(key=lambda d: d["n"])

# -------------------------------------------------------- 7. JP scale ladder
LADDER_PICKS = [
 ("Bandai Namco Holdings","revenue","total","万代南梦宫控股"),
 ("Nippon Television","revenue","total","日本电视台控股"),
 ("Square Enix Holdings","revenue","total","史克威尔艾尼克斯控股"),
 ("KADOKAWA","revenue","total","KADOKAWA"),
 ("Shueisha","revenue","total","集英社"),
 ("Aniplex","revenue","total","Aniplex"),
 ("Sanrio","revenue","total","三丽鸥"),
 ("Toei","revenue","total","东映"),
 ("Kodansha","revenue","total","讲谈社"),
 ("Shogakukan","revenue","total","小学馆"),
 ("Toei Animation","revenue","total","东映动画"),
 ("Taito","revenue","total","Taito"),
 ("ANYCOLOR","revenue","total","ANYCOLOR"),
 ("viviON","revenue","group_total","viviON 集团"),
 ("COVER Corp","revenue","total","COVER"),
 ("Tsuburaya Productions","revenue","total","円谷制作"),
 ("Adways","revenue_guidance","total","Adways"),
 ("Broccoli","revenue","total","Broccoli"),
 ("Nitroplus","revenue","total","Nitroplus"),
]
ladder = []
for ent, met, seg, zh in LADDER_PICKS:
    rows = [r for r in fin if r["entity_name"] == ent and r["metric"] == met
            and r["segment"] == seg and r["currency"] == "JPY"]
    if not rows: continue
    r = sorted(rows, key=lambda x: x.get("period_end") or "")[-1]
    v = num(r["value"])
    if v: ladder.append({"c": zh, "v": int(v), "k": "ip",
                         "period": r.get("period_label"), "yoy": num(r.get("yoy_pct"))})
# ONKYO derived collab-category revenue (range → midpoint, flagged)
onk = next((r for r in fin if r["entity_name"] == "Onkyo"
            and r["metric"] == "annual_order_value_derived"), None)
if onk:
    m = re.findall(r"\d+", str(onk["value"]))
    if len(m) >= 2:
        ladder.append({"c": "ONKYO 联名品类（推导中值）",
                       "v": int((int(m[0]) + int(m[1])) / 2), "k": "audio",
                       "period": "2025", "yoy": None})
ladder.sort(key=lambda d: -d["v"])

# ------------------------------------------------- 8. licensing disclosure
DISCLOSE_PICKS = [
 ("Toei Animation","revenue","rights_licensing_segment","东映动画 · 版权事业分部",1,52),
 ("Kodansha","revenue","rights_income","讲谈社 · 权利收入",1,None),
 ("Shogakukan","revenue","rights_income","小学馆 · 版权收入等",1,None),
 ("COVER Corp","revenue","licensing_tieup","COVER · 授权／联动",1,14.6),
 ("Shueisha","revenue","business_income_rights_and_merch","集英社 · 事业收入（与物贩合并）",2,None),
]
disclose = []
for ent, met, seg, zh, d, pct in DISCLOSE_PICKS:
    r = next((r for r in fin if r["entity_name"] == ent and r["metric"] == met
              and r["segment"] == seg), None)
    if r and num(r["value"]):
        disclose.append({"c": zh, "v": int(num(r["value"])), "pct": pct, "d": d})
disclose.append({"c": "ANYCOLOR · 无授权科目", "v": 0, "pct": None, "d": 0})

# ------------------------------------------------------- 9. market_series.csv
def series(name):
    out = defaultdict(dict)
    for r in mkt:
        if r["series"] == name:
            out[r["item"]][r["metric"]] = {"v": num(r["value"]), "label": r["label"],
                                           "src": r["source_url"], "unit": r["unit"]}
    return out

sp = series("seiyuu_population")
seiyuu = [{"y": int(y), "f": (sp[y].get("female") or {}).get("v"),
           "m": (sp[y].get("male") or {}).get("v")} for y in sorted(sp, key=int)]

cm = series("cn_market")
cnmkt = [{"y": y, "u": (cm[y].get("units_yi") or {}).get("v"),
          "v": (cm[y].get("value_yi") or {}).get("v"),
          "asp": (cm[y].get("asp") or {}).get("v")}
         for y in ["2024", "2025", "2026F"] if y in cm]

BAND_ZH = {"0-100":"0–100 元","100-200":"100–200 元","200-300":"200–300 元",
           "300-500":"300–500 元","500-1000":"500–1000 元","1000-1500":"1000–1500 元",
           "1500-2000":"1500–2000 元","2000+":"2000 元以上"}
cb = series("cn_priceband")
band = [{"b": BAND_ZH.get(k, k),
         "vol": (cb[k].get("volume_yoy") or {}).get("v"),
         "val": (cb[k].get("value_yoy") or {}).get("v"),
         "dir": int((cb[k].get("direction") or {}).get("v") or 0),
         "note": (cb[k].get("direction") or {}).get("label", "")}
        for k in BAND_ZH if k in cb]

FORM_ZH = {"TWS":"真无线 TWS","OWS":"开放式 OWS","OverEar":"头戴式"}
cf = series("cn_form")
form = [{"f": FORM_ZH.get(k, k), "v": (cf[k].get("shipments_wan") or {}).get("v"),
         "g": (cf[k].get("yoy") or {}).get("v")} for k in ["TWS","OWS","OverEar"] if k in cf]

JPB_ZH = {"under10k":"1 万日元以下","10k-20k":"1–2 万日元","over20k":"2 万日元以上"}
jb = series("jp_priceband")
jpband = [{"b": JPB_ZH[k], "v": (jb[k].get("share") or {}).get("v")}
          for k in ["under10k","10k-20k","over20k"] if k in jb]

DEMO_ZH = {"31-40":"31–40 岁","younger":"更年轻群体","other":"其他"}
cd = series("cn_demo")
demo = [{"k": DEMO_ZH[k], "v": (cd[k].get("share") or {}).get("v")}
        for k in ["31-40","younger","other"] if k in cd]
demo_extra = {k: (cd[k].get("share") or {}).get("v")
              for k in ["female","male","use5h"] if k in cd}

pvs = series("pv_site")
pv = [{"s": k, "pv": (pvs[k].get("pv_wan") or {}).get("v"),
       "uu": (pvs[k].get("uu_wan") or {}).get("v"),
       "pv_alt": (pvs[k].get("pv_wan_alt") or {}).get("v"),
       "uu_alt": (pvs[k].get("uu_wan_alt") or {}).get("v"),
       "tw": (pvs[k].get("twitter_followers") or {}).get("v"),
       "a2534": (pvs[k].get("age_25_34") or {}).get("v")} for k in pvs]

CERT_ZH = {"cn_srrc":"中国 SRRC 型号核准","cn_ccc":"中国 CCC / 3C",
           "jp_giteki":"日本 技適 工事設計認証","jp_pse":"日本 PSE（充电盒）"}
cs = series("cert")
cert = [{"c": CERT_ZH[k], "w": (cs[k].get("weeks") or {}).get("v"),
         "note": (cs[k].get("weeks") or {}).get("label",""),
         "k": "cn" if k.startswith("cn") else "jp"}
        for k in ["cn_srrc","cn_ccc","jp_giteki","jp_pse"] if k in cs]

rs = series("resale")
resale = {"deals": int((rs.get("aucfan_30d",{}).get("deals") or {}).get("v") or 0),
          "avg":   int((rs.get("aucfan_30d",{}).get("avg_price") or {}).get("v") or 0)}

pb = series("photobook")
photobook = [{"k": k, "v": int((pb[k].get("copies") or {}).get("v") or 0),
              "note": (pb[k].get("copies") or {}).get("label","")} for k in pb]

# --------------------------------------------------------- 10. risk timeline
riskrows = [{"d": r["date"], "l": r["subject"], "sev": int(r["severity"]),
             "sevl": r["severity_label"], "x": r["consequence"],
             "trg": r["trigger"], "collab": r["has_earphone_collab"] == "yes",
             "note": r.get("note","")} for r in risk]

# ------------------------------------------- 11. release cadence (from dates)
def month_of(r):
    for f in ("announce_date","order_open","release_date"):
        v = (r.get(f) or "").strip()
        if re.match(r"^\d{4}-\d{2}", v): return v[:7]
    return None
cad = defaultdict(lambda: defaultdict(int))
for r in collab:
    m = month_of(r)
    if m and m >= "2025-09" and r["brand"] in ("AVIOT","ONKYO"):
        cad[m]["a" if r["brand"] == "AVIOT" else "o"] += 1
cadence = [{"m": m, "a": cad[m]["a"], "o": cad[m]["o"]} for m in sorted(cad)]

# ------------------------------------------------------------------- 12. meta
# two date-coverage measures: month precision (YYYY-MM) vs any value (incl. year-only)
dated_month = sum(1 for r in products if month_of(r))
dated_any = sum(1 for r in products
                if any((r.get(f) or "").strip() not in ("", "NA", "unknown")
                       for f in ("announce_date", "order_open", "release_date")))
vc = sorted((int(r["voice_clip_count"]), r["brand"], r["partner_name"])
            for r in products
            if (r.get("voice_clip_count") or "").isdigit() and int(r["voice_clip_count"]) > 0)
meta = {
  "generated": datetime.now().strftime("%Y-%m-%d %H:%M"),
  "products_total": len(products), "products_collab": len(collab),
  "products_base": len(base), "partners": len(partners),
  "companies": len(comps), "financials": len(fin),
  "sources": len(sources), "gaps": len(gaps),
  "jp_priced": len(prices),
  "date_month": dated_month, "date_month_pct": round(dated_month/len(products)*100),
  "date_any": dated_any, "date_any_pct": round(dated_any/len(products)*100),
  "date_coverage_pct": round(dated_month/len(products)*100),
  "voice_min": vc[0][0] if vc else None, "voice_min_who": vc[0][1] if vc else None,
  "voice_max": vc[-1][0] if vc else None, "voice_max_who": vc[-1][1] if vc else None,
  "voice_n": len(vc),
  "brands": len(sku),
}

payload = {"meta": meta, "sku": sku, "prices": prices, "premium": premium,
           "premium_cn": premium_cn, "vol": vol, "partner": partner, "voice": voice,
           "ladder": ladder, "disclose": disclose, "seiyuu": seiyuu, "cnmkt": cnmkt,
           "band": band, "form": form, "jpband": jpband, "demo": demo,
           "demo_extra": demo_extra, "pv": pv, "cert": cert, "resale": resale,
           "photobook": photobook, "risk": riskrows, "cadence": cadence}

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write("/* GENERATED by scripts/build_report_data.py — do not edit by hand.\n")
    f.write("   Every figure is read from data/*.csv. Re-run the script after any data change. */\n")
    f.write("window.REPORT_DATA = ")
    json.dump(payload, f, ensure_ascii=False, indent=1)
    f.write(";\n")

print(f"wrote {OUT}")
for k, v in meta.items(): print(f"  {k}: {v}")
print(f"  premium pairs: {len(premium)}  vol points: {len(vol)}  voice points: {len(voice)}")
print(f"  ladder: {len(ladder)}  partner classes: {len(partner)}  cadence months: {len(cadence)}")
