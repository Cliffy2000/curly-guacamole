# Data dictionary

Five CSVs in `data/`, all d3-loadable via `d3.csv()`. Joined on the ID columns below.
This file describes what is actually in the files — it replaces an earlier aspirational
schema draft that was abandoned before the data existed.

## Conventions

- **Empty cell = not found or not applicable.** It never means zero. Anything actively
  searched for and not found has a row in `gaps.csv`.
- **Dates** are ISO 8601 with meaningful partial precision: `2024`, `2024-03`, `2024-03-15`.
  Partial dates are not padded to look more precise than the source.
- **Currency** is native (`JPY`, `CNY`). **No USD conversion has been applied anywhere** —
  no FX rate is fixed yet (`gaps.csv` G034). Do not compare JPY and CNY values directly
  until a rate and date are chosen.
- **`confidence`** on every product and company row:
  `verified_primary` (brand/agency official source) · `verified_secondary` (trade press) ·
  `partial` (some fields sourced, key fields missing) · `lead_only` (aggregator only,
  unverified — **do not chart as fact**)
- **Derived values** are labelled `derived` in `financials.csv` and show their arithmetic
  in `notes`. Nothing is modelled or estimated.
- **Multi-value cells** use `;` as the internal separator (codecs, channels, roles).

## Current file sizes (2026-09-09)

`products.csv` 241 SKU rows · `partners.csv` 94 · `companies.csv` 61 · `financials.csv` 98 ·
`sources.csv` 374 · `gaps.csv` 69.

