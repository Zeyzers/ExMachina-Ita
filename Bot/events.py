from setup import *
import utils
client.remove_command('help')

@client.event
async def on_ready():
    member_count = 0
    guild_string = ''
    for g in client.guilds:
            guild_string += f"{g.name} - {g.id} - Members: {g.member_count}\n"
            member_count += g.member_count
            print(g)
            await utils.__sync_commands_to_guild(client, g)

    print(f"\n---\n"
        f"Il bot '{client.user.name}' si è connesso, attivo su {len(client.guilds)} server:\n{guild_string}"
        f"---\n"
    )

        # imposta lo stato del bot
    await client.change_presence(
        activity=discord.Activity(type=discord.ActivityType.custom, name='Usa -help', state= 'Usa -help')
    )


# Definisci una funzione per iniziare a digitare
async def start_typing(ctx):
    async with ctx.channel.typing():
        await asyncio.sleep(1)

# Definisci una funzione per smettere di digitare
async def stop_typing(ctx):
    await asyncio.sleep(1)  # Aggiungi un ritardo per assicurarti che l'indicatore di digitazione sia visibile


# Registra start_typing come before_invoke per tutti i comandi
@client.before_invoke(start_typing)
async def before_command_invoke(ctx):
    pass

# Registra stop_typing come after_invoke per tutti i comandi
@client.after_invoke(stop_typing)
async def after_command_invoke(ctx):
    pass


@client.command(name='help', description='Mostra i comandi disponibili e le loro descrizioni')
async def help_command(ctx):
    await ctx.send(embed=utils.generate_help_message(ctx))

@client.tree.command(name='help', description='Mostra i comandi disponibili e le loro descrizioni')
async def help_command(ctx):
    await ctx.response.send_message(embed=utils.generate_help_message(ctx))


@client.tree.command(name='ping', description='Fornisce la latenza tra il server e l\'API')
async def ping(ctx):
    await ctx.response.send_message(f"🏓La latenza è {round(client.latency * 1000)}ms.")

@client.command(name='ping', description='Fornisce la latenza tra il server e l\'API')
async def ping(ctx):
    await ctx.send(f"🏓La latenza è {round(client.latency * 1000)}ms.")








@client.tree.command(name='userinfo', description='Mostra informazioni su un utente')
async def userinfo(ctx, user: discord.Member = None):
    user = user or ctx.user
    roles = [role.mention for role in user.roles]
    embed = discord.Embed(title=f'Informazioni utente: {user.display_name}#{user.discriminator}', color=discord.Color.green())
    embed.set_thumbnail(url=user.display_avatar.url)
    embed.add_field(name='ID', value=user.id, inline=False)
    embed.add_field(name='Creato il', value=user.created_at.strftime('%Y-%m-%d'), inline=False)
    embed.add_field(name='Entrato nel server', value=user.joined_at.strftime('%Y-%m-%d'), inline=False)
    embed.add_field(name='Ruoli', value=', '.join(roles), inline=False)
    await ctx.response.send_message(embed=embed)


@client.command(name='userinfo', description='Mostra informazioni su un utente')
async def userinfo(ctx, user: discord.Member = None):
    user = user or ctx.author
    roles = [role.mention for role in user.roles]
    embed = discord.Embed(title=f'Informazioni utente: {user.display_name}#{user.discriminator}', color=discord.Color.green())
    embed.set_thumbnail(url=user.display_avatar.url)
    embed.add_field(name='ID', value=user.id, inline=False)
    embed.add_field(name='Creato il', value=user.created_at.strftime('%Y-%m-%d'), inline=False)
    embed.add_field(name='Entrato nel server', value=user.joined_at.strftime('%Y-%m-%d'), inline=False)
    embed.add_field(name='Ruoli', value=', '.join(roles), inline=False)
    await ctx.send(embed=embed)



@client.tree.command(name='serverinfo', description='Mostra informazioni sul server')
async def serverinfo(ctx):
    server = ctx.guild
    embed = discord.Embed(title=f'Informazioni server: {server.name}', color=discord.Color.blue())
    embed.set_thumbnail(url=server.icon)
    embed.add_field(name='Proprietario', value=server.owner, inline=False)
    embed.add_field(name='Membri', value=server.member_count, inline=False)
    embed.add_field(name='Data di creazione', value=server.created_at.strftime('%Y-%m-%d'), inline=False)
    await ctx.response.send_message(embed=embed)


