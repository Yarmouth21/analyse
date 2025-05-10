import yfinance as yf

# Télécharger les données journalières du S&P 500 sur 6 mois
sp500 = yf.download("^GSPC", period="6mo", interval="1d")

sp500["Daily_Variance_%"] = ((sp500["High"] - sp500["Low"]) / sp500["Low"]) * 100
sp500.to_csv("sp500_6mo_daily.csv", sep=";")


