from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():    
    return '<h1>Welcome!</h1>'


@app.route('/user/<u>')
def hello_user(u):
    return render_template('user.html', u=u)

if __name__ == '__main__':  
    print('starting Flask app', app.name)  
    app.run(debug=True)