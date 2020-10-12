from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/users/<int:userid>')
# GET, PUT, DELETE
def userid_route(userid):
  return f"Your user ID is {userid}"

@app.route('/username/<string:user>')
def user_route(user):
  return f"Hello, {user}!"
