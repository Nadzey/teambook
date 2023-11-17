# 📘 TeamBook

### Project Description 📝
**TeamBook*** is an automated test project using Selenium for web application testing. The project includes:

- **`pages`**: Folder with page classes for performing actions on the site and checking results.
  - `base_page`: The base class for all pages, implementing common methods.
  - `wiki_creation_page`: Class with methods for creating new space on a page.
- **`locators.py`**: File with element locators.
- **`tests`**: Folder with test files.
- **`conftest.py`**: File with fixtures for tests.
- **`results`**: Folder with test screenshots.

## Installation & Setup 🔧

### Dependency Installation
1. **Chromedriver Autoinstaller**
   - Install:
     ```bash
     pip install chromedriver-autoinstaller
     ```
   - [chromedriver-autoinstaller](https://pypi.org/project/chromedriver-autoinstaller/) автоматически устанавливает Chrome WebDriver для Google Chrome.
   - Check installation:
     ```bash
     pip show chromedriver-autoinstaller
     ```

2. **Python-dotenv**
   - Install:
     ```bash
     pip install python-dotenv
     ```
   - [python-dotenv](https://pypi.org/project/python-dotenv/) for managing `.env` files.

### `.gitignore` Setup 🛑
- Add the following lines to `.gitignore`:
- add/shelf/
- workspace.xml
- .pyc
- .env
- .pytest_cache/
- pycache/


### Creating `.env` файла 🔒
1. Create a .env file in the project root.
2. Enter the following data:
```
VALID_EMAIL=your_email
VALID_PASSWORD=your_password
```
3. For use in tests or pages:
```python
import os
from dotenv import load_dotenv

load_dotenv()
- VALID_EMAIL = os.environ["VALID_EMAIL"]
- VALID_PASSWORD = os.environ["VALID_PASSWORD"]
```

### GitHub Secrets 🔐
- Add data to GitHub Secrets:

1. Go to `Settings > Secrets and Variables > Actions`.
2. Create a new repository secret.

### Running Tests 🚀

### Local Execution

#### Headless Mode (без GUI)
- Without report: ```pytest tests```
- With report: ```pytest tests --alluredir results```
- Single test file: ```pytest tests/test_header.py```

#### Headed Mode (с GUI)
- Without report:: ```pytest tests --headed```
- With report: ```pytest tests --alluredir results --headed```
- Single test file:  ```pytest tests/test_header.py --headed```

#### Viewing Allure Reports 📊
Execute:
```bash
allure serve results
```
### Contact Information 📬
- 📧 nadiakoluzaeva@gmail.com
- 💬 [Мой Discord аккаунт](https://discord.com/users/nadia9022)
- 🔗 [LinkedIn](https://www.linkedin.com/in/nadzeya-kaluzayeva/)
- 📍 Philadelphia, 19116
