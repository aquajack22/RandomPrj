from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def root():
    return send_from_directory('html', 'index.html')

if __name__ == "__main__": 
    app.run(debug=True, host='0.0.0.0')
