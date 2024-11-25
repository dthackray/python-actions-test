from dash.testing.application_runners import import_app


def test_app_initialization():
    """Test that app initializes correctly"""
    # Import the app from src/app.py
    app = import_app("src.app")
    assert app is not None
    assert app.config.suppress_callback_exceptions is False
