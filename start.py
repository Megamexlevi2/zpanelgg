from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/api/comando', methods=['POST'])
def execute():
    data = request.json
    command = data.get("comando")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout if result.stdout else result.stderr

if __name__ == "__main__":
    site_url = os.getenv("RENDER_EXTERNAL_URL", "http://localhost:8080")
    print(f"Server running at: {site_url}")
    app.run(host="0.0.0.0", port=8080)