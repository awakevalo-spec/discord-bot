import discord
import asyncio
import random

# ==============================
# HIER DEIN BOT-TOKEN EINTRAGEN
# ==============================
TOKEN = "DEIN TOKEN HIER"

# Channel-ID, wo der Bot schreiben soll
CHANNEL_ID = 1450051131811041280

intents = discord.Intents.default()
client = discord.Client(intents=intents)

async def send_periodic_message():
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)

    while not client.is_closed():
        await channel.send(
            "🚨 **NEUES VIP VIDEO** 🚨\n\n"
            "Es wurde **JETZT** gerade ein neues Video in der VIP gruppe hochgeladen.\n"
            "Du bist noch nicht drinnen? 👉 "
            "https://discord.com/channels/1436987920178479157/1447976453500047472\n\n"
            
        )

        # 3–4 Minuten warten
        wait_time = random.randint(180, 240)
        await asyncio.sleep(wait_time)

@client.event
async def on_ready():
    print(f"✅ Bot ist online als {client.user}")
    asyncio.create_task(send_periodic_message())

client.run(TOKEN)
