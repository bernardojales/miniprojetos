# Docker-compose
It now came with Docker normal installation
so, you can setup your complete environment/infrastructure from a simple file called "docker-compose.yml"

## Main Commands

<strong>when should i use?</strong><br/>
when you need to setup a project that has docker-compose.yml file
```sh
docker compose up -d # setup all services described on docker-compose.yml
docker compose up -d <service_name> # setup service passed with configurations described on docker-compose.yml and their services dependencies
docker compose up -d <service1_name> <service2_name> <service..._name> # setup services passed with configurations described on docker-compose.yml and their services dependencies
```
<strong>when should i use?</strong><br/>
when you already has setuped a project that has docker-compose.yml file and want to stop all containers
```sh
docker compose down # setdown services described on docker-compose.yml
docker compose down -v # setdown services and destroy volumes described on docker-compose.yml
```