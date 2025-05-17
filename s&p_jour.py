import yfinance as yf

sp500 = yf.download("^GSPC", period="1d", interval="1m")

sp500.to_excel("sp_500_today.xlsx")