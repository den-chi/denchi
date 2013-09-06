# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect
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

def get_spec_posts(_type, lang, num = 5):
    posts = [page for page in pages if page.path.startswith(lang) \
                and 'date' in page.meta \
                and 'type' in page.meta and page.meta['type'] == _type]
    sorted_posts = sorted(posts, reverse=True,
        key=lambda page: page.meta['date'])[:num]
    return sorted_posts

@app.route('/')
def home():
    return redirect('/cn/')

@app.route('/<lang>/')
def home_lang(lang):
    return render_template('index.html', lang=lang,
                            event_pages  = get_spec_posts('event', lang),
                            practice_pages = get_spec_posts('practice', lang),
                            law_pages      = get_spec_posts('law', lang))

@app.route('/<path:path>/')
def page(path):
    lang = path.split('/')[0]
    page = pages.get_or_404(path)
    try:
        parent_idx = parent_map[lang]['/'+page.path]
        family = family_book[lang][parent_idx]
    except KeyError:
        print path
        family = [page.meta['title']]
    try:
        head_image = page.meta['head_image']
    except KeyError:
        head_image = None
    try:
        list_type = page.meta['list']
        posts = get_spec_posts(list_type, lang, 1000)
    except KeyError:
        posts = None
    return render_template('page.html', page=page,
        family=family, head_image=head_image, posts=posts, lang=lang)

@app.route('/sitemap/')
def site_map():
    urls = ['/cn', '/jp']
    return render_template('sitemap.html', pages=pages, urls=urls)

# -----------------------------------------------------------------------------

if __name__ == "__main__":
    app.run()

# -----------------------------------------------------------------------------