# Flask Basics

## Introduction

  - Micro Framework

https://flask.palletsprojects.com/en/1.1.x/

## Quickstart

  - Quickstart

```python
# simple start
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  return "Hello, World!"
```

  - Routing

```python
# routing
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  return "Hello, World!"

@app.route('/hi')
def hi():
  return "Hi, there!"
```

  - Variable Rules

```python
# routing
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  return "Hello, World!"

@app.route('/number/<int:id>')
def numb(id):
  return f"Hi, you asked for {id}!"

@app.route('/names/<str:name>')
def hi(name):
  return f"Hi, {name}!"
```



https://flask.palletsprojects.com/en/1.1.x/quickstart/

  - HTTP Methods

  https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
  https://flask.palletsprojects.com/en/1.1.x/quickstart/#http-methods

  - REST API

  https://www.restapitutorial.com/
  https://flask.palletsprojects.com/en/1.1.x/quickstart/#apis-with-json


## Flask RESTful

`pip install flask-restful`

```python
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
```
