# Court Data Fetcher 🏛️

A Python-based web app to fetch court case details from the Faridabad District Court website using **Flask** and **Selenium**.

---

## 🔍 What This Project Does

- Takes input from the user:  
  ➤ Case Type (e.g., CS)  
  ➤ Case Number (e.g., 123)  
  ➤ Filing Year (e.g., 2020)

- Automatically goes to the Faridabad court website
- Extracts case details like:
  - Parties involved
  - Filing date
  - Next hearing date
  - Case type & number
  - Order PDF (if available)

---

## 📁 Project Folder Structure

court-data-fetcher/
├── scraper/
│ └── court_scraper.py # Selenium scraper code
├── templates/
│ ├── index.html # Form page (input)
│ └── result.html # Output page (results)
├── app.py # Flask backend
├── chromedriver.exe # ChromeDriver for Selenium


## 🚀 How to Run This Project

### Step 1: Install Required Libraries
### step 2: Download ChromeDriver
### Step 3: Run the App

###step 1: Install Required Libraries
Make sure Python is installed. Then open a terminal and run:

```bash
pip install flask selenium

### Step 2: Download ChromeDriver
-Go to: https://googlechromelabs.github.io/chrome-for-testing/
-Download the version that matches your installed Chrome version
-Extract and place the chromedriver.exe inside the project folder (court-data-fetcher/)

### Step 3: Run the App
python app.py

Then open your browser and go to:
http://127.0.0.1:5000
Now you can enter case details and view the results.

📌 Why I Made This
This project is part of my Python internship learning. I used it to practice:
-Web scraping with Selenium
-Building Flask-based web apps
-HTML templating
-Debugging backend logic

👨‍💻 Author
Ayush Singh
GitHub: @ayushxx17
