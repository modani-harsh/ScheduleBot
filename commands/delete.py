async def delete(args, message, client) :
  wchannel = message.channel
  if (args) :
      id = args[0]
  else :
    await wchannel.send('Error: No ID specified.')
    return
  if (len(message.channel_mentions)) :
    channel_id = message.raw_channel_mentions[0]
    wchannel = await client.fetch_channel(channel_id)
  try :
    msg = await wchannel.fetch_message(id)
    if (message.author.guild_permissions.manage_messages or msg.author.name.split('#')[0] == message.author.name.split('#')[0]) :
      await msg.delete()
    else :
      await message.channel.send('You do not have permissions to delete that message.')
      return
  except :
    await message.channel.send('The channel mentioned may not be correct. Please mention the channel from which the message to be deleted is specified.')
    return
  
  await message.channel.send(f'Message with ID {id} deleted.', delete_after=5)