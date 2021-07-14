import sys 
import time
import telepot 
from telepot.loop import MessageLoop

### grupo  -1001458610971

def handle(msg):
    superuser = [1053185415,1087968824]
    admins=[1194527363,1316371868,1279446003,1352412689,875868982,757037814,1237760391,1100237818,936972448,993190617,1266038950,1553185954,776138009,1217426567,1192092937]
    #print(msg)
    msg_id = msg['message_id']
    from_chat = msg['from']['id']
    nombre = msg['from']['first_name']
    print(msg) 
    
    content_type,chat_type,chat_id = telepot.glance(msg)
    enlace = 'https://t.me/joinchat/GLX-v39tGgj8a4Wn'
    print(content_type,chat_type,chat_id)
    #print(msg)
    #print(from_chat)

    if from_chat in superuser:
        pass
    elif from_chat in admins:
        if content_type == 'photo' or content_type=='text':
            pass        
        else:            
            bot.deleteMessage((chat_id,msg_id))        
    else:            
        if content_type == 'photo':
            pass
        elif content_type =='text':
            if 'https://' in msg['text']:
                if 't.me' in msg['text'] or 'wa.' in msg['text'] or 'kwai.' in msg['text']:     
                    try:                                                    
                        bot.sendMessage(chat_id=superuser[0],text="Usuario: {}\nChat_id: {}\nMensaje: {}".format(nombre,from_chat,msg['text']))
                        bot.deleteMessage((chat_id,msg_id))
                    except e:
                        print(e)
                    finally:
                        pass
            else:
                try:           
                    bot.sendMessage(chat_id=superuser[0],text="Usuario: {}\nChat_id: {}\nMensaje: {}".format(nombre,from_chat,msg['text']))
                    bot.deleteMessage((chat_id,msg_id))
                except e:
                    print(e)
                finally:
                    pass
        else:
            try:
                bot.deleteMessage((chat_id,msg_id))
            except e:
                print(e)
            finally:
                pass
    

bot = telepot.Bot('1653442031:AAECGuxTzZXAlhjrK6U6c1C3PWHobKobDR8')
MessageLoop(bot,handle).run_as_thread()
print('Listening . . .')
while 1:
    time.sleep(10)



"""
{'message_id': 39,
 'date': 1615502309, 
 'chat': {'id': 1622438638, 'type': 'private', 'username': 'Hades1688', 'first_name': '.'},
 'text': 'Hola', 
 'entities': [], 
 'caption_entities': [], 
 'photo': [],
 'new_chat_members': [], 
 'new_chat_photo': [], 
 'delete_chat_photo': False, 
 'group_chat_created': False, 
 'supergroup_chat_created': False, 
 'channel_chat_created': False, 
 'from': {'id': 1622438638, 'first_name': '.', 'is_bot': False, 'username': 'Hades1688', 'language_code': 'es'}}
"""
