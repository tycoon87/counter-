#from flask import Flask, render_template, request, redirect
#app = Flask(__name__)
#count = 0
#
#@app.route('/')
#def index():
#      session['count'] += 1
#    return render_template('index.html', count=session['count'])
#
#@app.route('/counter',methods=['POST'])
#def prossesing():
#    count += 1
#
#@app.route('/increment', methods=['POST'])
#def increment_by_two():
#    session['count'] += 1
#    return redirect('/') 
# 
#@app.route('/clear', methods=['POST'])
#def clear():
#    session['count'] = 0
#    return redirect('/')    
#    
#app.run(debug=True)

#***********************************************************

from flask import Flask, render_template, request, redirect
app = Flask(__name__)
app.secret_key = 'SuperHiddenSecretHushHush'
app.count = 0

@app.route('/')
def index():
    session['count'] += 1
    return render_template('index.html', count=session['count'])

@app.route('/increment', methods=['POST'])
def increment_by_two():
    session['count'] += 1
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)