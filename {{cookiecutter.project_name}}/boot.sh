#!/usr/bin/env bash

function run() {
   source ./.env
   gunicorn -c gunicorn.py run:app
}

function deploy() {
    # note: this need to change your real path for project
     path="/home/ubuntu/flask_project/{{cookiecutter.project_name}}"
   if [ ! -d $path ]; then
   ssh  {{cookiecutter.vps_ssh}} "git clone https://github.com/Colaplusice/{{cookiecutter.project_name}} $path"
   else
   ssh  {{cookiecutter.vps_ssh}} "cd $path ; git pull"
   fi
   ssh  {{cookiecutter.vps_ssh}} "cd $path ; /home/ubuntu/miniconda3/bin/docker-compose up -d --build"
   ssh  {{cookiecutter.vps_ssh}} "cd $path ; git push github master"
}

function createdb() {
   mysql -u {{cookiecutter.database_username}} -p{{cookiecutter.database_password}} -e "create database $1 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
}

# import .sql to database
dump_sql(){
    if mysql -u$USER -p$PASS -h $HOST -P $PORT  $DB_NAME < "$2"
    then
        echo "success"
    else
        echo "failed，exit code is $?"
        exit $?
    fi
}

Action=$1
shift
 case "$Action" in
 run)
    run ;;
 deploy)
    deploy;;
 migrate)
 migrate;;
 createdb )
 createdb "$1";;
 dump_sql )
 dump_sql "$1";;
    *) echo 'usage: ./boot.sh command
     command:
     runserver:                  run
     update code and deploy:     deploy
     migrate data                migrate
     createdb                   createdb [dbname]
     dump_sql                   dump_sql [sql]
     ' ;;

esac
