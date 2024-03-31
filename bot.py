from telegram.ext import Updater, CommandHandler
import random

# Replace 'TOKEN' with your actual bot token
TOKEN = '6497404744:AAE9vw1gG1nXczJPFYKCBa_VaQAh-R2LfyU'

def ban_all(update, context):
    # Check if the command is being used in a group
    if update.message.chat.type != 'supergroup':
        update.message.reply_text("This command can only be used in a group.")
        return
    
    # Get the list of members in the group
    members = update.message.chat.get_members_count()
    
    # Get the list of user names to ban (assuming they are mentioned after /banall)
    user_names = context.args
    
    # Shuffle the list of user names to randomize the ban
    random.shuffle(user_names)
    
    # Ban each user
    for user_name in user_names:
        context.bot.kick_chat_member(update.message.chat_id, user_name)
    
    update.message.reply_text("All mentioned users have been banned.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("banall", ban_all))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
