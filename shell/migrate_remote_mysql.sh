#! /bin/bash

remote_ip=10.43.105.45
remote_username="devops"
remote_password="devops!"
local_username="zss"
local_password="zss"

database_name=redmine
migrate_tables="member_roles members projects roles users"

create_database_flag=true

function show_help
{
    local me="$(basename "$(test -L "$0" && readlink "$0" || echo "$0")")"
    echo "***recreate database and migrate remote mysql data***"
    echo "Usage: $me [OPTION]"
    echo "  OPTION:"
    echo "    -n|--no-create-database    do not create database, use local existed database"
    echo "    -h|--help                  show this help message"
}

function parse_args
{
    local optlist="$@"
    while true
    do
        case "$1" in
            "--no-create-database"|"-n")
                create_database_flag=false
                shift
                ;;
            "--help"|"-h")
                show_help;
                exit;
                ;;
            *)
                break
                ;;
        esac
    done
}

function create_database
{
    echo "create database $database_name..."
    mysql <<EOF
DROP DATABASE IF EXISTS $database_name;
CREATE DATABASE $database_name;
GRANT ALL PRIVILEGES ON *.* TO '$local_username'@'localhost' IDENTIFIED BY '$local_password';
GRANT ALL PRIVILEGES ON *.* TO '$local_username'@'%' IDENTIFIED BY '$local_password';
exit
EOF
}

function migrate_data
{
    for table in $migrate_tables
    do
        echo "migrating table '$table' from $remote_ip ..."
        mysqldump -h$remote_ip -u$remote_username -p$remote_password --opt $database_name $table | mysql $database_name
    done

    echo "migrating mysql data completed!"
}

parse_args $@
[[ "$create_database_flag" == "true" ]] && create_database
migrate_data
