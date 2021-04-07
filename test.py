import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-1829797681845-1910880424580-nKuFbTsHvjGzp2THw4S1gu1Z"
 
post_message(myToken,"#bott","We can do anything")