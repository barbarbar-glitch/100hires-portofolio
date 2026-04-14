import asyncio
from linkedin_scraper import BrowserManager

async def main():
    async with BrowserManager(headless=False) as browser:
        print("Log into LinkedIn in the browser window that opens...")
        await browser.page.goto("https://www.linkedin.com/login")
        input("Press Enter after you've logged in successfully...")
        await browser.save_session("session.json")
        print("Session saved to session.json!")

asyncio.run(main())
