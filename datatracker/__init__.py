import os
import json
import requests

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )


    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import sample, game
    app.register_blueprint(sample.bp)
    app.register_blueprint(game.bp)
    # app.add_url_rule('/', endpoint='index')


    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
