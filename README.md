# rest-api

This is a REST API application that returns an issues filtered by label

##Instalation
sudo docker run -h postgres --rm --name postgres -e POSTGRES_PASSWORD=password -e POSTGRES_USER=user -e POSTGRES_DB=db -e USERMAP_UID=999 -e USERMAP_GID=999 -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres

sudo docker build -t rabbit_to_postgres .

sudo docker run -h rabbit_to_postgres --name rabbit_to_postgres -d --env-file=.env rabbit_to_postgres 