@client.command(name='serverinfo', description='Mostra informazioni sul server')
async def serverinfo(ctx):
    server = ctx.guild
    embed = discord.Embed(title=f'Informazioni server: {server.name}', color=discord.Color.blue())
    embed.set_thumbnail(url=server.icon)
    embed.add_field(name='Proprietario', value=server.owner, inline=False)
    embed.add_field(name='Membri', value=server.member_count, inline=False)
    embed.add_field(name='Data di creazione', value=server.created_at.strftime('%Y-%m-%d'), inline=False)
    await ctx.send(embed=embed)




@client.tree.command(name='roll', description='Tira una quantità personalizzata di dadi con un numero personalizzato di facce')
async def roll(ctx, qty: int, sides: int):
    rolls = [random.randint(1, sides) for i in range(qty)]
    plural = 'dadi' if len(rolls)>1 else 'dado'
    await ctx.response.send_message(f"Tirando {qty} {plural} con {sides} facce: {rolls}")

@client.command(name='roll', description='Tira una quantità personalizzata di dadi con un numero personalizzato di facce')
async def roll(ctx, qty: int, sides: int):
    rolls = [random.randint(1, sides) for i in range(qty)]
    plural = 'dadi' if len(rolls)>1 else 'dado'
    await ctx.send(f"Tirando {qty} {plural} con {sides} facce: {rolls}")



@client.command(name='kick', description='Espelle un utente dal server con una motivazione opzionale')
async def kick(ctx: commands.Context, member: discord.Member, *, reason: str = None):
    if ctx.author.guild_permissions.kick_members:
        if reason is None:
            reason = "Motivo non fornito."
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} è stato espulso dal server. Motivo: {reason}")
    else:
        await ctx.send("Non hai il permesso di utilizzare questo comando.")


@client.tree.command(name='kick', description='Espelle un utente dal server con una motivazione opzionale')
async def kick(ctx: commands.Context, member: discord.Member, *, reason: str = None):
    author = ctx.user
    if author.guild_permissions.kick_members:
        if reason is None:
            reason = "Motivo non fornito."
        await member.kick(reason=reason)
        await ctx.response.send_message(f"{member.mention} è stato espulso dal server. Motivo: {reason}")
    else:
        await ctx.response.send_message("Non hai il permesso di utilizzare questo comando.")



@client.command(name='ban', description='Vieta un utente dal server con una motivazione opzionale')
async def ban(ctx: commands.Context, member: discord.Member, *, reason: str = None):
    if ctx.author.guild_permissions.ban_members:
        if reason is None:
            reason = "Motivo non fornito."
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} è stato bannato dal server. Motivo: {reason}")
    else:
        await ctx.send("Non hai il permesso di utilizzare questo comando.")


@client.tree.command(name='ban', description='Vieta un utente dal server con una motivazione opzionale')
async def ban(ctx: commands.Context, member: discord.Member, *, reason: str = None):
    if ctx.user.guild_permissions.ban_members:
        if reason is None:
            reason = "Motivo non fornito."
        await member.ban(reason=reason)
        await ctx.response.send_message(f"{member.mention} è stato bannato dal server. Motivo: {reason}")
    else:
        await ctx.response.send_message("Non hai il permesso di utilizzare questo comando.")


@client.command(name='pardon', description='Sbanna un utente che era stato precedentemente bannato dal server.')
async def pardon(ctx, user_id: int):
    if ctx.user.guild_permissions.ban_members:
        # Recupera l'utente bannato
        banned_user = await ctx.guild.fetch_ban(discord.Object(id=user_id))

        # Sbanna l'utente
        await ctx.guild.unban(banned_user.user)

        # Informa l'utente dello sbannato
        await ctx.send(f"{banned_user.user.name}#{banned_user.user.discriminator} è stato sbannato dal server.")
    else:
        await ctx.send("Non hai il permesso di utilizzare questo comando.")



@client.command(name="clear", description="Cancella una quantità specificata di messaggi dal canale corrente")
async def clear(ctx: commands.Context, amount: int):
    if ctx.author.guild_permissions.manage_messages:
        await ctx.send(f"Sto cancellando {amount} messaggi.")
        await ctx.channel.purge(limit=amount+1)
    else:
        await ctx.send("Non hai il permesso di utilizzare questo comando.")

@client.tree.command(name="clear", description="Cancella una quantità specificata di messaggi dal canale corrente")
async def clear(ctx: commands.Context, amount: int):
    if ctx.user.guild_permissions.manage_messages:
        await ctx.response.send_message(f"Sto cancellando {amount} messaggi.")
        await ctx.channel.purge(limit=amount+1)
    else:
        await ctx.response.send_message("Non hai il permesso di utilizzare questo comando.")



