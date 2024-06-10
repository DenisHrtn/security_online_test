import os


def load_fixtures(fixtures_dir):
    """
    Function for automatic loading fixtures
    For run script:
        python3 load_fixtures.py
    """
    if not os.path.exists(fixtures_dir):
        os.system(f'python manage.py loaddata users/{fixtures_dir}/*.json')
        os.system(f'python manage.py loaddata tasks/{fixtures_dir}/*.json')
        print(f'{fixtures_dir} loaded')
        exit(0)


load_fixtures('fixtures')
