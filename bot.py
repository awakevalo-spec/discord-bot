import os
import discord
import asyncio
import random

# Token kommt aus Render Environment Variable
TOKEN = os.getenv("DISCORD_TOKEN")

# ✅ ALLE Channel-IDs HIER EINTRAGEN
CHANNEL_IDS = [
    1450051131811041280,
    1450076102188863640,
    1450076267918528553,
    1450076352316309534,
    1450076466103586888,
    1450076519874564096,
    1450076651777163355,
    1451881109104365599,
    1452290446549057617,
    1453526923195056222  # <-- NEU HINZUGEFÜGT
]


intents = discord.Intents.default()
client = discord.Client(intents=intents)

MESSAGE = (
    "🚨 **NEUES VIP VIDEO** 🚨\n\n"
    "Es wurde **JETZT** gerade ein neues Video in der VIP Gruppe hochgeladen.\n"
    "Sichere dir jetzt deinen Zugang!"
)

async def send_periodic_messages():
    await client.wait_until_ready()

    channels = []
    for cid in CHANNEL_IDS:
        channel = client.get_channel(cid)
        if channel:
            channels.append(channel)
        else:
            print(f"❌ Channel nicht gefunden: {cid}")

    if not channels:
        print("❌ KEINE Channels gefunden – prüfe IDs & Bot-Rechte")
        return

    print(f"✅ {len(channels)} Channels aktiv")

    while not client.is_closed():
        for channel in channels:
            try:
                await channel.send(MESSAGE)
                print(f"📨 Nachricht gesendet in #{channel.id}")
            except Exception as e:
                print(f"❌ Fehler in {channel.id}: {e}")

        # ⏱️ 3–4 Minuten warten
        wait_time = random.randint(180, 240)
        await asyncio.sleep(wait_time)

@client.event
async def on_ready():
    print(f"✅ Bot ist online als {client.user}")
    client.loop.create_task(send_periodic_messages())

client.run(TOKEN)




