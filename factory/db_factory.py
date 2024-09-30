""" Creating instance functions """

from models import Collections, Clients, Databases
from database.db_build import Users, Orders, Products
from database.mongo import MongoClient, Database

# creating Clients factory instance
def create_client_instances() -> Clients:
    return Clients(
        client=MongoClient(connection="YOUR_CONNECTION")
    )

# creating Databases factory instance
def create_database_instances() -> Databases:
    return Databases(
        database=Database(connection="YOUR_CONNECTION", database="YOUR_DATABASE")
    )

# creating Collections factory instance
def create_collection_instances() -> Collections:
    return Collections(
        users=Users(connection="YOUR_CONNECTION", database="YOUR_DATABASE", collection="YOUR_COLLECTION"),
        orders=Orders(connection="YOUR_CONNECTION", database="YOUR_DATABASE", collection="YOUR_COLLECTION"),
        products=Products(connection="YOUR_CONNECTION", database="YOUR_DATABASE", collection="YOUR_COLLECTION")
    )
