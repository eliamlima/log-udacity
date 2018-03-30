#!/usr/bin/env python3
#
# A buggy web service in need of a database.

from flask import Flask, request, redirect, url_for

from newsdb import get_posts

app = Flask(__name__)

# HTML template for the Log News page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>Log NEWS</title>
    <style>
      h1 { text-align: center; }
      form {margin: 20px;}
      button {margin-top: 10px;}
      <!-- textarea { width: 400px; height: 100px; } -->
      <!-- div.post { border: 1px solid #999;
                 padding: 10px 10px;
                 margin: 10px 20%%; } -->
      <!-- hr.postbound { width: 50%%; } -->
      <!-- em.date { color: #999 } -->
    </style>
  </head>
  <body>
    <h1>Log News</h1>
    <form method=post>
      <!-- <div><textarea id="content" name="content"></textarea></div> -->
      <input type="radio" name="options" id="option1" value="top3"> \
      Top 3 Articles </input><br>
      <input type="radio" name="options" id="option2" value="topauthors">\
      Top Authors </input><br>
      <input type="radio" name="options" id="option3" value="errors"> \
      Days with more than 1 percent errors </input><br>
      <div><button id="go" type="submit">Submit</button></div>
    </form>
    <!--post content will go here-->

</html>
'''

# HTML template for the queries
POST = '''\
    <div class=post>%s - %s views</div>
'''

@app.route('/', methods=['GET'])
def main():
    '''Main page of the forum.'''
    return HTML_WRAP


@app.route('/', methods=['POST'])
def post():
    '''New post submission.'''
    message = request.form['options']

    if message == "top3":
        return(redirect(url_for('top3')))
    elif message == "topauthors":
        return(redirect(url_for('topauthors')))
    elif message == "errors":
        return(redirect(url_for('errors')))
    else:
        return "No option selected"


@app.route('/top3')
def top3():
    posts = "".join(POST % (text, num) for text, num in get_posts('top3'))
    return posts


@app.route('/topauthors')
def topauthors():
    posts = "".join(POST % (text, num) for text, num
                    in get_posts('topauthors'))
    return posts


@app.route('/errors')
def errors():
    POST = '''\
        <div class=post>%s - %s %% errors</div>
    '''
    posts = "".join(POST % (text.strftime('%B %d, %Y'), num)
                    for text, num in get_posts('errors'))
    return posts


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
