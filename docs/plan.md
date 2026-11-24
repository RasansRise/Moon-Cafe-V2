# Moon Café — Website Redesign & Rebuild Plan

> **Document type:** Project implementation plan / single source of truth for scope and requirements  
> **Version:** 1.6 — Developer handoff reconciliation (2026-11-23)  
> **Prepared:** 2026-11-19  
> **Status:** Working implementation baseline — desktop visual structure accepted by project owner; content, responsive QA, hosting and client sign-off pending  
> **Website:** https://www.mooncafe-sa.com/  
> **SEO companion:** `seo-strategy.md` — proposed website sitemap, URL plan, technical/on-page/local SEO and launch checklist.  
> **Design companion:** `design.md` — approved desktop visual reference, components, planned behavior and implementation-time responsive rules.

## 0. How to use this document

This file is the primary reference for what to build and how to validate the Moon Café website. All work should be traced back to a requirement or an explicitly approved change. It does **not** approve a particular visual layout; those decisions belong in `design.md`.

**Requirement status legend:**
- **[CONFIRMED]** — explicitly agreed based on client/project discovery.
- **[PROPOSED]** — recommended approach, subject to approval / verification.
- **[TBD]** — unanswered, awaiting information or a decision.
- **[OUT OF SCOPE]** — specifically excluded from this release.

**Priority:** P0 = required before launch; P1 = important; P2 = optional/post-launch.  
**Change process:** Record a request, its reason and its impact on scope, timing and content; get client approval before implementation. Update this file and the decision log.

---

## 1. Project overview

### 1.1 Background

Moon Café has an existing bilingual informational website that introduces the brand, shows its menu/products and branch locations, and provides contact information. The current website is considered dated in visual presentation and content, with an unclear homepage structure, an inconvenient menu experience, and a branches page that needs substantial improvement.

### 1.2 Problem statement

Users—especially university students looking for menu details or branch locations—need to find information quickly and clearly. The current site does not sufficiently represent Moon Café's established brand or make essential information as accessible as desired.

### 1.3 Project type and approach

- **[CONFIRMED]** Build the new website **from scratch**, rather than modifying/reusing the old site's code.
- **[CONFIRMED]** Use **HTML, CSS and vanilla JavaScript**; do not introduce React, Next.js, a database, or a custom admin dashboard by default.
- **[CONFIRMED]** The site is **informational/catalogue-only**, not an online store.
- **[CONFIRMED]** A dark overall visual direction is required; detailed design decisions will be documented in `design.md`.
- **[PROPOSED]** Use static, structured content files to keep the site maintainable without a backend.

### 1.4 Users

- **Primary:** University students (many existing branches are located in universities).
- **Secondary:** Coffee lovers and other people interested in the brand and its menu.
- **[PROPOSED]** Prioritize quick mobile journeys, while supporting desktop and tablet equally well.

## 2. Business objectives and success criteria

| ID | Objective | Acceptance / evidence | Status |
|---|---|---|---|
| OBJ-01 | Modernize brand presentation and explain Moon Café's history and identity | Client approves content and final visual presentation; story is accurate and consistent across languages | [CONFIRMED objective / PROPOSED acceptance] |
| OBJ-02 | Make the menu easier to navigate and its information clearer | Users can identify product name, image, ingredients, relevant sizes, prices, and calories for each applicable size without opening a separate product page | [CONFIRMED] |
| OBJ-03 | Make branch information easy to find and understand | User can identify a branch, find its confirmed address, and open directions where a valid link is available | [CONFIRMED objective / PROPOSED acceptance] |
| OBJ-04 | Keep the website simple and fast | Test against agreed performance targets on mobile and desktop | [CONFIRMED objective / PROPOSED measurable target] |
| OBJ-05 | Consistent bilingual experience | Arabic and English pages have equivalent key information, functioning navigation and correct text direction | [CONFIRMED] |

### 2.1 Proposed measurable quality gates (to ratify)

- **[PROPOSED]** Mobile Lighthouse Performance >= 90 on representative pages using a repeatable testing setup; Accessibility and Best Practices >= 90. These are **targets**, not current measurements.
- **[PROPOSED]** Core Web Vitals targets: LCP <= 2.5 s, INP <= 200 ms, CLS <= 0.1 at the 75th percentile once real-user data is available. Lab measurements are diagnostic, not equivalent to field data.
- **[PROPOSED]** Test 3–5 representative users: locate a specified item with its calories and price, and identify a specified branch and directions, without moderator assistance. Agree timing/accuracy thresholds before testing.
- **[PROPOSED]** No critical keyboard, contrast or navigation barriers at launch; WCAG 2.2 AA as an accessibility goal where feasible.

## 3. Scope boundaries

### 3.1 Confirmed in scope

