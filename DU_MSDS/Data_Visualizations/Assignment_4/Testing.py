from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Blues8
import pandas as pd
import icecream as ic

df = pd.read_csv('StrumData_Duncan_testing.csv')
earnings = df['earnings']

# Creat ColumnDataSource from dataframe
source = ColumnDataSource(df)

# State list
state_list = source.data['state'].tolist()
# earnings_list = source.data['earnings'].tolist()

output_file('index.html')

# Add plot
p = figure(title="Testing",
           y_range=state_list,
           plot_width=800,
           plot_height=600,
           x_axis_label='X Axis Label',
           tools="pan,box_select,zoom_in,zoom_out,save,reset")

#render glyph
p.hbar(y='state',
       right='earnings',
       left=0,
       height=0.4,
       fill_color=factor_cmap('Title', palette=Blues8, factors=state_list),
       fill_alpha=0.9,
       source=source,
       legend='earnings')

p.legend.orientation = 'vertical'
p.legend.location = 'top_right'
p.legend.label_text_font_size='10px'

# Add Tooltips
hover = HoverTool()
hover.tooltips = """
    <div>
        <h3>@state</h3>
        <div><strong>Earnings: </strong>@earnings</div>
    </div>
"""

p.add_tools(hover)

show(p)