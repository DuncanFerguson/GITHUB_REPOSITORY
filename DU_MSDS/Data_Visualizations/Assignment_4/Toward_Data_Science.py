import pandas as pd

from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import row, column

from bokeh.models import Select, CheckboxButtonGroup ### Widgets

### Dataset Imports
from bokeh.sampledata.stocks import GOOG as google
from sklearn.datasets import load_iris, load_wine


checkbox_options = ['open','high','low','close']
color_mapping = {0:"tomato", 1:"dodgerblue", 2:"lime"}
price_color_map = {"open":"dodgerblue", "close":"tomato", "low":"lime", "high":"orange"}

#### IRIS Dataset Loading #####
iris = load_iris()

iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df["FlowerType"] = iris.target


### Google Price Dataset Loading ##############
google_df = pd.DataFrame(google)
google_df["date"] = pd.to_datetime(google_df["date"])



### Line Chart of Google Prices Code Starts ###########

line_chart = figure(plot_width=1000, plot_height=400, x_axis_type="datetime",
                    title="Google Stock Prices from 2005 - 2013")

line_chart.line(
                x="date", y="open",
                line_width=0.5, line_color="dodgerblue",
                legend_label = "open",
                source=google_df
                )

line_chart.xaxis.axis_label = 'Time'
line_chart.yaxis.axis_label = 'Price ($)'

line_chart.legend.location = "top_left"

### Line Chart of Google Prices Code Ends ###########


### Scatter Chart Of IRIS Dimesions Code Starts ###########
scatter = figure(plot_width=500, plot_height=400,
                 title="Sepal Length vs Sepal Width Scatter Plot")

for cls in [0,1,2]:
    scatter.circle(x=iris_df[iris_df["FlowerType"]==cls]["sepal length (cm)"],
               y=iris_df[iris_df["FlowerType"]==cls]["sepal width (cm)"],
               color=color_mapping[cls],
               size=10,
               alpha=0.8,
               legend_label=iris.target_names[cls])

scatter.xaxis.axis_label= "sepal length (cm)".upper()
scatter.yaxis.axis_label= "sepal width (cm)".upper()

### Scatter Chart Of IRIS Dimesions Code Ends ###########


### Bar Chart Of IRIS Dimesions Code Starts ###########
iris_avg_by_flower_type = iris_df.groupby(by="FlowerType").mean()

bar_chart = figure(plot_width=500, plot_height=400,
                    title="Average Sepal Length (cm) per Flower Type")

bar_chart.vbar(x = [1,2,3],
                width=0.9,
                top=iris_avg_by_flower_type["sepal length (cm)"],
                fill_color="tomato", line_color="tomato", alpha=0.9)

bar_chart.xaxis.axis_label="FlowerType"
bar_chart.yaxis.axis_label="Sepal Length"

bar_chart.xaxis.ticker = [1, 2, 3]
bar_chart.xaxis.major_label_overrides = {1: 'Setosa', 2: 'Versicolor', 3: 'Virginica'}

### Bar Chart Of IRIS Dimesions Code Starts ###########


### Widgets Code Starts ################################
drop_scat1 = Select(title="X-Axis-Dim",
                    options=iris.feature_names,
                    value=iris.feature_names[0],
                    width=225)

drop_scat2 = Select(title="Y-Axis-Dim",
                    options=iris.feature_names,
                    value=iris.feature_names[1],
                    width=225)

checkbox_grp = CheckboxButtonGroup(labels=checkbox_options, active=[0], button_type="success")

drop_bar = Select(title="Dimension", options=iris.feature_names, value=iris.feature_names[0])

### Widgets Code Ends ################################


##### Code to Update Charts as Per Widget  State Starts #####################

def update_line_chart(attrname, old, new):
    '''
        Code to update Line Chart as Per Check Box Selection
    '''
    line_chart = figure(plot_width=1000, plot_height=400, x_axis_type="datetime",
                        title="Google Stock Prices from 2005 - 2013")

    for option in checkbox_grp.active:
        line_chart.line(
                x="date", y=checkbox_options[option],
                line_width=0.5, line_color=price_color_map[checkbox_options[option]],
                legend_label=checkbox_options[option],
                source=google_df
            )

    line_chart.xaxis.axis_label = 'Time'
    line_chart.yaxis.axis_label = 'Price ($)'

    line_chart.legend.location = "top_left"

    layout_with_widgets.children[0].children[1] = line_chart


def update_scatter(attrname, old, new):
    '''
        Code to update Scatter Chart as Per Dropdown Selections
    '''
    scatter = figure(plot_width=500, plot_height=400,
                     title="%s vs %s Scatter Plot"%(drop_scat1.value.upper(), drop_scat2.value.upper()))

    for cls in [0,1,2]:
        scatter.circle(x=iris_df[iris_df["FlowerType"]==cls][drop_scat1.value],
                   y=iris_df[iris_df["FlowerType"]==cls][drop_scat2.value],
                   color=color_mapping[cls],
                   size=10,
                   alpha=0.8,
                   legend_label=iris.target_names[cls])

    scatter.xaxis.axis_label= drop_scat1.value.upper()
    scatter.yaxis.axis_label= drop_scat2.value.upper()

    layout_with_widgets.children[1].children[0].children[1] = scatter


def update_bar_chart(attrname, old, new):
    '''
        Code to Update Bar Chart as Per Dropdown Selections
    '''
    bar_chart = figure(plot_width=500, plot_height=400,
                       title="Average %s Per Flower Type"%drop_bar.value.upper())

    bar_chart.vbar(x = [1,2,3],
             width=0.9,
             top=iris_avg_by_flower_type[drop_bar.value],
             fill_color="tomato", line_color="tomato", alpha=0.9)

    bar_chart.xaxis.axis_label="FlowerType"
    bar_chart.yaxis.axis_label=drop_bar.value.upper()

    bar_chart.xaxis.ticker = [1, 2, 3]
    bar_chart.xaxis.major_label_overrides = {1: 'Setosa', 2: 'Versicolor', 3: 'Virginica'}

    layout_with_widgets.children[1].children[1].children[1] = bar_chart

##### Code to Update Charts as Per Widget  State Ends #####################


#### Registering Widget Attribute Change with Methods Code Starts #############
checkbox_grp.on_change("active", update_line_chart)

drop_scat1.on_change("value", update_scatter)
drop_scat2.on_change("value", update_scatter)

drop_bar.on_change("value", update_bar_chart)

#### Registering Widget Attribute Change with Methods Code Ends #############

####### Widgets Layout #################
layout_with_widgets = column(
                            column(checkbox_grp, line_chart),
                            row(
                                column(row(drop_scat1, drop_scat2), scatter),
                                column(drop_bar, bar_chart)))


############ Creating Dashboard ################
curdoc().add_root(layout_with_widgets)