""" Models for db instances """

from dataclasses import dataclass

from database.db_build import Users, Orders, Products
from database.mongo import MongoClient, Database


@dataclass
class Clients:
    client: MongoClient


@dataclass
class Databases:
    database: Database


@dataclass
class Collections:
    users: Users
    orders: Orders
    products: Products
