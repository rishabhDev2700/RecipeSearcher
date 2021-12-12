from flask import Flask, render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config['DEBUG'] = True
    app.config.from_mapping(
        SECRET_KEY='dev'
    )
    return app


if __name__ == '__main__':
    create_app().run()
