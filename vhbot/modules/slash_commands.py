"""
Handles slash commands
"""
import discord
from discord.ext import commands
from discord import app_commands
import typing

import requests
import json


# noinspection PyUnresolvedReferences
@app_commands.command(name="contract", description="temp desc")
@app_commands.guild_install()
async def contract(interaction: discord.Interaction):
    contracts_url = "https://raw.githubusercontent.com/fanaticscripter/Egg/refs/heads/master/contracts/data/contracts.json"
    contracts_json = await download_json(contracts_url)
    contracts_for_command_raw = contracts_json[-5:]
    contracts_for_command = [str]
    for contract in contracts_for_command_raw:
        print(contract['id'])
        contracts_for_command.append(contract['id'])
    print(contracts_for_command)
    # await interaction.response.send_message(contracts_for_command)
    await interaction.response.send_message("check logs")


# noinspection PyUnresolvedReferences
@app_commands.command(name="post_contract", description="Post a new contract to the contracts channel.")
@app_commands.guild_install()
async def post_contract(interaction: discord.Interaction, contract: str, coop_name: str):
    link = f"https://eicoop-carpet.netlify.app/{contract}/{coop_name}/"
    await interaction.response.send_message(link)


@post_contract.autocomplete("contract")
async def post_contract_autocomplete(
    interaction: discord.Interaction,
    current: str
) -> typing.List[app_commands.Choice[str]]:
    contracts_for_command = await load_contracts()
    data = []
    for contract in contracts_for_command:
        data.append(app_commands.Choice(name=contract, value=contract))
    return data


async def download_json(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None
    except json.JSONDecodeError as e:
         print(f"JSON decode error: {e}")
         return None

async def load_contracts() -> [str]:
    contracts_url = "https://raw.githubusercontent.com/fanaticscripter/Egg/refs/heads/master/contracts/data/contracts.json"
    contracts_json = await download_json(contracts_url)
    contracts_for_command_raw = contracts_json[-5:]
    contracts_for_command = []
    for contract in contracts_for_command_raw:
        contracts_for_command.append(contract['id'])
    print(contracts_for_command)
    return contracts_for_command


async def setup(bot: commands.Bot):
    # bot.tree.add_command(contract)
    bot.tree.add_command(post_contract)
