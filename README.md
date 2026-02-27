This repository contains a solution to a test assignment for test automation using Python and the Playwright framework.

## Prerequisites
- Python 3.8 or newer installed

## Installation and launch

1. **Clone the repository and navigate to the folder:**
```bash
git clone https://github.com/tusarek/yunex-playwright-task.git
cd yunex_test
```
2. **Create and activate a virtual environment (recommended):**
```bash
python3 -m venv venv
source venv/bin/activate
```
3. **Install depencencies:**
```bash
pip install -r requirements.txt
```
4. **Install Playwright browsers:**
```bash
playwright install
```
5. **Run the tests:**
```bash
pytest yunex_playwright_test.py
```