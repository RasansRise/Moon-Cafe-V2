# Moon Café — SEO Strategy & Website Sitemap

> **Version:** 1.5 — Developer handoff consistency update (2026-11-23)  
> **Date:** 2026-11-23  
> **Status:** Draft / development reference — page inventory confirmed; URL routes, content and hosting pending confirmation  
> **Related:** `plan.md`, `menu-inventory.md`, `design.md`  
> **Site:** https://www.mooncafe-sa.com/

## 1. Goals and boundaries

Improve discoverability of the Moon Café brand, products/menu, and branch information in Arabic and English without compromising the agreed simple, fast, static HTML/CSS/vanilla JS architecture.

- **Confirmed:** bilingual website; menu index plus separate page for each category in each language (no product-detail URLs); branches in a **three-column desktop card grid** (responsive 2/1); no product search; no ordering; content edited by developer; Google Analytics and Google Search Console integrations excluded.
- **Proposed SEO:** technical indexing readiness, accurate on-page metadata, crawlable bilingual text, image optimization, internal linking, local-business consistency, and migration redirects.
- **Not promised:** rankings, indexing timelines, rich results, or traffic increases. A sitemap can help discovery but does not guarantee indexing.

## 2. Website sitemap / information architecture (PROPOSED)

```text
Moon Café
├── Arabic (DEFAULT) /
│   ├── Home / (including About section)
│   ├── Menu /menu/
│   │   ├── Drinks / المشروبات [SECTION ONLY — no new URL]
│   │   │   ├── Hot Coffee /menu/hot-coffee/
│   │   │   ├── Hot Drinks /menu/hot-drinks/
│   │   │   ├── Iced Coffee /menu/iced-coffee/
│   │   │   ├── Crash /menu/crash/
│   │   │   └── Refreshing Drinks /menu/refreshing-drinks/
│   │   └── Food / الأكل [SECTION ONLY — no new URL]
│   │       ├── Bakery & Desserts /menu/bakery-desserts/
│   │       ├── Sandwiches & Croissants /menu/sandwiches-croissants/
│   │       └── Snacks /menu/snacks/
│   ├── Branches /branches/
│   └── Contact /contact/
└── English /en/ (same structure, /en/ prefix)
    ├── Home /en/
    ├── Menu /en/menu/
    │   ├── Drinks [5 category pages]
    │   └── Food [3 category pages]
    ├── Branches /en/branches/
    └── Contact /en/contact/
```

**Confirmed navigation grouping:** Drinks contains 5 categories (38 listed entries); Food contains 3 categories (31 listed entries). These are headings/sections on the Menu page, **not independently indexable pages**; no `/menu/food/` or `/menu/drinks/` route is planned. Each of the 8 categories retains its own bilingual page.

**Confirmed page inventory / proposed URLs:** Each language has four core pages (Home, Menu index, Branches, Contact) **plus a dedicated page for each approved menu category**; total = **8 + (2 × 8) = 24 localized pages**. About is a section within Home, **not** a separate page or XML sitemap entry. The route syntax remains proposed, not approved. Every approved category will be its own **indexable HTML page** (provided it has useful unique content). Optional subcategories, if any, remain a taxonomy decision and are not automatically additional pages. No standalone product URLs; no branch detail URLs under the approved scope. **[CONFIRMED]** The root `/` serves the Arabic homepage directly (no language chooser or forced redirect). English uses `/en/`. Never redirect visitors based on geolocation or browser language in a way that blocks crawling or removes manual language choice.

**Category SEO rule:** give each category page its own localized title, meta description, H1, canonical URL, reciprocal `hreflang` to its matching translated category, internal links from the menu index, and XML sitemap entry. Do not add individual product URLs. Eight bilingual category names are now supplied in `menu-inventory.md`; final category copy and URL slugs are pending approval.

### Eight named category pages under two groups (proposed URL slugs)

All routes below are **URL candidates**, not approved or verified server paths. The same slug is proposed in both locales for maintainability.

