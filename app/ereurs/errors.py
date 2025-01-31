from flask import jsonify
from werkzeug.exceptions import HTTPException

def handle_http_exception(e):
    response = {
        "error": e.description,
        "code": e.code
    }
    return jsonify(response), e.code

# 404 error handler
def handle_404(e):
    return jsonify({"error": "Page not found", "code": 404}), 404

# 500 error handler
def handle_500(e):
    return jsonify({"error": "Internal Server Error", "code": 500}), 500

# Function to register error handlers in the main app
def register_error_handlers(app):
    app.register_error_handler(HTTPException, handle_http_exception)  # Generic HTTP errors
    app.register_error_handler(404, handle_404)  # Specific error
    app.register_error_handler(500, handle_500)