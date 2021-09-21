# ScheduleBot
A Discord bot used to schedule messages to be sent by users at a specific time.

Users can send the following commands:
- `s!echo` - users can schedule messages to be sent by their webhook using this command
- `s!del` - users can delete their own messages or messages sent by their webhook with this command
- `s!prefix` - used to set the server prefix of the bot (replaces s!)
- `s!timezone` - users can use this to help with scheduling messages
- `s!help` - to provide help on the commands.

## s!echo
A command that can be used to send messages from your own webhook.  
**Syntax:**  
`{prefix}echo "<content>" <channel> <date> <time>`

`<content>` defaults to a blank string, `<channel>` defaults to the channel that the message is sent in, and `<date>` and `<time>` default to current date and time.  
**Note:** The order of the arguments is irrelevant, but the content of the message must be enclosed in double quotes.

## s!del
A command that can be used to delete messages from your own webhook.  
**Syntax:**  
`{prefix}del <message channel> <message id>`

The channel needs to be mentioned if the message is coming from another channel, otherwise it is optional.  
**Note**: You can only delete your messages or messages from your own webhook unless you have the Manage Messages permission.

## s!timezone
A command that lets users set their timezone for scheduling messages.  
**Syntax:**  
`{prefix}timezone <(±)%H:%M>`

If timezone is not set, the bot operates at UTC.

## s!prefix
A command that lets users set the prefix to replace the server prefix.  
**Syntax:**  
`{prefix}prefix "<new_prefix>"` 

**Note:** The new prefix must be in double quotes.

## s!help
A command that provides help on using commands.  
Use `{prefix}help <command>` for help on the command.  
**Note**: If the `<command>` is not provided, or is not a command in this list, then it defaults to general help.
