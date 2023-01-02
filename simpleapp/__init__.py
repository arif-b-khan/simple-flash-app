from flask import Flask
from .system.hostinfo import HostInfo

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    My flask app
    My Ip: {0}
    Name: {1}
    '''.format(HostInfo.get_ip(), HostInfo.gethostname())

if __name__ == "__main__":
    app.run()