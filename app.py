from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/user/login', methods=['GET'])
def user_login():
    return render_template('user/login.html')

@app.route('/professional/login', methods=['GET'])
def service_professional_login():
    return render_template('user/login.html')

@app.route('/admin/login', methods=['GET'])
def admin_login():
    return render_template('user/login.html')

@app.route('/user/register', methods=['GET'])
def user_register():
    return render_template('user/register.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=7000) 




