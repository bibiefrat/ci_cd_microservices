#FROM python:3.8.12-slim-buster
FROM python:3.10

# YOUR COMMANDS HERE
# ....
# ....
# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]

