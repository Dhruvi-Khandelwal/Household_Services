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

@app.route('/user/service_prof_signup', methods=['GET'])
def service_prof_signup():
    return render_template('user/service_prof_signup.html')

@app.route('/user/professional_dashboard', methods=['GET'])
def professional_dashboard():
    return render_template('user/professional_dashboard.html')

@app.route('/user/professional_search', methods=['GET'])
def professional_search():
    return render_template('user/professional_search.html')

@app.route('/user/professional_summary', methods=['GET'])
def professional_summary():
    return render_template('user/professional_summary.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=7000) 