- Rebuild the existing informational website using HTML, CSS and JavaScript.
- Arabic and English language experiences, including RTL/LTR behavior.
- A newly organized homepage focused on the brand and its established history.
- A main Menu landing page organized under **two navigation groups: Drinks (المشروبات) and Food (الأكل)**, with **one dedicated page per approved product category** in each language; no standalone product detail pages.
- Products display the **name, image, price, calories** (where applicable by size), and **ingredients**.
- Variable product configurations: some items have multiple sizes; others may have a single size or different applicable fields.
- A **3-column desktop branches card grid**, using the **new final client-approved branch list** and a photo per branch; responsive adaptation during implementation.
- Contact information and clickable communication links.
- Link to the **external points/redemption program** and explanation of how it works (approved content and destination pending).
- Responsive behavior, performance optimization, basic on-page technical SEO and quality assurance.
- Original copywriting in Arabic and English (source content/assets to be provided and reviewed).

### 3.2 Explicitly out of scope

- **[OUT OF SCOPE]** Online ordering, cart, checkout, payment collection or sales transactions.
- **[OUT OF SCOPE]** Individual product detail pages.
- **[OUT OF SCOPE]** Product search (this is a project choice, *not* a technical consequence of lacking a database).
- **[OUT OF SCOPE]** Branch filtering by area/university; use a straightforward **card grid**, with no filters.
- **[OUT OF SCOPE]** Downloadable PDF menu; menu is available on the website only.
- **[OUT OF SCOPE]** Contact form; contact details and external links only.
- **[OUT OF SCOPE]** Google Analytics and Google Search Console integrations.
- **[OUT OF SCOPE]** Client-facing product or branch editing dashboard / CMS.
- **[OUT OF SCOPE]** New standalone Privacy Policy / Terms pages unless legal or operational requirements later make them necessary (then raise a change request).
- **[OUT OF SCOPE]** Loyalty points balance, login, redemption or integration inside this website; only outbound link/instructions.

### 3.3 Pending scope decisions

- **[CONFIRMED]** About/brand story is a section on Home; no standalone About page.
- **[CONFIRMED]** Four core page types per language (Home, Menu, Branches and Contact), **plus one page for each product category per language**. Total count = 8 + (2 × approved category count). Exact URL format/slugs remain proposed; category count is now **8**.
- **[CONFIRMED]** Each product category has a dedicated page. **[CONFIRMED working inventory]** Eight named categories and 69 listed entries are documented in `menu-inventory.md`; they are now organized into two CONFIRMED menu groups (Drinks: 5 categories / 38 entries; Food: 3 categories / 31 entries). These groups organize navigation, **not additional landing pages**. No further subcategories were supplied.
- **[TBD]** Actual brand founding/operating date; manual examples show **Since 2007** while previous site review identified a reference to 2010. Do not publish either until validated.
- **[TBD]** Whether all branches have precise Google Maps links, opening hours and phone numbers; do not invent missing fields.

## 4. Information architecture / tentative page responsibilities

| Page | Intended responsibility | Status |
|---|---|---|
| Home | Introduce brand; Hero with its own Menu CTA, About, **Featured Menu product carousel**, Branches Preview, Loyalty instructions/outbound link | [CONFIRMED visual structure / pending content] |
| Menu index | Present two main sections, **Drinks (المشروبات)** and **Food (الأكل)**; each lists its categories and links directly to the category pages | [CONFIRMED] |
| Category page (one per category per language) | Three-column desktop **product card grid**; details opened via an accessible popup with ingredients and variant-specific prices/calories; no product detail page | [CONFIRMED visual pattern / data TBD] |
| Branches | Show a **grid of branch cards** (desktop 3 / tablet target 2 / mobile target 1), with verified photos, addresses and directions links; no filters | [CONFIRMED layout / PROPOSED responsive columns] |
| Contact | Show contact channels and outbound links; no form | [CONFIRMED] |
| About (Home section) | Brand introduction and heritage content within the Home page, not an independent URL | [CONFIRMED] |


### 4.1 Confirmed menu hierarchy (2026-11-19)

**Menu → Drinks (المشروبات)** — 5 categories, 38 listed entries:

| Category (AR) | Category (EN) | Listed entries |
|---|---|---:|
| القهوة الساخنة | Hot Coffee | 17 |
| المشروبات الساخنة | Hot Drinks | 9 |
| القهوة الباردة | Iced Coffee | 4 |
| الكراش | Crash | 3 |
| المشروبات المنعشة | Refreshing Drinks | 5 |

**Menu → Food (الأكل)** — 3 categories, 31 listed entries:

| Category (AR) | Category (EN) | Listed entries |
|---|---|---:|
| المخبوزات والحلويات | Bakery & Desserts | 17 |
| الساندوتشات والكرواسون | Sandwiches & Croissants | 10 |
| السناكس | Snacks | 4 |

