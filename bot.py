import discord
import requests
import pandas as pd
import ta
import asyncio
import os
import time

from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

# Period used to calculate RSI.
PERIOD = 14

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    # Event handler when the bot is ready
    print(f'We have logged in as {client.user}')
    await fetch_and_notify_rsi()

async def fetch_and_notify_rsi():
    # Fetches K-line data and notifies if RSI is above 70 or below 30
    while True:
        data = fetch_klines()
        rsi = calculate_rsi(data)

        if rsi is not None:
            print(f'RSI: {rsi}')
            if rsi > 70 or rsi < 30:
                print("Sending alert")
                await send_message(f'RSI Alert! Current RSI: {rsi}')

        last_candle = data[0]
        # Last candle close time (in seconds).
        close_time = int(last_candle[0]) // 1000
        # Next candle should be available in 1h from the last candle close time.
        next_candle_time = close_time + 3600
        current_time = int(time.time())
        # Wait 1 more second to make sure the new candle is available.
        sleep_time = next_candle_time - current_time + 1

        if sleep_time > 0:
            print(f'Sleep for {sleep_time}s')
            await asyncio.sleep(sleep_time)
        

def fetch_klines():
    # Fetches the latest K-line data from Bybit API
    url = "https://api.bybit.com/v5/market/kline"
    params = {
        "category": "spot",
        "symbol": "SOLUSDT",
        "interval": "60", # Time frame is 60 minutes.
        "limit": PERIOD, # We are only interested in the last `PERIOD` candles.
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    data = response.json()
    return data.get("result", {}).get("list", [])

def calculate_rsi(data):
    # Calculates the RSI value from K-line data
    df = pd.DataFrame(data, columns=['start', 'open', 'high', 'low', 'close', 'volume', 'quote_volume'])
    df['close'] = df['close'].astype(float)
    rsi = ta.momentum.RSIIndicator(df['close'], window=PERIOD).rsi()
    return rsi.iloc[-1]

async def send_message(message):
    # Sends a message to the specified Discord channel
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(message)

if __name__ == '__main__':
    # Runs the Discord bot
    client.run(TOKEN)
