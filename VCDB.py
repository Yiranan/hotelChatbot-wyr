from pymilvus import MilvusClient
import config

class MyVCDB:
    def __init__(self,collection_name):
        client = MilvusClient("wyr.db")
        client.drop_collection(collection_name=collection_name)
        client.create_collection(collection_name=collection_name,dimension=config.VECTOR_SIZE)
        self.client = client
        self.collection_name=collection_name


    def add_parsed_text(self,id,vector,content):
        self.client.insert(
            collection_name=self.collection_name,
            data=[
                {"id":id,"vector":vector,"content":content},
            ]
        )
