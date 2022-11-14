"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>Hi! This is the home page.</html>
    <a href="http://127.0.0.1:5000/hello">Hello!</a>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        
        <div>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">

        <select name="compliments" id="compliments">
          <option value="awesome"> awesome </option>
          <option value="terrific"> terrific </option>
          <option value="smashing"> smashing </option>
          <option value="oh-so-not-meh">oh-so-not-meh</option>
        </select>
        </form>
        </div>

        <div>
        <form action="/mean_greet">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">

        <select name="diss" id="diss">
          <option value="terrible"> terrible </option>
          <option value="awful"> awful </option>
          <option value="trash"> trash </option>
        </select>
        </form>
        </div>

      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    # compliment = choice(AWESOMENESS)

    compliment = request.args.get('compliments')
    # x = y
    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """


@app.route('/mean_greet')
def mean_great_person():
  """Diss the user"""

  player = request.args.get("person")
  diss = request.args.get("diss")

  return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
