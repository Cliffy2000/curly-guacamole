# Brief 2-1 (seiyuu / PR) and 2-2 (policy) — data collected

Retrieved 2026-09-09. Working notes, not a report.

---

## 1. JAPANESE VOICE ACTOR POPULATION — complete 25-year series

Source: Oricon reporting on 『声優名鑑』 (Seiyuu Meikan), the annual industry directory.
This is the authoritative published series for the brief's 声優人数増加変化 question.

| Year | Female | Male | Total |
|---|---|---|---|
| **2001** (first edition) | **225** | 145 | **370** |
| 2004 | 438 | — | — |
| 2008 | 535 | — | — |
| 2014 | 644 | — | — |
| 2016 | 728 | — | — |
| 2018 | 800 | — | — |
| 2019 | 847 | — | — |
| 2020 | 907 | — | — |
| 2021 | 955 | — | — |
| 2022 | **1,003** | — | — |
| 2023 | 1,039 | — | — |
| 2024 | 1,063 | — | — |
| 2025 | 1,099 | — | — |
| **2026** | **1,135** | **702** | **1,837** |

**Derived:** female **×5.04** over 25 years; total **×4.96**. Female broke 500 in **2008** and
1,000 in **2022**. Female has set a record for **15 consecutive years**; male for **14**.
Female share of the directory: 60.8% in 2001 → **61.8% in 2026** — the ratio has been remarkably
stable despite the fivefold expansion.

⚠ **The directory is not the population.** At a November 2022 press conference on the invoice
system it was reported that **over 10,000 people** in Japan are described as "voice actors." So
声優名鑑 captures roughly 18% of the working population — it is a *notability filter*, which is
arguably the right filter for this brief but must be labelled as such.

Sources: https://www.oricon.co.jp/news/2441186/full/ (2026 total 1,837) ·
https://www.oricon.co.jp/news/2435784/full/ (2026 female 1,135, 15-year record) ·
https://www.oricon.co.jp/news/2368259/full/ (2025 female 1,099, 14-year record) ·
https://www.oricon.co.jp/news/2226513/full/ (20-year 370→1,658) ·
https://www.oricon.co.jp/news/2223606/full/ (1,003) · https://www.oricon.co.jp/news/2183721/full/ (955)

---

## 2. 名作之壁吧 RANKING METHODOLOGY — resolved

The brief specifies 名作之壁吧 as the reference with bangumi downweighted and a CN:JP:other
ratio of 3:4:3. The actual methodology is now confirmed:

**Four rating sites, and only four:**
| Site | Sphere |
|---|---|
| **Bangumi** | Chinese |
| **Filmarks** | Japanese |
| **MyAnimeList** | English |
| **AniList** | English |

**This maps cleanly onto the brief's 3:4:3** — CN = Bangumi (30%), JP = Filmarks (40%),
other = MyAnimeList + AniList (30%, presumably 15% each). Bangumi being a single site carrying
the whole 30% CN weight *is* the downweighting relative to a naive four-way 25% split.

**Inclusion criteria:** episodes of 20+ minutes, total 8+ episodes.
**Two rankings per season:** 首月排行 (first-month) and 完结排行 (complete), each with a stated
data cutoff — e.g. July 4 for the April-season complete ranking, August 1 for the July-season
first-month ranking.
**Delayed titles** are handled case-by-case, either kept in season or moved to a rebroadcast season.
The weighting algorithm is explained at the start of each Bilibili video, not in text form.
The channel changed its scoring method at some point — discussion at Zhihu question 517825413.

**Available ranking editions found:** 2026年一月新番完结, 2026年四月新番首月, 2026年四月新番完结,
2026年七月新番首月, plus a mid-season TOP20 for July 2026 including April half-cours titles.

⚠ **The ranking lists themselves are video-only.** Direct fetch of the Bilibili pages returns
HTTP 412. The titles and scores will need to be transcribed from the videos or reconstructed from
the four source sites directly. **Reconstructing from source is probably better** — it makes the
weighting explicit and auditable rather than inheriting an undocumented algorithm.

