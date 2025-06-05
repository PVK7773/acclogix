from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    email = request.form.get('email')
    password = request.form.get('password')
    # Simple static login check for demo purposes
    if email == "prakash@acclogix.com" and password == "welcome123":
        return render_template('dashboard.html', name="Prakash V")
    else:
        return redirect(url_for('login'))

@app.route('/documents/<filename>')
def download_file(filename):
    return send_from_directory('static/documents', filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
