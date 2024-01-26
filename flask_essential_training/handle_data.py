from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/handle_data', methods = ['POST'])
def handle_data():

    #Get the content type.
    content_type = request.headers.get('Content-Type')
    print(f'Content type is: {content_type}')

    if content_type == 'text/plain':
        data = request.data.decode('utf-8')
        return jsonify({'message': 'Text data received', 'data': data})
    
    elif content_type == 'application/json':
        data = request.json
        return jsonify({'message': 'JSON data received', 'data': data})
    
    elif content_type.split(";")[0] == 'multipart/form-data':
        data = request.form.to_dict()
        return jsonify({'message': 'Multipart form data received', 'data': data})
    
    elif content_type == "application/x-www-form-urlencoded":
        data = request.form.to_dict()
        return jsonify({'message': 'URL form data received', 'data': data})
    
    else:
        return jsonify({'message': f'Unsupported data type {content_type}'}), 400
    
if __name__ == '__main__':
    app.run(debug = True)
