from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def fetch_court_data(case_type, case_number, filing_year):
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    chromedriver_path = os.path.join(os.getcwd(), 'chromedriver.exe')

    try:
        service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=service, options=options)
        driver.get('https://services.ecourts.gov.in/ecourtindia_v6/?p=casestatus/index')

        wait = WebDriverWait(driver, 10)

        # Select State
        Select(wait.until(EC.presence_of_element_located((By.NAME, 'state_code')))).select_by_visible_text('Haryana')

        # Select District
        Select(wait.until(EC.presence_of_element_located((By.NAME, 'dist_code')))).select_by_visible_text('Faridabad')

        # Fill case details
        wait.until(EC.presence_of_element_located((By.ID, 'case_type'))).send_keys(case_type)
        driver.find_element(By.ID, 'case_no').send_keys(case_number)
        driver.find_element(By.ID, 'case_year').send_keys(filing_year)

        driver.find_element(By.ID, 'submit').click()

        # Wait for results
        wait.until(EC.presence_of_element_located((By.ID, 'parties')))

        parties = driver.find_element(By.ID, 'parties').text
        filing_date = driver.find_element(By.ID, 'fdate').text
        next_hearing = driver.find_element(By.ID, 'next_date').text

        try:
            pdf_url = driver.find_element(By.ID, 'order_pdf').get_attribute('href')
        except:
            pdf_url = "Not Available"

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
