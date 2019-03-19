# {{cookiecutter.project_name}}

 - 进入Shell
 ```
 flask shell
 ```

 - 本地启动

 ```
 flask server
 ````

 - gunicorn启动

 ```
gunicorn -c gunicorn/xxxx.pymanage:app
 ```

 - run command

 ```
 flask <command name>
 ```

 - run celery

 ```
flask celery worker --loglevel=debug
 ```

 - run celery beat

 ```
flask celery beat --loglevel=debug
 `
