#!/usr/bin/env python3
"""
Build the Menu section of the site (Arabic at /menu/…, English at /en/menu/…):

  /menu/                       Menu landing — all categories under "Drinks" and "Food"
  /menu/{category}/            One page per category — product grid + details popup
  (same under /en/menu/)

Sources:
  data/products.json           categories (group, cover image) and products
  index.html / en/index.html   shared header, side drawer and footer

Run from the project root:   python3 tools/build-menu.py
Re-run after changing products.json or the homepage header/footer.
All content is written as static HTML (crawlable, works without JS).
"""
import html
import json
import posixpath
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "data/products.json").read_text(encoding="utf-8"))
SITE = "https://www.mooncafe-sa.com"
CATS = DATA["categories"]
GROUPS = DATA["groups"]
PRODUCTS = DATA["products"]
BY_ID = {p["id"]: p for p in PRODUCTS}

ARROW = ('<svg class="icon-flip" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6" fill="none" '
         'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>')
CHEVRON = ('<svg class="icon-flip" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 5l7 7-7 7" fill="none" '
           'stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>')

T = {
    "ar": {
        "home_file": ROOT / "index.html", "home_base": "/", "prefix": "/", "dir": "rtl",
        "menu_title": "المنيو | مون كافيه",
        "menu_description": "تصفّح منيو مون كافيه: القهوة الساخنة والباردة، المشروبات المنعشة، المخبوزات والحلويات، الساندوتشات والسناكس.",
        "eyebrow": "مـــــون كافيـــــة",
        "h1": "المنيو",
        "intro": "اختر القسم واكتشف منتجاته.",
        "menu": "المنيو",
        "products": "{n} منتج",
        "explore": "اكتشف القسم",
        "explore_aria": "اكتشف {name}",
        "cat_title": "{name} | منيو مون كافيه",
        "cat_description": "{name} في منيو مون كافيه: {list}.",
        "breadcrumb": "مسار التنقل",
        "back": "العودة إلى المنيو",
        "prev": "القسم السابق",
        "next": "القسم التالي",
        "view": "عرض التفاصيل",
        "view_aria": "عرض تفاصيل {name}",
        "close": "إغلاق",
        "ingredients": "المكونات",
        "size": "الحجم", "price": "السعر", "calories": "السعرات",
        "pending": "التفاصيل قيد التأكيد.",
    },
    "en": {
        "home_file": ROOT / "en/index.html", "home_base": "/en/", "prefix": "/en/", "dir": "ltr",
        "menu_title": "Menu | Moon Café",
        "menu_description": "Browse the Moon Café menu: hot and iced coffee, refreshing drinks, bakery and desserts, sandwiches and snacks.",
        "eyebrow": "Moon Café",
        "h1": "Our Menu",
        "intro": "Pick a category and explore its products.",
        "menu": "Menu",
        "products": "{n} products",
        "explore": "Explore",
        "explore_aria": "Explore {name}",
        "cat_title": "{name} | Moon Café Menu",
        "cat_description": "{name} at Moon Café: {list}.",
        "breadcrumb": "Breadcrumb",
        "back": "Back to menu",
        "prev": "Previous category",
        "next": "Next category",
        "view": "View Details",
        "view_aria": "View details for {name}",
        "close": "Close",
        "ingredients": "Ingredients",
        "size": "Size", "price": "Price", "calories": "Calories",
        "pending": "Details pending confirmation.",
    },
}

esc = html.escape


# ---- URL helpers -----------------------------------------------------------
def to_abs(value, base):
    if value.startswith(("#", "http:", "https:", "mailto:", "tel:", "//")) or value == "" or value.startswith("/"):
        return value
    m = re.match(r"([^?#]*)(.*)", value)
    path, tail = m.group(1), m.group(2)
    norm = posixpath.normpath(posixpath.join(base, path or "./"))
    if (path == "" or path.endswith("/") or path in (".", "..")) and not norm.endswith("/"):
        norm += "/"
    return norm + tail


