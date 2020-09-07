#! /usr/bin/env python3
import configparser
import requests
import discord
import asyncio
import json
import os

config = configparser.ConfigParser()
config.read('config.ini')
token = config['keys']['discord']

bot = commands.Bot(command_prefix='?', description='Small bot')

if (not os.path.exists("fights")):
	os.mkdir("fights")

#Asynchronous tasks

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(name='newcmd', pass_context='true')
async def addfight(ctx, name, strat)
	file = open("fights/" + name, "w+")
	file.write(strat)
	await ctx.channel.send("The fight is correctly added")

@bot.command(name='fight', pass_context='true')
async def fight(ctx, name)
	file = open("fights/"+name, "r")
	await ctx.channel.send(file.read())

bot.run(token)