**Recency: `announce_date` / `order_open` / `release_date` are populated on 122 of 241 rows (50%).**
The client priority is that items over ~5 years old matter less than current ones, so filter on
these fields. Backfilled from chronological press archives (`aviot.jp/press/`,
`prtimes.jp/topics/keywords/Zeeny`, ONKYO's DreamNews archive) rather than product pages, which
mostly omit dates. Remaining undated rows are concentrated in the 2021-era Universal Music stock
and some ONKYO/Zeeny SKUs — see `gaps.csv` G057.

**Two sellers are dormant, not current** — filter accordingly:
- **Universal Music (TOoKA BASE)**, 29 SKUs, almost all 2021–2022; all brand news Nov 2025–Jul 2026
  is band merchandise, no earphone collabs (`gaps.csv` G056).
- **Zeeny**, 17 SKUs, all dated announcements fall between 2022-12 and 2023-09; nothing after.

## data/products.csv — one SKU each

Key: `product_id` (`P0001`…). Join to `companies.csv` on brand name, to `financials.csv`
on `entity_id`.

Columns: `product_id`, `brand`, `brand_country`, `product_name`, `model_code`,
`partner_name`, `partner_class`, `partner_agency`, `form_factor`, `connectivity`,
`collab_depth`, `price_value`, `price_currency`, `price_tax_basis`, `voice_clip_count`,
`announce_date`, `order_open`, `release_date`, `availability`, `driver_config`,
`bt_version`, `codecs`, `battery_bud_h`, `battery_case_h`, `water_rating`, `weight_g`,
`units_sold`, `units_basis`, `channel`, `confidence`, `notes`

Enum values in use:
- `partner_class`: `vtuber_individual`, `vtuber_unit`, `seiyuu_individual`, `seiyuu_group`,
  `illustrator_vtuber`, `utaite_individual`, `musician`, `celebrity_comedian`,
  `virtual_singer`, `virtual_character`, `anime_ip`, `game_ip`, `character_ip`,
  `literary_ip`, `tokusatsu_ip`, `music_project`, `tv_programme`, `tv_programme_ip`,
  `radio_programme`, `esports_club`, `platform_brand`, `brand_partner`,
  `reviewer_influencer`, `other_ip`, `none`, `unknown`
- `collab_depth`: `cosmetic`, `cosmetic_plus_media`, `co_tuned`, `co_designed`,
  `original_signature`, `none`, `unknown`
- `form_factor`: `iem`, `tws_iem`, `ear_clip`, `over_ear_closed`, `bone_conduction`
- `availability`: `limited_active`, `limited_sold_out`, `standing_catalog`, `discontinued`
- `price_tax_basis`: `incl`, `excl`, `incl_with_shipping`, **`incl_member`**
- `units_basis`: `company_disclosed`, `crowdfunding_backers`, `disclosed_partial`

**`incl_member` matters for premium maths.** AVIOT labels every collab SKU with a 会員価格
(member price). Base-platform rows carry both, so **always compare member-to-member**.
Base-platform reference rows are P0153–P0158, plus P0118 (Moondrop RAYS) and P0119 (final
ZE500 NYUMIN). They have `partner_class = none` and `collab_depth = none` — **filter them out
of any collab count**, and use them as the denominator for premium calculations.

**Charting caveats.** `price_value` mixes JPY and CNY — always facet or filter by
`price_currency`. `voice_clip_count` is present on ~22 rows; for the Gintama models
(P0006–P0009) the published figure of 360+ is a **combined** total across four SKUs, recorded
on P0006 only. `units_sold` is populated on 4 rows out of 158; see `gaps.csv` G033 for why
(Japan runs made-to-order, so volumes are structurally undisclosed).

**Measured collab premiums** (all member-to-member, both sides sourced):
TE-Q3/Q3R +73.3% to +112.0% · TE-V1R +59.4% · TE-J2 +33.5% · WA-J1 +29.8% · WB-P1 +24.9% ·
Moondrop RAYS +10.0%. The premium is **inverse to base price** — the collaboration adds a
roughly fixed absolute JPY 8,000–12,000, not a fixed percentage.

## data/partners.csv — 55 rows, one talent, character or property each

Key: `partner_id` (`T001`…). Join to `products.csv` on `partner_name`.

Columns: `partner_id`, `name_native`, `name_latin`, `partner_class`, `talent_roles`,
`agency_name`, `agency_status`, `origin_market`, `audience_metric`, `audience_value`,
`audience_as_of`, `brands_partnered`, `confidence`, `notes`

**Scope: talent-side partners only.** Anime, game and tokusatsu franchises are captured
per-SKU in `products.csv` and are deliberately *not* duplicated here — this file exists to
characterise the human and virtual partners, where agency structure and exclusivity matter.

`agency_status`: `agency`, `label`, `rightsholder`, `independent`, `unknown`.
**`independent` is the analytically important value** — T001 (Suou Patra), T004 (Shigure Ui),
T036 (Kagura Mea) and T037 (Kagura Nana) are unaffiliated, meaning a single-counterparty deal.

`audience_value` is populated on only 2 of 55 rows (`gaps.csv` G044). `brands_partnered` is
semicolon-separated and is what shows talent **non-exclusivity** — T005, T006 and T003 each
appear across two or three competing audio brands.

## data/companies.csv — 43 rows, one legal entity each

Key: `company_id` (`C001`…).

Columns: `company_id`, `name_latin`, `name_native`, `legal_name`, `roles`, `country`,
`hq_city`, `founded`, `ownership`, `exchange`, `ticker`, `parent_company`, `employees`,
`collab_sku_count`, `website`, `confidence`, `notes`

`roles`: `audio_brand`, `talent_agency`, `ip_rightsholder`, `platform`, `music_label`,
`game_publisher`, `goods_distributor`, `retailer`, `oem_codeveloper`, `peripheral_maker`,
`software_licensor`, `broker`, `media`, `tv_network`, `audio_drama_producer`

**`collab_sku_count` = 0 has two very different meanings.** For C015 (Audio-Technica) and
C033–C043 it means *searched and confirmed absent* — deliberate non-participants, which
is a finding. For C021/C022 (COVER, ANYCOLOR) it means they are rightsholders, not sellers.
Read `notes` before charting this column.

⚠ **`collab_sku_count` is stale and should not be charted.** It was set before the
seller-by-seller catalogue pass and understates several brands badly (Universal Music reads 2,
actual is 29). **Derive counts from `products.csv` instead**, filtering out
`partner_class = none` (base-platform reference rows). Current actual counts by brand:
AVIOT 73 · ONKYO 35 · Universal Music 29 · MOONDROP 18 · Zeeny 17 · final 15 · Sony 5 ·
Victor 4 · SONGX 3 · Taito/Cafereo 2 · Hi-Unit 2 · qdc, intime, Xinghaibei, Owltech,
MissEvan, LUKLUK 1 each.

**Agency roster sizes live in `financials.csv`, not here** — as `metric = roster_size` rows,
because they are point-in-time values that change. Aoni ~492 · Mausu ~155 · I'm Enterprise 100+ ·
Nijisanji ~150 · hololive 78 · VirtuaReal 61 · Nanashi Inc 25 · Kiramune 20 · Aogiri 11.

## data/financials.csv — 37 rows, long format

One row per entity × metric × period. Designed for direct use in time-series and
comparison charts.

Columns: `entity_id`, `entity_name`, `metric`, `segment`, `period_label`, `period_type`,
`period_end`, `value`, `unit`, `currency`, `yoy_pct`, `confidence`, `source_url`, `notes`

`unit` is `million`, `percent`, `million_units`, `persons`, `units`, `count`,
`order_of_magnitude`, or `absolute` — **always read it.** Japanese filings quote in 億円
(hundred-millions) and automated summaries garbled the magnitude twice during this research,
once by 10× and once by 100×. Values here are normalised to `million` JPY/CNY.

`entity_id` also carries non-company keys: `MKT01`/`MKT02` (market aggregates),
`AD01`–`AD05` (Chinese audio-drama titles), and `P00xx` (product-level campaign figures).

## data/sources.csv — 200 rows, the source ledger

Key: `source_id` (`S001`…). Every URL retrieved during this research.

Columns: `source_id`, `url`, `publisher`, `publisher_type`, `doc_type`, `language`,
`reliability_tier`, `retrieved_date`, `topic`

`reliability_tier`: **1** brand/agency official · **2** regulatory filing / IR ·
**3** crowdfunding platform · **4** established trade press · **5** general press ·
**6** community or aggregator (**discovery leads only — never cite a figure from tier 6**)

The `topic` column flags retrieval failures inline: mojibake, HTTP 403, unparseable PDF,
paywalled, and "NOT YET READ" for located-but-unread sources.

## data/gaps.csv — 34 rows, the register of what is missing

Key: `gap_id` (`G001`…).

Columns: `gap_id`, `entity_type`, `entity_id`, `entity_name`, `field`, `status`,
`priority`, `searches_attempted`, `explanation`, `date`

`status`: `not_found`, `not_disclosed`, `conflicting_sources`, `paywalled`, `partial`,
`not_set`

**This file is a deliverable, not housekeeping.** Three rows are findings in their own right:
- **G022** — no collaboration with a named Chinese voice actor exists in the evidence, after
  nine targeted searches. An evidenced negative.
- **G009** — ANYCOLOR structurally does not disclose licensing revenue, so Nijisanji collab
  income is unobservable. COVER is the only public window.
- **G001** — no royalty or licensing rate appears in ~200 sources. Expected to stay unfound
  without direct industry contact.
