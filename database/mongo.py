""" Database class with 3 main essences """

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection


class MongoClient:

    def __init__(self, connection: str):
        self._connection: AsyncIOMotorClient = AsyncIOMotorClient(connection, serverSelectionTimeoutMS=5000)

    @property
    def connection(self) -> AsyncIOMotorClient:
        return self._connection

    async def test_connection(self):
        try:
            await self._connection.server_info()
            return "Connection is good!"
        except RuntimeWarning as rw:
            print(f"Exception with {rw}")


class Database(MongoClient):

    def __init__(self, connection: str, database: str):
        super().__init__(connection)
        self._database: AsyncIOMotorDatabase = self.connection.get_database(name=database)

    @property
    def database(self) -> AsyncIOMotorDatabase:
        return self._database


class Collection(Database):

    def __init__(self, connection: str, database: str, collection: str) -> None:
        super().__init__(connection, database)
        self._collection: AsyncIOMotorCollection = self.database.get_collection(name=collection)

    @property
    def collection(self) -> AsyncIOMotorCollection:
        return self._collection

    async def collection_method(self, name: str):
        new_name = await self._collection.rename(new_name=name)
        return new_name
