from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram import ChatAction

# Replace 'TOKEN' with your actual bot token
TOKEN = '6497404744:AAE9vw1gG1nXczJPFYKCBa_VaQAh-R2LfyU'

ENTER_GROUP_ID = 0

def start(update, context):
    update.message.reply_text("Please enter the group ID to get the member count and usernames.")
    return ENTER_GROUP_ID

def get_members(update, context):
    group_id = update.message.text
    
    # Send typing action while fetching members
    update.message.chat.send_action(ChatAction.TYPING)
    
    try:
        # Get the list of members in the group
        members = context.bot.get_chat_members(group_id)
        member_usernames = [member.user.username for member in members if member.user.username is not None]
        member_count = len(member_usernames)
        usernames_text = "\n".join(member_usernames)
        reply_text = f"The group {group_id} has {member_count} members:\n\n{usernames_text}"
        update.message.reply_text(reply_text)
    except Exception as e:
        update.message.reply_text("Error fetching members. Please check the group ID and try again.")

    return ConversationHandler.END

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('getmembers', start)],
        states={
            ENTER_GROUP_ID: [MessageHandler(Filters.text & ~Filters.command, get_members)]
        },
        fallbacks=[]
    )

    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
