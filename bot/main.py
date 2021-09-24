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
    quote = json_data[0]["q"]
    quotee = json_data[0]["a"]
    return f"{quote} -{quotee}"


def get_cat_fact():
    response = requests.get("https://catfact.ninja/fact")
    json_data = response.json()
    return json_data["fact"]


@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))


@client.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")


@client.command()
async def inspire(ctx):
    await ctx.send(get_quote())


@client.command()
async def catfact(ctx):
    await ctx.send(get_cat_fact())


client.run(token)
