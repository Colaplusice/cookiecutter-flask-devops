#  cookiecutter template for Flask project

## feature

- [ x ]  html5-boilerplate for template
- [ x ]  docker & docker-compose & gitlab-ci for deployment on vps 
- [ x ]  per-commit & pytest & flake8 & black for code control.


## usage

### install cookiecutter
    
pip install cookiecutter

### generate project

cookiecutter <https://github.com/Colaplusice/cookiecutter-flask-devops.git>
or
```bash
cd ~/.cookiecutters/
git clone  https://github.com/Colaplusice/cookiecutter-flask-devops.git
```
and you can `cookiecutter cookiecutter-flask-devops` everywhere 

## option args

- --no-input
- -f --overwrite-if-exists
- --config-file PATH

## project options

- project_name  # project name to generate
- app_name      # app name
- create_api  yes/no # whether to generate rest api