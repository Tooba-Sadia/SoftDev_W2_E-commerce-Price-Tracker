# Daraz Laptop Scraper (Playwright + Python)

This project is a simple **web scraper** that uses [Playwright](https://playwright.dev/python/) with Python to scrape the **top 10 laptop listings** from [Daraz.pk](https://www.daraz.pk/).  
It extracts product names and prices, then saves them into a CSV file (`daraz.csv`).

---
## Features
- Automates a search for **"laptop"** on Daraz.

- Extracts **product names** and **prices** from the search results.
  
- Saves the top **10 results** into a CSV file.
  
- Takes a **screenshot** of the search results page.
  
- Records a **video of the browsing session** (saved in the `videos/` directory).
  
- Resets the CSV file on each run (only fresh top 10 items are saved).

## Problem Approach
- Search Input: Used CSS selectors with IDs (input#q) for the search box, since IDs don’t change often.

- Product Data Extraction:

- Used class selectors inside <div> elements (div.RfADt for product titles, div.aBrP0 for prices).

- Iterated through results using the nth() function to extract the top 10 products.

- Storage: Each product (index, name, price) was appended to a CSV file. If the file existed, it was reset to avoid duplicate entries.

## Challenges Faced:
### Choosing Selectors:

- The first instinct was to use XPath, but I avoided it since Daraz’s structure changes often.

- CSS selectors with IDs and classes proved to be more reliable.

### Timeouts & Dynamic Loading:

- Daraz has a lot of images and scripts. To handle this, I used wait_until="domcontentloaded" and added a custom timeout.

### Handling Page Elements:

- Sometimes the search box was not found due to loading issues, so I had to wrap it in a try-except.

### Duplicate / Old Data in CSV:

- If the CSV file already existed, old data would remain. To fix this, I reset (os.remove) the CSV at the start.

### Performance Considerations:

- Loading all images slows things down, so the scraper is set to focus only on DOM content instead of full page load.

### Anti-Bot Measures:

- Daraz (like most e-commerce sites) can change structure or block suspicious activity. I added slow_mo=2000 to make the browsing appear more human-like.

## Key TakeAways:

- CSS selectors are usually more reliable than XPath for e-commerce scraping.

- Always handle timeouts, exceptions, and dynamic loading when scraping modern websites.

- Resetting or cleaning your data source (CSV) ensures fresh results on every run.

- Scraping responsibly (delays, small datasets) helps avoid being blocked by websites.

- Screenshots and video recordings are useful for debugging automation flows.
