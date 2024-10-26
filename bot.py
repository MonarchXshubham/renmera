import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "7902240685:AAHnLDSB1OdPPnUNhKR59ze9MzbalSVj84s")

API_ID = int(os.environ.get("API_ID", "28243586"))

API_HASH = os.environ.get("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")

STRING = os.environ.get("STRING", "BQGu9oIAs57G1lpOnIeg2TXfG4cvZAV0LQCQ9Y-lUpaKL_WXQ4ii93_V0HnAEoIYzBwjOL7195DJ12oTZvcDW-ckg0at565C3Pv4UwEKGT_O9RtPHEOjozGBTs4QwE-xQ2QVqvIXXDTRrwCdRKmRxldqMPGNP9K4WVsAE7PWyV1IaJz41r2hxFDjIs9bslEtaXdAdU4KFabLR8MoVjVFuJpQ4MNqbDU_4zBaCfA8MAS-r3MlU2Cd8-4iX0GH6OpLqiJDNNo1n9b_YWuXdvBvYbdZNfZWxGRGBBZJpyOTjT6ojn20Lr-PedKkliUuSwA_MtWrF9j_cImREjL2LvZHLQQ584My9wAAAAHVLmyUAA")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