**Totals:** 8 category pages per language; 69 supplied menu entries. Each category has its own dedicated page; the two parent menu groups are **navigation/content sections, not separate webpages**. Overall page count stays **24 localized pages** (4 core + 8 category pages in each language). Proposed category slugs are listed in `menu-inventory.md` and `seo-strategy.md`; no extra `/menu/food/` or `/menu/drinks/` URL is approved. Product names and variants are preserved in the inventory and still need final validation.

**Navigation:** Desktop **Mega Menu** with Drinks/Food columns, eight category links and **Explore Full Menu** is accepted as a visual baseline; mobile accordion/navigation behavior is specified for implementation in `design.md`. **External points program:** provide an obvious link and clear instructions in a suitable location, to be finalized during content/UX planning; it is **not** an internal loyalty system.

## 5. Functional requirements

| ID | Requirement | Priority | Status |
|---|---|---|---|
| FR-01 | All approved pages accessible in Arabic and English | P0 | [CONFIRMED] |
| FR-02 | Correct language direction, translated navigation and page content | P0 | [CONFIRMED] |
| FR-03 | Provide an obvious way to switch languages while retaining equivalent page context where possible | P0 | [PROPOSED] |
| FR-04 | Menu index displays two main groups—Drinks and Food—with their respective category links; each category leads to a dedicated localized crawlable page | P0 | [CONFIRMED] |
| FR-04A | Every category page has a stable URL and displays its category products without separate product pages; no separate parent-group pages | P0 | [CONFIRMED] |
| FR-05 | Product listing shows a product name and image | P0 | [CONFIRMED] |
| FR-06 | Product **details popup** shows ingredients when provided; product grid itself stays visually lightweight | P0 | [CONFIRMED behavior / content pending] |
| FR-07 | Product listing shows size-specific prices and calories where sizes exist; a single-size item works without artificial sizes | P0 | [CONFIRMED] |
| FR-08 | No separate product URLs/detail pages are required | P0 | [CONFIRMED] |
| FR-09 | Same menu and prices apply across all branches | P0 | [CONFIRMED] |
| FR-10 | Branches appear in a **grid of cards** with a photo, name, address and verified directions action, sourced from a verified master sheet; target 3 desktop / 2 tablet / 1 mobile columns | P0 | [CONFIRMED visual baseline / PROPOSED responsive layout] |
| FR-11 | Show branch address and link to Google Maps directions **only when verified** | P0 | [PROPOSED; data pending] |
| FR-12 | Display branch hours/phone **only where client supplies and verifies these values** | P1 | [TBD data availability] |
| FR-13 | Contact page shows client-approved contact methods as clickable links | P0 | [CONFIRMED] |
| FR-14 | Include external loyalty-program link and approved instructions explaining how to use it | P0 | [CONFIRMED concept / TBD details] |
| FR-15 | Website operates without database, online transactions, contact forms or admin dashboard | P0 | [CONFIRMED] |
| FR-16 | Product and branch updates are performed by a developer editing project files and redeploying | P0 | [CONFIRMED] |
| FR-17 | No product search, branch filters or downloadable PDF menu | P0 | [CONFIRMED] |
| FR-18 | On desktop, header Menu offers a **two-column Mega Menu** (Drinks/Food) and a View All Menu destination; on compact screens use expandable mobile navigation | P0 | [CONFIRMED visual structure / PROPOSED responsive behavior] |
| FR-19 | Product cards open keyboard-accessible details dialog; no product detail page | P0 | [CONFIRMED interaction / PROPOSED accessibility contract] |
| FR-20 | Homepage **Hero Explore Menu CTA** points to locale-specific Menu page, independent of header CTA | P0 | [CONFIRMED] |
| FR-21 | Homepage features a product preview carousel, About, branch preview and Rewards section with external provider link | P0 | [CONFIRMED structure / rewards content TBD] |

### 5.1 Edge-case rules for product display

- **[PROPOSED]** Never display invented or automatically duplicated prices/calories.
- **[PROPOSED]** If an approved product is available in only one configuration, omit a size selector unless useful for clarity.
- **[PROPOSED]** If an item has multiple sizes, represent each size with its own verified price and calories; do not assume equal calories or pricing.
- **[PROPOSED]** Do not show placeholders such as `0 kcal`, `0 SAR`, or `N/A` as if they were verified facts. Flag missing mandatory data for the client before launch.
- **[TBD]** Whether ingredients are only text or also require allergen labeling; allergen disclosure was **not** confirmed.

## 6. Content and data model (implementation proposal)

