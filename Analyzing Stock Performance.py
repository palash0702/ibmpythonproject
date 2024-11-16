import pandas as pd
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.offline import init_notebook_mode, iplot

# Graph function
def make_graph(stock_data, revenue_data, stock, output_file = "graph.html"):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    # Filter Data
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    # Add Traces
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    # Updated axes
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Quartely Revenue ($US Millions)", row=2, col=1)
    # Adding layout
    fig.update_layout(showlegend=False, height=900, title=stock, xaxis_rangeslider_visible=True)
    fig.write_html(output_file)
    print(f"Graph saved to {output_file}")

## yFinance API to get Stock data
# Loading the Tesla stock data using YF API
tesla = yf.Ticker('TSLA')
# Loading the share price data
tesla_data = tesla.history(period="max")
# Resetting the index
tesla_data.reset_index(inplace=True)
# Displaying first 5 rows
tesla_data.head()

## HTML Revenue Data
# Reading revenue data from html
tesla_revenue_data = pd.read_html('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/'
                                  'IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm')
# Accessing the 2nd table
tesla_revenue_data = tesla_revenue_data[1]
# Renaming the columns
tesla_revenue_data.columns = ['Date','Revenue']
# Replacing string characters and changing the data type to float
tesla_revenue_data['Revenue']=tesla_revenue_data['Revenue'].replace('[$,]','', regex=True).astype(float)
# Dropping N/A values
tesla_revenue_data.dropna(inplace=True)
# Displaying bottom 5
tesla_revenue_data.tail()

make_graph(tesla_data, tesla_revenue_data, 'TESLA',"tesla_graph.html")


# Loading stock data
gamestop = yf.Ticker('GME')
# Loading sharep price data
gme_data = gamestop.history(period="max")
# Resetting index
gme_data.reset_index(inplace=True)
# Displaying first 5 rows
gme_data.head()

# Reading revenue data from HTML
gme_revenue_data = pd.read_html('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/'
                                'IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html')
# Reading data from 2nd table
gme_revenue_data = gme_revenue_data[1]
# Renaming the columns
gme_revenue_data.columns = ['Date','Revenue']
# Removing string characters and changing the datatype to float
gme_revenue_data['Revenue'] = gme_revenue_data['Revenue'].replace('[$,]','',regex=True).astype(float)
# Displaying bottom 5 rows
gme_revenue_data.tail()

make_graph(gme_data, gme_revenue_data, 'GameStop',"gme_graph.html")
