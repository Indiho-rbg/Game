from flask import Flask

app = Flask(__name__)

@app.route('/')
def handler(request):
    return 'Hello from serverless function'
    
if __name__ == "__main__":
    app.run()
