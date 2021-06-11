# api/views.py

from flask import request,send_file,Response,make_response,render_template
from api import app
from api import question

@app.route('/download')
def show_entries():
    user_name = request.args.get('account','')
    num = request.args.get('num','')

    user_information = question.get(user_name,num)

    downloadFileName = user_name +'_'+ num +'.json'

    response = make_response()
    response.data = open(downloadFileName,'rb').read()
    response.headers['Content-Type'] = 'application/octet-stream'
    response.headers['Content-Disposition'] = 'attachment; filename='+ downloadFileName
    return response

@app.route('/')
def root():
    return render_template('download/index.html',title='sitsumonbako_jsondownload')
