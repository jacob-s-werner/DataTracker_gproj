from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint

bp = Blueprint('game', __name__)

@bp.route('/gamingConsole')
def best_selling_console():
    message = "This text is coming from the 'sample.py' module, not the html file!"
    phrase = "Python is cool!"
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
