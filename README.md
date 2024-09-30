# Template for using Python-motor (MongoDB driver)

This template can be useful for developers who often uses MongoDB in their projects. Look description to understand a conception.
## Stack:
- Python 3.10.6
- motor 3.6.0
- MongoDB 7.0.2
- Docker 20.10.21
- docker-compose 2.12.2

## Description
Concept of project is divide MongoDB entities by creating classes:
1. Client
2. Database
3. Collection 

Then function was created a functions which make instances of Clients, Databases and Collection as a factory by dataclasses.

As an example, there is a schema of MongoDB entities in the project.

![Image alt](https://github.com/Ivanbyone/motor-mongo-template/raw/main/image/db_structure.png)

## Local development
1. Clone this repo:
```commandline
git clone https://github.com/Ivanbyone/motor-mongo-template
```
2. Replace arguments "YOUR_CONNECTION", "YOUR_DATABASE", "YOUR_COLLECTION" or create secret params.
3. Run docker-compose command
```commandline
docker-compose up --build -d
```

Now you can make some queries to MongoDB in your localhost.

Have a good development!