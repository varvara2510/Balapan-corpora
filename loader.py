from elasticsearch import Elasticsearch
import json

es = Elasticsearch(hosts="http://localhost:9200")

print(f"Connected to Elasticsearch cluster `{es.info()['cluster_name']}`")

with open("./drakon_output.json", encoding='utf-8') as file:
    data = file.readlines()

for json_object in data:
    document = json.loads(json_object)
    es.index(index="aidar_mai", document=document)
