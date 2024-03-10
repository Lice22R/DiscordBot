from . settings import *


@client.event   
async def on_ready():
    logger.info('BOT Launched')
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

@client.event
async def on_member_join(member):
    try:
        channel = client.get_channel( 1050504789605228567 )
        # Получаем объект роли по ID
        starting_role = discord.utils.get(member.guild.roles, id= 1216498611068604498) # Тут в id должна быть константная переменная

        # Проверяем, найдена ли роль
        if starting_role:
            # Выдаем роль участнику
            await member.add_roles(starting_role)
            await channel.send(embed= discord.Embed(description=f'Пользователь {member.name} тут'))

            print(f"Role {starting_role.name} added to {member.display_name}")
        else:
            print(f"Role with ID {1216498611068604498} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

@client.command(pass_context=True)
async def flavor(ctx):
    await ctx.send("Choose a flavor!", view=MyView())
