Project Title: Automated Rental Property Finder for Pune
This project is designed to automate the process of finding rental rooms/flats in Pune using BeautifulSoup and Selenium Driver. It leverages web scraping techniques to extract information from a static webpage provided by nobroker.com and automates the filling of a Google Form with the collected data.

Features
Web Scraping: Utilizes BeautifulSoup to parse and extract data from the static webpage containing rental listings in Pune.
Data Collection: Gathers information such as property address, rent, and link from the filtered rental listings.
Form Filling Automation: Utilizes Selenium WebDriver to automate the process of filling a Google Form with the collected data.
Pre-Applied Filters: The static webpage has pre-applied filters including room type, tenant type, rent range, furnishing, and minimum number of bathrooms.
Pre-Requirements
Ensure you have the following dependencies installed:

BeautifulSoup
Selenium
Requests
How to Use:
Clone this repository to your local machine.

Install the required dependencies using pip:

Copy code
pip install beautifulsoup4 selenium requests
Run the Python script flats_in_pune.py.

The script will scrape the data from the provided static webpage, collect the required information, and automate the process of filling the Google Form.

Google Form Questions
The Google Form used for data collection consists of the following questions:

What's the address of the property?
What's the rent of the property?
What's the link of the property?
Disclaimer
This project is for educational and demonstrative purposes only. Use it responsibly and in accordance with the terms of service of the websites being scraped.
