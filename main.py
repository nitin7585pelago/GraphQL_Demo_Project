from flask import Flask
from flask_graphql import GraphQLView

app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)