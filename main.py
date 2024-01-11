from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

API_KEY = "4b1a0e44-0205-4ad8-9158-3c10c3e87ae9"


class News:
    def __init__(self, tit):
        self.tit = tit


# Create news objects
news1 = News("Demo")

# Store news objects in a list
news_list = [news1]


@app.route('/api/news', methods=['GET'])
@cross_origin()
def get_news():
    api_key = request.args.get('api_key')

    if api_key != API_KEY:
        return jsonify({'error': 'Invalid API key'}), 401

    news_data = []
    for news in news_list:
        news_data.append({
            'tit': news.tit
        })

    return jsonify({'news': news_data})


if __name__ == '__main__':
    app.run(debug=True)

