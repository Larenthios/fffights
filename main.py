#! /usr/bin/env python3
import configparser
import requests
import discord
import asyncio
import json
import os

client = discord.Client()
triggerchar = '?'
onfig = configparser.ConfigParser()
config.read('config.ini')
token = config['keys']['discord']

#Asynchronous tasks

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith(triggerchar + 'addfight')
        tab = message.content.split()
        name = tab[1]
        strat = ' '.join(tab[2:])
        file = os.mkdir("fights/" + name)
        file.write(strat)
    elif message.content.startswith(triggerchar + 'fight')
        tab = message.content.split()
        name = tab[1]
        s = file.read("fights/" + name)
        await client.send_message(message.channel, s)

client.run(token)