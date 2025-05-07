# Intro to Pytest

This repository is part of the **Introduction to Pytest** course by [Test Automation University](https://testautomationu.applitools.com/pytest-tutorial/). It contains examples demonstrating various aspects of testing in Python using [pytest](https://docs.pytest.org/).

## Project Overview

The project includes:

- **Modules:**
  - **Accumulator:** A class for accumulating values in [stuff/accum.py](stuff/accum.py). The corresponding tests in [tests/test_accum.py](tests/test_accum.py) verify its behavior.
  - **Math Operations:** Basic math tests including parameterized tests shown in [tests/test_math.py](tests/test_math.py).
  - **API Testing:** An example of testing an external API (DuckDuckGo) in [tests/test_api.py](tests/test_api.py).
  - **UI Testing:** Automated UI testing using Playwright demonstrated in [tests/test_ui.py](tests/test_ui.py).

- **Other Files:**
  - **pytest.ini:** Contains configuration and custom markers for pytest.
  - **assets/style.css:** The style file used for generating test reports or documentation.
  - **htmlcov:** Directory where the HTML coverage report is generated.

## Getting Started

1. **Install Dependencies**

    If you have a requirements file (or add dependencies as needed), install them:
    ```bash
    pip install -r requirements.txt
    ```
   
    For UI testing using Playwright, run:
    ```bash
    pip install playwright
    playwright install
    ```

2. **Run the Tests**

    To run all tests:
    ```bash
    python3 -m pytest
    ```

    To run tests by marker (for example, UI tests):
    ```bash
    python3 -m pytest -m ui
    ```


## Course Topics
- **Introduction to Pytest:** Learn the basics of writing and running tests in Python.
- **Fixture Usage:** Understand how to use fixtures for test setup as shown in test_accum.py
- **Parameterization:** See examples of parameterized testing in test_math.py
- **API Testing:** Get insights into testing HTTP APIs in test_api.py
- **UI Testing with Playwright:** Automate browser interactions, demonstrated in test_ui.py


## License
This project is provided for educational purposes as part of the Test Automation University course.

Happy Testing!