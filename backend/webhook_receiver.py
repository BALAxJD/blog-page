from flask import Flask, request
import hmac
import hashlib
import subprocess
import os

app = Flask(__name__)

GITHUB_SECRET = "django-insecure-j=$cc66&=!)xkl!l)=w*2_xol**u9(%^0mmve((p_e7y(!0f5t"
REPO_PATH = "/home/jamesdon/blog-page/backend"

@app.route("/webhook", methods=["POST"])
def webhook():
    signature = request.headers.get("X-Hub-Signature")
    if not verify_signature(request.data, signature):
        return "Invalid signature", 403

    # Pull the latest changes
    subprocess.run(["git", "-C", REPO_PATH, "pull"])
    subprocess.run(["source", REPO_PATH + "/venv/bin/activate && pip install -r " + REPO_PATH + "/requirements.txt"], shell=True)
    subprocess.run(["touch", REPO_PATH + "/reload"])

    return "Success", 200

def verify_signature(payload, signature):
    computed_signature = "sha1=" + hmac.new(GITHUB_SECRET.encode(), payload, hashlib.sha1).hexdigest()
    return hmac.compare_digest(computed_signature, signature)

if __name__ == "__main__":
    app.run(port=5003)
