from flask import Flask, request, jsonify
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)

# Sample student marks dictionar

# Load student marks from JSON file
with open('q-vercel-python.json', 'r') as f:
    student_marks = json.load(f)
student_marks = {student['name']: student['marks'] for student in student_marks}
@app.route('/api', methods=['GET'])
def get_marks():
    # Get 'name' parameters from query string
    names = request.args.getlist('name')
    result = {"marks": []}

    for name in names:
        marks = student_marks.get(name, "Marks not found")
        result['marks'].append(marks)

    return jsonify(result)

# Needed to run Flask in Vercel
if __name__ == '__main__':
    app.run()
