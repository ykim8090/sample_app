from flask import Flask, render_template, request
import giphypop
import os

app = Flask(__name__)

g = giphypop.Giphy()

@app.route('/')
def index():
	name = request.values.get('name', 'Nobody')
	greeting = "Hello {}".format(name)
	return render_template('index.html', greeting=greeting)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/results')
def results():
	search_results = request.values.get('input')
	results = g.search(search_results)
	media = []

	for result in results:
		media.append(result.media_url)

	return render_template('results.html', input=input, gifs=media)

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)