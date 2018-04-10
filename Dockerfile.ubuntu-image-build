FROM ubuntu:latest
LABEL Sreejon="sreejon_doom@yahoo.com"

#Update
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

# Bundle source files
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app

# Install python app dependencies
RUN pip install -r requirements.txt

COPY . /app

# Expose port
ENTRYPOINT ["python"]
CMD ["api.py", "-p 8080"]