@client.command(name='lockdown', description='Blocca o sblocca un canale per limitare o consentire i messaggi degli utenti.')
async def lockdown(ctx, channel: discord.TextChannel, action: str):
    if ctx.author.guild_permissions.administrator:
        if action.lower() == 'lock':
            # Blocca il canale
            await channel.set_permissions(ctx.guild.default_role, send_messages=False)
            await ctx.send(f"{channel.mention} è stato bloccato. Gli utenti non possono più inviare messaggi.")
        elif action.lower() == 'unlock':
            # Sblocca il canale
            await channel.set_permissions(ctx.guild.default_role, send_messages=True)
            await ctx.send(f"{channel.mention} è stato sbloccato. Gli utenti ora possono inviare messaggi.")
        else:
            await ctx.send("Azione non valida. Specifica 'lock' o 'unlock'.")


@client.command(name='rolereact', description='Configura reazioni di ruolo per consentire agli utenti di assegnarsi ruoli reagendo ai messaggi.')
async def rolereact(ctx):
    # Recupera i ruoli esistenti del server e convertili in una lista
    roles = list(ctx.guild.roles)

    # Rimuovi il ruolo @everyone dalla lista
    roles.remove(ctx.guild.default_role)

    # Chiedi all'amministratore di selezionare ruoli ed emoji
    await ctx.send("Seleziona i ruoli e le relative emoji da aggiungere come reazioni al messaggio. Formato: menzione_ruolo:emoji, nome_ruolo:emoji, ...")
    try:
        response = await client.wait_for('message', timeout=60, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
    except asyncio.TimeoutError:
        await ctx.send("Hai impiegato troppo tempo per rispondere.")
        return

    # Analizza la risposta dell'amministratore e convalida i ruoli ed emoji selezionati
    role_emoji_pairs = [pair.strip().split(':') for pair in response.content.split(',')]
    valid_pairs = []
    for pair in role_emoji_pairs:
        if len(pair) == 2:
            role, emoji = pair
            role = role.strip()
            emoji = emoji.strip()
            # Controlla se il ruolo è menzionato
            if role.startswith('<@&') and role.endswith('>'):
                role_id = int(role[3:-1])
                role_object = discord.utils.get(ctx.guild.roles, id=role_id)
                if role_object:
                    role_name = role_object.name
                    valid_pairs.append((role_name, emoji))
            else:
                # Controlla se esiste il nome del ruolo
                if discord.utils.get(ctx.guild.roles, name=role):
                    valid_pairs.append((role, emoji))

    # Crea un messaggio con le istruzioni per le reazioni di ruolo
    instructions = "Reagisci a questo messaggio per assegnarti un ruolo!\n\n"
    for role_name, emoji in valid_pairs:
        role = discord.utils.get(ctx.guild.roles, name=role_name)
        instructions += f"Reagisci con {emoji} per assegnarti il ruolo {role_name}.\n"

    message = await ctx.send(instructions)

    # Aggiungi le reazioni corrispondenti a ciascun ruolo ed emoji selezionati
    for role_name, emoji in valid_pairs:
        await message.add_reaction(emoji)

    # Funzione per gestire gli eventi di reazione
    async def reaction_handler(reaction, user):
        if user == client.user:
            return
        if reaction.message == message and reaction.emoji in [emoji for _, emoji in valid_pairs]:
            role_name = next(role for role, emoji_pair in valid_pairs if emoji_pair == reaction.emoji)
            role = discord.utils.get(ctx.guild.roles, name=role_name)
            if role:
                await user.add_roles(role)
                await user.send(f"Ti è stato assegnato il ruolo: {role.name}")

    # Attendere le reazioni e chiamare la funzione reaction_handler
    client.add_listener(reaction_handler, name="on_reaction_add")



@client.command(name='tempvoice', description='Crea canali vocali temporanei che vengono eliminati automaticamente dopo un periodo di inattività.')
async def tempvoice(ctx):
    # Crea il canale vocale temporaneo
    new_channel = await ctx.guild.create_voice_channel(name="Canale Temporaneo")

    # Imposta le autorizzazioni per il nuovo canale
    await new_channel.set_permissions(ctx.guild.default_role, connect=True, speak=True)

    # Informa l'utente sul canale creato
    await ctx.send(f"È stato creato un canale vocale temporaneo: {new_channel.mention}. Questo canale verrà eliminato automaticamente dopo un periodo di inattività.")

    # Definisci un'attività di sfondo per controllare l'attività del canale
    async def check_activity():
        while True:
            # Attendere 5 minuti
            await asyncio.sleep(150)

            # Controlla se ci sono membri connessi al canale
            if not new_channel.members:
                # Elimina il canale se nessuno è connesso
                await new_channel.delete()
                break  # Esci dal ciclo una volta eliminato il canale

    # Avvia l'attività di sfondo
    client.loop.create_task(check_activity())

