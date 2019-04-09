# {{cookiecutter.project_name}}

- use Shell: `python run.py shell`

- develop run: `python run.py runserver`

- create database: `./boot.sh createdb [dbname]`

- migrate: `python run.py migrate`

- gunicorn run: `gunicorn -c gunicorn.py run:app`

- docker-compose: docker-compose up