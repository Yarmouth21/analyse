import pandas as pd
import numpy as np

# Charger ton fichier Excel ou CSV
# Exemple : df = pd.read_csv('tes_données.csv')
df = pd.read_excel("sp_500_today.xlsx")  # à adapter

# Assure-toi que les colonnes sont bien numériques
colonnes = ['Close', 'Open', 'High', 'Low', 'Volume']
for col in colonnes:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# --- EMA ---
df['EMA9'] = df['Close'].ewm(span=9, adjust=False).mean()
df['EMA21'] = df['Close'].ewm(span=21, adjust=False).mean()

# --- VWAP ---
cum_vol = df['Volume'].cumsum()
cum_vol_price = (df['Close'] * df['Volume']).cumsum()
df['VWAP'] = cum_vol_price / cum_vol

# --- RSI ---
delta = df['Close'].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(14).mean()
avg_loss = loss.rolling(14).mean()
rs = avg_gain / avg_loss
df['RSI'] = 100 - (100 / (1 + rs))

# --- Bollinger Bands ---
sma20 = df['Close'].rolling(window=20).mean()
std20 = df['Close'].rolling(window=20).std()
df['Bollinger_Mid'] = sma20
df['Bollinger_Upper'] = sma20 + 2 * std20
df['Bollinger_Lower'] = sma20 - 2 * std20

# Nettoyage des lignes incomplètes
df.dropna(inplace=True)

# Sauvegarder le résultat
df.to_excel("données_avec_indicateurs.xlsx", index=False)
