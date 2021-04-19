from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
from .game_database import game_data
import requests, json

bp = Blueprint('game', __name__)


@bp.route('/gamingConsole')
def best_selling_console():


    sales_per_console = {}
    best_selling_console = (0, "")
    console_list = []

    for game in game_data:
        platform = game['platform']
        sales = game['globalSales']
        if game['year'] is not None and game['year'] > 2012:
            if platform not in sales_per_console:
                sales_per_console[platform] = sales
            else:
                sales_per_console[platform] += sales

    for console in sales_per_console:
        console_list.append((sales_per_console[console], console))

    console_list.sort(key = lambda x: -x[0])
    message = f"The best selling console is {best_selling_console[1]} since 2013 with {best_selling_console[0]} sales"
    phrase = "fasdfadf"
    return render_template('sample/index.html', message=message, word=phrase, display_list=console_list)


@bp.route('/game', methods=('GET', 'POST'))
def game_search():
    if request.method == 'POST':
        game_title = request.form['title']
        error = None

        if not game_title:
            error = 'You must enter a title'

        if error is not None:
            flash(error)
        elif request.form['title'] == "go home":
            return redirect(url_for('sample.index'))
        else:
            matches = {}
            for gameObj in game_data:
                gameTitle = gameObj['name'].lower()
                if gameTitle.find(game_title.lower()) != -1:
                    if gameTitle in matches:
                        matches[gameTitle][1].append((gameObj['platform'], gameObj['globalSales']))
                    else:
                        matches[gameTitle] = [gameObj, [(gameObj['platform'], gameObj['globalSales'])]]

            return render_template('sample/postform.html', page_title=game_title)
    else:
        return render_template('sample/postform.html', page_title="PostForm from Module Function")

@bp.route('/genreSearch', methods=('GET', 'POST'))
def genre_search():
    if request.method == 'POST':
        game_genre = request.form['genre']
        game_year = request.form['year']
        error = None

        if not game_genre:
            error = 'You must enter a genre'
        if not game_year:
            error = 'You must enter a year'
        game_year = int(game_year)
        if error is not None:
            flash(error)
        else:
            result = 0
            for gameObj in game_data:
                gameGenre = gameObj['genre'].lower()
                gameYear = gameObj['year']
                if gameGenre.find(game_genre.lower()) != -1:
                    if gameYear is not None and gameYear == game_year:
                        result += gameObj['globalSales']

            return render_template('game/genreSearchResult.html', page_title="Searc Results", page_genre = game_genre,\
                                   page_year = game_year, num_sold = result)
    else:
        return render_template('game/genreSearch.html', page_title="PostForm from Module Function")

@bp.route('/consoleWarWinner')
def console_war_winner():
    message = "This text is coming from the 'sample.py' module, not the html file!"
    phrase = "Python is cool!"
    return render_template('sample/index.html', message=message, word=phrase)
