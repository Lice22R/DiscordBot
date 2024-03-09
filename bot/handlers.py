from . settings import *


@client.event   
async def on_ready():
    print('BOT connected') 

@client.command(pass_context=True)
async def hello(ctx):
    await ctx.send('Hello, im a test bot for discord')

class MyView(discord.ui.View):
    @discord.ui.select(
        placeholder = PLACEHOLDER,
        min_values = 1,
        max_values = len(CHOOSEN_GAMES),
        options = [discord.SelectOption(
                label=game['label'], 
                description=game['description'],
                emoji=game['emoji'],
                value=game['value']
            ) 
            for game in CHOOSEN_GAMES
        ]
    )
    async def select_callback(self, select, interaction):
        await interaction.response.send_message(f"Awesome! I like {select.values[0]} too!", ephemeral=True)

@client.command(pass_context=True)
async def flavor(ctx):
    await ctx.send("Choose a flavor!", view=MyView())
