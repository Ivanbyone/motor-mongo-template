""" """

import asyncio

from factory import *


async def main() -> None:
    """
    Main function with creating instances of Factory functions
    :return: None
    """
    clients = create_client_instances()
    databases = create_database_instances()
    collections = create_collection_instances()

    # testing connection by URI from MongoClient
    result = await clients.client.test_connection()
    print(result)

    # testing DB functions
    new_id = await collections.users.insert_doc({"id": 6578787})
    new_order = await collections.orders.insert_doc({"order_id": 547676645, "product": "Apple"})
    print(new_order)
    print(new_id)


if __name__ == '__main__':
    try:
        asyncio.run(main()) # Starting program
    except Exception as e:
        print(f"Program fell down with {e}")