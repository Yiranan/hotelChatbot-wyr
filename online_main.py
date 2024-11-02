from getVector import PARSE
from pymilvus import MilvusClient

parse_vector=PARSE()



client = MilvusClient("wyr.db")


client.load_collection(collection_name="wyr_collection")


def RAG(query_vector,top_n):
    # query_vector=parse_vector.parse(query)
    results=client.search(collection_name="wyr_collection",
            data=[query_vector],
            # filter=f"document == '{document}'",
            limit=top_n,
            output_fields=["content"],
        )
    prompt_str=""
    for item in results:
        for i in range(top_n):
            # print(item[i]['entity']['content'])
            prompt_str+=item[i]['entity']['content']+'\n'
    return prompt_str


if __name__=="__main__":
    vector=parse_vector.parse("How can I contact Warwick Conferences?")
    prompt=RAG(vector,1)
    print(prompt)
