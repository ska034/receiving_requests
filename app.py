import requests, json
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    res = requests.get("https://api.reddit.com/r/python/hot").text
    json_file = json.loads(res)
    return f'''
    Author: {json_file['data']['children'][0]['data']['author']} 
    <p>Title: {json_file['data']['children'][0]['data']['title']}
'''


if __name__ == '__main__':
    app.run(debug=False)
