import os
import urllib.request
from playwright.sync_api import sync_playwright

os.makedirs('deliverables/evidence', exist_ok=True)

# 1. Click tests against localhost:8000
test_urls = [
    ("CTA 1 Primary", "http://localhost:8000/LANDING_PAGE/index.html?utm_source=newsletter&utm_medium=email&utm_campaign=nov2026_studio_notes"),
    ("CTA 2 Banner", "http://localhost:8000/LANDING_PAGE/index.html?utm_source=newsletter&utm_medium=email&utm_campaign=nov2026_studio_notes"),
    ("Footer Preferences Anchor", "http://localhost:8000/LANDING_PAGE/index.html?utm_source=newsletter&utm_medium=email&utm_campaign=nov2026_studio_notes#preferences"),
    ("Footer Unsubscribe Anchor", "http://localhost:8000/LANDING_PAGE/index.html?utm_source=newsletter&utm_medium=email&utm_campaign=nov2026_studio_notes#unsubscribe"),
    ("Footer Contact Anchor", "http://localhost:8000/LANDING_PAGE/index.html?utm_source=newsletter&utm_medium=email&utm_campaign=nov2026_studio_notes#contact")
]

print("=== URL Verification ===")
for name, url in test_urls:
    try:
        req = urllib.request.urlopen(url)
        print(f"[{req.getcode()}] {name}: OK")
    except Exception as e:
        print(f"[ERR] {name}: {e}")

# 2. Playwright rendering & screenshot verification
file_url = f"file:///{os.path.abspath('deliverables/newsletter.html').replace(os.sep, '/')}"

with sync_playwright() as p:
    browser = p.chromium.launch()
    version = browser.version
    print(f"\nPlaywright Chromium Version: {version}")
    
    # Desktop 1440px
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto(file_url)
    page.wait_for_load_state("networkidle")
    scroll_w = page.evaluate("document.documentElement.scrollWidth")
    container_w = page.evaluate("document.querySelector('.email-container').offsetWidth")
    print(f"1440px viewport: scrollWidth={scroll_w}px (scrollWidth <= 1440: {scroll_w <= 1440}), containerWidth={container_w}px")
    page.screenshot(path="deliverables/evidence/desktop_1440.png", full_page=True)
    page.close()

    # Tablet / Breakpoint 600px
    page = browser.new_page(viewport={"width": 600, "height": 900})
    page.goto(file_url)
    page.wait_for_load_state("networkidle")
    scroll_w = page.evaluate("document.documentElement.scrollWidth")
    print(f"600px viewport: scrollWidth={scroll_w}px (scrollWidth <= 600: {scroll_w <= 600})")
    page.screenshot(path="deliverables/evidence/viewport_600.png", full_page=True)
    page.close()

    # Mobile 375px
    page = browser.new_page(viewport={"width": 375, "height": 812})
    page.goto(file_url)
    page.wait_for_load_state("networkidle")
    scroll_w = page.evaluate("document.documentElement.scrollWidth")
    print(f"375px viewport: scrollWidth={scroll_w}px (scrollWidth <= 375: {scroll_w <= 375})")
    page.screenshot(path="deliverables/evidence/mobile_375.png", full_page=True)
    page.close()

    # Block images test (Alt text check)
    page = browser.new_page(viewport={"width": 600, "height": 900})
    page.route("**/*.{png,jpg,jpeg,svg,gif}", lambda route: route.abort())
    page.goto(file_url)
    page.wait_for_load_state("networkidle")
    page.screenshot(path="deliverables/evidence/images_blocked_600.png", full_page=True)
    print("Images blocked screenshot captured.")
    page.close()

    # Verify anchor scrolling on landing page
    landing_url = "http://localhost:8000/LANDING_PAGE/index.html"
    for anchor in ["#preferences", "#unsubscribe", "#contact"]:
        page = browser.new_page(viewport={"width": 1000, "height": 800})
        page.goto(f"{landing_url}{anchor}")
        page.wait_for_load_state("networkidle")
        visible = page.is_visible(anchor)
        print(f"Landing page anchor {anchor} target element visible: {visible}")
        page.close()

    browser.close()
