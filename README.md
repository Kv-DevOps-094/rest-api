# rest-api

This is a REST API application that returns an issues filtered by label

##Instalation
sudo docker build -t rabbit_to_postgres .

sudo docker run -h rabbit_to_postgres --name rabbit_to_postgres -d --env-file=.env rabbit_to_postgres 