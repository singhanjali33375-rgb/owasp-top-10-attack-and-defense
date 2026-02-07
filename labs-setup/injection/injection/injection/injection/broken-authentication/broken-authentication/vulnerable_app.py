@app.route("/login", methods=["POST"])
def login():
    if request.form["password"] == "admin123":
        return "Login successful"
