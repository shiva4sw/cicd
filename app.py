from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>Reva Univesity</h1>Azure Training...<hr/>@copy'

if __name__=='__main__':
    app.run(debug=True)