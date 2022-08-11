from discord_webhook import DiscordWebhook, DiscordEmbed
import schedule,time

webhook = DiscordWebhook(url='')
embed = DiscordEmbed(title='', description='''
Have a nice day!
''', color='0099ff')
webhook.add_embed(embed)

def messagesend():
    response = webhook.execute()

schedule.every().monday.at("13:00").do(messagesend)
print("started!")
while True:
    schedule.run_pending()
    time.sleep(1)
