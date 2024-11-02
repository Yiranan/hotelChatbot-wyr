import config

from tqdm.asyncio import tqdm

from VCDB import MyVCDB
from getVector import PARSE
import re


vector_db=MyVCDB("wyr_collection")
print("vector DB created")

parse_vector=PARSE()
print("parse model load success")

file_id=0
filename="QA_text.txt"

with open(filename, 'r', encoding='utf-8') as file:

    text = file.read()


segments = re.split(r'\s*\d+\.\s*', text)[1:]  # segmentation
print("segment success")

for chunk in tqdm(segments,total=len(segments)):
    print(chunk)
    vector=parse_vector.parse(chunk)
    file_id+=1
    vector_db.add_parsed_text(file_id,vector,chunk)

print("offline parse success")


