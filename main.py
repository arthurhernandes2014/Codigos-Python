# Importando a libry do Discord.
from asyncio.windows_events import NULL
import discord
from discord.client import _cancel_tasks
from discord.ext import commands, tasks
import random
import datetime
from discord.utils import async_all

# Inserindo o prefixo do BOT e também colocando a função CASE onde consegue distinguir de letras maisculas...
# e minusculas para o nosso bot.
client = commands.Bot(command_prefix = "!", case_insensitive = True)

# Evento quando que quando o BOT estiver on ele ira mandar uma mensagem que está on.
@client.event
async def on_ready():
    print('*-----------------*')
    print('Entramos como {0.user}'.format(client))
    print('O ID é {}'.format(client.user.id))
    print('*----------------*')

    # Aqui starta a função de timer pra vir junto com o bot para não dar erro.
    current_time.start() 

# Função onde o BOT ira retornar uma mensagem para o usuário, usando função assincrono ou em outras palavras...
# é uma corrotina, onde não tem ordem para iniciar e não precisa esperar nenhuma outra função.
@client.command()
async def ola(ctx):
    await ctx.send(f'Olá, {ctx.author}')

# Canal que apaga os xingamentos do servidor.
@client.event
async def on_message(ctx):
    # Aqui é uma resolução caso o author seja o mesmo que o usuário.
    if ctx.author == client.user:
        return
    
    # Preciso achar um jeito de colocar os xingamentos dentro de uma lista e ler essa lista toda.
    # Aqui é as palavras que o bot vai bloquear dentro dos canais.
    if "macaco" or "makaco" or "macako" or "makako" or "preto" in ctx.content:
        await ctx.channel.send(f"Ei {ctx.author.name}, não xinga seu macaco burro!")

        # Aqui vai apagar os xingamentos.
        await ctx.delete()
    
    await client.process_commands(ctx)

# Essa função é basicamente a rolagem dos dados, utilizando a função assincrona e o método await para mandar uma...
# MSG para o servidor quando requisitado, como diz o nome é uma função de espera que tá pronta para ser executada.
@client.command()
async def dado(ctx, num = ''):
    # Condição que verifica se o user digitou algum número.
    if(num == ''):
        await ctx.send(f'Digite um número seu macaco, burro...')
    # Condição onde rola dois dados e traz dois números aleatórios.
    elif (int(num) > 6): 
        varNum = random.randint(1,int(num))  
        varNum2 = random.randint(1,int(num)) 
        await ctx.send(f'Os números rolados dos dados é {varNum} e {varNum2}')
    # Condição onde rola três dados e traz dois números aleatórios.
    elif (int(num) > 12):
        varNum = random.randint(1,int(num))  
        varNum2 = random.randint(1,int(num)) 
        varNum3 = random.randint(1,int(num)) 
        await ctx.send(f'Os números rolados dos dados é {varNum} e {varNum2} e {varNum3}')
    # Condição onde rola apenas um dado e taz um número aleatório.
    else:
        varNum = random.randint(1,int(num))     
        await ctx.send(f'O número rolado do dado é {varNum}')

# Criação da função onde fica todo os backscreen do bot, onde mostra o Title, descrição, cor, imagem, autor, thumbs...
# footer e fields.
@client.command()
async def ajuda(ctx):
    botDescription = discord.Embed(
        title = 'Titúlo do Thurzin',
        description = 'Descrição do Thurzin',
        color = discord.Colour.blue()
    )
    
    botDescription.set_author(name = "Thurzin", icon_url = 'https://image.flaticon.com/icons/png/512/2857/2857351.png')
    botDescription.set_thumbnail(url = 'https://blog.fortestecnologia.com.br/wp-content/uploads/2020/01/fortes-tecnologia-inteligencia-artificial.png')
    botDescription.set_image(url = 'https://img.ibxk.com.br/2020/07/28/28180233520250.jpg?w=1120&h=420&mode=crop&scale=both')
    botDescription.set_footer(text='Teste de Footer')

    botDescription.add_field(name = 'Nome do Field', value = 'Valor do Field', inline = True)
    botDescription.add_field(name = 'Nome do Field', value = 'Valor do Field', inline = True)
    botDescription.add_field(name = 'Nome do Field', value = 'Valor do Field', inline = False)
    botDescription.add_field(name = 'Nome do Field', value = 'Valor do Field', inline = True)
    botDescription.add_field(name = 'Nome do Field', value = 'Valor do Field', inline = True)

    await ctx.send(embed = botDescription )

# Função que traz a hora e o dia atual, a cada 1 hora e imprime na sala do discord.
@tasks.loop(hours=1)
async def current_time():
    # Método dá biblioteca datetime onde pega o horario e o dia de agora, e passando tudo para a variavel now.
    now = datetime.datetime.now()

    # Passando a hora e o dia para a váriavel now.
    now = now.strftime("%d/%m/%Y às %H:%M:%S")

    # Pegando o ID da sala onde o bot era ficar colocando a data. Sala de Teste do Thurzin Bot.
    channel = client.get_channel(882045776933584996)

    # Imprime a mensagem no canal com a seguinte frase e a hora.
    await channel.send("Data atual: " + now)


# Rodando o BOT pegando o TOKEN dele que foi fornecido pelo site no Discord
client.run('ODgyMDM5OTM5MTQ2MDYzODky.YS1ltQ.Si4eQ5hY1VdTG6qRkYhk1Gv3ODc')
