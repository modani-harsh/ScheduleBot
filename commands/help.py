import discord

async def help(message, args = [], prefix = 's!') :
  if (args and args[0]) :
    if (args[0] == 'del') :
      wembed = discord.Embed(title=f'`{prefix}del`')
      wembed.description = f'A command that can be used to delete messages from your own webhook. Type `{prefix}del <message channel> <message id>` to delete it. The channel needs to be mentioned if the message is coming from another channel, otherwise it is optional.\nNote: You can only delete your messages or messages from your own webhook unless you have the Manage Messages permission.'
      wembed.set_footer(text='Scheduler')
      await message.channel.send(embed=wembed)

    elif (args[0] == 'echo') :
      wembed = discord.Embed(title=f'`{prefix}echo`')
      wembed.description = f'A command that can be used to send messages from your own webhook.\n\n**Syntax:**\n`{prefix}echo "<content>" <channel> <date> <time>`\n\n`<content>` defaults to a blank string, `<channel>` defaults to the channel that the message is sent in, and `<date>` and `<time>` default to current date and time.\n**Note:** The order of the arguments is irrelevant, but the content of the message must be enclosed in double quotes.'
      wembed.set_footer(text='Scheduler')
      await message.channel.send(embed=wembed)

    elif (args[0] == 'help') :
      wembed = discord.Embed(title=f'`{prefix}help`')
      wembed.description = f'{prefix}help provides help on using commands. Use `{prefix}help <command>` for help on the command.'
      wembed.set_footer(text='Scheduler')
      await message.channel.send(embed=wembed)

    elif (args[0] == 'timezone') :
      wembed = discord.Embed(title=f'`{prefix}timezone`')
      wembed.description = f'{prefix}timezone lets users set their timezone for scheduling messages. Use it in the format `{prefix}timezone <(±)%H:%M> to get the timezone offset in minutes. If timezone is not set, the bot operates at UTC.'
      wembed.set_footer(text='Scheduler')
      await message.channel.send(embed=wembed)

    elif (args[0] == 'prefix') :
      wembed = discord.Embed(title=f'`{prefix}prefix`')
      wembed.description = f'{prefix}prefix lets users set the prefix to replace `{prefix}`. Use it in the format `{prefix}prefix "<new_prefix>"` with the new prefix in double quotes.'
      wembed.set_footer(text='Scheduler')
      await message.channel.send(embed=wembed)
      
    else :
      wembed = general_help(message, prefix)
      await message.channel.send(f'Oops! {args[0]} does not seem to be a valid command. Here is help for the bot:', embed=wembed)
  else :
    wembed = general_help(message, prefix)
    await message.channel.send(embed=wembed)

def general_help(message, prefix = 's!') :
  wembed = discord.Embed(title='Scheduler')
  wembed.description = f'**A bot to help with your message scheduling needs\n\nCommands:**\n\n• `{prefix}del`\n• `{prefix}echo`\n• `{prefix}help`\n• `{prefix}timezone`\n• `{prefix}prefix`\n\nTo see more on each command, simply type `{prefix}help <command>`'
  wembed.set_footer(text='Scheduler')
  return wembed
