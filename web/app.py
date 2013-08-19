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
    def get_spec_posts(_type, num = 3):
        posts = [page for page in pages if 'date' in page.meta \
                 and 'type' in page.meta and page.meta['type'] == _type]
        sorted_posts = sorted(posts, reverse=True,
            key=lambda page: page.meta['date'])[:num]
        return sorted_posts
    return render_template('index.html',
                            seminar_pages  = get_spec_posts('seminar'),
                            practice_pages = get_spec_posts('practice'),
                            law_pages      = get_spec_posts('law'))

@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    try:
        parent_idx = parent_map['/'+page.path]
        family = family_book[parent_idx]
    except KeyError:
        family = []
    try:
        head_image = page.meta['head_image']
    except KeyError:
        head_image = None
    return render_template('page.html', page=page,
        family=family, head_image=head_image)

@app.route('/sitemap/')
def site_map():
    return render_template('sitemap.html', pages=pages)

# -----------------------------------------------------------------------------

if __name__ == "__main__":
    app.run()

# -----------------------------------------------------------------------------