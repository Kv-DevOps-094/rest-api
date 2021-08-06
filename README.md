# RestAPI

This is a REST API application that returns an issues filtered by label

## Installation

### Install docker
#### CentOS
    sudo dnf update -y
    sudo dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo
    sudo dnf install docker-ce
    sudo systemctl start docker
    sudo systemctl enable docker

### Install Git
#### CentOS

    sudo dnf install git -y

### Create network

    sudo docker network create --driver bridge --subnet 10.0.1.0/24 --ip-range 10.0.1.0/24 bridge_issue

### Create projects folder
    mkdir /home/projectIssues
    cd /home/projectIssues

### Clone RestAPI project
    git init
    sudo git clone https://github.com/Kv-DevOps-094/rest-api.git /home/projectIssues/restapi
    sudo git clone -b develop https://github.com/Kv-DevOps-094/rabbit-to-bd.git /home/projectIssues/rabbit-to-bd

### Copy service files to:
    cp -f /home/projectIssues/restapi/docker.postgres.service /etc/systemd/system/
    cp -f /home/projectIssues/restapi/docker.rabbit_to_db.service /etc/systemd/system/
    cp -f /home/projectIssues/restapi/docker.restapi.service /etc/systemd/system/

### Create RestAPI container

    sudo docker build /home/projectIssues/restapi -t resrapi .
    sudo docker build  /home/projectIssues/rabbit-to-bd -t rabbit_to_postgres .

