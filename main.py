import os
import discord
import commands.echo as echo
import commands.delete as delete
import commands.help as help
import commands.timezone as tz
import commands.prefix as prf
import json

client = discord.Client()
prefixes = []

def readPrefix() :
  global prefixes
  with open('config.json', 'r') as config :
    prefixes = json.loads(config.read())["prefix"]

readPrefix()

@client.event
async def on_ready() :
  print(f'Logged in as {client.user}')
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='s!help'))

@client.event
async def on_message(message) :
  global prefixes
  c_guild_id = message.guild.id
  prefix = prefixes[str(c_guild_id)]
  if message.author == client.user :
    return
  if not message.content.startswith(prefix) :
    return
  args = []
  parts = message.content[len(prefix):].lstrip(' ').split('"')
  for i in range(len(parts)) :
    if (i%2) :
      args.append(parts[i])
    elif (parts[i]) :
      args.extend(parts[i].lstrip(' ').split(' '))
  
  command = args.pop(0).lower()

  if (command == 'del') :
    await delete.delete(args, message, client)

  elif (command == 'echo') :
    await echo.echo(client, message, parts, args)

  elif (command == 'help') :
    await help.help(message, args, prefix)

  elif (command == 'prefix') :
    changed = await prf.prefix(message, parts)
    if (changed) :
      readPrefix()
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{prefix}help'))

  elif (command == 'timezone') :
    await tz.timezone(message, args)
    
token = os.environ['TOKEN']

@client.event
async def on_guild_join(guild) :
  global prefixes
  prefixes[str(guild.id)] = 's!'
  with open('config.json', 'r') as config :
    settings = json.loads(config.read())
    settings["prefix"] = prefixes
    config.close()
    config = open('config.json', 'w')
    config.write(json.dumps(settings))

client.run(token)