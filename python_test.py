import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://example.com/")
    page.get_by_text("Example DomainThis domain is").click()
    page.get_by_role("heading", name="Example Domain").click()
    page.get_by_text("This domain is for use in").click()
    page.get_by_role("link", name="Learn more").click()
    page.get_by_role("article").click()
    page.get_by_role("link", name="About", exact=True).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
