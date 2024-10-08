from flask import Flask, render_template
from flask_login import (
    LoginManager, login_required, current_user, login_user, logout_user)


app = Flask(__name__)
login_manager = LoginManager(app)
login_manager.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
