def len_command(command):
    cmd,text=command.split(' ')
    lengeth=len(text)
    response = "文字列ノ長サハ{}文字デス。".format(lengeth)
    return response