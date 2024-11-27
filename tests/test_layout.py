from dash import html

from src.components.layout import create_layout


def test_layout_structure(dash_app):
    """Test that the layout contains expected components"""
    layout = create_layout()
    assert layout is not None

    # Find Graph components by ID
    def find_component_by_id(children, component_id):
        if getattr(children, "id", None) == component_id:
            return True
        if hasattr(children, "children"):
            if isinstance(children.children, (list, tuple)):
                return any(
                    find_component_by_id(child, component_id)
                    for child in children.children
                )
            return find_component_by_id(children.children, component_id)
        return False

    # Check for main components
    assert find_component_by_id(layout, "sales-trend"), "Sales trend graph not found"
    assert find_component_by_id(
        layout, "product-comparison"
    ), "Product comparison graph not found"


def test_layout_header(dash_app):
    """Test that the header is present"""
    layout = create_layout()

    # Find H1 component
    def find_h1(children):
        if isinstance(children, html.H1):
            return children
        if hasattr(children, "children"):
            if isinstance(children.children, (list, tuple)):
                for child in children.children:
                    result = find_h1(child)
                    if result:
                        return result
            else:
                return find_h1(children.children)
        return None

    header = find_h1(layout)
    assert header is not None, "Header not found"
    assert header.children == "Sales Dashboard", "Incorrect header text"
