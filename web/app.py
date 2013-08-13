# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from prepare import prepare

# -----------------------------------------------------------------------------

app = Flask(__name__)
app.config.from_pyfile('settings.py')
pages = FlatPages(app)
freezer = Freezer(app)
family_book, parent_map = prepare()

# -----------------------------------------------------------------------------

@app.route('/')
def home():
    posts = [page for page in pages if 'date' in page.meta]
    sorted_posts = sorted(posts, reverse=True,
        key=lambda page: page.meta['date'])
    return render_template('index.html', pages=sorted_posts)

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    family = []
    try:
        parent_idx = parent_map['/'+page.path]
        family = family_book[parent_idx]
    except KeyError:
        pass
    return render_template('page.html', page=page, family=family)

@app.route('/sitemap/')
def site_map():
    return render_template('sitemap.html', pages=pages)

# -----------------------------------------------------------------------------

if __name__ == "__main__":
    app.run()

# -----------------------------------------------------------------------------