**[PROPOSED]** Maintain content in version-controlled JSON (or JS data modules) and local optimized images. No database, CMS or backend required for the confirmed scope. Keep business data separate from layout code so developer updates do not require modifying page HTML manually.

### 6.1 Product data — proposed logical schema

```json
{
  "id": "example-product-id",
  "menuGroupId": "drinks-or-food",
  "categoryId": "example-category-id",
  "subcategoryId": null,
  "name": { "ar": "...", "en": "..." },
  "image": "/assets/products/example.webp",
  "ingredients": { "ar": "...", "en": "..." },
  "variants": [
    { "sizeId": "regular", "sizeLabel": { "ar": "...", "en": "..." }, "priceSar": null, "caloriesKcal": null }
  ],
  "displayOrder": 1,
  "isVisible": true
}
```

The example uses **null solely as a placeholder**, never as a value to display. For a single-size product, use one variant; user-facing presentation need not display its size label. The group key is a logical navigation property (drinks/food), not an extra page. Additional subcategory fields are optional and not currently approved. Currency is presumed to be SAR because the café operates in Saudi Arabia—**confirm with the final menu sheet**.

### 6.2 Branch data — proposed logical schema

```json
{
  "id": "example-branch-id",
  "name": { "ar": "...", "en": "..." },
  "address": { "ar": "...", "en": "..." },
  "universityOrArea": { "ar": "...", "en": "..." },
  "googleMapsUrl": null,
  "openingHours": null,
  "phone": null,
  "displayOrder": 1
}
```

Only render validated fields. **No branch search or filters**; the university/area field can clarify a branch card without offering filtering.

### 6.3 Other content and asset requirements

- **[CONFIRMED]** Write new website copy, not merely reuse old copy as-is.
- **[CONFIRMED]** Client will provide updated product information, approved branch list, images and relevant content; these have **not yet been received**. All screenshot copy, sample item photos, prices, hours, city names and rewards claims are placeholders only.
- **[CONFIRMED]** Images/assets are expected to be supplied with sensible filenames and product/branch associations; validate actual delivery.
- **[PROPOSED]** Build an inventory sheet for products, variants, ingredients, translations, images and status; separate inventory for branches.
- **[PROPOSED]** Maintain page-level Arabic/English copy in structured files and proofread both independently.
- **[TBD]** Definitive establishment year, full brand story, final category names, actual product counts, branch-specific fields and loyalty program details.

## 7. Brand inputs (reference only; detailed design deferred)

The provided **Moon Café Brand Manual.pdf** (74 pages) is an approved project reference, **subject to confirming whether it is the latest edition**. Its logo guidelines include Arabic and English treatments, monochrome variants and restrictions on distortions and effects (roughly pp. 5–12). Page 13 specifies primary gold `#DAAF67` with secondary values `#FED899` and `#FFE7C2`, alongside black/white. Page 14 specifies **Proxima Nova** (English) and **Helvetica Neue Arabic**. The manual also contains moon/coffee imagery, a geometric pattern and dark brand applications.

- **[CONFIRMED]** Client wants a dark-mode website.
- **[PROPOSED]** Preserve the brand identity instead of creating a new logo or brand system.
- **[TBD]** Verify use rights and obtain original SVG/logo and licensed web font files or an approved alternative if licenses are unavailable.
- **Deferred to `design.md`:** exact background values, contrast combinations, components, typography scale, spacing, patterns, composition, photography direction, responsive layouts and animations.

## 8. Technical approach

### 8.1 Architecture

- **[CONFIRMED]** HTML, CSS, vanilla JavaScript.
- **[CONFIRMED]** Start from a clean codebase; do not reuse legacy site code by default.
- **[CONFIRMED]** No database, custom backend or client-facing admin panel.
- **[PROPOSED]** Static HTML pages + organized CSS/JS modules + structured data files, with a build-free workflow unless asset tooling adds value.
- **[PROPOSED]** Reusable header, footer and product/branch rendering utilities, avoiding duplicative code and keeping both languages in sync.
- **[PROPOSED]** Avoid heavy third-party libraries; add them only where a proven requirement justifies their cost.

### 8.2 Localization

- **[CONFIRMED]** Complete Arabic and English site.
- **[CONFIRMED]** Arabic is the default language at `/`, with Arabic pages directly under `/menu/`, `/branches/` and `/contact/`; English pages use `/en/`. **[PROPOSED]** Directory-style URLs and exact slugs, subject to hosting/legacy-redirect checks.
- **[PROPOSED]** Set `lang` and `dir` appropriately, support RTL/LTR layout, translated metadata and accessible language switch.

### 8.3 Performance and accessibility

