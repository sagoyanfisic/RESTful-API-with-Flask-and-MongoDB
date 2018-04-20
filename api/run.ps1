#!/bin/bash

docker run --name test_api_container -it -d -p 8080:8080 flask_api:latest