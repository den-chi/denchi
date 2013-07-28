import os
try:
    from flask import Flask
except ImportError:
    os.system('pip install Flask')
    from flask import Flask
try:
    from flask_flatpages import FlatPages
except ImportError:
    os.system('pip install Flask-FlatPages')
    from flask_flatpages import FlatPages

DEBUG = True
FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = '.txt'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)

@app.route('/')
def index():
    return "Hello World"

@app.route("/update")
def update():
    os.system('git pull')
    return 'Successfully updated!'

@app.route('/<path:path>/')
def page(path):
    return pages.get_or_404(path).html

if __name__ == '__main__':
    app.run(host='0.0.0.0')