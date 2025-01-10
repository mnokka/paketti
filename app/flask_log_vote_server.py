from flask import Flask, request, jsonify, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "test_secret_key" 

# Two candidates to vote
votes = {"Candidate 1": 0, "Candidate 2": 0}
USER_CREDENTIALS = {"username": "testuser", "password": "password"}

# Health endpoint
@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

# Login endpoint
@app.route("/login", methods=["POST"])
def login():
    data = request.form
    username = data.get("username")
    password = data.get("password")
    if username == USER_CREDENTIALS["username"] and password == USER_CREDENTIALS["password"]:
        session["logged_in"] = True
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

# Vote endpoint
@app.route("/vote", methods=["POST"])
def vote():
    if not session.get("logged_in"):
        return jsonify({"message": "Unauthorized"}), 401

    candidate = request.form.get("candidate")
    if candidate in votes:
        votes[candidate] += 1
        return jsonify({"message": "Vote counted", "votes": votes}), 200
    return jsonify({"message": "Invalid candidate"}), 400

# Results endpoint
@app.route("/results")
def results():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    return jsonify(votes)

# Logout endpoint
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)