#!/bin/bash

docker-compose down
docker-compose stop
docker rmi -f app_api:latest
docker rmi -f app_db:latest