⚠ **Unresolved in the brief:** it says 流媒体表现较好的作品 (works performing well on streaming)
but then references rating sites. Streaming performance and rating score are different metrics and
would produce different top-25 lists. Also the number of quarters to cover is unstated.

Sources: https://www.bilibili.com/video/BV1ohuu6LEfK/ · https://www.bilibili.com/video/BV131596GECe/ ·
https://www.bilibili.com/video/BV14JdhBKEcs/ · https://www.bilibili.com/video/BV1HFN46dEvi/ ·
https://www.bilibili.com/video/BV1jDgA6wE2V/ · https://www.zhihu.com/question/517825413

---

## 3. PR / INFORMATION-RELEASE SITES — with traffic, since click counts are unobtainable

The brief asks for per-article click counts and histograms. **News sites do not publish
per-article click data.** What they do publish, in ad rate cards, is site-level PV and UU. That
is the correct substitute and it is comparable across sites.

**アニメイトタイムズ animate Times** — the dominant seiyuu news property, run by the Animate group.
- **~24.16 mn monthly PV / ~10.69 mn monthly UU** (September 2025 actuals)
- Alternate figure: **28.18 mn PV / 12.14 mn UU** (PC+SP combined, earlier period)
- Official Twitter ~**670,000** followers (April 2023)
- **Audience: male 50% / female 50%; 25–34 ≈ 31%**
- Has a dedicated 声優 section and a 声優ニュース tag feed
- Media kit available via its ad page and via Media Radar

**Other sites identified, PV not yet collected:**
- **声優グランプリ seigura.com** — the main seiyuu magazine's official site
- **アニメハック** anime.eiga.com/person/ — Eiga.com's seiyuu database
- **声優共演検索** seiyu.ie-t.net — includes 出演数順 (by appearance count) seasonal seiyuu lists.
  **Directly useful for the brief's 出演作品数 field.**
- **声優アニメディア** — magazine with a published ad rate card at zasshi-ad.com
- newmatosoku.com/seiyuu/ — aggregator of 5ch/Twitter chatter, tier 6

Sources: https://www.animatetimes.com/ad/ · https://media-radar.jp/detail6638.html ·
https://ja.wikipedia.org/wiki/アニメイトタイムズ · https://seigura.com/ ·
https://anime.eiga.com/person/ · https://seiyu.ie-t.net/syutsuensu.php?s=sum ·
https://www.zasshi-ad.com/media/game/seiyuanimedia.html

## 3b. Photobook sales — partially obtainable

