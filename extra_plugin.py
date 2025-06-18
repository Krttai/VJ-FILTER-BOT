from pyrogram import Client, filters
from config import FILE_STORE_CHANNEL, DELETE_CHANNELS

# Save incoming media from private chats to the file store channel
@Client.on_message(filters.private & (filters.document | filters.video | filters.audio | filters.photo))
async def store_to_channel(client, message):
    try:
        sent = await message.copy(FILE_STORE_CHANNEL)
        await message.reply_text(f"✅ Saved to file store.\n\nID: `{sent.message_id}`")
    except Exception as e:
        await message.reply_text(f"❌ Store failed: `{e}`")

# Auto-delete media/messages from specified channels
@Client.on_message(filters.channel)
async def auto_delete_channel_files(client, message):
    try:
        if message.chat.id in DELETE_CHANNELS:
            await message.delete()
            print(f"🗑️ Deleted from {message.chat.id}")
    except Exception as e:
        print(f"❌ Delete error: {e}")
