import re
import discord
from dice import rol_dices

class Dice_Roll_Command:
  regex_command = re.compile("^\s*[+-]?\s*\d*d[1-9]\d*(\s*[+-]?\s*\d*d[1-9]\d*|\s*[+-]\s*\d+)*\s*$", flags=re.IGNORECASE)
  regex_rolls = re.compile("([+-]?)(\d*)(d([1-9]\d*))?")

  def get_regex():
    return Dice_Roll_Command.regex_command

  async def execute_command(message: discord.Message):
    roll_string = Dice_Roll_Command.remove_whitespace(message.content).lower()
    print(roll_string)
    
    if Dice_Roll_Command.is_small_dice_roll(roll_string):
      await message.channel.send('rolling '+ roll_string +': **' + Dice_Roll_Command.roll_dices_string(roll_string) + '** by ' + message.author.display_name)
    else:
      await message.channel.send('big boy roll by '+ message.author.display_name)
      await message.channel.send(Dice_Roll_Command.roll_dices_string(roll_string))

  def remove_whitespace(s: str):
    regex_whitespace = re.compile(r'\s+')
    return re.sub(regex_whitespace, '', s)

  def roll_dices_string(dices_string : str):
    result = 0
    operations = re.findall(Dice_Roll_Command.regex_rolls, dices_string)
    for operation in operations:
      result += Dice_Roll_Command.calc_dice_operation(operation)
    return str(result)

  def calc_dice_operation(parts : tuple):
    value = 0
    sign = 1 if parts[0] != '-' else -1
    print(parts)

    if parts[2] != '':
      times = int(parts[1]) if parts[1] != '' else 1
      sides = int(parts[3])
      value += rol_dices(times, sides)
    elif parts[1] != '':
      value = int(parts[1])

    return sign * value

  def is_small_dice_roll(roll_string: str):
    text_size = 8 + 4 + 6
    max_display_name_size = 32
    return len(roll_string) * 2 + text_size + max_display_name_size <= 2000