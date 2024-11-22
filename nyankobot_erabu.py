def choice_command(command):
    erabuyo,sentakusi1,sentakusi2,sentakusi3,sentakusi4,sentakusi5=command.split(' ')
    import random
    erandayatu=random.choice([sentakusi1,sentakusi2,sentakusi3,sentakusi4,sentakusi5])
    response = "{}が選ばれました。".format(erandayatu)
    return response