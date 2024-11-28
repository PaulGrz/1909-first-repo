from telethon import TelegramClient, events

# Replace with your own values
api_id = '23083054'
api_hash = '2c743dac928e2b74c8af45938cdb0c3c'
phone_number = '+972544437401'

# Create the Telethon client
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.ChatAction)
async def new_member_handler(event):
    # Check if the event involves a new user joining
    if event.user_joined or event.user_added:
        for user in event.users:
            try:
                # Send a private message to the new user
                await client.send_message(
                    user.id,
                    "היי , אני ראיתי שיש לך נינטנדו סוויץ ,\nאני מציע פריצה גם לאולד גם לV2 שמאפשרת להוריד את כל המשחקים !\nהאם זה יכול לעניין אותך ? 😎\n\nשאלות ותשובות בקבוצה:\nhttps://t.me/NintendoChipMod"
                )
                print(f"Message sent to {user.first_name} ({user.id})")
            except Exception as e:
                print(f"Could not message {user.first_name}: {e}")

# Start the client
async def main():
    await client.start(phone=phone_number)
    print("Client is running...")
    await client.run_until_disconnected()

client.loop.run_until_complete(main())