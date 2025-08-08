<<<<<<< HEAD
from flask import Flask, render_template, request
from scraper.court_scraper import fetch_court_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch_case():
    case_type = request.form['case_type']
    case_number = request.form['case_number']
    filing_year = request.form['filing_year']
    print(f"Form received: {case_type} {case_number} {filing_year}")
    
    data = fetch_court_data(case_type, case_number, filing_year)
    return render_template('result.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask, render_template, request
from scraper.court_scraper import fetch_court_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch_case():
    case_type = request.form['case_type']
    case_number = request.form['case_number']
    filing_year = request.form['filing_year']
    print(f"Form received: {case_type} {case_number} {filing_year}")
    
    data = fetch_court_data(case_type, case_number, filing_year)
    return render_template('result.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 32d0591942f45005fc974b4166f7db1174dfc485
