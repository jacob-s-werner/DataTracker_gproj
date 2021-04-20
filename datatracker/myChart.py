from pychartjs import BaseChart, ChartType, Color
import json

def to_chart_data(platform_and_sales):
    '''
    :param platform_and_sales: list of tuples of platform name and sale
    :return: json object of the data for use with chart.js
    '''
    labels = ['one', 'two']
    result = json.dumps(labels)
    return result