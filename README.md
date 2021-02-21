# D4N155_bot

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/73da1c591b194b92b4c60c3fbc13801d)](https://app.codacy.com/manual/Jul10l1r4/D4N155_bot?utm_source=github.com&utm_medium=referral&utm_content=Jul10l1r4/D4N155_bot&utm_campaign=Badge_Grade_Dashboard)

Telegram bot: Using the OWASP D4N155 API. See: [owasp/D4N155](https://github.com/owasp/d4n155/tree/api)

## USE
Make the `.env` and set `TOKEN` for you Telegram bot: ([Make a bot](https://core.telegram.org/bots))
```bash
echo "TOKEN='xxxxxxxxxx'" > .env
```
## Set crontab
```bash
60 *	* * *	root	python3 /root/dandara/collector.py
```
