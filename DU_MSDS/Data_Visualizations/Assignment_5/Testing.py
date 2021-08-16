
import numpy as np
from bokeh.plotting import figure, output_file, show
output_file('exer1.html')
p=figure()
x=np.linspace(0,10,101)
y0=x
y1=x*x
y2=x*x*x
p.line(x,y0,legend="y=x",line_color='blue')
p.line(x,y1,legend='y=x^2',line_color='red')
p.line(x,y2,legend='y=x^3',line_color='violet')
show(p)