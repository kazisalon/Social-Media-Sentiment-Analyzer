from flask import Flask, request, jsonify
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    try:
        data = request.json
        text = data.get('text', '')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        # Create TextBlob object
        analysis = TextBlob(text)
        
        # Get the sentiment polarity (-1 to 1)
        polarity = analysis.sentiment.polarity
        
        # Determine sentiment category
        if polarity > 0:
            sentiment = 'positive'
        elif polarity < 0:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
            
        return jsonify({
            'text': text,
            'sentiment': sentiment,
            'polarity': polarity,
            'subjectivity': analysis.sentiment.subjectivity
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)