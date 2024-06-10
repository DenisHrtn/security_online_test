# Чтобы поднять проект:

- Установите виртуальное окружение и поставьте в него все зависимости из файла requirements.txt с помощью команды: `pip install -r requirements.txt`
- Далее сделайте миграции и зафиксируйте их с помощью команд `python manage.py makemigratons` и `python manage.py migrate`
- После установите фикстуры запустив файл `load_fixtures` командой `python load_fixtures.py`

# Ниже представлены креды для входа в аккаунты:

- `super_employee@gmail.com` pass: `super_employee`
- `customer_1@gmail.com` pass: `customer_1`
- `customer_2@gmail.com` pass: `customer_2`
- `employer_1@gmail.com` pass: `employer_1`
- `employer_2@gmail.com` pass: `employer_2`
- `employer_3@gmail.com` pass: `employer_3`

# Чтобы запустить проверку соответствия PEP 8, ошибок, сложности кода запустите команду:
- `flake8` находясь в корневой директории проекта

# Для запуска тестов:
- Команда `python manage.py test`

# Для запуска проекта с помощью Docker:
- Команда `docker-compose up --build`