from . settings import *


@client.event   
async def on_ready():
    logger.info('BOT Launched')
    print('BOT connected') 


class MyView(discord.ui.View):
    @discord.ui.select(
        placeholder = PLACEHOLDER,
        min_values = 1,
        max_values = len(CHOOSEN_GAMES),
        options = [discord.SelectOption(
                label=game.get('label', None),
                description=game.get('description', None),
                emoji=game.get('emoji', None),
                value=game.get('value', None)
            ) 
            for game in CHOOSEN_GAMES
        ]
    )
    async def select_callback(self, select, interaction):
        try:
            member = interaction.user
            for selected_value in select.values:
                role_id = ROLE_ASSOCIATIONS.get(selected_value)
                role = interaction.guild.get_role(int(role_id))
                if role is not None:
                    await member.add_roles(role)
                    await interaction.response.send_message(f"Роли успешно выданы!", ephemeral=True)
        except Exception as e:
            logger.error(e)


@client.event
async def on_member_join(member):
    try:
        channel = client.get_channel(1050504789605228567)
        starting_role = discord.utils.get(member.guild.roles, id=STARTING_ROLE_ID)
        if starting_role:
            await member.add_roles(starting_role)
            await channel.send(embed= discord.Embed(description=f'Пользователь {member.name} тут'))
            logger.info(f'User {member.name} joined us')
            logger.info(f'Role {starting_role.name} added to {member.display_name}')
        else:
            logger.error(f"STARTING_ROLE_ID not found.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")


@client.command(pass_context=True)
async def flavor(ctx):
    await ctx.send("Choose a flavor!", view=MyView())
    