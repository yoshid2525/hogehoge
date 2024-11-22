from nyankobot_heisei import heisei_command

from nyankobot_len import len_command

from eto_multiple_data import eto_command

from nyankobot_random import dice_command

from nyankobot_erabu import choice_command

from nyankobot_weather import weather_command

command_file=open('pybot.txt',encoding='utf-8')
raw_data=command_file.read()
command_file.close()
lines=raw_data.splitlines()
bot_dict={}
for a in lines:
    word_list=a.split(',')
    kye=word_list[0]
    response=word_list[1]
    bot_dict[kye]=response
def nyankobot_command(command):
    response=''
    for neko1 in bot_dict:
        if neko1 in command:
            response=bot_dict[neko1]
            break
    if '平成' in command:
        response=heisei_command(command)
    if '長さ' in command:
        response=len_command(command)
    if '干支' in command:
        response=eto_command(command)
    if 'サイコロ' in command:
        response=dice_command(command)
    if '選ぶ' in command:
        response=choice_command(command)   
    if '天気' in command:
        response=weather_command(command)
    if not command:
        response=('ない言ってるかまだ分からないにゃー（=´・ω・｀=） もっと練習するにゃ！\(=^^=)!')
    return response