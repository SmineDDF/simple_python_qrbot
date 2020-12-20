def remove_command(message_text):
    return message_text.split(' ', 1)[1]

def get_message_text(message_text):
    return message_text.lstrip().rstrip()
    
