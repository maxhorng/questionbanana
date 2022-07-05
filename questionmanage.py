#導入 Discord.py
import discord
#client 是我們與 Discord 連結的橋樑
client = discord.Client()

#調用 event 函式庫
@client.event   
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)
    game = discord.Game('StreetFighterV')
    await client.change_presence(status=discord.Status.idle, activity=game)
@client.event
#當有訊息時

async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    #如果包含 ，機器人回傳 
    if message.content.startswith('我想問'):
        role1 = message.guild.get_role(886882939227484170)#資工
        role2 = message.guild.get_role(993219166456778753)#資訊管理學系
        role3 = message.guild.get_role(993219246316331053)#資訊傳播學系
        role4 = message.guild.get_role(993225277897445477)#英國語文學系
        role5 = message.guild.get_role(993225338240913489)#西班牙語文學系
        role6 = message.guild.get_role(993225408877174824)#日本語文學系
        role7 = message.guild.get_role(993228438678806662)#中國文學系
        role8 = message.guild.get_role(993228529393209414)#社會工作與兒童少年福利學系
        role9 = message.guild.get_role(993228593083723866)#台灣文學系
        role10 = message.guild.get_role(993228631310618636)#法律學系
        role11 = message.guild.get_role(993228655994085476)#生態人文學系
        role12 = message.guild.get_role(993228748151332876)#大眾傳播學系
        role13 = message.guild.get_role(993233882075910167)#財務工程學系
        role14 = message.guild.get_role(993234151497007195)#應用化學系
        role15 = message.guild.get_role(993234279960154255)#食品營養學系
        role16 = message.guild.get_role(993234392984059995)#化妝品科學系
        role17 = message.guild.get_role(993234651567116299)#資料科學暨大數據分析與應用學系
        role18 = message.guild.get_role(993234790402768907)#企業管理學系
        role19 = message.guild.get_role(993234795259760680)#國際企業學系
        role20 = message.guild.get_role(993234798606815373)#會計學系
        role21 = message.guild.get_role(993234801517658244)#觀光事業學系
        role22 = message.guild.get_role(993234803077959761)#財務金融學系
        sprole1 = message.guild.get_role(993621670738804867)#測試一
        sprole2 = message.guild.get_role(993621719904419910)#側試二

        author= message.author
        outrole=''
        
        if role1 in message.author.roles:
            outrole='資工系'

        elif role2 in message.author.roles:
            outrole='資管系'
            
        elif role3 in message.author.roles:
            outrole='資傳系'

        elif role4 in message.author.roles:
            outrole='英文系'

        elif role5 in message.author.roles:
            outrole='西文系'

        elif role6 in message.author.roles:
            outrole='日文系'

        elif role7 in message.author.roles:
            outrole='中文系'

        elif role8 in message.author.roles:
            outrole='社工系'
            
        elif role9 in message.author.roles:
            outrole='台文系'
        elif role10 in message.author.roles:
            outrole='法律系'

        elif role11 in message.author.roles:
            outrole='生態人文學系'

        elif role12 in message.author.roles:
            outrole='大傳系'

        elif role13 in message.author.roles:
            outrole='財工系'

        elif role14 in message.author.roles:
            outrole='應化系'
            
        elif role15 in message.author.roles:
            outrole='食品營養系'

        elif role16 in message.author.roles:
            outrole='化科系'

        elif role17 in message.author.roles:
            outrole='資科系'

        elif role18 in message.author.roles:
            outrole='企管系'

        elif role19 in message.author.roles:
            outrole='國企系'

        elif role20 in message.author.roles:
            outrole='會計系'

        elif role21 in message.author.roles:
            outrole='觀光系'

        elif role22 in message.author.roles:
            outrole='財金系'
        elif sprole1 in message.author.roles:
            outrole='測試一'
        elif sprole2 in message.author.roles:
            outrole='測試二'

        await message.delete()
        await message.channel.send("["+outrole+"]"+message.author.mention+"\n"+message.content+"\n========================================") #"@%s",message.author.id,
        
        
        

client.run('OTkzMjXXXXXX') #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
