import scrapy # type: ignore
from scrapy.crawler import CrawlerProcess
from urllib.parse import urljoin

class GlamiraSpider(scrapy.Spider):
    name = 'lab-grown-diamond'
    start_urls = ['https://www.glamira.com/diamond-rings/lab-grown-diamond/',
    ]
    # categories = [
    #     # 'diamond-rings',
    #     'black-diamond',
    #     'yellow-diamond',  # Add more categories here
    # ]
    # start_urls = [f'https://www.glamira.com/{category}/' for category in categories]
    

    custom_settings = {
        'FEEDS': {
            'images.json': {'format': 'json'},
        },
    }

    def __init__(self):
        self.visited_urls = set()  # Set to track visited image URLs
        self.current_page = 1
        self.total_pages = None  # Number of pages to crawl
        
    
        
    def parse(self, response):
        if self.total_pages is None:
            self.total_pages = int(response.css('.item.product-item::attr(data-lastpage)').get())
            self.log(f"Total pages to crawl: {self.total_pages}")
        # Extract category from the URL
        category = response.url.split('/')[-2]
        for product in response.css(f'.item-page-{self.current_page}'):
            # Extract image URLs
            image_srcset = product.css('.product-item-info .product-image-photo::attr(srcset)').get()
            image_urls = []
            if image_srcset:
                image_urls = [urljoin(response.url, img.split()[0]) for img in image_srcset.split(',')]
            else:
                image_url = product.css('.product-item-info .product-image-photo::attr(src)').get()
                image_urls = [urljoin(response.url, image_url)]
            
            # Extract product details
            name = product.css('.product-item-details .product-name::text').get()
            short_des = product.css('.product-item-details .short-description::text').get()
            carat = product.css('.product-item-details .carat::text').get()

            yield {
                'category': category,
                'name': name.strip() if name else None,
                'description': short_des.strip() if short_des else None,
                'carat': carat.strip() if carat else None,
                'image_urls': image_urls
            }
        self.current_page += 1
        if self.current_page <= self.total_pages:
            next_page_url = f'https://www.glamira.com/diamond-rings/lab-grown-diamond/?p={self.current_page}'
            yield response.follow(next_page_url, self.parse)
      
# Running the spider
if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(GlamiraSpider)
    process.start()