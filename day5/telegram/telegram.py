import requests
from decouple import config 


# https://api.telegram.org/bot874191487:AAFSgw16GbNXHZu4u12Jr5RrnlUBhomSVbw/sendMessage?chat_id=856686046&text=%EC%99%9C%EC%9E%84%EB%A7%88

# https://api.telegram.org/bot874191487:AAFSgw16GbNXHZu4u12Jr5RrnlUBhomSVbw/getUpdates

#https://core.telegram.org/bots/api#authorizing-your-bot
# getMe
# getUpdates
# sendMessage with parameter 

def sendMessage(message) : 
    baseurl = "https://api.telegram.org"
    
    token = config("TELEGRAM_TOKEN")
    
    method = "getUpdates"
    updateurl = f"{baseurl}/bot{token}/{method}"
    res = requests.get(updateurl).json()
    chat_id = res.get('result')[0].get('message').get('from').get('id')
    
    method = "sendMessage"
    #messageurl = baseurl + token + method + f"?chat_id={chat_id}&text={message}"
    messageurl = f"{baseurl}/bot{token}/{method}?chat_id={chat_id}&text={message}"
    messageres = requests.get(messageurl).text

