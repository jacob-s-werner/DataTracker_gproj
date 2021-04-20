from flask import Flask, jsonify, request, redirect, flash, render_template, url_for, Blueprint
from .game_database import game_data

bp = Blueprint('game', __name__)

@bp.route('/')
def index():
    message = "Welcome"
    return render_template('game/index.html', message=message)

@bp.route('/gamingConsole')
def best_selling_console():

    sales_per_console = {}
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
    message = f"The best selling console is {console_list[0][1]} since 2013 with {console_list[0][0]} sales"
    return render_template('game/bestSellingConsole.html', message=message, display_list=console_list)


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
                if request.form.get('exact_match'):
                    if gameTitle == game_title.lower():
                        if gameTitle in matches:
                            matches[gameTitle][1].append((gameObj['platform'], gameObj['globalSales']))
                        else:
                            matches[gameTitle] = [gameObj, [(gameObj['platform'], gameObj['globalSales'])]]
                else:
                    if gameTitle.find(game_title.lower()) != -1:
                        if gameTitle in matches:
                            matches[gameTitle][1].append((gameObj['platform'], gameObj['globalSales']))
                        else:
                            matches[gameTitle] = [gameObj, [(gameObj['platform'], gameObj['globalSales'])]]

            i = 0
            gameList = []
            for key in matches:
                gameList.append(key)
                i += 1
                # Only up to 10
                if i == 10:
                    break
            return render_template('game/gameDetails.html', page_title=game_title, game_data=matches, game_list=gameList, post_data=True)
    else:
        return render_template('game/gameDetails.html', page_title="PostForm from Module Function", game_data=None, game_list=None, post_data=False)

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
            platformData = {}
            numSold = 0
            for gameObj in game_data:
                gameGenre = gameObj['genre'].lower()
                gameYear = gameObj['year']
                if gameGenre.find(game_genre.lower()) != -1:
                    if gameYear is not None and gameYear == game_year:
                        platform = gameObj['platform']
                        numSold += gameObj['globalSales']
                        if platform in platformData:
                            platformData[platform] += gameObj['globalSales']
                        else:
                            platformData[platform] = gameObj['globalSales']

            return render_template('game/genreSearchResult.html', page_title="Search Results", platform_data = platformData,\
                                   page_year = game_year, num_sold = numSold)
    else:
        return render_template('game/genreSearch.html', page_title="PostForm from Module Function")

@bp.route('/consoleWarWinner')
def console_war_winner():

    publisher_by_platform = {}
    results = []

    for game in game_data:
        platform = game['platform']
        sales = game['globalSales']
        publisher = game['publisher']

        if platform not in publisher_by_platform:
            publisher_by_platform[platform] = {}

        publishers = publisher_by_platform[platform]
        if publisher not in publishers:
            publishers[publisher] = sales
        else:
            publishers[publisher] += sales

    for platform in publisher_by_platform:
        platform_sales = publisher_by_platform[platform]
        publisher_name = ""
        highest_sales = 0
        for publisher in platform_sales:
            if platform_sales[publisher] > highest_sales:
                highest_sales = platform_sales[publisher]
                publisher_name = publisher

        results.append((platform, publisher_name, highest_sales))

    return render_template('game/consoleWarWinner.html', page_title="Console War Winner", game_data=results)