import discord,os,random,requests

TOKEN = os.environ['TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

def randHex():
    randomText=""
    for _ in range(6):
        randomText+="0123456789ABCDEF"[random.randrange(16)]
    return randomText

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith(r'\emoji'):
        texts=message.content.split(r' ')
        
        color=texts[1]
        if color=="r":
            color=randHex()
        color=color.upper()+"FF"
        content=texts[2].replace("_","%0A")

        data=requests.get("https://emoji-gen.ninja/emoji_download?align=center&amp;back_color=00000000&amp;color=%s&amp;font=notosans-mono-bold&amp;locale=ja&amp;public_fg=true&amp;size_fixed=false&amp;stretch=true&amp;text=%s"%(color,content)).content
        
        name=texts[3] if len(texts)>=4 else texts[2]

        await message.guild.create_custom_emoji(name=name,image=data)

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)