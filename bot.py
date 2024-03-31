from telegram.ext import Updater, CommandHandler
from telegram import ChatAction

# Replace 'TOKEN' with your actual bot token
TOKEN = '6497404744:AAE9vw1gG1nXczJPFYKCBa_VaQAh-R2LfyU'

def get_members(update, context):
    # Check if the command has the group ID
    if len(context.args) != 1:
        update.message.reply_text("Please provide the group ID.")
        return
    
    group_id = context.args[0]
    
    # Send typing action while fetching members
    update.message.chat.send_action(ChatAction.TYPING)
    
    try:
        # Get the list of members in the group
        members = context.bot.get_chat_members_count(group_id)
        update.message.reply_text(f"The group {group_id} has {members} members.")
    except Exception as e:
        update.message.reply_text("Error fetching members. Please check the group ID and try again.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("getmembers", get_members))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