| Arabic | English | Arabic candidate | English candidate |
|---|---|---|---|
| القهوة الساخنة | Hot Coffee | `/menu/hot-coffee/` | `/en/menu/hot-coffee/` |
| المشروبات الساخنة | Hot Drinks | `/menu/hot-drinks/` | `/en/menu/hot-drinks/` |
| القهوة الباردة | Iced Coffee | `/menu/iced-coffee/` | `/en/menu/iced-coffee/` |
| الكراش | Crash | `/menu/crash/` | `/en/menu/crash/` |
| المشروبات المنعشة | Refreshing Drinks | `/menu/refreshing-drinks/` | `/en/menu/refreshing-drinks/` |
| المخبوزات والحلويات | Bakery & Desserts | `/menu/bakery-desserts/` | `/en/menu/bakery-desserts/` |
| الساندوتشات والكرواسون | Sandwiches & Croissants | `/menu/sandwiches-croissants/` | `/en/menu/sandwiches-croissants/` |
| السناكس | Snacks | `/menu/snacks/` | `/en/menu/snacks/` |

**SEO implication:** Drinks and Food group headings are not XML sitemap entries. 8 category URLs per language + 4 standard URLs per language = **24 proposed canonical pages** in the XML sitemap. No product URLs and no `#about` anchor URL. Ensure each category gets distinctive bilingual H1/title/description and HTML-readable product text.

### Proposed URL inventory

| Content | Arabic canonical candidate | English canonical candidate | Status |
|---|---|---|---|
| Home | `/` | `/en/` | Proposed |
| Menu index | `/menu/` | `/en/menu/` | Proposed routes, confirmed page type |
| Drinks / Food group headers | none | none | Confirmed Menu sections only; no separate URLs or XML sitemap entries |
| Each menu category | `/menu/{category-slug}/` | `/en/menu/{category-slug}/` | Confirmed dedicated pages; names supplied; slugs proposed |
| Branches | `/branches/` | `/en/branches/` | Proposed |
| Contact | `/contact/` | `/en/contact/` | Proposed |
| About (Home section) | `/#about` (proposed anchor) | `/en/#about` (proposed anchor) | Confirmed section only; **exclude anchors from XML sitemap** |

**All final public URLs must use the chosen production host, consistent HTTPS + host preference, trailing-slash policy, and canonicalization.** Do not assume the server supports directory-style routes until hosting is checked. If not, use an equivalent stable `.html` scheme and adapt every reference consistently.

## 3. Target searches and page intent (research pending)

No actual search-volume or competitor ranking data have been collected. Avoid claims of high-volume keywords.

| Page | Likely user intent | Example discovery themes (not validated keywords) |
|---|---|---|
| Home | Identify brand and its offering | Moon Café / مون كافيه, coffee brand in Saudi Arabia |
| Menu | Browse offerings and item information | منيو مون كافيه, Moon Café menu, products/calories/prices |
| Branches | Find physical locations | فروع مون كافيه, Moon Café branches, university-specific branch names |
| Contact | Find official channels | التواصل مع مون كافيه, Moon Café contact |

**Content rules:** prioritise accurate brand names and natural Arabic/English copy; do not stuff keywords; do not claim availability in a branch unless verified; do not create city/branch landing pages solely for SEO without a clear user need and approved scope.

## 4. On-page SEO implementation

### 4.1 Per-page metadata

- Unique, descriptive `<title>` on **every language-specific URL**. Brand name and page purpose, with natural phrasing; no hard character-count rule.
- Unique `<meta name="description">` aligned with visible page content; not a ranking guarantee or fixed-length requirement.
- Absolute self-referencing `<link rel="canonical">` for each language page (do **not** canonicalize Arabic to English).
- Correct `<html lang="ar" dir="rtl">` or `<html lang="en" dir="ltr">`; translate navigation, visible copy, titles, descriptions, and meaningful image alts.
- Pair equivalent Arabic/English URLs with reciprocal `hreflang="ar-SA"` and `hreflang="en"` links (or `ar` / `en` if broader markets are approved); self-referential entries included. Use `x-default` pointing to `/` only if a deliberate fallback is desired; it is optional and must not contradict Arabic/English `hreflang` pairs.
- Descriptive Open Graph title, description and real branded share image; social preview metadata are useful but are separate from search ranking.
- Favicon and consistent site name/branding.

**Metadata template (illustrative, not final published copy):**

```html
<html lang="ar" dir="rtl">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>منيو مون كافيه | Moon Café</title>
  <meta name="description" content="تعرّف على مشروبات ومنتجات مون كافيه، والأسعار والسعرات الحرارية المتاحة لكل حجم.">
  <link rel="canonical" href="https://www.mooncafe-sa.com/menu/">
  <link rel="alternate" hreflang="ar-SA" href="https://www.mooncafe-sa.com/menu/">
  <link rel="alternate" hreflang="en" href="https://www.mooncafe-sa.com/en/menu/">
</head>
```

### 4.2 Heading hierarchy and semantics