- **[PROPOSED]** Optimize/compress product images; prefer responsive WebP/AVIF with source fallback as appropriate.
- **[PROPOSED]** Avoid loading all menu imagery at full resolution on first paint; apply lazy loading outside the initial viewport, with a clear priority for the hero/LCP asset.
- **[PROPOSED]** Use semantic HTML, descriptive alt text, visible focus styles, keyboard-operable navigation and legible text contrast on dark backgrounds.
- **[PROPOSED]** Use system or properly licensed web fonts with loading/fallback strategy; defer font choice to design approval.
- **[PROPOSED]** Keep JS progressive where practical: core information remains discoverable; ensure rendering and indexing are tested if data are injected via JS.

### 8.4 SEO and redirects

- **[PROPOSED]** Preserve relevant existing URL equity with an explicit old-to-new URL map and permanent redirects if URLs change.
- **[PROPOSED]** Add per-language title/description, canonical/hreflang (when routing is confirmed), sitemap.xml and robots.txt; use `seo-strategy.md` for implementation rules and validation.
- **[PROPOSED]** Check metadata and product/branch visibility in source/rendered HTML; metadata alone is not a substitute for crawlable content.
- **[CONFIRMED]** Do **not** add Google Analytics or Search Console integrations, unless the client later changes scope. `sitemap.xml` and `robots.txt` are still part of the proposed SEO implementation even without Search Console.

### 8.5 Hosting / deployment

- **[TBD]** Domain/hosting access, current server capability, SSL, DNS and deployment method. Access will be requested when needed nearer launch; **do not postpone feasibility checks that require hosting information until the last day**.
- **[PROPOSED]** Prepare a staging preview before launch; back up the old site and save current DNS/server configuration.
- **[PROPOSED]** Agree deployment owner, rollback procedure and who maintains the website after handover.

## 9. Integrations and outbound links

| Integration | Decision |
|---|---|
| Online payment/order system | [OUT OF SCOPE] |
| Contact form/email delivery service | [OUT OF SCOPE] |
| Google Analytics / Search Console | [OUT OF SCOPE] |
| Google Maps | [PROPOSED] Outbound directions links per branch; no embedded map or API is required by default |
| Moon Café points/rewards app/program | [CONFIRMED] External link + explanation only; URL/instructions [TBD] |
| Social media / external channels | [PROPOSED] Link to approved official profiles once provided |
| PDF menu | [OUT OF SCOPE] |

## 10. SDLC execution phases and exit gates

### Phase 1 — Planning & Discovery
**Inputs:** client discussion, old website, brand manual.  
**Work:** goals, audience, scope, audit, risks, initial feasibility and plan.  
**Deliverables:** `plan.md`, outstanding decisions, initial content request, high-level estimates.  
**Exit:** client approves scope, major decisions/unknowns have owners, and the work is feasible.  
**Current status:** In progress; initial discovery complete, sign-off/feasibility pending.

### Phase 2 — Requirements & Information Architecture
**Work:** finalize page list, taxonomy and menu structure, product and branch field definitions, user journeys, accessibility/localization requirements and acceptance cases.  
**Deliverables:** approved sitemap, content inventory, detailed requirements/acceptance matrix.  
**Exit:** all launch-critical requirements are testable and signed off.

### Phase 3 — UI/UX Design
**Work:** desktop visual structure and shared components defined; responsive layout details are deliberately finalized and tested **during implementation**. Finish the Contact page specification and gather missing assets.  
**Deliverables:** `design.md`, six approved desktop visual references (Home, Menu, Category, Popup, Branches, Mega Menu), plus a Contact page specification; responsive behavior guidelines.  
**Exit:** project-owner-approved desktop visual baseline recorded; client/final approval and responsive verification remain pending. Do **not** treat placeholder copy in mockups as approved content.

### Phase 4 — Development
**Work:** codebase setup, **mobile-first responsive implementation alongside each page/component**, layouts/components, bilingual content handling, menu and branches data rendering, external links and optimization. Ensure desktop structure remains aligned with approved screenshots.  
**Deliverables:** complete staging website, developer update instructions.  
**Exit:** feature complete against approved scope.

### Phase 5 — QA and User Acceptance Testing
**Work:** functional checks, bilingual proofreading, cross-device/browser testing, performance, accessibility, SEO links, negative/edge-case tests and client review.  
**Deliverables:** test report, defect list, client UAT sign-off.  
**Exit:** no blocker/critical defects; agreed acceptance thresholds met.

### Phase 6 — Deployment & Handover
**Work:** hosting setup, old-site backup, redirect deployment, SSL/DNS, smoke test, rollback readiness and documentation.  
**Deliverables:** live site, source repository/package, content update guide, backup/rollback notes.  
**Exit:** final launch verification and client acceptance.

### Phase 7 — Maintenance
**Work:** address post-launch defects, content updates by developer, periodic checks and agreed maintenance.  
**Deliverables:** support responsibilities and change log.  
**Exit:** maintenance arrangement confirmed (period/frequency TBD).

