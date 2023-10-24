from  flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# from app import db


app = Flask(__name__)

# db config for postgresql
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Pasuwok@123@localhost/flask_intro'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# app.app_context()
# with app.app_context():
#     # Now you can perform operations that require the application context
#     db.create_all()  # Example operation

class Todo(db.Model):
 #   __tablename__='to_do'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id
    
    # def __init__(self,id,content,date_created):
    #     self.id = id
    #     self.content = content
    #     self.date_created = date_created

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # return 'hello world'
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        # # using postgresql
        # task_content = request.form['content']
        # new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task!'

    else:
        # taks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)