- One clear **primary H1 topic** per page as a straightforward editorial convention, then H2 for major sections, H3 for nested sections; don't use headings merely to control font size.
- Sample hierarchy: Menu index: H1 for menu, H2 for category teasers. Each category page: one category H1, optional subcategory H2, product titles as H2/H3 in a meaningful semantic hierarchy (do not choose headings for visual size alone).
- Home H1 should express the brand rather than a generic “Welcome”; exact copy is deferred to content/design.
- Use semantic `<header>`, `<nav>`, `<main>`, `<section>` when appropriate, `<footer>` and real text links.
- Never replace searchable product names, prices, ingredient text or branch addresses with text baked into images.

### 4.3 Images & alt text

- Informational images: concise, factual, context-aware `alt` in the page language, e.g. `alt="كابتشينو من مون كافيه"`; translate for English.
- Decorative patterns/backgrounds: `alt=""` if `<img>` is used; ideally decorative CSS where appropriate.
- Linked logo: accessible name consistent with destination; avoid redundant repeated announcement.
- Filenames describe content (`moon-cafe-cappuccino.webp`) and assets use meaningful paths. Filenames alone don't replace `alt`.
- Compression, responsive `srcset`/`sizes`, WebP/AVIF as appropriate, declared width/height; lazy-load below-the-fold images, **not** the LCP/hero image.
- Confirm the supplied photography represents actual menu products, not branding mockups misrepresented as real items.

### 4.4 Internal links

- Primary navigation links directly to Home/Menu/Branches/Contact in each language; no JS-only click targets for fundamental navigation.
- Home links naturally to Menu and Branches; Contact and Branches link to official contact and verified directions.
- Language switch links to equivalent page, not always Home.
- No broken anchors, empty `href`, placeholder destinations, orphan pages or duplicate URL variants.

## 5. Crawlability, indexability and static rendering

- Product names, sizes, ingredients, prices, calories, and branch name/address must be crawlable in **rendered HTML**. Prefer pre-rendered/static HTML for key content, or validate indexing/rendering if JS injects JSON-fed content; a database is not required for search engine visibility.
- Ensure stable 200 HTTP responses for published pages and meaningful 404 for removed pages.
- Do not use `noindex` on published pages. Staging must be blocked from indexing (password protection preferred); remove any staging-only protection/`noindex` on production.
- No robots disallow rule that blocks required JS/CSS/content. `robots.txt` controls crawling, **not** reliable removal from search results.
- Use relative local paths for assets, valid UTF-8 and text content in both languages.

## 6. `sitemap.xml` — XML sitemap requirements

**Build during development from the *approved* canonical URL inventory.** It is not sensible to ship a production sitemap until route names and hosting behavior are final.

- Serve publicly at `https://www.mooncafe-sa.com/sitemap.xml` (or the approved canonical host).
- Include only live, indexable **200-status canonical URLs**, both languages; no old URLs, redirects, About anchors, product anchors, external loyalty URL, staging, images-only asset files or 404s.
- Use absolute URLs and UTF-8 XML; include optional `lastmod` **only** when it is accurate and updated on substantial page changes.
- A simple `urlset` is sufficient for this small site. `hreflang` may be placed on pages in `<head>`; no need to duplicate in XML. If both implementations are chosen, keep them synchronized.
- Reference the sitemap in root `robots.txt`:

```txt
User-agent: *
Allow: /

Sitemap: https://www.mooncafe-sa.com/sitemap.xml
```

**Draft example only — NOT ready to deploy:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://www.mooncafe-sa.com/</loc></url>
  <url><loc>https://www.mooncafe-sa.com/menu/</loc></url>
  <!-- Add one URL for EACH approved Arabic category page; slugs TBD -->
  <url><loc>https://www.mooncafe-sa.com/branches/</loc></url>
  <url><loc>https://www.mooncafe-sa.com/contact/</loc></url>
  <url><loc>https://www.mooncafe-sa.com/en/</loc></url>
  <url><loc>https://www.mooncafe-sa.com/en/menu/</loc></url>
  <!-- Add one URL for EACH approved English category page; slugs TBD -->
  <url><loc>https://www.mooncafe-sa.com/en/branches/</loc></url>
  <url><loc>https://www.mooncafe-sa.com/en/contact/</loc></url>
