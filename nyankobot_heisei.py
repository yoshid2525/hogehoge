def heisei_command(command):
    heisei,year_str=command.split(' ')
    #文字列が数値に変換可能かを確認
    if year_str.isdigit():
        year=int(year_str)
        if year >= 1989:
            heisei_year=year-1988
            response='西暦{}年は、平成{}年です'.format(year,heisei_year)
        else:
            response='西暦{}年は、平成じゃないよー.format'(year)
    else:
        response="数値を指定してください"
    #except ValueError:
        #response='数値を入力してにゃー'
    return response 