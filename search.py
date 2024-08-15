from flask import Flask, request, jsonify
from googlesearch import search

app = Flask(__name__)

def twitter_search(position, company):
    query = f'site:twitter.com "{position}" "{company}" in bio'
    results = []
    for j in search(query, num=10, stop=10, pause=2):
        results.append(j)
    return results

@app.route('/search', methods=['GET'])
def search_twitter():
    position = request.args.get('position')
    company = request.args.get('company')
    
    if not position or not company:
        return jsonify({"error": "Please provide both 'position' and 'company' parameters."}), 400
    
    results = twitter_search(position, company)
    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)
