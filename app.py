import requests, json
from flask import Flask, request, render_template

import date
from date import Date
from jinja2 import Template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/r/<subreddit>", methods=['GET', 'POST'])
def subreddit(subreddit):
    if request.method == 'GET':
        if request.args.get('subreddit'):
            subreddit = request.args.get('subreddit')

    limit = request.args.get('limit') if request.method == 'GET' else request.form.get('limit')

    if limit:
        res = requests.get(f"https://api.reddit.com/r/{subreddit}/hot?limit={limit}")
    else:
        res = requests.get(f"https://api.reddit.com/r/{subreddit}/hot")

    if res.status_code != 200:
        return render_template('error.html', text=res.text, title=subreddit, limit=limit)
    else:
        json_file = json.loads(res.text)

        subreddits_list = []
        for i in json_file['data']['children']:
            subreddit_dict = {}
            subreddit_dict['author'] = i['data']['author']
            subreddit_dict['title'] = i['data']['title']
            subreddit_dict['date_post'] = date.Date(i['data']['created']).date_history()
            subreddit_dict['url_post'] = i['data']['url']
            subreddits_list.append(subreddit_dict)

        return render_template('subreddits.html', title=subreddit, subreddits_list=subreddits_list, limit=limit)


if __name__ == '__main__':
    app.run(debug=False)
