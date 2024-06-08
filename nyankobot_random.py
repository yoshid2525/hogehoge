def dice_command(command):
    import random
    saikoronokazu=random.randrange(1,7)
    response = "サイコロで-{}-が出たよ!!。".format(saikoronokazu)
    return response