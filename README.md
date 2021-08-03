# rest-api

This is a REST API application that returns an issues filtered by label

##Instalation

###Create network
docker network create --driver bridge --subnet 10.0.1.0/24 --ip-range 10.0.1.0/24 bridge_issue

###Create configure and run PostgreSQL container 
sudo docker run -h postgres --rm --name postgres --net bridge_issue --env-file=.env -e USERMAP_UID=999 -e USERMAP_GID=999 -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres

###Create RestAPI container
sudo docker build -t resrapi .

###Run RestAPI container
sudo docker run -h restapi --name restapi --net bridge_issue -d -p 5000:5000 --env-file=.env resrapi
