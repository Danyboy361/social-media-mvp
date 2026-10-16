import os
import sqlite3
from datetime import datetime, timezone
from functools import wraps
from flask import Flask, g, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

APP_SECRET = os.environ.get("APP_SECRET_KEY", "local-development-key-change-me")
DATABASE = os.environ.get("DATABASE_PATH", "/data/social.db")

app = Flask(__name__)
app.config.update(SECRET_KEY=APP_SECRET, SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE="Lax")

def connect_db():
    db_dir = os.path.dirname(DATABASE)
    if db_dir:
        os.makedirs(db_dir, exist_ok=True)
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    with connect_db() as db:
        db.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE COLLATE NOCASE,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            content TEXT NOT NULL CHECK(length(content) BETWEEN 1 AND 280),
            created_at TEXT NOT NULL
        );
        CREATE INDEX IF NOT EXISTS idx_posts_created_at ON posts(created_at DESC, id DESC);
        """)

@app.before_request
def ensure_db():
    if not getattr(g, "_db_checked", False):
        init_db()
        g._db_checked = True

def current_user():
    user_id = session.get("user_id")
    if not user_id:
        return None
    with connect_db() as db:
        return db.execute("SELECT id, username FROM users WHERE id = ?", (user_id,)).fetchone()

def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not current_user():
            flash("Please sign in to continue.", "error")
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return wrapped

@app.get("/")
def index():
    user = current_user()
    with connect_db() as db:
        posts = db.execute("""
            SELECT posts.id, posts.content, posts.created_at, users.username
            FROM posts JOIN users ON users.id = posts.user_id
            ORDER BY posts.created_at DESC, posts.id DESC
            LIMIT 100
        """).fetchall()
    return render_template("index.html", user=user, posts=posts)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        if not (3 <= len(username) <= 30) or not username.replace("_", "").isalnum():
            flash("Username must be 3–30 characters and contain only letters, numbers, or underscores.", "error")
            return render_template("register.html")
        if len(password) < 8:
            flash("Password must be at least 8 characters.", "error")
            return render_template("register.html")
        try:
            with connect_db() as db:
                db.execute("INSERT INTO users(username, password_hash, created_at) VALUES (?, ?, ?)",
                           (username, generate_password_hash(password), datetime.now(timezone.utc).isoformat()))
        except sqlite3.IntegrityError:
            flash("That username is already taken.", "error")
            return render_template("register.html")
        flash("Account created. Please sign in.", "success")
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        with connect_db() as db:
            user = db.execute("SELECT id, username, password_hash FROM users WHERE username = ? COLLATE NOCASE",
                              (username,)).fetchone()
        if not user or not check_password_hash(user["password_hash"], password):
            flash("Invalid username or password.", "error")
            return render_template("login.html")
        session.clear()
        session["user_id"] = user["id"]
        flash("You are signed in.", "success")
        return redirect(url_for("index"))
    return render_template("login.html")

@app.post("/logout")
@login_required
def logout():
    session.clear()
    flash("You have signed out.", "success")
    return redirect(url_for("index"))

@app.post("/posts")
@login_required
def create_post():
    content = request.form.get("content", "").strip()
    if not content or len(content) > 280:
        flash("Posts must contain 1–280 characters.", "error")
        return redirect(url_for("index"))
    user = current_user()
    with connect_db() as db:
        db.execute("INSERT INTO posts(user_id, content, created_at) VALUES (?, ?, ?)",
                   (user["id"], content, datetime.now(timezone.utc).isoformat()))
    flash("Post published.", "success")
    return redirect(url_for("index"))

@app.get("/health")
def health():
    try:
        with connect_db() as db:
            db.execute("SELECT 1")
        return {"status": "ok"}, 200
    except sqlite3.Error:
        return {"status": "error"}, 503

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
