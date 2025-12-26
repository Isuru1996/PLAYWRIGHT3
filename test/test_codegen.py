import re

from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("feed the dog")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("water to plants")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("buy chocolate")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("listitem").filter(has_text="water to plants").get_by_label(
        "Toggle Todo"
    ).check()
    expect(page.get_by_text("water to plants")).to_be_visible()
    page.get_by_role("link", name="Active").click()
    expect(page.get_by_text("feed the dog")).to_be_visible()
    expect(page.get_by_text("buy chocolate")).to_be_visible()
    page.get_by_role("link", name="Completed").click()
    expect(page.get_by_role("heading", name="todos")).to_be_visible()
