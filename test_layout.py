def test_layout_structure(dash_app):
    """Test that the layout contains expected components"""
    layout = dash_app.layout
    assert layout is not None

    # Test presence of main components
    children = layout.children
    assert any(child.id == "sales-trend" for child in children)
    assert any(child.id == "product-comparison" for child in children)


def test_page_title(dash_test_client):
    """Test that the page title is correct"""
    response = dash_test_client.get("/")
    assert response.status_code == 200
    assert b"Sales Dashboard" in response.data
