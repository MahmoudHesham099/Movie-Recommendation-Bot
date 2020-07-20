from rivescript import RiveScript
import os.path

file = os.path.dirname(__file__)
brain = os.path.join(file,'./brain')

bot = RiveScript(utf8=True)
bot.load_directory(brain)
bot.sort_replies()

def chat(message):
    if message == "":
        return -1, "No message found "
    else:
        response = bot.reply("user", message)
    if response:
        return 0, response
    else:
        return -1, "No response found"