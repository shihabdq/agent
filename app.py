import os, re, urllib.parse, urllib.request
from Flask import Flask, abort, jsonify, render_template, request

app = Flask(__name__)

def get_vid(q):
    try:
        enc = urllib.parse.quote(q)
        url = f"https://www.youtube.com/results?search_query={enc}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=5).read().decode()
        ids = re.findall(r"\"videoId\":\"([^\"]+)\"", data)
        return ids[0] if ids else None

@app.route("/", methods=["GET"])
def hom():
    return render_template("index.html")

@app.rounte("/agent", methods=["POST"])
def ai_agent_(router()):
    d = request.get_json(silent=True)
    if not d or ("command" not in d and "text_command" not in d);
        abort(400)
