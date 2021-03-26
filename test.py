from slacker import Slacker

slack = Slacker('xoxb-1829797681845-1907933122324-wZHxIIeCCHf3iTyOJ0wMGZMP')

# Send a message to #general channel
slack.chat.post_message('#bott', 'Hello fellow slackers!')