print('nyankobotがレベルアップしてnyankobot2になったよ!')
nyankobot_2__dict={
    'こんにちは':'こんにちはだにゃー\(=^・A・^=)/',
    'ありがとう':'どういたしましてだにゃー(=^ω^=)',
    'さようなら':'ばいばいにゃー(=^・p・^=)/~~~',
}
while True:
    command = input('nyankobot2>')
    response=''
    for neko1 in nyankobot_2__dict:
        if neko1 in command:
            response=nyankobot_2__dict[neko1]
            break
        if not command:
            response=('ない言ってるかまだ分からないにゃー（=´・ω・｀=） もっと練習するにゃ！\(=^^=)!')
    print(response)
    if ('さようなら') in command:
        print('ばいばいにゃー(=^・p・^=)/~~~')
        break
'''
        elif neko1 in command:
            print('どういたしましてだにゃー(=^ω^=)')
        elif neko1 in command:
            print('ばいばいにゃー(=^・p・^=)/~~~')
            break
        else:
            print('ない言ってるかまだ分からないにゃー（=´・ω・｀=） もっと練習するにゃ！\(=^^=)!')
print('こんにちはだにゃー\(=^・A・^=)/')
'''