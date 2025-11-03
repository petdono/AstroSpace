from flask import Flask, render_template, abort
from mistune import HTMLRenderer
import mistune
import os
import yaml


app = Flask(__name__)

class MyRenderer(HTMLRenderer):
    def codespan(self, text):
        return text

markdown = mistune.create_markdown(
    plugins=[
        'strikethrough',
        'table',
        'task_lists',
        'def_list',
        'footnotes',
        'abbr',
        'url',
        'mark',
        'math',
        'spoiler',
        'superscript',
        'subscript',
        'insert'
    ],
    renderer=MyRenderer()
)

CONTENT_DIR = "content"

def load_markdown(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    meta = {}
    body = content

    # Check if file starts with YAML front matter
    if content.startswith("---"):
        try:
            _, fm, body = content.split("---", 2)
            meta = yaml.safe_load(fm) or {}
        except ValueError:
            # no valid front matter block, fallback to plain content
            pass

    html = markdown(body)
    return meta, html

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/page/<name>")
def page(name):
    filepath = os.path.join(CONTENT_DIR, f"{name}.md")
    if not os.path.exists(filepath):
        abort(404)

    meta, html = load_markdown(filepath)
    return render_template("page.html", content=html, meta=meta)

if __name__ == '__main__':
    app.run(debug=True)