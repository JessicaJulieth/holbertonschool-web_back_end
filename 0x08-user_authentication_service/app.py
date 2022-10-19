#!/usr/bin/env python3
"""Basic Flask App,Register, etc
"""

from flask import Flask, jsonify, request, abort, make_response, redirect
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'])
def Bienvenue() -> str:
    """
    Return: JSON
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def register() -> str:
    """
    POST /users
    Return: JSON payload
    """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login() -> str:
    """
    POST /sessions
    LOGIN
    Return:
        JSON payload
    """
    email = request.form.get("email")
    password = request.form.get("password")
    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        respons = make_response({"email": email, "message": "logged in"})
        respons.set_cookie("session_id", value=s_id, domain="0.0.0.0",
                       secure=False)
        return respons
    else:
        abort(401)


@app.route("/sessions", methods=['DELETE'], strict_slashes=False)
def logout():
    """
    DELETE /sessions
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/")
    else:
        abort(403)


@app.route("/profile", methods=['GET'], strict_slashes=False)
def profile() -> str:
    """
    GET /profile
    """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route("/reset_password", methods=['POST'], strict_slashes=False)
def get_reset_password_token() -> str:
    """
    POST /reset_password
    Returns:
        JSON payload
    """
    try:
        email = request.form.get("email")
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": token}), 200
    except ValueError:
        abort(403)


@app.route("/reset_password", methods=['PUT'], strict_slashes=False)
def update_password() -> str:
    """
    PUT /reset_password
    Returns:
        JSON payload
    """
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_pass = request.form.get("new_pass")
    try:
        AUTH.update_password(reset_token, new_pass)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")