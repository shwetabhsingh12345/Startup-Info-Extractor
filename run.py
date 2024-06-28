import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow warnings

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
