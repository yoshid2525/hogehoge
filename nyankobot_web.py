from bottle import route, run, template, request
from datetime import datetime
from nyankobot_3_ import nyankobot_command
@route('/hello')
def hello():
    now=datetime.now()
    return template("nyankobot_template.html",input_text="",output_text="")

@route('/hello',method='POST')
def do_hello():
    input_text=request.forms.input_text
    output_text=nyankobot_command(input_text)
    return template('nyankobot_template.html',input_text=input_text,output_text=output_text)

    

run(host='localhost',port=8080,debug=True)