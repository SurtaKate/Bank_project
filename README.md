#Bank Web App UI Test Automation

Automated UI tests for the Bank Web Application (https://qatesting.vercel.app/bank) using Python, Playwright, and pytest.
This project follows the Page Object Model (POM) for maintainability and scalability.

#Project Structure

#Prerequisites

Python 3.8+
pip
Node.js (for Playwright browsers installation)
Installation

Clone the repository: git clone git@github.com:SurtaKate/Bank_project.git cd Bank_project

Create and activate a virtual environment: python -m venv .venv

On Unix/macOS:
source .venv/bin/activate

On Windows:
.venv\Scripts\activate

Install dependencies: pip install -r requirements.txt

Install Playwright browsers: playwright install

#Running Tests

To run all tests: pytest
Example: pytest tests/UI_Tests/test_login.py  
To run a specific test file: pytest tests/UI_Tests/test_login.py

#Test Cases

#Configuration

Test credentials are hardcoded in the test files. Update them as needed.
Browser runs in headed mode (headless=False). Change to headless=True for CI or faster runs.
Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

#License

#MIT

