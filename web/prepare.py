import os
import yaml
import codecs
import locale
import itertools
import jinja2
import re
import shutil

# -----------------------------------------------------------------------------

app_dir         = os.path.dirname(os.path.abspath(__file__))
page_dir        = os.path.join(app_dir, 'pages')
template_dir    = os.path.join(app_dir, 'templates')
image_root      = '/static/img/upload/'
default_charset = 'utf-8'

# -----------------------------------------------------------------------------

def make_nav(fn, extension = '.md'):
    def add_term(container, term):
        term = term.strip()
        if not term:
            return
        if term.startswith('/'):
            url = term
            path = ''.join([os.path.join(page_dir, url[1:]), extension])
            name = 'No Name'
            with codecs.open(path, 'r', encoding = default_charset) as f:
                lines = iter(f.read().split(u'\n'))
                # Read lines until an empty line is encountered.
                meta = u'\n'.join(itertools.takewhile(unicode.strip, lines))
                name = yaml.safe_load(meta)['title']
        elif '>>' in term:
            name, url = term.split('>>')[:2]
            name, url = name.strip(), url.strip()
        else:
            url = '#'
            name = term
        container.append(name)
        container.append(url)
    with codecs.open(fn, 'r', encoding = default_charset) as f:
        family_book = []
        for line in f.readlines():
            single_level = []
            raw_terms = line.split('::')
            add_term(single_level, raw_terms[0])
            if len(raw_terms) > 1:
                for level1_term in raw_terms[1].split(','):
                    add_term(single_level, level1_term)
            family_book.append(single_level)
    # structure:
    #    [[level0_name, level0_url, level1_name, level1_url, ...], [...], ...]
    return family_book

def make_nav_page(data_fn, src_fn, dst_fn, lang):
    with codecs.open(src_fn, 'r', encoding = default_charset) as f:
        template = jinja2.Template(f.read())
    family_book = make_nav(data_fn)
    rendered_navigation = template.render(nav = family_book, lang = lang)
    with codecs.open(dst_fn, 'w', encoding = default_charset) as f:
        f.write(rendered_navigation)
    os.remove(data_fn)
    return family_book


# -----------------------------------------------------------------------------

def convert_charset(src_fn, dst_fn,
    src_formats = [locale.getpreferredencoding(), 'ascii'],
    dst_format = default_charset):
    for src_format in src_formats:
        try:
            with codecs.open(src_fn, 'r', src_format) as src_f:
                with codecs.open(dst_fn, 'w', dst_format) as dst_f:
                    for line in src_f:
                        dst_f.write(line)
                    return True
        except UnicodeDecodeError:
            pass
    return False

def make_page_utf8(target_ext = '.txt'):
    def _walk(directory):
        for name in os.listdir(directory):
            full_name = os.path.join(directory, name)
            if os.path.isdir(full_name):
                _walk(full_name)
            elif name.endswith(target_ext):
                convert_charset(full_name, full_name[:-len(target_ext)]+'.md')
    _walk(page_dir)

# -----------------------------------------------------------------------------

def make_image(target_ext = '.md'):
    def _process(fn):
        content_image_regex = re.compile(r'(!.*?\[.*?\].*?)\((.*?)\)', re.I)
        head_image_regex = re.compile(
            r'(head_image:)\s*(.*?\.((jpg)|(jpeg)|(gif)|(png)|(bmp)))', re.I)
        with codecs.open(fn, 'r+', encoding = default_charset) as f:
            content = f.read()
            # replace link
            f.seek(0)
            dst_link = r'\1(%s\2)' % image_root
            content = content_image_regex.sub(dst_link, content)
            dst_link = r'\1 %s\2' % image_root
            content = head_image_regex.sub(dst_link, content)
            f.write(content)
            f.truncate()
    def _walk(directory):
        for name in os.listdir(directory):
            full_name = os.path.join(directory, name)
            if os.path.isdir(full_name):
                _walk(full_name)
            elif name.endswith(target_ext):
                _process(full_name)
    _walk(page_dir)

# -----------------------------------------------------------------------------

def make_parent_map(family_book):
    parent_map = {}
    for i, level0 in enumerate(family_book):
        for j in xrange(3, len(level0), 2):
            parent_map[level0[j]] = i
    return parent_map

# -----------------------------------------------------------------------------

def prepare():
    make_page_utf8()
    family_book, parent_map = {}, {}
    for lang in ['cn', 'jp']:
        family = make_nav_page(
            data_fn = os.path.join(page_dir, lang, 'navigation.md'),
            src_fn  = os.path.join(template_dir, 'navigation.html'),
            dst_fn  = os.path.join(template_dir,
                'rendered_navigation_%s.html' % lang),
            lang = lang)
        parent = make_parent_map(family)
        family_book[lang] = family
        parent_map[lang] = parent
    make_image()
    return family_book, parent_map

# -----------------------------------------------------------------------------

if __name__ == "__main__":
    prepare()

# -----------------------------------------------------------------------------
