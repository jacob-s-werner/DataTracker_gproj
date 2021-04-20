from pychartjs import BaseChart, ChartType, Color
import json

class MyBarGraph(BaseChart)
    type = ChartType.Bar

    class data:
        label = "Game"
        data = [12, 19, 3, 17, 10]
        backgroundColor = Color.Green

    def __init__(self, game):
        jsonStr = json.dumps(game)

