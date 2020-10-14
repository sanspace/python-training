# Day 7 Tasks

## Learn

## Practice

  - Implement as many HTTP methods as you can in flask (GET, POST, PUT and etc)
  - Create a RESTful API to have Developers, Tasks
    - /developers
    - /developers/2
    - /developers/1/tasks
    - /developers/1/ /3
    - /tasks

    - Implementation Tips
      - Collection of Developers or a Single Developer (same for tasks)

```python

DEVELOPERS = {}
TAKS = {}

class DevelopersList(Resource):
  def get(self): # /developers GET 200
    # return all developers
    pass

  def post(self): # /developers POST 201
    # receive request data
    # validate received data
    # add new dev to the list
    pass

class Developer(Resource):
  def get(self,): # /developers/5 GET 200
    # lookup id in the collection
    # return the details 200
    # not found 404
    pass

  def put(self,): # /developers/5 PUT 2xx
    # lookup item in collection
    # update the properties
    # return the details 2xx
    # not found 404
    pass

  def delete(self,): # /developers/5 2xx
    # lookup
    # delete
    # return empty with code
    # not found 404

```