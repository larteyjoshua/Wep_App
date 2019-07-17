from flask import Flask, render_template, request,redirect
 
items =[]
app = Flask(__name__)
 
@app.route('/foo/<name>')
def foo(name):
    return render_template('todolist.html', to=name,items=items)

    

@app.route('/add_todo')
def add_todo():
    item =request.args.get('item')
    items.append(item)
    return redirect("http://localhost:5000/foo/joshua", code=302)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')