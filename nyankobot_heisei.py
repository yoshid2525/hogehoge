def heisei_command(command):
    heisei,year_str=command.split(' ')
    year=int(year_str)
    if year >= 1989:
        heisei_year=year-1988
        response='西暦{}年は、平成{}年です'.format(year,heisei_year)
    else:
        response='西暦{}年は、平成じゃないよー.format'(year)
    return response