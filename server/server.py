from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# Example functions
def function1(inputs):

    return sum(map(int, inputs))

def function2(inputs):
    return min(map(int, inputs))

function_map = {
    "Function1": function1,
    "Function2": function2,
    # to be added
}

@app.route('/execute', methods=['POST'])
def execute():
    data = request.get_json()  # Get the incoming JSON data
    function_name = data.get('name')
    inputs = data.get('inputs')

    # Call the appropriate function based on the name
    if function_name in function_map:
        result = function_map[function_name](inputs)
        return jsonify(result=result)  # Return result as JSON
    else:
        return jsonify(result="Function not found"), 404  # Handle unknown functions

if __name__ == '__main__':
    app.run(port=5000)  # Run server on localhost:5000