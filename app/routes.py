from app import app

@app.route('/')
@app.route('/index')
def index():
  return "Hello, World!"

@app.route('/zach')
def zach():
  return "Zach is cool!"