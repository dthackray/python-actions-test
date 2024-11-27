import pytest
from dash.testing.application_runners import import_app


@pytest.fixture
def dash_app():
    """Create a Dash app fixture for testing"""
    app = import_app("src.app")
    return app


@pytest.fixture
def dash_test_client(dash_app):
    """Create a test client for the Dash app"""
    return dash_app.server.test_client()
