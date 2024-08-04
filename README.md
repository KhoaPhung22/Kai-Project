 Glamira Web Crawler
## Overview
This project is a web crawler built using Scrapy to extract information about diamond rings and diamond necklaces with the total about 100000 data crawled from the Glamira website.
The files (Black_Diamond.py,Blue_Diamond.py,Brown_Diamond.py ,Green_Diamond.py ,glamiraspider1.py ,lab-grown-diamond.py) are used for crawled diamond_rings and stored them them in images.json
The files (necklaces.py,necklaces-black-diamond.py, necklaces-blue-diamond.py,necklaces-brown-diamond.py,necklaces-green-diamond.py,necklaces-lab-grown-diamond.py, necklaces-yellow-diamond.py) are used for crawled necklacess and stored them them in necklaces.json
## Features
- Crawl multiple subcategories dynamically.
- Extract product information including:
  - Name
  - Short description
  - Carat
  - Image URLs
- Handle pagination to traverse all product pages.
## Prerequisites
Ensure you have the following installed:
- Python 3.7 or higher
- Scrapy
