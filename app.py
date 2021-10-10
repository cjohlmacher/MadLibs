from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story_choices

app = Flask(__name__)
app.config['SECRET_KEY'] = 'placeholder'
debug = DebugToolbarExtension(app)

@app.route('/')
def choose_story():
    return render_template("home.html", story_choices=story_choices)

@app.route('/form', methods=["GET","POST"])
def show_form():
    idx = int(request.form["id"])
    print('idx: ',idx)
    story = story_choices[idx]
    return render_template("form.html", prompts=story.prompts, story_id=idx)

@app.route('/story/<id>', methods=["GET"])
def show_story(id):
    idx = int(id)
    story_text=story_choices[idx].generate(request.args)
    print(story_text)
    return render_template("story.html", story_text=story_text)
