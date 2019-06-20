#! /usr/bin/env python3
import configparser
import requests
import discord
import asyncio
import json
import os

client = discord.Client()
triggerchar = '?'
config = configparser.ConfigParser()
config.read('config.ini')
token = config['keys']['discord']

if (not os.path.exists("fights")):
	os.mkdir("fights")

#Asynchronous tasks

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
	if message.content.startswith(triggerchar + 'addfight'):
		tab = message.content.split()
		name = tab[1]
		strat = ' '.join(tab[2:])
		file = open("fights/" + name, "w+")
		file.write(strat)
		await message.channel.send("fight was added")
	elif message.content.startswith(triggerchar + 'fight'):
		tab = message.content.split()
		name = tab[1]
		print("accessing " + name)
		file = open("fights/" + name, "r")
		s = file.read()
		await message.channel.send(s)

client.run(token)
