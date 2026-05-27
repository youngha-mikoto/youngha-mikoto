import os
from playwright.sync_api import sync_playwright


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://atcoder.jp/users/youngha_mikoto", wait_until="networkidle")

        os.makedirs("images", exist_ok=True)

        status_element = page.query_selector("#ratingStatus")
        if status_element:
            status_element.screenshot(path="images/ratingStatus.png")
            print("ratingStatus.png saved.")
        else:
            print("ratingStatus element not found.")

        graph_element = page.query_selector("#ratingGraph")
        if graph_element:
            graph_element.screenshot(path="images/ratingGraph.png")
            print("ratingGraph.png saved.")
        else:
            print("ratingGraph element not found.")

        browser.close()


if __name__ == "__main__":
    main()
