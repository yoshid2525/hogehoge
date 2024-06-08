from datetime import date,datetime

today=date.today()
#print(today)
#print(type(today))
now=datetime.now()
#print("年:{}.".format(now.year))
#print("月:{}.".format(now.month))
#print("日:{}.".format(now.day))
#print("時:{}.".format(now.hour))
#print("分:{}.".format(now.minute))
#print("秒:{}.".format(now.second))
#print("マイクロ秒:{}.".format(now.microsecond))

def today_command(commamd):
    print("今日は{}日だにゃー.".format(now.day))

def now_command(commamd):
    print("今は{}時だにゃー.".format(now.hour))

def weekday_command(command):#commandで受け取った日にちを曜日に変換
    try:
        ata=command.split()
        year=int(data[1])
        month=int(data[2])
        day=int(data[3])
        one_day=(year,month,day)

        week_name={
            0:"月曜日",
            1:"火曜日",
            2:"水曜日",
            3:"木曜日",
            4:"金曜日",
            5:"土曜日",
            6:"日曜日",
        }
        weekday=week_name[one_day.weekday()]
            
        response='{}は{}曜日だにゃー'.format(one_day,weekday)
    except IndexError:
        response='３つの値(年月日)をしてにゃー'
        
    except ValueError:
        response="正しい日付を指定してにゃー"

    
        return response