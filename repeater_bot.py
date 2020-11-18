from telethon import TelegramClient, events

BOT_TOKEN = '1417551617:AAGP0J_U6JdzKd7ygOuaRSyRJ2yqQirUO4s'
API_ID = 2444478
API_HASH = '16895919d3d8a4e6bca9ba083b211845'

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)


@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    """Send a message when the command /start is issued."""
    await event.respond('Привет! Я бот-попугай, повторяю твои сообщения)')
    raise events.StopPropagation


@bot.on(events.NewMessage)
async def echo(event):
    """Echo the user message."""
    await event.respond(event.text)


def main():
    """Start the bot."""
    bot.run_until_disconnected()


if __name__ == '__main__':
    main()
