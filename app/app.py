from flask import Flask, request, jsonify
import os, psycopg2

DB_HOST = os.environ.get("DATABASE_HOST","haproxy")
DB_PORT = int(os.environ.get("DATABASE_PORT",5432))
DB_USER = os.environ.get("DATABASE_USER","appuser")
DB_PASS = os.environ.get("DATABASE_PASSWORD","apppass")
DB_NAME = os.environ.get("DATABASE_NAME","labdb")

def get_conn():
    return psycopg2.connect(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASS, dbname=DB_NAME, connect_timeout=5)

app = Flask(__name__)

@app.route("/")
def index():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT count(*) FROM app.messages;")
        cnt = cur.fetchone()[0]
        cur.close()
        conn.close()
        return jsonify({"status":"ok","messages":cnt})
    except Exception as e:
        return jsonify({"status":"error","error":str(e)})

@app.route("/messages", methods=["POST"])
def add_message():
    data = request.json or {}
    text = data.get("text","hello")
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("INSERT INTO app.messages (text) VALUES (%s);", (text,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"status":"ok"})
    except Exception as e:
        return jsonify({"status":"error","error":str(e)})

@app.route("/messages", methods=["GET"])
def list_messages():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT id, text, created_at FROM app.messages ORDER BY id DESC LIMIT 10;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify([{"id":r[0],"text":r[1],"created_at":r[2].isoformat()} for r in rows])
    except Exception as e:
        return jsonify({"status":"error","error":str(e)})
