import asyncio
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
import click


async def async_main(the_url):
    browser_conf = BrowserConfig(headless=True)  # or False to see the browser
    run_conf = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS
    )

    async with AsyncWebCrawler(config=browser_conf) as crawler:
        result = await crawler.arun(
            url=the_url,
            config=run_conf
        )
        print(result.markdown)

@click.command()
@click.argument('url', default='https://example.com', required=False)
def main(url):
    asyncio.run(async_main(url))

if __name__ == "__main__":
    main()
