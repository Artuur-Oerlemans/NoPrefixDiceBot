import re
import discord
from commands.Help_Command import Help_Command
from commands.Dice_Roll_Command import Dice_Roll_Command

is_roll_regex = re.compile("^\s*\d*d[1-9]\d*(\s*\+\s*\d*d[1-9]\d*)*(\s*[+-]\s*\d+)*\s*$")

async def detect_commands(message: discord.Message):

  if Dice_Roll_Command.get_regex().match(message.content):
    await Dice_Roll_Command.execute_command(message)
  elif Help_Command.get_regex().match(message.content):
    await Help_Command.execute_command(message)