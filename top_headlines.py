from flask import Flask, render_template

from functions import *

app = Flask(__name__)

nyt_key = api_key

@app.route('/')
def index():    
    return '<h1>Welcome!</h1>'


@app.route('/user/<u>')
def hello_user(u):

    story_list_json = get_stories('technology')
    headlines = get_headlines(story_list_json)

    top5 = headlines[:5]

    '''
    for h in headlines:
        print(h)
    '''

    return render_template('user.html', u=u,my_headlines=top5)

if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)