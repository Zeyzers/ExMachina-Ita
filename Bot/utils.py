async def __sync_commands_to_guild(self, guild: discord.Guild):
        """!
        Funzione per inviare tutti i comandi a un server
        Farlo per tutti i server all'avvio è inefficiente, ma un modo rapido per inviare nuovi comandi a tutti i server
        """
        try:
            self.tree.copy_global_to(guild=guild)
            await self.tree.sync(guild=guild)
        except discord.errors.Forbidden:
            print(f"Non ho i permessi per inviare i comandi slash a: '{guild.name}'")



# Funzione per generare dinamicamente il messaggio di aiuto
def generate_help_message(ctx):
    embed = discord.Embed(title='# Comandi del Bot', description='### Ecco i comandi disponibili e le loro descrizioni:', color=discord.Color.dark_purple())

    sorted_commands = sorted(client.commands, key=lambda cmd: cmd.name)
    for command in sorted_commands:
        if not command.hidden:
            embed.add_field(name=f"**[-{command.name}]**", value=command.description, inline=False)

    return embed

