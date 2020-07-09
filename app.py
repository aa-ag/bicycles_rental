from webapp import app,routes
from flask_sqlalchemy import SQLAlchemy

if __name__ == "__main__":
    app.run(debug = True)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
db = SQLAlchemy(app)