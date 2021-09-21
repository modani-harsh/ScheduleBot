import json

async def prefix(message, parts) :
  if (len(parts) > 1) :
    if (parts[1].strip(' ')) :
      prefix = parts[1].strip(' ')
      with open('config.json', 'r') as config :
        settings = json.loads(config.read())
        settings["prefix"][str(message.guild.id)] = prefix
        config.close()
        config = open('config.json', 'w')
        config.write(json.dumps(settings))
        config.close()
        await message.channel.send(f'Prefix set to {prefix}. Use this in future commands.')
        return True
    else :
      await message.channel.send('Prefix is blank.')
      return False

  else :
    await message.channel.send('Unable to resolve prefix. Ensure that prefix is enclosed in double quotes.')
    return False
        