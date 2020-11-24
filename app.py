from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample
from stories import story

app = Flask(__name__)

app.config['SECRET_KEY'] = 'key'
debug = DebugToolbarExtension(app)


@app.route('/')
def get_words():
    """Generate and show form to ask words."""
    prompts = story.prompts
    return render_template("index.html", prompts=prompts)


@app.route('/story')
def render_story():
    """Renders story with passed in arguments."""
    text = story.generate(request.args)

    return render_template("story.html", text=text)
