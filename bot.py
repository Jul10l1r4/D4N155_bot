from telegram.ext import Updater, CommandHandler
import logging
from dotenv import load_dotenv
from requests import get
from os import getenv

load_dotenv()

logger = logging.getLogger(__name__)

def get_json_response(url):
    api_response = get(url)
    return api_response.json()

def domain(bot, update):
    domain_name = update.message.text.split(" ")[1]
    api_formated_response = get_json_response(f"https://d4n155.herokuapp.com/domain/{domain_name}")
    domain_list = api_formated_response["result"]["data"]
    domain_length = api_formated_response["result"]["length"]
    nl = '\n'
    message_domain = f"🔗URL LIST {nl}🎯{domain_name}{nl}{nl.join(domain_list)}{nl}📡{domain_length} urls"
    update.message.reply_text(message_domain)

def read_text(bot, update):
    words = update.message.text.split(" ")[1:]
    api_formated_response = get_json_response(f"https://d4n155.herokuapp.com/make/{' '.join(words)}")
    remote_wordlist = api_formated_response["result"]["wordlist"]["url"]
    wordlist_length = api_formated_response["result"]["wordlist"]["length"]
    nl = '\n'
    message_text = f"WORDLIST{nl}🔍{words}{nl}🔗{remote_wordlist}📡{wordlist_length} words"
    update.message.reply_text(message_text)

def read_url(bot, update):
    url = update.message.text.split(" ")[1]
    api_formated_response = get_json_response(f"https://d4n155.herokuapp.com/domain/0?url={url}")
    remote_wordlist = api_formated_response["result"]["wordlist"]["url"]
    wordlist_length = api_formated_response["result"]["wordlist"]["length"]
    nl = '\n'
    message_text = f"WORDLIST{nl}🎯{url}{nl}🔗{remote_wordlist}📡{wordlist_length} words"
    update.message.reply_text(message_text)


def help_msg(bot, update):
    message_help = (
        "OWASP D4N155 🕵🏿️‍♂️\nis an information security audit tool that creates intelligent wordlists based on the content of the target page using OSINT.\n"
        "⚒Github: https://github.com/owasp/D4N155\n"
        "🔗Site: https://owasp.org/www-project-d4n155/\n"
        "📦Docker: https://github.com/OWASP/D4N155/packages/129009\n"
        "📡API: https://github.com/OWASP/D4N155/tree/api\n"
        "🐃GPLv3\n"
        "USE\n"
        "/domain domain-here.com\n"
        "/text text here with whitespace\n"
        "/make https://url.complete.com\n"
        "/help for show it"
        )
    update.message.reply_text(message_help)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    """Start the bot."""
    updater = Updater(getenv('TOKEN'))
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("domain", domain))
    dp.add_handler(CommandHandler("text", read_text))
    dp.add_handler(CommandHandler("make", read_url))
    dp.add_handler(CommandHandler("help", help_msg))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
