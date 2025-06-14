# Marketplace price tracking app

### Description
This is a Telegram Bot for tracking price changes on online marketplaces such as [Ozon](https://www.ozon.ru/), [Yandex.Market](https://market.yandex.ru) and [Wildberries](https://www.wildberries.ru)

### Quick Start
1. Clone repo
```bash
git clone git@github.com:Evgeniy-Golodnykh/marketplace_price_tracking.git
```
2. Creates the virtual environment
```bash
python3 -m venv venv
```
3. Activates the virtual environment
```bash
source venv/bin/activate
```
4. Upgrade PIP and install the requirements packages into the virtual environment
```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```
5. Install Chromium for marketplace websites scraping
```bash
playwright install --with-deps chromium
```
6. Go to src folder
```bash
cd src
```
7. To run the application use command
```bash
python3 -m main.py
```

### Technology
[Python](https://www.python.org), [Playwright](https://playwright.dev/python/), [SQLAlchemy](https://www.sqlalchemy.org), [PostgreSQL](https://www.postgresql.org), [Aiogram](https://aiogram.dev), [Docker](https://www.docker.com), [GitHub Actions](https://github.com/features/actions)

### Author
[Evgeniy Golodnykh](https://github.com/Evgeniy-Golodnykh)

### CI/CD pipeline status
![marketplace price tracking workflow](https://github.com/Evgeniy-Golodnykh/marketplace_price_tracking/actions/workflows/marketplace_price_tracking_workflow.yml/badge.svg)
