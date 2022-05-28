from flask import Flask, render_template, request
import adjusted_prices_dao

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('html/index.html')

@app.route('/about')
def about():
    return root()

@app.route('/price')
def get_price():
    ticker = request.args.get('ticker', type = str)
    date = request.args.get('date', type = str)
    return str(adjusted_prices_dao.get_closing_price(ticker, date))

@app.route('/volume')
def get_volume():
    ticker = request.args.get('ticker', type = str)
    date = request.args.get('date', type = str)
    return str(adjusted_prices_dao.get_volume(ticker, date))

@app.route('/variation')
def get_variation():
    ticker = request.args.get('ticker', type = str)
    initial_date = request.args.get('initial_date', type = str)
    finish_date = request.args.get('finish_date', type = str)
    return str(adjusted_prices_dao.get_variation(ticker, initial_date, finish_date))

