
  # Amazon Auto Tests

**Automated UI Testing for Amazon Web Platform**  
Built with **Python**, **Selenium**, and **Pytest**.  
Structured with **Page Object Model (POM)** for better scalability and readability.  
Ready for integration with **GitHub Actions** for CI/CD.

---

## Project Overview
This project demonstrates automation testing of selected Amazon website features.  
It is designed to showcase clean code practices, modular structure, and effective test automation techniques.

---

## Technologies Used
- Python 3.10
- Selenium WebDriver
- Pytest
- webdriver-manager
- Page Object Model (POM) design pattern

---

## Project Structure
```
amazon-autotests/ 
├── pages/ 
│   ├── base_page.py 
│   ├── home_page.py 
│   └── login_page.py 
├── tests/ 
│   ├── test_login.py 
│   └── test_homepage.py 
├── test_data/ 
│   └── (data files if needed) 
├── utils/ 
│   └── (utility functions if needed) 
├── conftest.py 
├── requirements.txt 
├── pytest.ini 
└── README.md
```

## How to Run Tests

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yevhen-kyrianov/amazon-autotests.git
   cd amazon-autotests

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate     # On Windows: venv\Scripts\activate

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the tests:
   ```bash
   pytest tests/ --html=reports/report.html

Future Improvements
  Integration with GitHub Actions for Continuous Integration.
  Expansion of test coverage (functional, negative, UI validation).
  Support for multiple browsers (Chrome, Firefox).
  Adding API testing examples.

## API Tests

Located in `tests/api/`, these are basic examples using `requests` to demonstrate API testing.

Author
Yevhen Kyrianov



