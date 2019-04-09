#!/usr/bin/env bash

function run() {
   source .env
   gunicorn -c gunicorn.py run:app
}

function deploy() {
    # note: this need to change your real path for project
   ssh  {{cookiecutter.vps_ssh}} "cd /home/ubuntu/{{cookiecutter.project_name}}; git pull"
   ssh  {{cookiecutter.vps_ssh}} "cd /home/ubuntu/{{cookiecutter.project_name}}; /home/ubuntu/miniconda3/bin/docker-compose up -d --build"
   ssh  {{cookiecutter.vps_ssh}} "cd /home/ubuntu/{{cookiecutter.project_name}}; git push github master"
}

function create_db() {
   mysql -u {{cookiecutter.database_username}} -p{{cookiecutter.database_username}} -e "create database $1 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
}
Action=$1
shift
 case "$Action" in
 run)
    run ;;
 deploy)
    deploy;;
 run_celery)
 run_celery;;
 run_celery_beat)
 run_celery_beat;;
 migrate)
 migrate;;
 create_db )
 create_db "$1";;
    *) echo 'usage: ./boot.sh command
     command:
     runserver:                  run
     update code and deploy:     deploy
     migrate data                migrate
     create_db                   create_db [dbname]
     ' ;;

esac
