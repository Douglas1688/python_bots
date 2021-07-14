import telebot

bot = telebot.TeleBot("1653442031:AAECGuxTzZXAlhjrK6U6c1C3PWHobKobDR8")

# handle commands, /start
@bot.message_handler(commands=['start'])
def handle_command(message):
    bot.reply_to(message, "Hello, welcome to Telegram Bot!")
    
# handle all messages, echo response back to users
@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    """if message.content_type == 'text':
        print('Esto es texto')
    elif message.content_type =='photo':
        print('Esto es foto')"""
    print(message)

	#bot.reply_to(message,message.id)
    
@bot.message_handler(content_types=["new_chat_members"])
def foo(message):
    bot.reply_to(message, "welcome")
@bot.message_handler(content_types=["left_chat_members"])
def fo(message):
    bot.reply_to(message, "Bye")


bot.polling()


"""
{'content_type': 'text',
 'id': 147,
 'message_id': 147,
 'from_user': {'id': 1622438638, 'is_bot': False, 'first_name': '.', 'username': 'Hades1688', 'last_name': None, 'language_code': 'es', 'can_join_groups': None, 'can_read_all_group_messages': None, 'supports_inline_queries': None}, 
 'date': 1615515997, 
 'chat': {'id': 1622438638, 'type': 'private', 'title': None, 'username': 'Hades1688', 'first_name': '.', 'last_name': None, 'photo': None, 'bio': None, 'description': None, 'invite_link': None, 'pinned_message': None, 'permissions': None, 'slow_mode_delay': None, 'sticker_set_name': None, 'can_set_sticker_set': None, 'linked_chat_id': None, 'location': None}, 
 'forward_from': None, 
 'forward_from_chat': None, 
 'forward_from_message_id': None, 
 'forward_signature': None, 
 'forward_sender_name': None, 
 'forward_date': None, 
 'reply_to_message': None, 
 'edit_date': None, 
 'media_group_id': None, 
 'author_signature': None, 
 'text': 'Hola', 
 'entities': None, 
 'caption_entities': None, 
 'audio': None, 
 'document': None, 
 'photo': None, 
 'sticker': None, 
 'video': None, 
 'video_note': None, 
 'voice': None, 
 'caption': None, 
 'contact': None, 
 'location': None, 
 'venue': None, 
 'animation': None, 
 'dice': None, 
 'new_chat_member': None, 
 'new_chat_members': None, 
 'left_chat_member': None, 
 'new_chat_title': None, 
 'new_chat_photo': None, 
 'delete_chat_photo': None, 
 'group_chat_created': None, 
 'supergroup_chat_created': None, 
 'channel_chat_created': None, 
 'migrate_to_chat_id': None, 
 'migrate_from_chat_id': None, 
 'pinned_message': None, 
 'invoice': None, 
 'successful_payment': None, 
 'connected_website': None, 
 'reply_markup': None, 
 'json': {'message_id': 147, 'from': {'id': 1622438638, 'is_bot': False, 'first_name': '.', 'username': 'Hades1688', 'language_code': 'es'}, 'chat': {'id': 1622438638, 'first_name': '.', 'username': 'Hades1688', 'type': 'private'}, 'date': 1615515997, 'text': 'Hola'}}




{'content_type': 'text', 'id': 148, 'message_id': 148, 'from_user': {'id': 1053185415, 'is_bot': False, 'first_name': 'Ing. Douglas', 'username': 'douglas1688', 'last_name': 'Vásquez', 'language_code': 'es', 'can_join_groups': None, 'can_read_all_group_messages': None, 'supports_inline_queries': None}, 'date': 1615516005, 'chat': {'id': 1053185415, 'type': 'private', 'title': None, 'username': 'douglas1688', 'first_name': 'Ing. Douglas', 'last_name': 'Vásquez', 'photo': None, 'bio': None, 'description': None, 'invite_link': None, 'pinned_message': None, 'permissions': None, 'slow_mode_delay': None, 'sticker_set_name': None, 'can_set_sticker_set': None, 'linked_chat_id': None, 'location': None}, 'forward_from': None, 'forward_from_chat': None, 'forward_from_message_id': None, 'forward_signature': None, 'forward_sender_name': None, 'forward_date': None, 'reply_to_message': None, 'edit_date': None, 'media_group_id': None, 'author_signature': None, 'text': 'Hola', 'entities': None, 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'animation': None, 'dice': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'reply_markup': None, 'json': {'message_id': 148, 'from': {'id': 1053185415, 'is_bot': False, 'first_name': 'Ing. Douglas', 'last_name': 'Vásquez', 'username': 'douglas1688', 'language_code': 'es'}, 'chat': {'id': 1053185415, 'first_name': 'Ing. Douglas', 'last_name': 'Vásquez', 'username': 'douglas1688', 'type': 'private'}, 'date': 1615516005, 'text': 'Hola'}}
"""