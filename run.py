from flaskblog import app

if __name__ == '__main__':

    app.app_context().push()

    # Run the Flask application
    app.run(debug=True)