from flask import Flask, render_template, request
from scraper.court_scraper import fetch_court_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', error=None)

@app.route('/fetch', methods=['POST'])
def fetch_case():
    case_type = request.form.get('case_type', '').strip()
    case_number = request.form.get('case_number', '').strip()
    filing_year = request.form.get('filing_year', '').strip()

    #  Input validation
    if not case_type or not case_number or not filing_year:
        return render_template('index.html', error="⚠ Please fill in all fields before submitting.")

    try:
        #  Call scraper
        data = fetch_court_data(case_type, case_number, filing_year)

        #  If scraper returns no data
        if not data.get('parties'):
            return render_template('result.html', error="❌ No case found. Please check your details and try again.", data=None)

        return render_template('result.html', data=data)

    except Exception as e:
        print(f"[ERROR] {e}")
        return render_template('result.html', error="⚠ An unexpected error occurred. Please try again later.", data=None)

if __name__ == '__main__':
    app.run(debug=True)  # Change to debug=False for production
