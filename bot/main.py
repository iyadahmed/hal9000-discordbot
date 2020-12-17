import discord
import requests
import json
import subprocess as sp

client = discord.Client()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return quote


def run_python(code):
    proc = sp.run(['python3', './run_python.py', code],
                  capture_output=True,
                  timeout=1,
                  encoding='UTF-8')
    result = "Results:\n{0.stdout}\nErrors: {0.stderr}".format(proc)
    return result

def run_c(code):
    pass


@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content.startswith('$hello'):
        await msg.channel.send('Hello')

    elif msg.content.startswith('$inspire'):
        quote = get_quote()
        await msg.channel.send(quote)

    elif msg.content.startswith('$py'):
        result = run_python(msg.content.strip('$py'))
        await msg.channel.send(result)


client.run('Nzg4NzIwNDEwMDA2Mzg4NzU2.X9nnHw.3lW_oO6HeMXJma8zDeCQgl53yW0')
