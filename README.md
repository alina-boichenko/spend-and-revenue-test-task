# spend-and-revenue-test-task

## Installation
Python3, Django must be already installed
```
git clone https://github.com/alina-boichenko/spend-and-revenue-test-task.git
cd spend-and-revenue-test-task
python3 -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirement.txt
python manage.py migrate
python manage.py runserver 
```

## Features
Implemented endpoints in which you can receive querysets of the RevenueStatistic model and SpendStatistic model.

## Swagger Documentation
http://localhost:8000/api/schema/swagger/