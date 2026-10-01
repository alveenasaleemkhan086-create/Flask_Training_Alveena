from flask import Flask,render_template,request,redirect,url_for


app=Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello, I am Alveena Khan</h1>"

@app.route('/welcome')
def welcome():
    return "<h1>Welcome to Flask Training class.</h1>"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/success/<int:a>')
def success(a):
    return "The Person is Pass and the Score is:"+str(a)

@app.route('/fail/<int:b>')
def fail(a):
    return "The Person is Fail and the Score is:"+str(a)

@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        english=float(request.form['english'])
        average=(maths+science+english)/3
        result=""
        if average>=80:
            result="success"
        else:
            result="fail"
        return redirect(url_for(result,a=average))


if __name__=='__main__':
    app.run(debug=True)