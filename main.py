from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello Readers! I am a sample Python application running on Azure Web Apps'

if __name__ == '__main__':
  app.run()
