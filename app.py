import json
from flask import Flask, request, Response, render_template
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch(hosts="http://localhost:9200")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    search_body = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["kk", "ru"],
                "fuzziness": "AUTO"
            }
        }
    }
    response = es.search(index="aidar_mai", body=search_body)
    hits = response['hits']['hits']
    return render_template('results.html', hits=hits)

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
