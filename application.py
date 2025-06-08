from flask import Flask,request,url_for,render_template, redirect


application = Flask(__name__)
app = application

#items that already exist in the todo list
tasks = [
    {'id':1,'name':"activity 1",'description':"talk shit to deadpool"},
    {'id':2,'name':'activity 2','description':"take a shit"},
    {'id':3,'name':'activity 3','description':'move a rock'}


]


@app.route('/')
def home():
    return render_template("home.html",tasks = tasks)

@app.route('/update/<int:task_id>',methods = ['GET','POST'])
def update(task_id):
    global tasks

    if request.method =='POST':
        #we gotta delete that task and then add this new updated one.
        tasks = [task for task in tasks if task["id"]!= task_id]

        updated_task = {'id':task_id,'name':request.form['name'],'description':request.form['description']}

        tasks.append(updated_task)
        tasks.sort(key=lambda x: x['id'])

        return redirect(url_for('home'))

    
    #this part gets executed normally if it's not a put request.
    task = next((task for task in tasks if task['id']==task_id),None)
    if not task:
        return "Task not found",404
    return render_template('update.html',task=task)

@app.route('/add',methods = ['GET','POST'])
def add():


    if request.method == 'POST':

        name = request.form["name"]
        description = request.form["description"]

        task_id = tasks[-1]['id']+1

        tasks.append({'id':task_id,'name':name,'description':description})

        return redirect(url_for('home'))

        

    return render_template('add.html')
    

@app.route('/delete/<int:task_id>',methods = ['GET','POST'])
def delete(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"]!= task_id]

    #return f"Task with id {task_id} is deleted"
    return redirect(url_for('home'))




if  __name__=='__main__':
    app.run(host="0.0.0.0")