Oricon tracks seiyuu photobooks that chart. Observed figures:
**佐倉綾音 Sakura Ayane 10,712 copies (#1 among female seiyuu) · 水樹奈々 Nana Mizuki 5,664 (#2).**
⚠ A Chiebukuro answer clarifies these are **cumulative Oricon-tracked sales, not first-week**.
**Scale benchmark:** the top idol comparison, 生田絵梨花's 『インターミッション』, did **178,688
first week** — so a top female seiyuu photobook is roughly **1/17th** the scale of a top idol
photobook. Useful for calibrating expectations on merch attach rates.
アニメイトタイムズ maintains a 2026 list of female seiyuu gravure/photobook releases — the source
for the 写真集数量 field.
Sources: https://detail.chiebukuro.yahoo.co.jp/qa/question_detail/q14257125974 ·
https://www.animatetimes.com/news/details.php?id=1590509900 · https://the0ries.com/nshphotobook/

---

## 4. SECTION 2-2 — POLICY AND CERTIFICATION

### 4.1 China — selling a TWS earphone

| Requirement | Detail |
|---|---|
| **SRRC** 无线电发射设备型号核准 | **Mandatory.** MIIT State Radio Regulation. Any radio transmitter above **10 mW** needs the 型号核准证. Timeline: ~5 working days initial + ~30 working days to certificate; **~8 weeks total** including testing. **Valid 5 years.** Current fee schedule is **no charge**, but contract materials must be submitted after issuance |
| **CCC / 3C** | **Mandatory** — Bluetooth earphones fall inside the 3C catalogue. Processing **4–6 weeks, up to 2 months** |
| **进网许可证 (MIIT network access)** | Cited as required alongside the above |

⚠ One Zhihu thread questions whether Bluetooth earphones currently require both CCC and SRRC —
the CCC catalogue has been revised over time. **Verify against the current 强制性产品认证目录
before relying on this.**
Sources: https://www.52audio.com/archives/12793.html · https://www.bst-cert.com/8669.html ·
https://www.bst-cert.com/8664.html · http://cqa-cert.com/xwzx/info_30_itemid_2497.html ·
http://www.cqa-cert.com/xwzx/info_30_itemid_2423.html · https://www.zhihu.com/question/624149054

### 4.2 Japan — 技適 and PSE

**技適 (giteki) / 工事設計認証:**
Bluetooth falls under the 電波法. Only 総務大臣-registered certification bodies may certify.
Two routes: **技術基準適合証明** (per-unit testing) and **工事設計認証** (per-model, by document
plus test) — **mass-produced goods use 工事設計認証**. Requires a radio test sample plus document
set. One documented case took **~1 month** from first contact with the certification body to
completion. **TELEC** is the principal registered body; agency services exist.
⚠ Fee figures not found.
Sources: https://www.telec.or.jp/services/tech/ · https://www.musen-connect.co.jp/blog/course/other/japan-radio-law-experience-memo/ ·
https://www.musen-connect.co.jp/blog/course/other/japan-radio-law-basic/ · https://www.wti.jp/contents/giteki.htm ·
https://www.cqlab.jp/技適と認証/

**PSE — a direct correction to the company file's reading.**
The company file (PS⑥) says a TWS having a battery does not automatically mean the earphone
requires PSE, and that the charging case needs separate confirmation. The confirmation is:

> METI amended the interpretation of the 電気用品安全法 in **February 2018** to bring portable
> lithium-ion batteries into scope, and **from 2019-02-01 mobile batteries AND fully wireless
> earphones — specifically their charging cases — cannot be manufactured, imported or sold in
> Japan without PSE marking.**

So **the charging case IS in scope and PSE applies.** The nuance the company file describes (a
battery fully installed inside a final device not being treated as import/sale of the battery
itself) is real but does **not** exempt a TWS charging case. Sodium-ion batteries are outside PSE
scope, which is technically true but not a practical route.
Sources: https://www.meti.go.jp/policy/consumer/seian/denan/mlb_faq.html ·
https://www.elecom.co.jp/pickup/mobile_battery/basic17.html · https://www.ankerjapan.com/blogs/magazine/what-is-pse ·
https://jp.litime.com/blogs/knowledge/what-is-pse-mark · https://gk-post.com/5283

### 4.3 Legal prohibitions — the voice-rights layer, which the brief does not name but needs

**JAPAN: there is no settled protection for voice.**
パブリシティ権 (publicity rights) is established by the Supreme Court's **ピンク・レディー事件**
judgment (2012). Holdings: (1) the publicity right derives from personality rights; (2) unauthorised
use of a likeness is tortious when done **solely to exploit customer-attracting power**; (3) that
means using the likeness as an independent object of appreciation or as a commodity, attaching it
to differentiate goods, or using it in advertising.
**Critically: whether VOICE, manner of speaking, signature, clothing or bearing are protected as
"characteristics other than name and likeness" is NOT settled in Japanese law — no established
view exists.** For a voice-collab product this means the **contract carries the whole weight**;
there is no statutory fallback if a licence is ambiguous about voice use.
Sources: https://www.kottolaw.com/column/000371.html · https://chosakukenhou.jp/pinklady/ ·
https://www.thomsonreuters.co.jp/ja/westlaw-japan/column/2012/120319/ ·
https://ozaki-lawoffice.jp/ピンクレディー事件… · https://atlawyer.jp/column/AqXHmvfZ (声とAIとパブリシティ権) ·
https://lex.juris.hokudai.ac.jp/gcoe/journal/IP_vol41/41_7.pdf

**CHINA: voice IS explicitly protected, and there is binding precedent on synthetic voice.**
**民法典 (Civil Code) Article 1023** — protection of a natural person's **voice** applies by
reference to the protection of portrait rights, establishing voice as a distinct personality
interest.
**2024-04-23, Beijing Internet Court** — China's first AI-generated-voice personality-rights case,
first-instance judgment. Plaintiff Ms. Yin, a voice actor, found her AI-cloned voice used in
platform dubbing videos.
Holdings: where the voice is **identifiable by the relevant public**, personality-right protection
**extends to AI-generated voice**; commercial AI use requires **specific express authorisation**,
and **a general voice/copyright licence is NOT sufficient**. Identifiability is judged by whether
an ordinary listener in the relevant field can recognise it. **Damages CNY 250,000**, jointly
against the culture-media company and the software company.
⚠ A later Chinese court found an AI voice did **not** infringe personality rights, so the standard
may be evolving — flagged, not resolved.
**Direct relevance:** the company's plan includes an app with **voice packs**. Under Art. 1023
plus this precedent, putting a seiyuu's voice into an app for the Chinese market requires
**specific express authorisation for that use** — a general collab licence will not cover it.
Sources: https://m.thepaper.cn/newsDetail_forward_28886704 ·
https://www.21jingji.com/article/20240424/herald/54b6e304560e0edaf360e674c661a7a1.html ·
https://www.marks-clerk.com/zh-hans/观点/最新见解/102k392-中国首例ai声音人格权侵权案裁判要旨及影响/ ·
https://www.marks-clerk.com/zh-hans/观点/最新见解/102kv8h-中国-另一法院认定ai声音不侵犯人格权… ·
https://www.allbrightlaw.com/CN/10531/d4e97d7a844e3037.aspx ·
https://k.sina.com.cn/article_7879996098_1d5af32c206801lpmi.html

---

## 5. SECTION 2-2 — CHINA BOYCOTT CASES INVOLVING JAPANESE VOICE TALENT

Documented incidents with observable commercial consequences. Framed as a risk taxonomy because
the mechanism repeats; individual names are recorded only where the incident and its commercial
outcome are publicly reported.

### 5.1 The trigger categories, from the observed cases
1. **Yasukuni Shrine** — visiting, or disclosing a past visit, including visits many years prior
2. **Taiwan as a country** — flags, map labels, analytics country lists, the word 国
3. **Hong Kong political comment**
4. **Historical/wartime content or ancestry** — including an author's past statements, and one case
   of a seiyuu disclosing descent from a wartime figure
5. **Association by content** — where the *work* rather than the talent is the trigger

### 5.2 Case log

**2018 — 『二度目の人生を異世界で』 (Rebirth in a Different World). The most severe case found.**
The original author had posted hate speech on Twitter about China and Korea, and apologised.
On **2018-06-06 at ~10:00, four cast members simultaneously announced withdrawal**:
**増田俊樹 Masuda Toshiki**, **安野希世乃 Yasuno Kiyono**, **中島愛 Nakajima Megumi**,
**山下七海 Yamashita Nanami**. The same day the October TV anime's **broadcast and production were
cancelled**. **Hobby Japan halted shipment of all 18 published novel volumes**; the print edition
went out of print, was self-recalled, and the series was discontinued.
**Commercial consequence: an entire anime adaptation and an 18-volume novel line terminated.**
Sources: https://nlab.itmedia.co.jp/cont/articles/3279428/ · https://akiba-souken.com/article/34543/ ·
https://www.cinra.net/article/column-201806-nidomenojinsei · https://ja.wikipedia.org/wiki/二度目の人生を異世界で ·
https://www.thepaper.cn/newsDetail_forward_2178899

**2019 — 朴璐美 Paku Romi and 置鮎龍太郎 Okiayu Ryōtarō.** Boycotted over comments on Hong Kong.
Source: https://www.163.com/dy/article/GD1MSM5105467D9Z.html

**2020-09 — 桐生ココ Kiryu Coco and 赤井はあと Akai Haato (hololive / COVER Corp).**
On 2020-09-25 Coco displayed Google Analytics on stream showing **Taiwan listed as a country**;
the stream was being mirrored to hololive's official Bilibili channel. Haato had separately
referred to **"the country of Taiwan."** By the morning of **2020-09-26 all hololive talents lost
Bilibili streaming permissions**, cancelling scheduled streams including Aki Rosenthal's
Bilibili-exclusive and Minato Aqua's new-costume reveal. COVER consulted its Chinese partners, who
advised that a strongly-worded statement was necessary, and issued statements on Bilibili and
Twitter. **Both talents were suspended (謹慎).**
**This is the bidirectional case:** COVER's "One China" framing then caused a second backlash in
**Taiwan and Japan**. hololive subsequently withdrew from Bilibili operations.
Sources: https://note.com/aneks/n/n3b815826b56e · http://ymst0524.livedoor.blog/archives/23830623.html ·
https://izumino.hatenablog.com/entry/2020/11/20/072005 · https://anond.hatelabo.jp/20200926221643 ·
https://note.com/sharktornade/n/nfc3a51dad30f · https://matomedane.jp/potato/page/60774

**2021-02 — 茅野愛衣 Kayano Ai. The most commercially consequential single-talent case.**
On her 10th-anniversary radio channel she said she had visited **Yasukuni Shrine** near her
workplace to pray for good work. Chinese backlash followed; her agency apologised.
From **June 2021** she was progressively removed or replaced across Chinese titles:
**『アークナイツ』Arknights** (stated as "at the developer's request"), **『崩壊学園』Honkai Gakuen**,
**『陰陽師』Onmyoji**, **『永遠の七日』Eternity of 7 Days**.
On **2021-06-20 『碧藍航線』Azur Lane China removed all voice lines for the seven ships she voiced**
— including **愛宕 Atago, 加賀 Kaga, レナウン Renown, グラーフ・ツェッペリン Graf Zeppelin** —
without prior notice to players.
⚠ **Name-garbling warning:** several English-language summaries render this incident as
"Maaya Uchida" (内田真礼). The Chinese sources say 茅野爱衣 explicitly and the affected Azur Lane
ships are Kayano Ai's roles. **The subject is 茅野愛衣 Kayano Ai.** Some sources also date it
February 2020 rather than 2021 — the 2021 dating is better supported.
Sources: https://www.koenote.info/entry/20210626 · https://news.qq.com/rain/a/20210621A01BV000 ·
https://www.sohu.com/a/473173788_121134816 · https://gnn.gamer.com.tw/detail.php?sn=216873 ·
https://www.zhihu.com/question/466122140 · https://www.zhihu.com/question/444206340/answer/1728357328 ·
https://sarattosokuhou.com/entame/kayano-yasukuni/ · https://www.youxi369.com/gonglue/85573.html

**2021 — 本渡楓 Hondo Kaede and 桑原由気 Kuwahara Yuki.** Photographs at Yasukuni Shrine alongside
statues of militarism figures circulated. Hondo additionally stated on a radio programme that she
is a descendant of **東郷平八郎 Tōgō Heihachirō**.
Sources: https://zhuanlan.zhihu.com/p/351978165 · https://www.rfa.org/mandarin/yataibaodao/junshiwaijiao/ql2-02162021074826.html

**2025-02 — a BanG Dream! voice actress** used a **Taiwan flag**, causing 大炎上 in China.
Source: http://www.anige-sokuhouvip.com/blog-entry-75627.html

**2025-03 — 森久保祥太郎 Morikubo Shōtarō.** Dropped from **three characters** in a Chinese game
with no explanation given, causing significant backlash in Japan. Reported as replaced by
寺島惇太 Terashima Junta.
Sources: https://www.youtube.com/watch?v=ygXW74zPhts · https://x.com/hksamyip/status/1900764100118147540

**2025-09 — 『鳴潮』Wuthering Waves** announced replacing the **Mandarin** voice of the female
protagonist following a voice-actor speech controversy. Note Wuthering Waves is a **Moondrop
collab partner** (U.C.T.S.).
Source: https://www.gamersky.com/news/202509/2010250.shtml

**2025-12 — sector-wide.** Japanese entertainers' performances in China were cancelled en masse
following Prime Minister **高市早苗 Takaichi Sanae's** Taiwan remarks; China issued travel
warnings. Taiwan's premier publicly invited the affected performers.
**This is the first case in the log where the trigger was neither the talent nor the work but the
Japanese government** — i.e. an exposure no partner-selection process can screen for.
Sources: https://ja.wikipedia.org/wiki/高市早苗による台湾有事発言 ·
https://www.recordchina.co.jp/b965615-s25-c10-d0193.html

**2026-03 — 佐藤拓也 Satō Takuya.** Dropped from **『恋と深空』Love and Deepspace** (Rey) and
**『アークナイツ』Arknights** (Midnight) over past posts. Separately reported as having been
replaced in a Chinese game over a Yasukuni visit **17 years earlier**.
Sources: https://oniji.hatenablog.com/entry/2026/08/01/210000 · https://c.m.163.com/news/a/KN8E4QM7051486RA.html

**Adjacent precedent, not Japanese seiyuu:** 張哲瀚 Zhang Zhehan (Chinese actor, 2021, Yasukuni
photographs) lost all endorsements — shows the ceiling severity of the mechanism.
Source: https://www.rfa.org/mandarin/yataibaodao/kejiaowen/hx2-08162021090910.html

### 5.3 The finding that matters most for partner selection

**Four of the seiyuu who already have earphone collaboration products appear in this log.**
- **茅野愛衣 Kayano Ai** — Universal Music TOoKA BASE collab SKU (`P0081`) — 2021 Yasukuni case,
  removed from at least five Chinese titles
- **森久保祥太郎 Morikubo Shōtarō** — TOoKA BASE collab SKU (`P0169`) — 2025 dropped from three
  Chinese game characters
- **安野希世乃 Yasuno Kiyono** — **Moondrop's 梦回 collab partner** (`P0097`), the only human-talent
  collab in the entire Chinese dataset — withdrew from 『二度目の人生を異世界で』 in 2018
- **増田俊樹 Masuda Toshiki** — TOoKA BASE collab SKU (`P0165`) — withdrew from the same 2018 title

The 安野希世乃 case is the most instructive: a seiyuu who withdrew from a China-controversial
Japanese project later became the face of a **Chinese** audio brand's only human-talent collab.
Withdrawal read as *distancing from* the offending work, which is the opposite of a liability.

### 5.4 Still needed
| Item | Status |
|---|---|
| Cases from 2006–2017 | **thin** — the log is dense from 2018 onward but the brief asks for ~20 years |
| Kayano Ai incident date | **2021-02 vs 2020-02 conflict** — needs one authoritative source |
| BanG Dream! seiyuu name | not identified in the source found |
| Morikubo — which game, which three characters | not named in sources found |
| Whether any incident affected a *hardware* product | **no case found** — all observed consequences were game voice removals, anime cancellation, or event cancellation |
| Japan-side backlash cases (the mirror risk) | only the hololive case documented so far |
| Reputation/termination clause norms in JP talent contracts | **not searched yet** |
