import yfinance as yf

def get_historical_data(ticker, start_date, end_date):
    print(f"Descargando datos para {ticker} desde {start_date} hasta {end_date}...")
    data = yf.download(ticker, start=start_date, end=end_date)
    print(data.head())
    return data