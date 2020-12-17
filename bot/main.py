import discord
from discord.ext import commands
import requests
import json
import subprocess as sp
import os

client = commands.Bot(command_prefix="$")
token = os.getenv("DISCORD_BOT_TOKEN")


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


@client.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")


@client.command()
async def inspire(ctx):
    await ctx.send(get_quote())


@client.command()
async def py(ctx, arg):
    result = run_python(arg)
    await ctx.send(result)

client.run(token)
