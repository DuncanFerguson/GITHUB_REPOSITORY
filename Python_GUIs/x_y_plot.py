import matplotlib.pyplot as plt


def makeLineGraph(x,y):
    """This Takes any x, y values and makes a clean looking Line Graph. There are various different layouts described
    below throughout the comments for editing the graph."""
    plt.plot(x, y, 'b')
    plt.xlabel('x-Labels')
    plt.ylabel('y-Labels')
    # plt.legend()
    plt.title('standardtitle')
    plt.xticks(rotations=45)
    plt.show()  # Showing the code
    return


