from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def index():
	return render_template('sample_page.html')

app.run(debug=True)
