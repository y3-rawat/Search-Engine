from flask import Flask, request, render_template
from googlesearch import search

app = Flask(__name__)

def twitter_search(position, company):
    query = f'site:twitter.com "{position}" "{company}" in bio -inurl:status'
    results = []
    for j in search(query, num=10, stop=10, pause=2):
        results.append(j)
    return results

@app.route('/', methods=['GET', 'POST'])
def search_twitter():
    if request.method == 'POST':
        position = request.form['position']
        company = request.form['company']
        
        if not position or not company:
            return render_template('search.html', error="Please provide both position and company.", results=None)
        
        results = twitter_search(position, company)
        return render_template('search.html', results=results)
    
    return render_template('search.html', results=None)

if __name__ == '__main__':
    app.run(debug=True)
