# Selenium tests (Python, pytest)

Requires Python 3.10+ and Chrome. Selenium Manager downloads the driver automatically.

    pip install -r requirements.txt
    APP_BASE_URL=http://localhost:8080 pytest
    HEADLESS=false pytest     # watch the browser