## 11. QA / acceptance checklist (initial)

- [ ] Every approved page works in Arabic and English.
- [ ] Switching language leads to the corresponding content and correct text direction.
- [ ] All approved menu categories have working localized pages; their products appear in the correct category order.
- [ ] Single-size and multiple-size products display correct price and calorie values.
- [ ] Ingredients are accurate and available in both languages where provided.
- [ ] No product pages, search, ordering, checkout, contact form, branch filters or PDF menu are accidentally introduced.
- [ ] All branch names/addresses match the final approved list.
- [ ] Every displayed Maps link opens the correct branch location; missing links are not fabricated.
- [ ] External rewards-program link and instructions are correct and approved.
- [ ] All phone/email/social links work and point to approved destinations.
- [ ] Mobile/tablet/desktop and major browser tests pass.
- [ ] No visible layout breaks in RTL or LTR.
- [ ] Lighthouse and performance tests run on Home, Menu, Branches and Contact on representative devices.
- [ ] Keyboard navigation, contrast, focus indicators and alt text are reviewed.
- [ ] No broken links, missing images, console errors or malformed metadata.
- [ ] Old important URLs are mapped to working new URLs / redirects as applicable.
- [ ] Website has a working HTTPS certificate and a verified backup/rollback process.
- [ ] Client reviews the final release and signs off.

## 12. Risks, assumptions and dependencies

| ID | Risk / dependency | Impact | Mitigation / owner |
|---|---|---|---|
| R-01 | Updated menu, images and translations not yet delivered | Incomplete menu, stalled design/development | Client supplies; project team tracks asset checklist |
| R-02 | Final branch list/coordinates/hours not yet validated | Wrong directions or inaccurate information | Client provides and signs off branch sheet |
| R-03 | Brand heritage year unresolved (2007 vs 2010) | Incorrect brand story | Client confirms when copy is developed |
| R-04 | Drinks/Food navigation hierarchy now confirmed; grouping of S/D variants and exact URL paths remain unresolved | Rework in UI and data structure | Resolve during requirements phase before final design |
| R-05 | Hosting access not yet available | Deployment constraints / possible late blockers | Identify hosting setup early enough to test compatibility |
| R-06 | No fixed budget/deadline | Scope drift / open-ended project | Estimate effort and agree milestones and scope baseline |
| R-07 | Fonts may require licensing / redistribution restrictions | Unlicensed font usage | Obtain licensed webfonts or approve a substitute |
| R-08 | Client approvals or external rewards instructions delayed | Blocked content sign-off | One client approver; track decisions and content dependencies |
| R-09 | Client has no CMS; updates depend on developer | Operational latency after launch | Document file format and update/redeploy procedure |
| R-10 | Existing URLs not preserved after rebuild | Search traffic / broken inbound links | Capture current URL inventory, implement appropriate redirects |

## 13. Assets and information needed from client

- [x] Working list of 8 categories in 2 main menu groups and 69 menu entries supplied in Arabic and English (`menu-inventory.md`); [ ] client approval of final names/variant grouping and missing fields.
- [ ] Per-product name, image, ingredients, applicable sizes, price and calories by size.
- [ ] Final approved branch list, addresses and verified Google Maps links; hours/phone where available.
- [ ] Original brand logo source assets and confirmation that manual is current.
- [ ] New brand-story content and confirmed founding/operating year.
- [ ] Official social links, phone, email and any application store links to be displayed.
- [ ] Points-program official external URL, how-to instructions, eligibility and terminology.
- [ ] Approved media/photos and rights to use them on the website.
- [ ] Domain/hosting access and deployment contact before deployment preparation.

## 14. Open decisions register

| ID | Question | Owner | Due by | Status |
|---|---|---|---|---|
| D-01 | About / brand story is a Home section; no standalone About URL | Client | 2026-11-19 | CONFIRMED |
| D-02 | Dedicated pages per category confirmed; 8 supplied category names / 69 entries recorded; subcategory headings and canonical slugs? | Client / UX | Requirements sign-off | PARTIALLY CONFIRMED — 8 named categories |
| D-03 | Which year/history wording is authoritative? | Client | Content sign-off | TBD |
| D-04 | Do all branches have verified Maps links, hours and phone numbers? | Client | Branch data sign-off | TBD |
| D-05 | Product count recorded as 69 listed entries; verify variant grouping, final size/price/calorie/ingredient/image fields? | Client | Content inventory sign-off | TBD |
| D-06 | Official points-program URL and instructions, and where linked? | Client / UX | Content sign-off | TBD |
| D-07 | Final route structure and legacy URL redirects? | Developer | Before implementation | TBD |
| D-08 | Hosting specifics and production release ownership? | Client / Developer | Before deployment planning | TBD |
| D-09 | Webfont licensing and approved assets? | Client / Design | Design sign-off | TBD |
| D-10 | Project effort estimate, milestone dates and client approval? | Project lead / Client | Planning sign-off | TBD |
| D-11 | Exact measurable user-test and performance thresholds? | Project lead / Client | QA-plan approval | TBD |

