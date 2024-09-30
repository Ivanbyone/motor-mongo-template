""" Classes with specific collection methods """

from database.mongo import Collection


class Users(Collection):

    def __init__(self, connection, database, collection):
        super().__init__(connection, database, collection)


    async def insert_doc(self, data: dict):
        result = await self.collection.insert_one(data)
        return result


class Orders(Collection):
    #
    def __init__(self, connection, database, collection):
        super().__init__(connection, database, collection)

    async def insert_doc(self, data):
        result = await self.collection.insert_one(data)
        return result


class Products(Collection):
    #
    pass
