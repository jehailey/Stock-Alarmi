#!/usr/bin/env bash

sudo docker-compose --project-name stock-alarmi up --build -d
docker exec -it postgres_db psql -U postgres -c "create database $1"
python database_test.py $1
