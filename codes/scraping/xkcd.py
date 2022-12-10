from playwright.sync_api import Playwright, sync_playwright, expect
import sh
import wget


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=2*1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://xkcd.com/")
    page.get_by_role("link", name="Random").first.click()
    img = page.query_selector_all('#comic img')
    url = f"https:{img[0].get_attribute('src')}"
    print(f'Downlodaing: {url}')
    wget.download(url)
    # ---------------------
    # print('')
    # breakpoint()
    # filename = url.split('/')[-1]
    # print('Opening file')
    # sh.nomacs(filename)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
