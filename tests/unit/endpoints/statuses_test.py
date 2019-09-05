from flask_testing import TestCase
from flask import Flask

import mock


class StatusesTest(TestCase):

    def create_app(self, *_):
        from app.endpoints.statuses import blueprint as status_bp
        app = Flask(__name__)
        app.config['TESTING'] = True

        app.register_blueprint(status_bp)
        return app

    def test_status(self):
        response = self.client.get("/status")
        self.assert200(response)

    def test_healthz(self):
        response = self.client.get("/healthz")
        self.assert200(response)

    """
    @mock.patch.object(Database, 'is_database_ok')
    def test_ready_ok(self, is_database_ok):
        is_database_ok.return_value = True
        response = self.client.get("/ready")
        self.assert200(response)

    @mock.patch.object(Database, 'is_database_ok')
    def test_ready_error(self, is_database_ok):
        is_database_ok.return_value = False

        response = self.client.get('/ready')
        self.assertStatus(response, 503)
    """
