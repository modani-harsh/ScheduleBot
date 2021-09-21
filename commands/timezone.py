import json

async def timezone(message, args) :
  if (len(args)) :
    offset = args[0][1:].split(':')
    try :
      for i in range(len(offset)) :
        offset[i] = int(offset[i])
      if not (0 <= offset[0] < 12 and 0 <= offset[1] < 60 and args[0][0] in '+-') :
        await message.channel.send('Inavlid timezone format. Use `(±)%H:%M` format.')
        return
    except :
      await message.channel.send('Inavlid timezone format. Use `(±)%H:%M` format.')
      return
  else :
    await message.channel.send('Timezone not specified.')
    return
  
  with open('config.json', 'r') as config :
    settings = json.loads(config.read())
    username = f'{message.author}'
    userl = settings["users"].copy()
    for user in userl :
      if username in user.keys() :
        user[username] = args[0]
        break
    else :
      userl.append({username:args[0]})
    settings["users"] = userl
    config.close()
    config = open('config.json', 'w')
    config.write(json.dumps(settings))
    config.close()
    await message.channel.send(f'Timezone `{args[0]}` added successfully.')