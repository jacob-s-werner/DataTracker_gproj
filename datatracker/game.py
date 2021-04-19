from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
import requests, json

bp = Blueprint('game', __name__)


@bp.route('/gamingConsole')
def best_selling_console():
    response = requests.get('https://api.dccresource.com/api/games')
    games = response.json()

    sales_per_console = {}
    best_selling_console = (0, "")

    for game in games:
        platform = game['platform']
        sales = game['globalSales']

        if platform not in sales_per_console:
            sales_per_console[platform] = sales
        else:
            sales_per_console[platform] += sales

    for console in sales_per_console:
        if sales_per_console[console] > best_selling_console[0]:
            best_selling_console = (sales_per_console[console], console)

    message = f"The best selling console is {best_selling_console[1]} with {best_selling_console[0]} sales"
    phrase = "fasdfadf"
    return render_template('sample/index.html', message=message, word=phrase)


@bp.route('/game', methods=('GET', 'POST'))
def game_search():
    message = "This text is coming from the 'sample.py' module, not the html file!"
    phrase = "Python is cool!"
    return render_template('sample/index.html', message=message, word=phrase)

@bp.route('/genreSearch', methods=('GET', 'POST'))
def genre_search():
    message = "This text is coming from the 'sample.py' module, not the html file!"
    phrase = "Python is cool!"
    return render_template('sample/index.html', message=message, word=phrase)

@bp.route('/consoleWarWinner')
def console_war_winner():
    message = "This text is coming from the 'sample.py' module, not the html file!"
    phrase = "Python is cool!"
    return render_template('sample/index.html', message=message, word=phrase)
