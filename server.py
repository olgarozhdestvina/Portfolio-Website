from flask import Flask, session, flash, redirect, request, render_template, url_for
from werkzeug.exceptions import BadRequest, NotFound, MethodNotAllowed, InternalServerError
import os
from datetime import timedelta
import csv

app = Flask(__name__, template_folder=os.getcwd(), static_folder='assets')

# Secret key to login.
app.secret_key = 'someKey'

# Store session.
app.permanent_session_lifetime = timedelta(minutes=30)
# session.permanent = True <--- only for active http


@app.route('/')
def index():
    return render_template('index.html')


def write_to_file(data):
    with open('database.csv', 'a') as database:
        name = data['name']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', lineterminator='\n', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])
        return name


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        # set session
        session.permanenet = True
        data = request.form.to_dict()
        name = write_to_file(data)
        error = None
        if error is None:
            flash(f'Thank you, {name}! I will get in touch with you shortly.', 'success')
            return redirect(url_for('index'))
        else:
            flash(error, 'Something went wrong. Please try again!')
            


# Error handlers.
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return 'Bad request!', 400


@app.errorhandler(NotFound)
def handle_bad_request1(e):
    return 'Page is not found!', 404


@app.errorhandler(MethodNotAllowed)
def handle_bad_request2(e):
    return 'Method is not allowed!', 405


@app.errorhandler(InternalServerError)
def handle_bad_request3(e):
    return 'Internal server error!', 500

if __name__ == '__main__':
    app.run(debug=True)