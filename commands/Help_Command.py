import re
import discord

class Help_Command:
  regex = re.compile("^dhelp\s*$", flags=re.IGNORECASE)

  def get_regex():
    return Help_Command.regex

  async def execute_command(message: discord.Message):
    help_embed = discord.Embed(title="Help", description="List of commands")
    help_embed.add_field(name="dice roll", value="ex.: d20, 2d6+5", inline=False)
    help_embed.add_field(name="get list of commands", value="dhelp", inline=False)
    await message.channel.send(embed=help_embed)