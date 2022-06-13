import database
import validation

INVALID_TICKER_DATE = "Not a valid ticker or date"

def get_closing_price(ticker, date):
    if validation.is_valid_date(date) == False:
        return INVALID_TICKER_DATE
    global INVALID_TICKER_DATE
    conn, cursor = database.get_connection()
    cursor.execute("SELECT price "\
                   "FROM adjusted_prices ap "\
                   "INNER JOIN stock s ON s.id = ap.stock_id "\
                   "WHERE s.ticker = %s AND ap.date = %s", (ticker, date))
    result = cursor.fetchone()
    if result is None:
        return INVALID_TICKER_DATE
    return result[0]

def get_volume(ticker, date):
    if validation.is_valid_date(date) == False:
        return INVALID_TICKER_DATE
    global INVALID_TICKER_DATE
    conn, cursor = database.get_connection()
    cursor.execute("SELECT volume "\
                   "FROM adjusted_prices ap "\
                   "INNER JOIN stock s ON s.id = ap.stock_id "\
                   "WHERE s.ticker = %s AND ap.date = %s", (ticker, date))
    result = cursor.fetchone()
    if result is None:
        return INVALID_TICKER_DATE
    return result[0]

def get_variation(ticker, initial_date, finish_date):
    if validation.is_valid_date(initial_date) == False:
        return INVALID_TICKER_DATE
    if validation.is_valid_date(finish_date) == False:
        return INVALID_TICKER_DATE
    global INVALID_TICKER_DATE
    price1 = get_closing_price(ticker, initial_date)
    if price1 == INVALID_TICKER_DATE:
        return "Invalid initial date or ticker"
    price2 = get_closing_price(ticker, finish_date)
    if price2 == INVALID_TICKER_DATE:
        return "Invalid finish date"
    return price2/price1 - 1
