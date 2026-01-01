import yfinance as yf

sp500 = yf.download(
    "^GSPC",
    start="2020-01-01",
    end="2025-12-31",
    interval="1d"
)

sp500.to_csv("./data/raw/sp500_prices.csv")