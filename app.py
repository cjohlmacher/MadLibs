from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'placeholder'
debug = DebugToolbarExtension(app)

@app.route('/')
def show_form():
    print(story.prompts)
    return render_template("home.html", prompts=story.prompts)

@app.route('/story', methods=["GET","POST"])
def show_story():
    story_text=story.generate(request.args)
    print(story_text)
    return render_template("story.html", story_text=story_text)
