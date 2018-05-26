FROM mongo:latest

COPY ./userdata.json /userdata.json

CMD mongoimport --host db --port 5000 --db userdata --collection users --file userdata.json