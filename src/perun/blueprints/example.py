import os

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

flask_view_name = 'example_page'

example_page = Blueprint(flask_view_name, __name__,
                        template_folder=os.path.dirname(__file__) + '/templates')


@example_page.route('/', defaults={'page': 'index'})
@example_page.route('/example_page/<page>')
def show(page):
    return 'TEST' + page


@example_page.route('/example_page')
def show2():
    return render_template('example/index.html.jinja2')