## 15. Decision log

| Date | Decision | Status |
|---|---|---|
| 2026-11-19 | Rebuild from scratch using HTML/CSS/JS | Confirmed |
| 2026-11-19 | Bilingual Arabic/English; dark visual direction | Confirmed |
| 2026-11-19 | Informational site only; no online sales or separate product pages | Confirmed |
| 2026-11-19 | Product name, photo, ingredients, price/calories with flexible sizing | Confirmed |
| 2026-11-19 | One menu/pricing system across branches | Confirmed |
| 2026-11-19 | No product search or branch filtering | Confirmed |
| 2026-11-19 | No CMS/dashboard; developer-managed content changes | Confirmed |
| 2026-11-19 | No PDF menu, contact form, Analytics or Search Console integration | Confirmed |
| 2026-11-19 | Loyalty program represented by external link and explanation only | Confirmed |
| 2026-11-19 | Category slugs, optional subcategories, product variants, historical date and some branch fields left TBD | Open |
| 2026-11-19 | Add a dedicated localized page for every menu category; retain menu index and exclude individual product pages | Confirmed |
| 2026-11-19 | About/brand story will be a Home section, not a standalone page | Confirmed |
| 2026-11-19 | Add SEO strategy and proposed bilingual sitemap, XML sitemap/robots requirements, alt text, headings, metadata, canonical/hreflang and migration redirects | Proposed — pending implementation approval |
| 2026-11-23 | Approve latest desktop design structure/style only; do not approve any mockup content or fake data | Confirmed by project owner |
| 2026-11-23 | Branches grid (3 columns desktop), neutral card borders, two-column desktop Mega Menu and product details popup | Confirmed by project owner |
| 2026-11-23 | Responsive adaptation/QA incorporated into development; do not require pre-built mobile/tablet mockup sets | Confirmed by project owner |

## 16. Proposed repository layout (Arabic at the root; hosting routing to verify)

```text
moon-cafe/
├── docs/
│   ├── plan.md
│   ├── design.md
│   ├── seo-strategy.md
│   ├── menu-inventory.md
│   └── project-structure.md
├── index.html                    # Arabic homepage: /
├── menu/
│   ├── index.html                # Arabic menu: /menu/
│   ├── hot-coffee/index.html     # Each Arabic category has its own directory
│   ├── hot-drinks/index.html
│   ├── iced-coffee/index.html
│   ├── crash/index.html
│   ├── refreshing-drinks/index.html
│   ├── bakery-desserts/index.html
│   ├── sandwiches-croissants/index.html
│   └── snacks/index.html
├── branches/index.html           # Arabic branches: /branches/
├── contact/index.html            # Arabic contact: /contact/
├── en/
│   ├── index.html                # English homepage: /en/
│   ├── menu/
│   │   ├── index.html            # English menu: /en/menu/
│   │   └── <eight-category-slugs>/index.html
│   ├── branches/index.html
│   └── contact/index.html
├── assets/
│   ├── images/{products,branches,brand}/
│   ├── icons/
│   └── fonts/                    # Licensed brand font files, local only
├── css/{base,layout,components,pages,utilities}.css
├── js/{main,navigation,menu,popup,animations}.js
├── data/{products,branches,content}.json
├── robots.txt
├── sitemap.xml                   # Generate from final verified canonical URLs
└── 404.html
```

Arabic is the **[CONFIRMED] default language**: `/` is the Arabic homepage; Arabic inner pages also have no language prefix. English lives under `/en/`. The directory-style URLs and slugs are **[PROPOSED]** until the hosting configuration is verified. Static server-rendered HTML pages (or pre-generated HTML at build time) are preferred for crawlability; client-side JSON can enrich UI and modal behavior without making all menu content JavaScript-only.

---

## 17. SEO strategy and sitemap planning (added in v1.1)

