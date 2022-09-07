import discord, random
baza = ("Да-да, Россия побила рекорд нищеты", "Ukraine is gonna win", "Да, обычно нищие так и говорят", "Ой, ну ты и нищенок")
Soviet = ("Не, ну это вообще нищета. Там только мороженое было вкуснее(До тех пор, пока граждане узнали о зарубежном)")
Empire = ("Че-че? Эта 'империя' уже давно уничтожена", "Ты, наверное, хотел сказать 'Нищая Империя'?")
Свобода = ('Сейчас же не 37-й год - что хочешь, то и говори, тем более в интернете, "черный воронок" за тобой завтра не приедет. Чего прятаться-то?')
Ukraine = ("Героям Слава!", "Скоро во всех селах России", "Уже готовишься?", "Скоро все так будем орать, да еще и репарации будем платить. Так что готовься, налоги скоро повысятся")
web_site = ('https://img2.reactor.cc/pics/post/full/%D0%BF%D0%BE%D0%BB%D0%B8%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F-%D0%BA%D0%B0%D1%80%D0%B8%D0%BA%D0%B0%D1%82%D1%83%D1%80%D0%B0-%D0%BF%D0%BE%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B0-%D0%BA%D0%B0%D1%80%D0%B8%D0%BA%D0%B0%D1%82%D1%83%D1%80%D0%B0-%D0%95%D0%BB%D0%BA%D0%B8%D0%BD-7547252.jpeg','https://img2.reactor.cc/pics/comment/%D0%BF%D0%BE%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B0-%D0%92%D1%82%D0%BE%D1%80%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2-%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D1%83-2022-%D0%93%D0%B8%D1%80%D0%BA%D0%B8%D0%BD-%D0%BF%D1%80%D0%B8%D0%BA%D0%BE%D0%BB%D1%8B-%D0%B4%D0%BB%D1%8F-%D0%B4%D0%B0%D1%83%D0%BD%D0%BE%D0%B2-4657977.jpeg')
TOKEN = "" # Enter your token here 

client = discord.Client()

@client.event
async def on_ready():
    print("{0.user} is now online!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Слава России' or 'Слава РФ'): # Про РФ
        await message.channel.send(random.choice(baza)) 
    if message.content.startswith('!фотожаба'): # Фотожабы
        await message.channel.send(random.choice(web_site))
    if message.content.startswith('Слава Украине' or 'слава Украине'): # Украина
        await message.channel.send(random.choice(Ukraine))
    if message.content.startswith('Есть ли свобода слова в России?'):  # Про свободу слова
        await message.channel.send(Свобода)
    if message.content.startswith('Российская Империя' or 'РИ'): # Про РИ
        await message.channel.send(random.choice(Empire)) 
    if message.content.startswith('СССР' or 'Советский Союз' or 'совок'):  #BadComedian
        await message.channel.send(Soviet)

client.run(TOKEN)


