#!/bin/bash

# docker stop container_name
# docker rm container_name
# docker rmi -f image_name

# docker stop rest_api
# docker rm rest_api
# docker rmi -f flask_api_image:latest

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)