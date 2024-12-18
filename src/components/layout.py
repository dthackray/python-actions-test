from dash import dcc, html

from src.components.figures import create_product_comparison, create_sales_trend
from src.data.loader import load_data


def create_layout():
    """Create the main layout of the dashboard."""
    df = load_data()

    return html.Div(
        [
            # Header
            html.H1("Sales Dashboard", className="text-3xl font-bold mb-8"),
            # KPI Cards
            html.Div(
                [
                    create_kpi_card("Total Sales", f"${df['sales'].sum():,.2f}"),
                    create_kpi_card("Total Units", f"{df['units'].sum():,}"),
                    create_kpi_card("Average Order", f"${df['sales'].mean():,.2f}"),
                ],
                className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8",
            ),
            # Charts
            html.Div(
                [
                    # Sales Trend Chart
                    html.Div(
                        [
                            html.H2("Sales Trend", className="text-xl font-bold mb-4"),
                            dcc.Graph(
                                id="sales-trend",  # Added ID here
                                figure=create_sales_trend(df),
                            ),
                        ],
                        className="bg-white p-6 rounded-lg shadow",
                    ),
                    # Product Comparison Chart
                    html.Div(
                        [
                            html.H2(
                                "Product Performance",
                                className="text-xl font-bold mb-4",
                            ),
                            dcc.Graph(
                                id="product-comparison",  # Added ID here
                                figure=create_product_comparison(df),
                            ),
                        ],
                        className="bg-white p-6 rounded-lg shadow",
                    ),
                ],
                className="grid grid-cols-1 lg:grid-cols-2 gap-8",
            ),
        ]
    )


def create_kpi_card(title, value):
    """Create a KPI card component."""
    return html.Div(
        className="bg-white p-6 rounded-lg shadow",
        children=[
            html.H3(title, className="text-gray-600 text-sm font-semibold"),
            html.P(value, className="text-2xl font-bold mt-2"),
        ],
    )
