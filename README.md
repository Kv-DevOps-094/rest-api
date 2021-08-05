# RestAPI

This is a REST API application that returns an issues filtered by label

## Installation

### Install docker
#### CentOS

    dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
    dnf install docker-ce
    systemctl start docker
    systemctl enable docker

#### Ubuntu

    apt-get -y install docker.io

### Create network

    sudo docker network create --driver bridge --subnet 10.0.1.0/24 --ip-range 10.0.1.0/24 bridge_issue

### Create projects folder
    mkdir projectIssues
    cd projectIssues

### Clone RestAPI project
    git init
    sudo git clone https://github.com/Kv-DevOps-094/rest-api.git
    cd rest-api

### Create, configure and run PostgreSQL container

    sudo docker run -h postgres --rm --name postgres --net bridge_issue -e POSTGRES_PASSWORD=Init1234 -e POSTGRES_HOST=postgres -e POSTGRES_USER=issueuser -e POSTGRES_PW=Init1234 -e POSTGRES_DB=issuedb -e USERMAP_UID=999 -e USERMAP_GID=999 -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data docker.io/library/postgres:latest

### Create RestAPI container

    sudo docker build -t resrapi .

### Run RestAPI container

    sudo docker run -h restapi --name restapi --net bridge_issue -d -p 5000:5000 -e github='https://github.com/Kv-DevOps-094/rest-api.git' -e POSTGRES_HOST=postgres -e POSTGRES_PORT=5432 -e POSTGRES_USER=issueuser -e POSTGRES_PW=Init1234 -e POSTGRES_DB=issuedb resrapi

