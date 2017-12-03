#! /usr/bin/env/ python
#-*- coding:utf-8 -*-
__author__ = 'BCAD66'

import discord
import asyncio
import os
import random

client = discord.Client()



@client.event
async def on_ready():
    print('Logged in as')
    print('client.user.name')
    print('client.user.id')
    print('-------')

@client.event
async def on_message(message):
    if message.content.startswith('~test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculationg message...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('~sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('~abbys'):
        path = './picture/'
        files = []
        tmp = await client.send_message(message.channel, 'selecting picture...')
        for x in os.listdir(path):
            if os.path.isfile(path + x):
                files.append(x)
        num = random.randint(0, len(files))
        print(len(files))
        print(num)
        fp = open(path + files[num])
        await asyncio.sleep(1)
        await client.send_file(message.channel,fp)

client.run('MzU3NDIzODk5NjI3MjI1MDg4.DQVPUg.ojkQuy69fSEAHN8QdFvRYubviHY')
