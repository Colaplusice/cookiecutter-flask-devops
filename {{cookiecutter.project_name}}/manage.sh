#!/usr/bin/env bash

#!/bin/bash


USER="root"
PASS="newpass"
HOST='localhost'
PORT=3306
DB_NAME="{{cookiecutter.project_name}}"



#CurDir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
check_non_empty() {
    # $1 is the content of the variable in quotes e.g. "$FROM_EMAIL"
    # $2 is the error message
    if [[ "$1" == "" ]]; then
        echo "ERROR: specify $2"
        exit 1
    fi
}

createdb() {
    
mysql -h $HOST -P $PORT  -u$USER -p$PASS <<EOF 2>/dev/null
CREATE DATABASE $DB_NAME CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EOF
    [ $? -eq 0 ] && echo Created DB SUCCESS! || echo DB already exist
}

# 导入sql数据
dump_sql(){
    if mysql -u$USER -p$PASS -h $HOST -P $PORT  $DB_NAME < "$2"
    then
        echo "导入数据成功"
    else
        echo "导入数据失败，状态码为 $?"
        exit $?
    fi
}


#################
# Start of script
#################

case "$1" in
    destroy) destroy ;;
    dump_sql) dump_sql "$2";;
    createdb) createdb "$2";;
    *)
        echo "Usage:"
        echo "./mysql.sh createdb [database]"
        echo "./mysql.sh destroy [database]"
        exit 1
    ;;
esac

exit 0