import os
import discord
import asyncio
import random

# Bot-Token aus Render Environment Variable
TOKEN = os.getenv("DISCORD_TOKEN")

# ALLE Channel-IDs
CHANNEL_IDS = [
    1450051131811041280,
    1450076102188863640,
    1450076267918528553,
    1450076352316309534,
    1450076466103586888,
    1450076519874564096,
    1450076651777163355
]

intents = discord.Intents.default()
client = discord.Client(intents=intents)

MESSAGE = (
    "🚨 **NEUES VIP VIDEO** 🚨\n\n"
    "Es wurde **JETZT** gerade ein neues Video in der VIP Gruppe hochgeladen.\n"
    "Sichere dir jetzt deinen Zugang!"
)

async def send_periodic_message():
    await client.wait_until_ready()

    while not client.is_closed():
        for channel_id in CHANNEL_IDS:
            channel = client.get_channel(channel_id)

            if channel:
                try:
                    await channel.send(MESSAGE)
                except Exception as e:
                    print(f"❌ Fehler in Channel {channel_id}: {e}")
            else:
                print(f"❌ Channel nicht gefunden: {channel_id}")

        # 3–4 Minuten warten
        wait_time = random.randint(180, 240)
        await asyncio.sleep(wait_time)

@client.event
async def on_ready():
    print(f"✅ Bot ist online als {client.user}")
    asyncio.create_task(send_periodic_message())

client.run(TOKEN)