</urlset>
```

If Search Console remains out of scope, the sitemap can still be discovered through `robots.txt`, but verification of discovery/indexing is more limited. Adding Search Console is a **future recommendation only**, not a silent change of scope.

## 7. Structured data (PROPOSED; verified facts only)

- Homepage: evaluate `Organization` (or suitable `LocalBusiness`) JSON-LD with official name, logo URL, website URL, and verified `sameAs` links.
- Branches page: evaluate `CafeOrCoffeeShop` / `LocalBusiness` JSON-LD for verified physical locations only. Each entry needs its own accurate name/address and other supported factual properties; don't mark all branches as one misleading location.
- Do not invent ratings, reviews, opening hours, phones, coordinates or offers. Do not add shopping `Product`/`Offer` markup merely to imply online sales or obtain rich results; decide any appropriate schema only after verifying eligibility and on-page content.
- Structured data must match content visible to users, validate syntax, and does not guarantee rich results.

## 8. Local SEO (branches)

- Keep official Arabic/English branch names consistent across the site and verified Google Maps/Business Profile listings where those exist.
- Include full text address, university/building/area and verified directions link for each branch; only show hours/phone after confirmation.
- No embedded Google Maps API is needed for simple outbound directions.
- No standalone branch landing pages are included in current scope; consider them only through a documented future change request.

## 9. Migration & URL preservation — CRITICAL

New codebase does not mean throwing away existing indexed URLs.

1. Before implementation, export/crawl the current live URL set (Arabic and English, including product-category pages), collect URLs linked from menus and any backlinks available.
2. Create a mapping **old URL → closest relevant new URL**, including historical category pages to map to their closest new category URLs; do not redirect every unrelated page automatically to Home.
3. Implement **server-side 301/308 redirects** where applicable, not only JavaScript redirects; host capabilities determine rules.
4. Avoid chains/loops; update internal links, canonical and hreflang to point directly at new URLs.
5. Verify old URLs return intended redirects and new URLs return 200; maintain redirects long-term, ideally at least a year and longer if useful.
6. Save a backup of old site before switching hosting/DNS.

**Pending:** actual legacy URL list, destination route format, and hosting-level redirect controls. Do not generate a final redirect map from assumptions.

## 10. Performance & accessibility as SEO-supporting quality

- Target strong mobile CWV: LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 at 75th percentile of real users, where field data are available; these are proposed targets, not measured results.
- Compress images, avoid render-blocking scripts, reserve image dimensions, limit third-party requests, load only necessary JS/CSS.
- Support keyboard access, sufficient text contrast on dark backgrounds, semantic headings, language/direction attributes, and descriptive link names.
- Performance work serves user experience first; a passing Lighthouse score alone does not guarantee rankings.

## 11. Phased SEO implementation checklist

### During requirements / IA
- [x] Confirm About section is within Home (no About page).
- [ ] Approve final bilingual URL patterns and menu taxonomy.
- [ ] Confirm directory-style URL support and canonical host; Arabic root-language behavior is approved.
- [x] Confirm separate category landing pages and no per-product landing pages.
- [x] Record 8 bilingual categories (69 listed entries); [ ] confirm final URL slugs and whether internal subcategory headings are needed.
- [ ] Gather verified brand facts, branch list, product copy, images, and current URL inventory.
- [ ] Decide page intent and write Arabic/English metadata briefs.

### During development
- [ ] Build crawlable semantic HTML for key menu and branch content.
- [ ] Implement unique per-page titles and meta descriptions for each language.
- [ ] Implement canonical and reciprocal hreflang on equivalent page pairs.
- [ ] Implement `lang`/`dir`, H1→H2→H3 heading structure and image alts.
- [ ] Implement responsive image optimization and meaningful internal links.
- [ ] Implement justified structured data with verified values only.
- [ ] Generate final `sitemap.xml` from canonical approved routes.
- [ ] Create `robots.txt`, align it with robots/noindex production rules.
- [ ] Implement legacy 301/308 redirect map and 404 handling.

### Pre-launch QA
- [ ] Crawl all language URLs and validate 200/3xx/404 behavior.
- [ ] Validate XML and check each URL in sitemap (correct host, indexable, 200, canonical).
- [ ] Validate HTML titles, descriptions, headings, alt text, canonical/hreflang and schema.
- [ ] Confirm no staging `noindex` or auth protections survive on production.
- [ ] Verify menu and branch details in rendered HTML even without user interactions.
- [ ] Verify links from Menu index to category pages and category product listings, all Maps links and rewards link.
- [ ] Test 301 redirects from legacy URLs, avoiding loops and unrelated destinations.
- [ ] Review Core Web Vitals/Lighthouse and mobile rendering.

### Post-launch
- [ ] Verify public reachability of sitemap and robots.txt, correct redirects, SSL, host consistency and expected pages.
- [ ] Periodically inspect key pages and broken links manually (since Search Console/Analytics are excluded).
- [ ] Update sitemap `lastmod` only on genuine changes and redeploy when page URLs change.

## 12. Decision register

| ID | Open item | When needed |
|---|---|---|
| SEO-01 | About is a section within Home; no standalone About URL | Confirmed 2026-11-19 |
| SEO-02 | Root Arabic routing **CONFIRMED**; verify directory-style paths, trailing slash and canonical host on hosting. | Before dev |
| SEO-03 | Actual legacy URL map and server redirect support? | Before deployment design |
| SEO-04 | Approved page copy and unique meta descriptions in both languages? | Content sign-off |
| SEO-05 | Verified branch addresses, links, hours/phones and official profiles? | Structured data/branches QA |
| SEO-06 | Brand founding year (2007 vs 2010)? | Brand copy sign-off |
| SEO-07 | Should Search Console remain excluded after launch? | Optional client scope reconsideration |

## 13. Reference material (external, guidance; not client-confirmed requirements)

- Google Search Central — Build and submit sitemap: https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- Google Search Central — SEO guide for developers: https://developers.google.com/search/docs/fundamentals/get-started-developers
- Google Search Central — Image SEO best practices: https://developers.google.com/search/docs/appearance/google-images
- Google Search Central — Canonical URLs: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- Google Search Central — Local business structured data: https://developers.google.com/search/docs/appearance/structured-data/local-business
- Google Search Central — Title links: https://developers.google.com/search/docs/appearance/title-link

### Decision update — 2026-11-19

The Menu landing page must visibly distinguish **Drinks (المشروبات)** and **Food (الأكل)** and link directly to each group’s assigned category pages. Preserve plain HTML anchor links to all eight categories for discoverability; avoid making category links accessible only after JavaScript. The grouping does **not** change the count of URLs in `sitemap.xml` (24 proposed localized page URLs).


## 14. Development-stage SEO coordination — 2026-11-23

- The accepted desktop screens are **visual references only**. They contain illustrative product names, prices, branch names/addresses and rewards claims that are **not approved SEO copy**; use only verified copy/metadata.
- The **Branches** page displays a three-column desktop **grid**, not a list. This has **no effect** on the SEO page inventory or URLs; ensure actual branch names, verified addresses and directions remain accessible as semantic HTML.
- **Responsive layouts are implemented while coding.** Test heading order, links, text visibility and image alt behavior at phone, tablet and desktop sizes in both locales; avoid JS-only hidden category links.
- The Home page **Rewards** and **About** sections are same-page anchors only, not indexed standalone pages. The featured-product homepage carousel is presentation, not new product URLs.
- The **Arabic-default path convention is confirmed**; the detailed **24 route implementations** still require hosting/legacy-URL verification; do not ship `sitemap.xml` with speculative paths.

## 15. Confirmed default language: Arabic at the root (2026-11-23)

- **Arabic homepage:** `https://www.mooncafe-sa.com/` — render Arabic HTML directly, with `lang="ar" dir="rtl"`.
- **Arabic internal pages:** `/menu/`, `/menu/{category-slug}/`, `/branches/`, `/contact/` — no `/ar/` prefix.
- **English equivalent pages:** `/en/`, `/en/menu/`, `/en/menu/{category-slug}/`, `/en/branches/`, `/en/contact/` — with `lang="en" dir="ltr"`.
- **Canonicals:** each Arabic/English URL must canonicalize to **itself**, not to the other language. The Arabic root `/` is not a redirect or duplicate of English.
- **`hreflang`:** reciprocal pairs on both translated pages (Arabic `ar-SA` or `ar` as approved, English `en`); do not point to `/ar/`. Optional `x-default` can point to `/` for fallback.
- **`sitemap.xml`:** include both languages' 24 canonical pages (12 Arabic root-based and 12 English `/en/`), excluding redirects and non-page section anchors.
- **Language switcher:** ` /menu/iced-coffee/ ↔ /en/menu/iced-coffee/` and `/ ↔ /en/`, preserving the equivalent page.
- **Legacy `/ar/` URLs:** do not manufacture a redirect target list; if they were publicly used, consider permanent redirects to Arabic root-based equivalents after auditing existing URLs and hosting rules.
- **Hosting requirement:** check that folder `index.html` correctly serves its directory route, and redirect/canonicalize the trailing-slash variants consistently.
