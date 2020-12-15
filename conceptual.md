### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  >Javascript is ran on both browser and server and Pyhthon is mostly used for server side programming.


- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  >{"a": 1, "b": 2, "c": 3}
  >(GET function) ****
  >A method that returns the value for the given key, if present in the dictionary. If not, then it will return None (if get() is used with only one argument)


- What is a unit test?
  >Separate testable parts of code. An individual program, class, method, function etc.


- What is an integration test?
  >Individual pieces of code are combined and tested as a group.


- What is the role of web application framework, like Flask?
  >A application used with Python that provides tools and libraries that help build web application. flask-debugtoolbar is one example of tools used for debugging and testing.


- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  >route URL vs Param ****
  >Query string is always a part of the URL. Parameters can be buried in form-data datastream when using POST method so they may not appear in the URL


- How do you collect data from a URL placeholder parameter using Flask?
  >from flask import request

  >@app.route(...)
  >def login():
      >username = request.args.get('username')


- How do you collect data from the query string using Flask?
  >from flask import request

  >@app.route('/data')
  >def data():
      >user=some-value)
      >user = request.args.get('user')


- How do you collect data from the body of the request using Flask?
  >from flask import request

  >@app.route('/', methods=['GET', 'POST'])
  >def parse_request():
      >data = request.data  


- What is a cookie and what kinds of things are they commonly used for?
  >Cookies collect user data stored on the user's computer web browser.


- What is the session object in Flask?
  >Session data is stored on the server.


- What does Flask's `jsonify()` do?
>Creates a response with the JSON code 
>Example:
>from flask import jsonify

>@app.route('/_get_current_user')
>def get_current_user():
    >return jsonify(username=g.user.username,
                   >email=g.user.email,
                   >id=g.user.id)
