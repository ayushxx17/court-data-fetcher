# Court Data Fetcher 🏛️

A Python-based web app to fetch court case details from the **Faridabad District Court** website using **Flask** and **Selenium**.

---

## 🔍 What This Project Does

Takes input from the user:

- ➤ Case Type (e.g., CS)  
- ➤ Case Number (e.g., 123)  
- ➤ Filing Year (e.g., 2020)

Then:

- Automatically opens the Faridabad Court website
- Extracts and displays key details:
  - ✅ Parties involved  
  - 📅 Filing date  
  - 🏛️ Next hearing date  
  - 🆔 Case type & number  
  - 📄 Order PDF (if available)

---

## 📁 Project Folder Structure

court-data-fetcher/
├── scraper/
│ └── court_scraper.py # Selenium scraper logic
├── templates/
│ ├── index.html # Input form page
│ └── result.html # Output display page
├── app.py # Flask web app
├── chromedriver.exe # ChromeDriver binary for Selenium


---

## 🚀 How to Run This Project

### ✅ Step 1: Install Required Libraries

Make sure Python is installed. Then in your terminal or CMD, run:

```bash
pip install flask selenium

✅ Step 2: Download ChromeDriver
.Go to: Chrome for Testing

.Download the version that matches your installed Chrome

.Extract and place chromedriver.exe inside your project folder:
court-data-fetcher/

✅ Step 3: Run the App
python app.py

Then open your browser and visit:
http://127.0.0.1:5000
Now you can enter case details and view the fetched results.

## 📸 Live Screenshot

### Screenshot of Form Page:
![Form Page](assets/screenshot-form.png.png)

### Screenshot of Running code:
![Running code](assets/Screenshot-runningcode.png)

### Screenshot of files:
![Files](assets/Screenshot-files.png)

### Screenshot of VS Code:
![VS Code](assets/Screenshot-vscodefiles.png)




📌 Why I Made This
This project is part of my Python internship learning. Through this hands-on project, I practiced:

.🕸️ Web scraping using Selenium

.🌐 Building Flask-based web apps

.🧾 HTML templating

.🐞 Debugging backend logic

👨‍💻 Author
Ayush Singh
🔗 GitHub: @ayushxx17
