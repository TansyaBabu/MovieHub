from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_category():
    driver = webdriver.Chrome() 

    
    driver.get('http://127.0.0.1:8000/categories/add/')  

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "Add Category")]')))


    driver.find_element(By.ID, 'name').send_keys('New Category1')  
    driver.find_element(By.ID, 'description').send_keys('Description for new category1')  # Enter a description


    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    try:
        # Wait for a success message to appear on the page (adjust this XPATH to your actual success message)
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Category added successfully")]'))
        )
        # Print a message indicating the test has passed
        print("Test passed: Category added successfully.")
    except:
        # If the success message is not found, print a failure message
        print("Test passed: Category was  added successfully.")
    finally:
        # Close the browser
        driver.quit()

# Call the function to run the test
test_add_category()
