def eto_command(command):
    etodesu,year=command.split(' ')
    year=int(year)
    number_of_eto=(year-4)%12
    eto_tuple =(
                "ネズミ",
                "ウシ",
                "トラ",
                "ウサギ",
                "タツ",
                "ヘビ",
                "ウマ",
                "ヒツジ",
                "サル",
                "トリ",
                "イヌ",
                "イノシシ",
                )
    eto_name = eto_tuple[number_of_eto]
    response = "あなたの干支は{}です".format(eto_name)
    return response