def to_rel(value, base):
    if not value.startswith("/") or value.startswith("//"):
        return value
    m = re.match(r"([^?#]*)(.*)", value)
    path, tail = m.group(1), m.group(2)
    r = posixpath.relpath(path, base.rstrip("/") or "/")
    if path.endswith("/") and not r.endswith("/"):
        r += "/"
    if r in (".", "./"):
        r = "./"
    if not r.startswith("."):
        r = "./" + r
    return r + tail


def rebase(fragment, old_base, new_base):
    return re.sub(r'\b(href|src)="([^"]*)"',
                  lambda m: f'{m.group(1)}="{to_rel(to_abs(m.group(2), old_base), new_base)}"', fragment)


# ---- shared header / drawer / footer from the homepage ---------------------
def shared_parts(lang, base, other_url, is_landing):
    t = T[lang]
    s = t["home_file"].read_text(encoding="utf-8")
    pre = s[s.index(">", s.index("<body")) + 1:s.index('<main id="main">')]
    footer = s[s.index('<footer class="site-footer">'):s.index("</footer>") + len("</footer>")]
    # Mark "Menu" as the current section (before rebasing, links are ./menu/)
    current = ' aria-current="page"' if is_landing else ' aria-current="true"'
    pre = pre.replace(' aria-current="page"', "")
    pre = pre.replace('class="primary-nav__link" href="./menu/"', f'class="primary-nav__link" href="./menu/"{current}', 1)
    pre = pre.replace('class="drawer__link" href="./menu/"', f'class="drawer__link" href="./menu/"{current}', 1)
    pre = rebase(pre, t["home_base"], base)
    footer = rebase(footer, t["home_base"], base)
    # Language switch → the equivalent page in the other language
    pre = re.sub(r'href="[^"]*"( hreflang="(?:ar|en)" lang="(?:ar|en)" data-lang-switch)',
                 f'href="{to_rel(other_url, base)}"\\1', pre)
    return pre, footer


def head(lang, base, title, description, ar_url, en_url, popup):
    rel = lambda p: to_rel(p, base)
    canonical = SITE + (ar_url if lang == "ar" else en_url)
    popup_js = f'\n  <script src="{rel("/js/popup.js")}" defer></script>' if popup else ""
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{T[lang]['dir']}" class="no-js">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <script>document.documentElement.classList.replace('no-js', 'js');</script>

  <!-- Generated by tools/build-menu.py — edit data/products.json or the script, not this file -->
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="ar-SA" href="{SITE}{ar_url}">
  <link rel="alternate" hreflang="en" href="{SITE}{en_url}">
  <link rel="alternate" hreflang="x-default" href="{SITE}{ar_url}">
  <meta name="theme-color" content="#080504">
  <link rel="icon" href="{rel('/assets/images/brand/logo.png')}" type="image/png">

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Moon Café">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:url" content="{canonical}">

  <link rel="stylesheet" href="{rel('/css/base.css')}">
  <link rel="stylesheet" href="{rel('/css/layout.css')}">
  <link rel="stylesheet" href="{rel('/css/components.css')}">
  <link rel="stylesheet" href="{rel('/css/pages.css')}">
  <link rel="stylesheet" href="{rel('/css/utilities.css')}">

  <script src="{rel('/js/navigation.js')}" defer></script>
  <script src="{rel('/js/animations.js')}" defer></script>
  <script src="{rel('/js/main.js')}" defer></script>{popup_js}
