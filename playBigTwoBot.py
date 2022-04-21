#version    1.2
#Date       2021/11/18

#導入 Discord.py
import discord
#為了asyncio.sleep()
import asyncio
import time
from discord.ext import commands
from discord import FFmpegPCMAudio
#import requests
import json
#from apikeys import *

#client 是我們與 Discord 連結的橋樑
client = discord.Client()

#調用 event 函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：', client.user)
    game = discord.Game('正在玩大老二')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == client.user:
        return
    if '老二' in message.content:
        #發送訊息，並將本次訊息資料存入tmpmsg，方便之後刪除
        tmpmsg = await message.channel.send('https://cdn.discordapp.com/attachments/528269514144481281/910174275963600977/big2.jpg')
        #停頓0.5秒
        await asyncio.sleep(0.5)
    if '重修' in message.content:
        #發送訊息，並將本次訊息資料存入tmpmsg，方便之後刪除
        tmpmsg = await message.channel.send('https://cdn.discordapp.com/attachments/528269514144481281/910593232767946772/unknown.png')
        #停頓0.5秒
        await asyncio.sleep(0.5)
    if (('政權' in message.content) or ('正銓' in message.content)):
        #發送訊息，並將本次訊息資料存入tmpmsg，方便之後刪除
        tmpmsg = await message.channel.send('頂級美女')
        #停頓0.5秒
        await asyncio.sleep(0.5)
    if '洗澡' in message.content:
        #發送訊息，並將本次訊息資料存入tmpmsg，方便之後刪除
        tmpmsg = await message.channel.send('https://cdn.discordapp.com/attachments/528269514144481281/905840804780707861/UsOlz26h.png')
        #停頓0.5秒
        await asyncio.sleep(0.5)
    if 'RBen' in message.content:
        #發送訊息，並將本次訊息資料存入tmpmsg，方便之後刪除
        tmpmsg = await message.channel.send('https://cdn.discordapp.com/attachments/655070031314550794/910778881424912414/72732732_416519608928455_7419913899169808384_n.jpg')
        #停頓0.5秒
        await asyncio.sleep(0.5)
    if '如果可以' in message.content:
        #發送訊息，並將本次訊息資料存入tmpmsg，方便之後刪除
        tmpmsg = await message.channel.send('妳的聲音 解開了故事的謎語\n落下一萬年的約定\n大樹下的妳 紅色圍巾 手心裡捧的雨\n哭了笑了 除了妳還是妳\n我們 如果又一次錯過 不敢牽起妳的手\n我會多麼寂寞 等待紅線來的時候\n如果可以 我想和妳回到那天相遇\n讓時間停止 那一場雨\n只想擁抱 妳在身邊的證據 吻妳的呼吸\n一眨眼 一瞬間 妳說好就是永遠\n不會變（嗚 嗚）\n大樹下的妳 紅色圍巾 手心裡捧的雨\n哭了笑了 除了妳還是妳\n我們 如果又一次錯過 不敢牽起妳的手\n如果沒有如果 等到紅線來的時候\n如果可以 我想和妳回到那天相遇\n讓時間停止 那一場雨\n只想擁抱 妳在身邊的證據 吻妳的呼吸\n一眨眼 一瞬間 妳說好就是永遠\n如果可以 茫茫人海千年一眼相遇\n月光下轉身 那就是妳\n紅線劃過 深藏輪迴的秘密 我揮霍運氣\n因為妳 才讓我 背對命運不害怕\n靠近了 相信了 到底我們愛得有多狼狽\n暴雨狂風也不想防備\n愛了 就愛了 只刻在我們淚光的約定\n火開出了花\n如果可以 我想和妳回到那天相遇\n讓時間停止 那一場雨\n只想擁抱 妳在身邊的證據 吻妳的呼吸\n一眨眼 一萬年 留給我別困住妳\n如果可以 茫茫人海千年一眼相遇\n月光下轉身 那就是妳\n紅線劃過 深藏輪迴的秘密 我花光運氣\n妳是我 賭上世界的 決定')
        #停頓0.5秒
        await asyncio.sleep(0.5)
    if '上水的花' in message.content:
        #發送訊息，並將本次訊息資料存入tmpmsg，方便之後刪除
        tmpmsg = await message.channel.send('你的冷淡 使人感覺\n我的熱情是欠債\n所有疼惜 甘若是笑虧\n原諒你頭一拜 對愛的反背\n我就跳入 心酸的大火\n\n感情愈重 愈來愈憨\n看無事實像瘋仔\n一直做夢 生活卡好過\n你哪著遐慘忍 講老實話\n連擱搬幸福 攏毋願奉陪\n\n上水的花 若是刺著心嘛會流血\n浪漫的愛 忽然間變風吹\n不管失眠幾落暝 我眼屎流外多\n猶原沒發覺 苦苦留戀是夯枷\n\n上水的花 欲飛看心情沒解說\n我的寂寞 是乎你的情批\n朋友罵我太狼狽 跟著妳玲瓏迺\n毋知你是我 度過烏暗的明月\n\n幾段感情 坎坎坷坷\n早就貧惰求啥貨\n妳的出現 改變了一切\n我飄浪的孤單 變做有家\n哪知咱的緣分 會遐呢短\n\n上水的花 欲飛看心情沒解說\n我的寂寞 是乎你的情批\n朋友苦勸我清醒 妳的情攏是假\n毋知你是我 度過烏暗的明月\n\n上水的花 若是刺著心嘛會流血\n浪漫的愛 忽然間變風吹\n不管失眠幾落暝 我眼屎流外多\n猶原沒發覺 苦苦留戀是夯枷\n\n上水的花 欲飛看心情沒解說\n我的寂寞 是乎你的情批\n朋友罵我太狼狽 跟著妳玲瓏迺\n毋知你是我 度過烏暗的明月\n\n有毒的美麗 是會變卦的 情話\n')
        #停頓0.5秒
        await asyncio.sleep(0.5)
    
        

client.run('OTEwNTg4NTE0MDc1MjgzNDU2.YZVBow.P_Z95hNHS1viXu5RPrMa_txyatg') #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面