def choice_command(command):
    sentakusi=command.split(' ')
    sentakusi[1:]
    import random
    erandayatu=random.choice(sentakusi)
    response = "{}が選ばれました。".format(erandayatu)
    return response