## SERVICE MIDDLEWARE 
this service will execute the functionalities that were stipulated for the relationship with the service-db (CRUD), for all the data in the database.

this service is connected by Docker containers from its Docker image. 

## Installation of dependencies

commands



```bash

pipenv shell
pipenv install

```

## Usage to run the program 

```bash

docker-compose -f Docker-compose.dev.yml up --build

```

## Important

Please make sure to update tests as appropriate.
if the command to run the program has an error add to the beginning of this default SUDO

## Remember

you must first run the service-db service to run this middleware service

## License
[MIT](https://choosealicense.com/licenses/mit/)