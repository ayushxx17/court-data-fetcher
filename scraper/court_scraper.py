from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

def fetch_court_data(case_type, case_number, filing_year):
    print("[INFO] fetch_court_data() called")
    print(f"[DEBUG] Inputs - Case Type: {case_type}, Case Number: {case_number}, Filing Year: {filing_year}")

    # Setup options
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Path to chromedriver.exe (ensure it's correct)
    chromedriver_path = os.path.join(os.getcwd(), 'chromedriver.exe')
    print(f"[DEBUG] Using chromedriver at: {chromedriver_path}")

    try:
        service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=service, options=options)

        driver.get('https://services.ecourts.gov.in/ecourtindia_v6/?p=casestatus/index')

        time.sleep(2)

        # Interact with dropdowns and inputs
        driver.find_element(By.NAME, 'state_code').send_keys('Haryana')
        time.sleep(1)
        driver.find_element(By.NAME, 'dist_code').send_keys('Faridabad')
        time.sleep(1)

        driver.find_element(By.ID, 'case_type').send_keys(case_type)
        driver.find_element(By.ID, 'case_no').send_keys(case_number)
        driver.find_element(By.ID, 'case_year').send_keys(filing_year)

        driver.find_element(By.ID, 'submit').click()
        time.sleep(5)

        # Extract data (update these selectors if needed)
        parties = driver.find_element(By.ID, 'parties').text
        filing_date = driver.find_element(By.ID, 'fdate').text
        next_hearing = driver.find_element(By.ID, 'next_date').text
        pdf_url = driver.find_element(By.ID, 'order_pdf').get_attribute('href')

        driver.quit()

        return {
            'case_type': case_type,
            'case_number': case_number,
            'filing_year': filing_year,
            'parties': parties,
            'filing_date': filing_date,
            'next_hearing': next_hearing,
            'pdf_url': pdf_url
        }

    except Exception as e:
        print(f"[ERROR] {e}")
        return {
            'case_type': case_type,
            'case_number': case_number,
            'filing_year': filing_year,
            'parties': '',
            'filing_date': '',
            'next_hearing': '',
            'pdf_url': 'Not Available'
        }
