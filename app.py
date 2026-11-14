from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home")

@app.route("/product")
def product():
    return render_template("product.html", title="Product")

@app.route("/cart")
def cart():
    return render_template("cart.html", title="Cart")

@app.route("/register")
def register():
    return render_template("register.html", title="Register")

@app.route("/login")
def login():
    return render_template("login.html", title="Login")

@app.route("/account")
def account():
    return render_template("account.html", title="Account")

@app.route("/logout")
def logout():
    return render_template("home.html")

@app.route("/reset")
def reset():
    return render_template("reset.html", title="Reset")

if __name__ == "__main__":
    app.run(debug=True)