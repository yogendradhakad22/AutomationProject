import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/auth/login")
    page.get_by_role("textbox", name="email@example.com").click()
    page.get_by_role("textbox", name="email@example.com").fill("yogendra@gmail.com")
    page.get_by_role("textbox", name="enter your passsword").click()
    page.get_by_role("textbox", name="enter your passsword").fill("Sd123@yog")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("textbox", name="search").click()
    page.get_by_role("textbox", name="search").fill("Adidas")
    page.get_by_role("textbox", name="search").press("Enter")
    page.get_by_role("textbox", name="search").fill("")
    page.get_by_role("textbox", name="search").press("Enter")
    page.get_by_role("button", name=" Add To Cart").nth(1).click()
    page.get_by_role("button", name="   Cart").click()
    page.get_by_role("button", name="Buy Now❯").click()
    page.get_by_role("textbox").nth(1).click()
    page.get_by_role("textbox").nth(1).fill("1234")
    page.get_by_role("textbox", name="Select Country").click()
    

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
