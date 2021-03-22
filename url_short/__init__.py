from flask import Flask

def create_app(test_config=None):
	app = Flask(__name__)
	app.secret_key = "fnenfjnfjd1221xjcnusndcdfsnefkefkwfmkenff"

	from . import url_short
	print(url_short)
	app.register_blueprint(url_short.bp)

	return app