- **[CONFIRMED page inventory / PROPOSED routes]** Four core pages per language plus a dedicated page for each category in each language: 8 + 2 × 8 = **24 indexable localized pages**. Confirmed default-language routing intent: Arabic homepage `/` and Arabic subpages without a locale prefix; English pages under `/en/`. Directory-style paths, slugs, and hosting behavior remain subject to verification.
- **[CONFIRMED]** About is a section of Home, with an optional in-page anchor such as `#about` for navigation only; it is not a separate indexed URL or `sitemap.xml` entry. Eight category names (69 entries) are supplied in `menu-inventory.md`; final slug paths and optional subcategories remain TBD. Category pages **are** indexable; no indexed product-detail or branch-detail pages are planned.
- **[PROPOSED]** Generate a real, publicly accessible `sitemap.xml` from approved canonical URLs during development; do not deploy the draft example as final. Link from `robots.txt`.
- **[PROPOSED]** Implement bilingual metadata, independent self-canonicals, reciprocal hreflang, descriptive alt text, semantic heading hierarchy, crawlable content, accessible internal links and validated branch/organization structured data only where supported by confirmed facts.
- **[PROPOSED]** Audit all existing Arabic/English URLs and deploy server-side redirects to relevant new URLs to protect existing discoverability.
- **[CONFIRMED]** Google Analytics and Google Search Console integrations remain out of scope. This does not prohibit technical SEO; it limits post-launch observability.
- **Reference:** `seo-strategy.md` contains the proposed URLs, requirements, examples, risks, decision register and phase-specific QA checklist. The final URL/metadata/redirect deliverables depend on confirmed content and hosting.

## 17.1 Developer handoff update — 2026-11-23

The six supplied **latest desktop references** are approved **for structure and styling only**: Homepage, Menu landing, Category Product page, Product Details Popup (open state), Branches Grid, and Mega Menu. The screenshots contain illustrative content; never publish sample prices, branch addresses, product names, rewards benefits or dates unless independently confirmed by client-provided final data.

**Shared visual choices:** dark background, exact Brand Manual font families and gold swatches; subtle **neutral 1px** borders on repeated cards; restrained gold accent/active states; a thin gold modal outline; a neutral outlined Mega Menu; desktop Menu sections (Drinks/Food), desktop category grid (Drinks 3 + 2, Food 3), three-column desktop product and branches grids. See `design.md` for responsive behavior.

**Responsive method:** no more obligatory Mobile/Tablet static image sets before code. Developer builds **mobile-first**, uses desktop screenshots as visual references, tests actual layout and interaction on mobile/tablet/desktop, then refines and obtains sign-off. **Contact visual mockup remains pending**; launch-critical client content and hosting access also remain pending.

## 18. Next action

1. Keep current desktop designs as **approved visual/structural references only**; no placeholder text, images or claimed facts are approved for publication.
2. Confirm **Contact page** appearance from the existing component system; no new form.
3. Begin implementation in **HTML, CSS, vanilla JS** with mobile-first behavior built and tested **as each section is implemented**; don't require another set of 18 static images.
4. Request actual content and verified product/branch/assets/loyalty URL; unresolved S/D grouping and missing per-variant information remain TBD.
5. Capture legacy URL inventory, confirm static-host routing/redirect capabilities early, and implement technical SEO alongside development.
6. Run AR/EN, accessibility, responsive, SEO, interaction and performance QA against real code; obtain client sign-off before launch.

> **Principle:** Unknowns remain `TBD` until verified. A design or implementation suggestion is not a client-approved requirement.

> **2026-11-19 update:** Eight category names and 69 listed menu entries supplied. See `menu-inventory.md`; do not infer prices, calorie counts, ingredients, image assets, or final variant grouping.

### Decision update — 2026-11-19: two main menu groups

- **[CONFIRMED]** Main Menu is divided into **Drinks / المشروبات** (Hot Coffee, Hot Drinks, Iced Coffee, Crash, Refreshing Drinks) and **Food / الأكل** (Bakery & Desserts, Sandwiches & Croissants, Snacks).
- **[CONFIRMED]** Group headers are a navigation and menu presentation hierarchy only; **do not create standalone Food or Drinks pages** under the present scope.
- **[CONFIRMED]** One page per category remains unchanged, so the count is **24 localized webpages** across AR/EN (assuming the proposed routing model).
- **[CONFIRMED — design.md]** Use two stacked **Drinks** and **Food** sections, with all eight category cards visible on the Menu landing page; no intermediate group pages.

### Arabic default routing decision — 2026-11-23

- **[CONFIRMED]** Arabic is the default and root-site language. `/` is the Arabic homepage; `/menu/`, `/branches/`, `/contact/` and `/menu/{slug}/` are Arabic URLs.
- **[CONFIRMED]** English is accessible under `/en/` (including `/en/menu/`, `/en/branches/`, `/en/contact/` and category pages).
- The language switcher must map each page to the *equivalent* page in the other language; Arabic links must not unexpectedly point to `/ar/`.
- The old `/ar/` prefix, if it ever existed publicly, is not an alternate canonical URL; only redirect it after confirming actual legacy URLs.
- See `project-structure.md` and `seo-strategy.md` for file paths, canonicals, `hreflang`, sitemap and redirect rules.
