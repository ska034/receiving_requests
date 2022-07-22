import requests, json
from flask import Flask, request, render_template
from date import Date
from jinja2 import Template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/r/<subreddit>", methods=['GET', 'POST'])
def subreddit(subreddit):

    if request.method == 'GET':
        subreddit = request.args.get('subreddit')

    limit = request.args.get('limit') if request.method == 'GET' else request.form.get('limit')


    if limit:
        res = requests.get(f"https://api.reddit.com/r/{subreddit}/hot?limit={limit}")
    else:
        res = requests.get(f"https://api.reddit.com/r/{subreddit}/hot")

    if res.status_code != 200:
        return render_template('error.html', text=res.text)
    else:
        json_file = json.loads(res.text)



        # for i in json_file['data']['children']:
        #     print(f'''
        #     Author: {i['data']['author']}
        #     Title: {i['data']['title']}''')

        return render_template('subreddits.html', title=subreddit, json_file=json_file)


@app.route("/test/", methods=["GET"])
def test():
    with open('json_file.json', 'r') as file:
        json_file = json.loads(file.read())

    # for i in json_file['data']['children']:
    #     print(f'''
    #     Author: {i['data']['author']}
    #     Title: {i['data']['title']}''')
    # if request.method == 'GET':
    #     print(request.args.get('subreddit'))
    #     print(request.args.get('limit'))

    return render_template('subreddits.html', title="python", json_file=json_file)


if __name__ == '__main__':
    app.run(debug=False)
