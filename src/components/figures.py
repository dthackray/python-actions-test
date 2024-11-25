import plotly.express as px


def create_sales_trend(df):
    """Create sales trend line chart."""
    # Group by date and calculate daily sales
    daily_sales = df.groupby("date")["sales"].sum().reset_index()

    fig = px.line(daily_sales, x="date", y="sales", title="Daily Sales Trend")

    fig.update_traces(line_color="#4C51BF")
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Date",
        yaxis_title="Sales ($)",
        hovermode="x unified",
    )

    return fig


def create_product_comparison(df):
    """Create product comparison bar chart."""
    product_sales = (
        df.groupby("product").agg({"sales": "sum", "units": "sum"}).reset_index()
    )

    fig = px.bar(
        product_sales,
        x="product",
        y="sales",
        title="Sales by Product",
        color="product",
        color_discrete_sequence=px.colors.qualitative.Set3,
    )

    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis_title="Product",
        yaxis_title="Sales ($)",
        showlegend=False,
    )

    return fig
