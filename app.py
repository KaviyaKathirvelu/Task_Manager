from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    due_date = db.Column(db.String(50), nullable=True)
    priority = db.Column(db.String(20), nullable=True)
    completed = db.Column(db.Boolean, default=False)  # Added completed field

# Initialize the database
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_task():
    data = request.json

    # Validation
    if not data or 'task_name' not in data:
        return jsonify({"error": "Missing required field: task_name"}), 400
    
    task = Task(
        name=data['task_name'],
        due_date=data.get('due_date'),
        priority=data.get('priority', "Medium")
    )
    
    db.session.add(task)
    db.session.commit()

    return jsonify({"message": f"Task '{task.name}' added successfully!"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    query = request.args.get('query', '').lower()

     # If a search query is provided, filter the tasks
    if query:
        tasks = Task.query.filter(Task.name.ilike(f'%{query}%')).paginate(page=page, per_page=per_page)
    else:
        tasks = Task.query.paginate(page=page, per_page=per_page)
    task_list = [{"id": task.id, "name": task.name, "due_date": task.due_date, "priority": task.priority, "completed": task.completed} for task in tasks.items]
   
    return jsonify(task_list)

@app.route('/update/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    data = request.json
    task.name = data.get('task_name', task.name)
    task.due_date = data.get('due_date', task.due_date)
    task.priority = data.get('priority', task.priority)
    
    db.session.commit()
    return jsonify({"message": f"Task '{task.name}' updated successfully!"})

@app.route('/delete/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": f"Task '{task.name}' deleted successfully!"})

@app.route('/search', methods=['GET'])
def search_tasks():
    query = request.args.get('query', '').lower()
    tasks = Task.query.filter(Task.name.ilike(f'%{query}%')).all()
    task_list = [{"id": task.id, "name": task.name, "due_date": task.due_date, "priority": task.priority, "completed": task.completed} for task in tasks]
    return jsonify(task_list)

@app.route('/complete/<int:task_id>', methods=['PATCH'])
def complete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    task.completed = not task.completed
    db.session.commit()
    return jsonify({"message": f"Task '{task.name}' marked as {'completed' if task.completed else 'not completed'}!"})

@app.route('/export', methods=['GET'])
def export_tasks():
    tasks = Task.query.all()
    task_list = [{"id": task.id, "name": task.name, "due_date": task.due_date, "priority": task.priority, "completed": task.completed} for task in tasks]
    return jsonify(task_list)

if __name__ == '__main__':
    app.run(debug=True)