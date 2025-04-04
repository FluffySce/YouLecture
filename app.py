from flask import Flask, request,jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/api/generate-lesson', methods=['POST'])
def generate_lesson():
    data = request.get_json()
    youtube_url = data.get('url')
    if not youtube_url:
        return jsonify({'error': 'Missing YouTube URL'}), 400
    # TEMP: Dummy lesson generation logic
    lesson_plan = {
        "title": "Sample Lesson Plan",
        "url": youtube_url,
        "points": [
            "Introduction to the topic",
            "Key highlights from the video",
            "Important terms and explanations",
            "Summary and takeaway"
        ]
    }
    
    return jsonify(lesson_plan), 200
if __name__ == '__main__':
    app.run(debug=True)