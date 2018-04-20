FROM alpine:latest
LABEL Sreejon="sreejon_doom@yahoo.com"

#Update
RUN apk add --update
RUN apk add python python-dev py-pip g++ make build-base mariadb-dev \
  && rm -rf /var/cache/apk/*

# Bundle source files
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

# Install python app dependencies
RUN pip install -r requirements.txt

COPY . /app

# Expose port
ENTRYPOINT ["python"]
CMD ["api.py", "-p 8080"]