import secrets
from app import create_app

app = create_app()
app.config['SECRET_KEY'] = secrets.token_hex(32)

if __name__ == '__main__':
    app.run(debug=True, port=5001)  