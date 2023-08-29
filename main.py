from flask import Flask,render_template,request,redirect
import pymysql

#create object of class
app=Flask('__name__')

'''
@app.route('/')
def index():
    return "Hello From Index"


@app.route('/contact')
def contact_function():
    return "Hello From Contacts"
'''
@app.route('/')
def index():
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todo")
        cu=db.cursor()
        q="select*from task"
        cu.execute(q)
        data=cu.fetchall()
        return render_template('dashboard.html',d=data)
    except Exception as e:
        return "error"+e
    
   

@app.route('/create')
def create():
    return render_template('form.html')
@app.route('/store',methods=['POST'])
def store():
    x=request.form['t']
    y=request.form['det']
    z=request.form['dt']

    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todo")
        cu=db.cursor()
        q="insert into task(title,detail,date) values('{}','{}','{}')".format(x,y,z)
        cu.execute(q)
        db.commit()
        #return "records inserted sucessfully"
        return redirect('/')
    except Exception as e:
        return "error"+e

#return x+"-"+y+"-"+z


@app.route('/delete/<rid>')
def delete(rid):
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todo")
        cu=db.cursor()
        q="delete from task where id='{}'".format(rid)
        cu.execute(q)
        db.commit()
        #return "records deleted sucessfully"
        return redirect('/')
    except Exception as e:
        return "error"+e
    #return "id to be deleted is"+rid


@app.route('/edit/<rid>')
def edit(rid):
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todo")
        cu=db.cursor()
        q="select * from task where id='{}'".format(rid)
        cu.execute(q)
        data=cu.fetchone()
        return render_template('edit_form.html',d=data)
        #return "records deleted sucessfully"
        return redirect('/')
    except Exception as e:
        return "error"+e


@app.route('/update/<rid>',methods=['POST'])
def update(rid):
     ut=request.form['t']
     udet=request.form['det']
     udt=request.form['dt']
     try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todo")
        cu=db.cursor()
        q="update task SET title='{}',detail='{}',date='{}' where id='{}'".format(ut,udet,udt,rid)
        cu.execute(q)
        db.commit()
       
        return redirect('/')
        #return "records deleted sucessfully"
     except Exception as e:
         return "error"+e
       
     #return ut
    
    
    
    
    
#To run server there is method named as run() inside Flask class

app.run(debug=True)
