import requests, json
from flask import Flask, request, render_template
from jinja2 import Template

app = Flask(__name__)


@app.route("/")
def index():
    return '''<h1>Enter subreddit in the request in the format:</h1>
    <p> 127.0.0.1://r/python
    <p><h1> You can add a post limit:</h1>
    <p> 127.0.0.1://r/python?limit=10'''


@app.route("/r/<subreddit>", methods=['GET', 'POST'])
def subreddit(subreddit):
    limit = request.args.get('limit')
    if limit:
        res = requests.get(f"https://api.reddit.com/r/{subreddit}/hot?limit={limit}")
    else:
        res = requests.get(f"https://api.reddit.com/r/{subreddit}/hot")

    if res.status_code != 200:
        return render_template('error.html', text=res.text)
    else:
        json_file = json.loads(res.text)

        for i in json_file['data']['children']:
            print(f'''
            Author: {i['data']['author']}
            Title: {i['data']['title']}''')

        # my_string = ''
        # for i in json_file['data']['children']:
        #     my_string += f'''<p>Author: {i['data']['author']}<br>
        #     Title: {i['data']['title']}
        #     '''
        return render_template('subreddits.html', title=subreddit, json_file=json_file)


if __name__ == '__main__':
    app.run(debug=False)
