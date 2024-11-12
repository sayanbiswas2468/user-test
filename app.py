from flask import Flask, redirect, url_for
import subprocess
from datetime import datetime
import pytz
import os

app = Flask(__name__)

def get_username():
    return os.getenv('USER') or os.getenv('USERNAME') or 'Unknown'

def get_top_output():
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1'], text=True)
        return top_output
    except subprocess.CalledProcessError:
        return "Error fetching top data"

@app.route('/')
def root():
    return redirect(url_for('htop'))

@app.route('/htop')
def htop():
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')
    
    name = "Sayan Biswas"  
    username = get_username()
    top_output = get_top_output()
    
    html_response = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>System Monitor</title>
        <style>
            body {{
                font-family: monospace;
                padding: 20px;
                background-color: #1e1e1e;
                color: #ffffff;
            }}
            pre {{
                background-color: #2d2d2d;
                padding: 15px;
                border-radius: 5px;
                overflow-x: auto;
            }}
        </style>
    </head>
    <body>
    <pre>
Name: {name}
User: {username}
Server Time (IST): {server_time}
TOP output:
{top_output}
    </pre>
    </body>
    </html>
    """
    
    return html_response

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)