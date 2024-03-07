# WebScraper

The service parses the pages of the provided resource. 


<!-- TOC -->
* /scrape - full resource parsing
* /update - scrape only those pages that are not listed in the filtered links file
* /fail_urls - get a list of failed links
* /scrape_one_page - parse only one specific page of the resource
* /add_custom_page - add page data to the parsed data file
* /load_data - get the contents of the parsed data file
<!-- TOC -->

check_scraper.py - the script checks the difference between the list of URLs of the last parsing and the current sitemap of the resource
