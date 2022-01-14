import re
import discord
from dice import roll_dices_string
from Advantage import Advantage


class Dice_Roll_Command:
    regex_command = re.compile(
        "^\s*[+-]?\s*\d*d[1-9]\d*(\s*[+-]?\s*\d*d[1-9]\d*|\s*[+-]\s*\d+)*\s*(a[dvantage]{0,8}|d[isadvantage]{0,11})?\s*$",
        flags=re.IGNORECASE)

    def get_regex():
        return Dice_Roll_Command.regex_command

    async def execute_command(message: discord.Message) -> None:
        roll_string_with_advantage = Dice_Roll_Command.remove_whitespace(
            message.content).lower()
        advantage = Dice_Roll_Command.getAdvantage(roll_string_with_advantage)
        print(advantage)
        roll_string = Dice_Roll_Command.remove_advantage(
            roll_string_with_advantage)

        if advantage == Advantage.NONE:
            await Dice_Roll_Command.roll_no_advantage(message, roll_string)
        elif advantage == Advantage.ADVANTAGE:
            await Dice_Roll_Command.roll_with_advantage(message, roll_string)
        elif advantage == Advantage.DISADVANTAGE:
            await Dice_Roll_Command.roll_with_disadvantage(
                message, roll_string)

    async def roll_no_advantage(message: discord.Message, roll_string) -> None:
        roll_result, rolls = roll_dices_string(roll_string)

        shortMessage = 'rolling ' + roll_string + ' by *' + message.author.display_name + "*\n**" + str(roll_result) + "**"

        if Dice_Roll_Command.has_allowed_message_size(shortMessage):
            await message.channel.send(shortMessage)
            if Dice_Roll_Command.has_allowed_message_size(str(rolls)):
                await message.channel.send(str(rolls))
        else:
            await message.channel.send('big boy roll by *' +
                                       message.author.display_name + "*")
            await message.channel.send(str(roll_result))

    async def roll_with_advantage(message: discord.Message,
                                  roll_string) -> None:

        first_result, first_rolls = roll_dices_string(roll_string)
        second_result, second_rolls = roll_dices_string(roll_string)

        if first_result >= second_result:
            result = "**" + str(first_result) + "** : " + str(second_result)
            final_rolls = first_rolls
        else:
            result = str(first_result) + " : **" + str(second_result) + "**"
            final_rolls = second_rolls

        shortMessage = 'rolling ' + roll_string + ' with advantage by *' + message.author.display_name + '*\n' + result
        if Dice_Roll_Command.has_allowed_message_size(shortMessage):
            await message.channel.send(shortMessage)
            if Dice_Roll_Command.has_allowed_message_size(str(final_rolls)):
                await message.channel.send(str(final_rolls))
        else:
            await message.channel.send('big boy roll with advantage by *' +
                                       message.author.display_name + "*")
            await message.channel.send(max(first_result, second_result))

    async def roll_with_disadvantage(message: discord.Message,
                                     roll_string) -> None:

        first_result, first_rolls = roll_dices_string(roll_string)
        second_result, second_rolls = roll_dices_string(roll_string)

        if first_result < second_result:
            result = "**" + str(first_result) + "** : " + str(second_result)
            final_rolls = first_rolls
        else:
            result = str(first_result) + " : **" + str(second_result) + "**"
            final_rolls = second_rolls

        shortMessage = 'rolling ' + roll_string + ' with disadvantage by *' + message.author.display_name + '*\n' + result
        if Dice_Roll_Command.has_allowed_message_size(shortMessage):
            await message.channel.send(shortMessage)
            if Dice_Roll_Command.has_allowed_message_size(str(final_rolls)):
                await message.channel.send(str(final_rolls))
        else:
            await message.channel.send('big boy roll with disadvantage by *' +
                                       message.author.display_name + "*")
            await message.channel.send(min(first_result, second_result))

    def remove_advantage(roll_string_with_advantage: str) -> str:
        match = re.search("(a[dvantage]{0,8}|d[isadvantage]{0,11})?\s*$",
                          roll_string_with_advantage)
        return roll_string_with_advantage[:match.start()]

    def remove_whitespace(s: str) -> str:
        regex_whitespace = re.compile(r'\s+')
        return re.sub(regex_whitespace, '', s)

    def getAdvantage(roll_string_with_advantage: str) -> Advantage:
        if bool(re.search("\da[dvantage]{0,8}$", roll_string_with_advantage)):
            return Advantage.ADVANTAGE
        elif bool(
                re.search("\dd[isadvantage]{0,11}$",
                          roll_string_with_advantage)):
            return Advantage.DISADVANTAGE
        else:
            return Advantage.NONE

    def has_allowed_message_size(message: str):
        return len(message) <= 2000
