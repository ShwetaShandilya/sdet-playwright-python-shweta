# Playwright Python Automation Framework

A UI automation framework built using Playwright, Pytest, and the Page Object Model (POM) design pattern.

## Features

* Playwright with Python
* Pytest test runner
* Page Object Model (POM)
* Environment-based configuration using `.env`
* ConfigReader utility
* Screenshot capture on test failure
* HTML reporting
* GitHub Actions CI integration
* Data-driven testing using JSON
* Multi-browser support (Chromium, Firefox, WebKit)
* Parallel execution with pytest-xdist

## Project Structure

```text
pages/
tests/
utils/
test_data/
.github/workflows/
conftest.py
pytest.ini
requirements.txt
run_tests.py
```

## Setup

Create virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
playwright install
```

## Execute Tests

Run smoke tests:

```bash
python run_tests.py
```

Or:

```bash
pytest -m smoke
```

Run tests in parallel:

```bash
pytest -n 2
```

## Reporting

HTML report is generated under:

```text
reports/report.html
```

Screenshots for failed tests are stored under:

```text
screenshots/
```

## CI/CD

GitHub Actions automatically executes smoke tests on:

* Push to main
* Pull requests

## Design Highlights

* Separation of concerns using Page Object Model
* Centralized configuration management
* Reusable Pytest fixtures
* Automatic resource cleanup using fixture teardown
* Browser-independent test execution

## Future Enhancements

* Allure reporting
* API automation integration
* Cross-browser matrix execution
* Docker support
* Test execution dashboards

```
```
