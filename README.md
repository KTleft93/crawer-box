BoxRec Selenium Crawler
Overview
A Python script using Selenium WebDriver to automate navigation on BoxRec.com. The script handles authentication and search functionality to access boxer profiles.
Features

Automated login handling for BoxRec.com
Search functionality for boxer profiles
Automatic navigation to search results
Graceful handling of both logged-in and logged-out states

Prerequisites
Install required packages:
bashCopypip install selenium
pip install webdriver-manager
Note: Chrome browser must be installed on your system.
Installation

Clone this repository
Install the required dependencies
Download ChromeDriver that matches your Chrome version

Code Structure
Required Imports
pythonCopyfrom selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
Driver Initialization
pythonCopydriver = webdriver.Chrome()
Main Function Implementation
pythonCopydef check_search_box_or_login():
    # Open BoxRec homepage
    homepage_url = 'https://boxrec.com/'
    driver.get(homepage_url)

    # Wait for the homepage to load completely
    time.sleep(2)

    try:
        # Check if the search box is available
        search_box = driver.find_element(By.NAME, 'si[search_text]')
        search_box.send_keys("Floyd Mayweather Jr")
        search_box.send_keys(Keys.RETURN)

        # Wait for search results to load
        time.sleep(2)

        # Click on the first relevant result
        first_result = driver.find_element(By.XPATH, 
            '//a[contains(text(), "Floyd Mayweather Jr")]')
        first_result.click()

        # Wait for the boxer's page to load
        time.sleep(2)

        print("Successfully navigated to Floyd Mayweather's page.")

    except Exception as search_exception:
        print("Search box not available, proceeding to login.")

        # Wait for the login page to load
        time.sleep(2)

        # Enter username and password
        username_input = driver.find_element(By.NAME, '_username')
        password_input = driver.find_element(By.NAME, '_password')
        password_input.send_keys(Keys.RETURN)

        # Wait for the page to load
        print('Successful Login!.. Proceeding to Home Page')
        time.sleep(1)

        # Check for the search box again after logging in
        try:
            search_box = driver.find_element(By.NAME, 'si[search_text]')
            search_box.send_keys("Floyd Mayweather Jr")
            search_box.send_keys(Keys.RETURN)

            print("Successfully navigated to Floyd Mayweather's page after login.")
        except Exception as e:
            print("Search box still not available after login.")
Usage
Execute the main function:
pythonCopycheck_search_box_or_login()
driver.quit()  # Close the browser when done
Configuration Required
Replace these values in the script:

BoxRec username credentials
BoxRec password credentials
Target boxer name (currently set to "Floyd Mayweather Jr")

Expected Output
Successful Flow
CopySuccessfully navigated to Floyd Mayweather's page.
Login Required Flow
CopySearch box not available, proceeding to login.
Successful Login!.. Proceeding to Home Page
Successfully navigated to Floyd Mayweather's page after login.
Extension Points
Adding Data Extraction
pythonCopydef extract_boxer_info():
    """
    Add selectors for boxer information
    """
    record = driver.find_element(By.XPATH, '//your-xpath-here')
    return record
Supporting Multiple Boxers
pythonCopydef search_boxer(boxer_name):
    """
    Generic search function for any boxer
    """
    search_box = driver.find_element(By.NAME, 'si[search_text]')
    search_box.send_keys(boxer_name)
    search_box.send_keys(Keys.RETURN)
Known Limitations

Hardcoded search for Floyd Mayweather Jr
No error handling for invalid credentials
Fixed time delays instead of explicit waits
No data extraction functionality implemented

Contributing
Areas for improvement:

Adding data extraction functionality
Implementing explicit waits instead of time.sleep()
Adding command line arguments for different boxers
Implementing proper error handling and logging

License
MIT License
Disclaimer
This tool is for educational purposes only. Ensure compliance with BoxRec's terms of service.
