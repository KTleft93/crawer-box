from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()


# Function to check for the search box and log in if not available
def check_search_box_or_login():
    # Open BoxRec homepage
    homepage_url = 'https://boxrec.com/'
    driver.get(homepage_url)

    # Wait for the homepage to load completely
    time.sleep(2)

    try:
        # Check if the search box is available
        search_box = driver.find_element(By.NAME, 'si[search_text]')  # Adjust based on the actual name or ID
        search_box.send_keys("Floyd Mayweather Jr")  # Type in the boxer's name
        search_box.send_keys(Keys.RETURN)  # Hit Enter

        # Wait for search results to load
        time.sleep(2)

        # Click on the first relevant result
        first_result = driver.find_element(By.XPATH, '//a[contains(text(), "Floyd Mayweather Jr")]')
        first_result.click()

        # Wait for the boxer's page to load
        time.sleep(2)

        print("Successfully navigated to Floyd Mayweather's page.")

    except Exception as search_exception:
        print("Search box not available, proceeding to login.")


        # Wait for the login page to load
        time.sleep(2)

        # Enter username and password
        username_input = driver.find_element(By.NAME, '_username')  # Adjust based on the actual name or ID
        password_input = driver.find_element(By.NAME, '_password')  # Adjust based on the actual name or ID

  
        password_input.send_keys(Keys.RETURN)  # Hit Enter to log in

        # Wait for the page to load
        print('Sucessful Login!.. Proceeding to Home Page')
        time.sleep(1)

        # Check for the search box again after logging in
        try:
            search_box = driver.find_element(By.NAME, 'si[search_text]')  # Adjust based on the actual name or ID
            search_box.send_keys("Floyd Mayweather Jr")  # Type in the boxer's name
            search_box.send_keys(Keys.RETURN)  # Hit Enter


            # Wait for the boxer's page to load


            print("Successfully navigated to Floyd Mayweather's page after login.")
        except Exception as e:
            print("Search box still not available after login.")


# Example usage
check_search_box_or_login()

# Close the browser
driver.quit()
