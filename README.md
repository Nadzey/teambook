# 📘 TeamBook

## Описание Проекта 📝
**TeamBook** - это автоматизированный тестовый проект, использующий Selenium для тестирования веб-приложений. Проект включает в себя:

- **`pages`**: Папка с классами страниц для выполнения действий на сайте и проверки результатов.
  - `base_page`: Базовый класс для всех страниц, реализующий общие методы.
  - `wiki_creation_page`: Класс с методами для создания нового пространства на странице.
- **`locators.py`**: Файл с локаторами элементов.
- **`tests`**: Папка с тестами.
- **`conftest.py`**: Файл с фикстурами для тестов.
- **`results`**: Папка со скриншотами тестов.

## Установка и Настройка 🔧

### Установка Зависимостей
1. **Chromedriver Autoinstaller**
   - Установка:
     ```bash
     pip install chromedriver-autoinstaller
     ```
   - [chromedriver-autoinstaller](https://pypi.org/project/chromedriver-autoinstaller/) автоматически устанавливает Chrome WebDriver для Google Chrome.
   - Проверка установки:
     ```bash
     pip show chromedriver-autoinstaller
     ```

2. **Python-dotenv**
   - Установка:
     ```bash
     pip install python-dotenv
     ```
   - [python-dotenv](https://pypi.org/project/python-dotenv/) для работы с файлами `.env`.

### Настройка `.gitignore` 🛑
Добавьте следующие строки в `.gitignore`:
add/shelf/
workspace.xml
.pyc
.env
.pytest_cache/
pycache/


### Создание `.env` файла 🔒
1. Создайте файл `.env` в корне проекта.
2. Введите в него данные:
VALID_EMAIL=your_email
VALID_PASSWORD=your_password

3. Для использования в тестах или страницах:
```python
import os
from dotenv import load_dotenv

load_dotenv()
VALID_EMAIL = os.environ["VALID_EMAIL"]
VALID_PASSWORD = os.environ["VALID_PASSWORD"]

## GitHub Secrets 🔐
Добавьте данные в GitHub Secrets:

1. Перейдите в `Settings > Secrets and Variables > Actions`.
2. Создайте новый секрет репозитория.

## Запуск Тестов 🚀

### Локальный Запуск

#### Headless режим (без GUI)
- Без отчета: `pytest tests`
- С отчетом: `pytest tests --alluredir results`
- Отдельный файл тестов: `pytest tests/test_header.py`

#### Headed режим (с GUI)
- Без отчета: `pytest tests --headed`
- С отчетом: `pytest tests --alluredir results --headed`
- Отдельный файл тестов: `pytest tests/test_header.py --headed`

### Просмотр отчетов Allure 📊
Запустите:
```bash
allure serve results