</head>"""


def products_in(cid):
    return [p for p in PRODUCTS if p["categoryId"] == cid]


def pname(p, lang):
    return p["name"].get(lang) or p["name"]["en"]


# ---- Menu landing ----------------------------------------------------------
def landing_main(lang, base):
    t = T[lang]
    rel = lambda p: to_rel(p, base)
    sections = []
    for g in GROUPS:
        cards = []
        cats = [c for c in CATS if c["group"] == g["id"]]
        for i, c in enumerate(cats):
            cover = BY_ID[c["cover"]]
            name = esc(c["name"][lang])
            href = to_rel(f"{t['prefix']}menu/{c['id']}/", base)
            cards.append(f"""          <li class="cat-card-item" data-reveal style="--reveal-delay:{i * 80}ms">
            <a class="cat-card" href="{href}" aria-label="{esc(t['explore_aria'].format(name=c['name'][lang]))}">
              <span class="cat-card__media"><img src="{rel(cover['image'])}" alt="" width="600" height="600" loading="lazy" decoding="async"></span>
              <span class="cat-card__body">
                <span class="cat-card__text">
                  <span class="cat-card__name">{name}</span>
                </span>
                <span class="cat-card__arrow">{ARROW}</span>
              </span>
            </a>
          </li>""")
        sections.append(f"""    <section class="menu-group menu-group--{g['id']}" id="{g['id']}" aria-labelledby="group-{g['id']}">
      <div class="container">
        <div class="menu-group__head">
          <h2 class="heading menu-group__title" id="group-{g['id']}">{esc(g['name'][lang])}</h2>
        </div>
        <ul class="cat-grid cat-grid--{len(cats)}" role="list">
{chr(10).join(cards)}
        </ul>
      </div>
    </section>""")
    return f"""
  <main id="main">
    <section class="menu-hero" aria-labelledby="menu-title">
      <div class="container menu-hero__inner">
        <p class="eyebrow menu-hero__eyebrow">{t['eyebrow']}</p>
        <h1 class="heading menu-hero__title" id="menu-title">{t['h1']}</h1>
        <p class="menu-hero__intro">{t['intro']}</p>
      </div>
    </section>

{chr(10).join(sections)}
  </main>
"""


# ---- Category page -----------------------------------------------------------
def dialog(t):
    dash_rows = "\n              ".join('<tr><td aria-hidden="true">—</td><td aria-hidden="true">—</td><td aria-hidden="true">—</td></tr>' for _ in range(4))
    return f"""
    <!-- Product details popup (filled by js/popup.js from the clicked card) -->
    <dialog class="product-dialog" aria-labelledby="pd-title" data-product-dialog>
      <button class="product-dialog__close" type="button" data-product-close>
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
        <span class="visually-hidden">{t['close']}</span>
      </button>
      <div class="product-dialog__inner">
        <div class="product-dialog__media"><img src="" alt="" width="1000" height="1000" data-pd-image></div>
        <div class="product-dialog__body">
          <p class="product-dialog__cat" data-pd-category></p>
          <h2 class="product-dialog__title" id="pd-title" data-pd-name></h2>

          <!-- PENDING: ingredients, sizes, prices and calories — no invented values (plan.md §5.1) -->
          <h3 class="product-dialog__label">{t['ingredients']}</h3>
          <p class="product-dialog__pending">{t['pending']}</p>

          <table class="product-dialog__table">
            <thead><tr><th scope="col">{t['size']}</th><th scope="col">{t['price']}</th><th scope="col">{t['calories']}</th></tr></thead>
            <tbody>
              {dash_rows}
            </tbody>
          </table>
          <p class="product-dialog__pending">{t['pending']}</p>
        </div>
      </div>
    </dialog>
