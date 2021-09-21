from datetime import datetime as dt, timedelta as td
import time
import discord
import json

async def echo(client, message, parts, args, msg = "** **", wtime=dt.now().time(), wdate=dt.now().date()) :
  if (len(parts) > 1) :
    if (parts[1]) :
      msg = parts[1]

  timedeficit = td(hours=0, minutes=0)
  with open('config.json', 'r') as config :
    settings = json.loads(config.read())
    userl = settings["users"]
    for user in userl :
      if (f'{message.author}' in user.keys()) :
        offset = user[f'{message.author}'][1:].split(':')
        sign = -int(user[f'{message.author}'][0]+'1')
        timedeficit = td(hours=sign*int(offset[0]), minutes=sign*int(offset[1]))
        break

  for targ in args :
    try :
      wtime = dt.strptime(targ, '%H:%M').time()
      break
    except :
      wtime = dt.now().time()

  for darg in args :
    try :
      wdate = dt.strptime(darg, '%d-%m-%Y').date()
      break
    except :
      wdate = dt.now().date()

  wchannel = message.channel
  if (len(message.channel_mentions)) :
    channel_id = message.raw_channel_mentions[0]

    wchannel = await client.fetch_channel(channel_id)

  w_displaydt = dt.combine(wdate, wtime)
  wdt = w_displaydt+timedeficit
  wembed = discord.Embed(title='Sending message:')
  wembed.description = f'{msg}\nin: <#{wchannel.id}>\non: {w_displaydt.date()} {w_displaydt.time()}:00 Local time'
  wembed.set_footer(text='Scheduler')
  confirm = await message.channel.send(embed=wembed)
  await confirm.add_reaction('✅')
  await confirm.add_reaction('❎')

  @client.event
  async def on_reaction_add(reaction, user) :
    if (user == message.author and reaction.emoji == '✅') :
      await message.channel.send('Message being sent.')
      while (dt.now() < wdt) :
        time.sleep(60-dt.now().time().second)
      else :
        webhook = await wchannel.create_webhook(name=message.author.name)
        await webhook.send(msg, username=message.author.name, avatar_url=message.author.avatar_url)
        await webhook.delete()
    elif (user == message.author and reaction.emoji == '❎') :
      await message.channel.send('Message cancelled.')