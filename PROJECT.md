# Collab Hi-Fi Headphones — Japan & China Market Research

**Client framing:** preliminary but complete market research for a company evaluating entry into
talent/IP-collaboration hi-fi headphones. Audience is technical. Deliverable is data-centred;
a D3.js report is built downstream from `data/*.json`.

**Standing evidence rule:** every figure traces to a retrieved primary or near-primary source
recorded in `data/sources.json`. Unsourced values are never estimated, interpolated, or
carried over from a neighbouring record. Absent values are recorded in `data/gaps.json` with
the searches attempted. "Not found" is a valid, expected, and reportable result.

---

## 1. Scope

### In scope
- **Product class:** hi-fi / audiophile-positioned personal audio. IEMs (wired and true-wireless),
  on-ear, over-ear closed, over-ear open. Wired and Bluetooth both included.
- **Geography:** Japan and China (mainland). Brands headquartered there, and collab SKUs
  released into those markets.
- **Collaboration counterparties, all of the following:**
  - Human talent as themselves — voice actors (seiyuu / 声优), ASMR performers, narrators,
    singers, streamers, idols.
  - Virtual talent — VTubers / VUPs, where the streamer and the character are one product.
  - Fictional characters and franchise IP — anime, game, audio-drama properties.
  - Agencies and platforms collaborating in their own name.
- **Companies profiled:** the audio brands shipping the product, and the rightsholders /
  agencies / platforms that control the talent and IP, including financials where filings exist.
- **Technical specification** of each SKU, and whether the collab altered anything acoustic
  or only cosmetic.

### Out of scope (explicit client decisions)
- Mainstream gaming headsets and mainstream consumer TWS not positioned as hi-fi.
- Korea.
- DAC dongles, amplifiers, cables, and non-audio merchandise as primary records — logged only
  as secondary evidence of deal scope when produced by the same partnership.

### Deprioritised by client, retained as low-cost fields only
Channel/distribution mechanics, price premium vs base SKU, chronology, regulatory context,
non-participating brands. Captured as columns because they are free to collect alongside
price and spec data. No analytical chapter is built on them unless requested.

---

## 2. Method

1. **Discovery** — enumerate every shipped collab SKU in both markets. Brand-side sweep
   (walk each candidate audio brand's collab/news archive) and partner-side sweep (walk each
   candidate agency/IP merch archive). Schema-independent; done first.
2. **Verification** — for each candidate, retrieve the primary announcement or product page,
   register it in `sources.json`, then populate `products.json`.
3. **Specification** — extract the tech block from the manufacturer spec page. Record the
   measurement unit alongside every value (notably sensitivity dB/mW vs dB/V) rather than
   normalising silently.
4. **Commercial** — launch price in native currency, plus crowdfunding campaign figures where
   the SKU was crowdfunded. Crowdfunding is the only channel that publishes exact unit and
   revenue data, so it is treated as the quantitative backbone.
5. **Volume reconstruction** — units and revenue are reconstructed only from disclosed figures,
   crowdfunding backer counts, marketplace sales counters, or company filings. Every such value
   carries a `units_sold_basis` flag naming the mechanism. Nothing is modelled from assumption.
6. **Company layer** — filings for listed entities; registry and press for private ones.
7. **Gap register** — anything sought and not found is written to `gaps.json`, not left silent.

### Source reliability tiers
Recorded per source in `sources.json` as `reliability_tier`:
1. Brand or agency official (press release, product page, spec sheet)
2. Regulatory filing / IR document (annual report, tanshin, 20-F, HKEX/SEC/TDnet)
3. Crowdfunding platform campaign page (platform-published figures)
4. Established trade press
5. General press
6. Community / aggregator — usable as a discovery lead only, never as a cited figure

---

## 3. Data layout

Normalised JSON in `data/`, joined on stable IDs, long format for anything time-varying.
Field-by-field definitions in `SCHEMA.md`.

| File | Grain |
|---|---|
| `products.json` | one collab SKU |
| `partners.json` | one talent, character, or IP |
| `companies.json` | one legal entity (audio brand, agency, rightsholder, platform) |
| `product_partners.json` | SKU-to-partner join, many-to-many |
| `financials.json` | company x fiscal period x metric (long) |
| `metrics.json` | entity x metric x date (long) — follower/subscriber counts etc. |
| `sources.json` | one retrieved source |
| `gaps.json` | one sought-and-missing value |

---

## 4. Progress log

| Date | Phase | State |
|---|---|---|
| 2026-09-07 | Setup | Scope agreed, schema defined, scaffold created |
| 2026-09-07 | Discovery | Started — brand-side sweep |