"""


def category_main(lang, base, idx):
    t = T[lang]
    rel = lambda p: to_rel(p, base)
    c = CATS[idx]
    group = next(g for g in GROUPS if g["id"] == c["group"])
    cat_name = c["name"][lang]
    items = []
    for i, p in enumerate(products_in(c["id"])):
        name = esc(pname(p, lang))
        loading = 'fetchpriority="high"' if i < 4 else 'loading="lazy"'
        items.append(f"""          <li class="menu-item">
            <article class="menu-card">
              <div class="menu-card__media"><img src="{rel(p['image'])}" srcset="{rel(p['image'])} 600w, {rel(p['imageLarge'])} 1000w" sizes="(min-width: 1200px) 300px, (min-width: 760px) 30vw, 48vw" alt="{name}" width="600" height="600" {loading} decoding="async"></div>
              <div class="menu-card__body">
                <h2 class="menu-card__name">{name}</h2>
                <button class="menu-card__more" type="button" aria-haspopup="dialog" aria-label="{esc(t['view_aria'].format(name=pname(p, lang)))}"
                  data-product-open data-name="{name}" data-category="{esc(cat_name)}" data-image="{rel(p['imageLarge'])}">{t['view']} {ARROW}</button>
              </div>
            </article>
          </li>""")

    menu_url = to_rel(f"{t['prefix']}menu/", base)
    prev_c, next_c = CATS[idx - 1], CATS[(idx + 1) % len(CATS)]
    pager = f"""        <nav class="cat-pager" aria-label="{t['menu']}">
          <a class="cat-pager__link cat-pager__link--prev" href="{to_rel(f"{t['prefix']}menu/{prev_c['id']}/", base)}">
            <span class="cat-pager__dir">{CHEVRON.replace('icon-flip', 'icon-flip cat-pager__back')} {t['prev']}</span>
            <span class="cat-pager__name">{esc(prev_c['name'][lang])}</span>
          </a>
          <a class="btn btn--outline cat-pager__all" href="{menu_url}">{t['back']}</a>
          <a class="cat-pager__link cat-pager__link--next" href="{to_rel(f"{t['prefix']}menu/{next_c['id']}/", base)}">
            <span class="cat-pager__dir">{t['next']} {CHEVRON}</span>
            <span class="cat-pager__name">{esc(next_c['name'][lang])}</span>
          </a>
        </nav>"""

    return f"""
  <main id="main">
    <section class="menu-hero menu-hero--category" aria-labelledby="cat-title">
      <div class="container menu-hero__inner">
        <nav class="breadcrumb" aria-label="{t['breadcrumb']}">
          <ol>
            <li><a href="{menu_url}">{t['menu']}</a></li>
            <li><a href="{menu_url}#{group['id']}">{esc(group['name'][lang])}</a></li>
            <li aria-current="page">{esc(cat_name)}</li>
          </ol>
        </nav>
        <h1 class="heading menu-hero__title" id="cat-title">{esc(cat_name)}</h1>
      </div>
    </section>

    <section class="menu-catalog" aria-labelledby="cat-title">
      <div class="container">
        <!-- Prices / calories / ingredients pending verified client data -->
        <ul class="menu-grid" role="list">
{chr(10).join(items)}
        </ul>
{pager}
      </div>
    </section>
{dialog(t)}  </main>
"""


# ---- write -------------------------------------------------------------------
def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build():
    count = 0
    for lang, t in T.items():
        other = "en" if lang == "ar" else "ar"
        # Menu landing
        base = f"{t['prefix']}menu/"
        pre, footer = shared_parts(lang, base, f"{T[other]['prefix']}menu/", True)
        page = (head(lang, base, t["menu_title"], t["menu_description"], "/menu/", "/en/menu/", False)
                + '\n<body class="page-menu">' + pre + landing_main(lang, base)
                + "\n  " + footer + "\n</body>\n</html>\n")
        write(ROOT / base.lstrip("/") / "index.html", page)
        count += 1
        # Category pages
        for idx, c in enumerate(CATS):
            base = f"{t['prefix']}menu/{c['id']}/"
            other_url = f"{T[other]['prefix']}menu/{c['id']}/"
            pre, footer = shared_parts(lang, base, other_url, False)
            names = [pname(p, lang) for p in products_in(c["id"])]
            sep = "، " if lang == "ar" else ", "
            desc = t["cat_description"].format(name=c["name"][lang], list=sep.join(names[:6]) + ("…" if len(names) > 6 else ""))
            page = (head(lang, base, t["cat_title"].format(name=c["name"][lang]), desc,
                         f"/menu/{c['id']}/", f"/en/menu/{c['id']}/", True)
                    + '\n<body class="page-menu page-category">' + pre + category_main(lang, base, idx)
                    + "\n  " + footer + "\n</body>\n</html>\n")
            write(ROOT / base.lstrip("/") / "index.html", page)
            count += 1
    print(f"wrote {count} pages (2 menu landings + {len(CATS)} categories × 2 languages)")


if __name__ == "__main__":
    build()
