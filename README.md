# Discord RSI Bot

## Description

Discord RSI Bot is a bot that monitors the Relative Strength Index (RSI) for the SOL/USDT trading pair on the spot market of Bybit. The bot sends a notification to a specified Discord channel when the RSI value exceeds 70 or falls below 30.


## Requirements

- Docker
- Python 3.10.12 (optional, if you want to run tests locally)

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/Gluszka13/discord-rsi-bot.git
    cd discord-rsi-bot
    ```

2. Create a `.env` file in the root directory and add your Discord bot token and channel ID:
    ```
    DISCORD_TOKEN=your_discord_bot_token
    CHANNEL_ID=your_channel_id
    ```

3. Build and run the Docker container:
    ```bash
    docker build -t discord-rsi-bot .
    docker run discord-rsi-bot
    ```

The bot will start and monitor the RSI value, sending notifications to the specified Discord channel when the RSI exceeds 70 or falls below 30.

## Running Tests

1. To run tests locally, ensure you have Python installed and the required libraries:
    ```bash
    pip3 install -r requirements.txt
    pip3 install unittest
    ```

2. Run the tests with the following command:
    ```bash
    python3 tests.py
    ```

## Additional Information

- Ensure that the environment variables in the `.env` file are set correctly.
- The bot monitors the SOL/USDT trading pair on the spot market with a 1-hour interval and period 14h.
- Notifications are sent to the specified Discord channel when the RSI value exceeds 70 or falls below 30.