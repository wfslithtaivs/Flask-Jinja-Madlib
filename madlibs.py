"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Gets input from user and directs to next page."""

    player = request.args.get("person")
    answer = request.args.get("response")

    if answer == "n":
        return render_template("goodbye.html",
                               person=player)
    else:
        return render_template("game.html",
                               person=player)


@app.route('/madlib')
def show_madlib():
    """Render madlib template"""

    player = request.args.get("person")
    clr = request.args.get("color")
    nn = request.args.get("noun")
    adj = request.args.get("adj")
    animals = request.args.getlist("animals")

    # which_template = choice([story1, story2])

    stories = {
                "initial": ["There once was a", "Nothing happens with"],
                "what_next": ["sitting in the Hackbright Lab.", "laying on the floor."],
                "problem": ["When", "Until", "While", "Unexpectadly"],
                "ending": ["went to pick it up, it burst into flames in a totally",
                "run out screaming", "flew away with cookies"]
               }

    story_parts = [
                  [choice(stories.get("initial")), player],
                  [clr, choice(stories.get("what_next"))],
                  [choice(stories.get("problem")), nn],
                  [choice(stories.get("ending")), adj + " way."]
                  ]

    return render_template("madlib.html",
                           story=story_parts,
                           list_of_values=animals)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
