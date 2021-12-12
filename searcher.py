import requests
from flask import Blueprint, g, redirect, render_template, request, session, url_for

bp = Blueprint('search', __name__, url_prefix='')


@bp.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['query']
        app_id = "b45d0929"
        app_key = "d64b4f3936b290abd2fb6368151f7a34"
        url = "https://api.edamam.com/api/recipes/v2?type=public&q={}&app_id={}&app_key={}".format(query, app_id, app_key)
        response = requests.get(url=url)
        recipes = response.json()['hits']
        print(recipes)
        return render_template('recipe-list.html', recipes=recipes)
    return render_template('index.html')




