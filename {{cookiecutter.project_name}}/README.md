# {{cookiecutter.project_name}}

- create database: `./boot.sh createdb [dbname]`

- migrate: `python run.py migrate`

- use Shell: `python run.py shell`

- develop run: `python run.py runserver`

- gunicorn run: `gunicorn -c gunicorn.py run:app`

- docker-compose: docker-compose up