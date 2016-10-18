# Import necessary code from flask, giphy and os
from flask import Flask, render_template, request
import giphypop
import os

# Create Flask instance in main module
app = Flask(__name__)

# Redefine giphy api as g
g = giphypop.Giphy()

# Main Page
@app.route('/')
def index():
	return render_template('index.html')

# About Us Page
@app.route('/about')
def about():
	return render_template('sample_page.html')

# GIFs search results page
@app.route('/results')
def results():
	search_results = request.values.get('input')
	results = g.search(search_results)
	search = request.args.get('input')
	media = []	

#Error Handling - if search is successful, it will go to results page. If not, it will go to an error page.
	try:
		for result in results:
			media.append(result.media_url)
		return render_template('results.html', search=search, gifs=media)
	except:
		return render_template('error_page.html')

# Deploying on localhost:5000
# app.run(debug=True) 

# Deploying on Heroku app
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
