import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "7902240685:AAHnLDSB1OdPPnUNhKR59ze9MzbalSVj84s")

API_ID = int(os.environ.get("API_ID", "28243586"))

API_HASH = os.environ.get("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")

STRING = os.environ.get("STRING", "AQGu9oIAU4Py7M1EH6w6f-Y8XezEeKPJq_8n02mAfY8A4uL3EBBMi6rWnIUbQqsddbpjkBpu7D28-TowTMAURn_NCR3K2RmrewP0deOQzsco_p7QLK_29tJ3ldnm4OdDsM4uSBe2kXwBnFP8FracySiyMH7xmPk3rzjm4cQU8ujvI6GDnafcdp_u_9BT0RB43AsCjQ8qOzAh7G55Slq5B_jesN0ailJBu_MV1J5o9QpPqkrLlEZQwlY4gRYqfDAQ8c4kiFcUgoU6A0m1v367Bq6fOtuJRjam-TerayDKgcPs3rTG2VJindCW_8BuKz25A3qHuSpzLFyoNVn6H2MeKNv-nahsigAAAAFZFXRRAA")



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
