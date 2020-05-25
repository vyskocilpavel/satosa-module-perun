import os

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from pathlib import Path

path = Path().absolute()

flask_view_name = 'simple_page'

simple_page = Blueprint(flask_view_name, __name__,
                        template_folder=os.path.dirname(__file__) + '/templates')


@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/test_page/<page>')
def show(page):

    return 'TEST' + page + '-' + simple_page.template_folder + '-' + str(path) + '-'


@simple_page.route('/test_page')
def show2():
    return render_template('test/index.html.jinja2')


def get_name():
    return 'simple_page'
