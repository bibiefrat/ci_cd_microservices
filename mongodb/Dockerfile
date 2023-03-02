FROM mongo:latest

RUN apt -y update
RUN apt install -y net-tools
RUN apt install -y iputils-ping



# Expose port #27017 from the container to the host
# Set /usr/bin/mongod as the dockerized entry-point application
#CMD mongod
RUN setsid /usr/bin/mongod &
#ENTRYPOINT mongod

