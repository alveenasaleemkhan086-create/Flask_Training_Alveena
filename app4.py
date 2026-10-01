from flask import Flask, redirect, url_for, render_template, request, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "library123"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/LibraryManagement'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print("Alveena")
db = SQLAlchemy(app)

class User(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Book(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.String(30), nullable=False)
    book_name = db.Column(db.String(100), nullable=False)
    book_number = db.Column(db.String(30), nullable=False)
    student_name = db.Column(db.String(80), nullable=False)
    issue_date = db.Column(db.String(20), nullable=False)
    due_date = db.Column(db.String(20), nullable=False)

with app.app_context(): db.create_all()

@app.route('/')
def home(): return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name, username, password = request.form['name'], request.form['username'], request.form['password']
        if User.query.filter_by(username=username).first():
            return render_template('signup.html', message='Username already exists')
        db.session.add(User(name=name, username=username, password=password))
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username, password = request.form['username'], request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['username'], session['name'] = user.username, user.name
            return redirect(url_for('dashboard'))
        return render_template('login.html', message='Invalid username or password')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session: return redirect(url_for('login'))
    return render_template('dashboard.html', name=session.get('name'))

@app.route('/issue-book', methods=['GET', 'POST'])
def issue_book():
    if 'username' not in session: return redirect(url_for('login'))
    if request.method == 'POST':
        book_id = request.form['book_id']
        book_name = request.form['book_name']
        book_number = request.form['book_number']
        student_name = request.form['student_name']
        issue_date = request.form['issue_date']
        due_date = request.form['due_date']
        new_book = Book(book_id=book_id, book_name=book_name, book_number=book_number,
                        student_name=student_name, issue_date=issue_date, due_date=due_date)
        db.session.add(new_book)
        db.session.commit()
        session['book_id'], session['book_name'] = book_id, book_name
        session['student_name'], session['issue_date'] = student_name, issue_date
        session['due_date'] = due_date
        return redirect(url_for('success'))
    return render_template('issue_book.html')

@app.route('/view-books')
def view_books():
    if 'username' not in session: return redirect(url_for('login'))
    books = Book.query.all()
    return render_template('view_books.html', books=books)

@app.route('/success')
def success():
    if 'username' not in session: return redirect(url_for('login'))
    return render_template('success.html', book_name=session.get('book_name'),
                           student_name=session.get('student_name'),
                           issue_date=session.get('issue_date'),
                           due_date=session.get('due_date'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__': app.run(debug=True)