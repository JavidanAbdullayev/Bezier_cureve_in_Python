# Student - Javidan Abdullayev

# Code to create Bezier Curve


# matplotlib library to plot lines and curves
#import matplotlib.pyplot as plt

# Point object has two coordinate x and y
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
	
# define points, you can add more point if you want or remove some
P0 = Point(2, 2)
P1 = Point(0, 1)
P2 = Point(3, -1)
P3 = Point(4, 1)
# If you create new Point object please don't forget putting it into 'list_of_points' variable


# I put all of my points into a list which is called 'list_of_points'
list_of_points = [P0, P1, P2, P3]
points = list_of_points   # I created second pointer to list_of_points variable because I will need it later

# This function is used to plot control polygon of bezier curve
def plot_control_polygon(points):
    step = 0.1
    for i in range(len(points) - 1):
        x_list = []
        y_list = []
        t = 0
        while t <= 1:
            x = points[i].x + t * (points[i + 1].x - points[i].x)
            y = points[i].y + t * (points[i + 1].y - points[i].y)
            x_list.append(x)
            y_list.append(y)
            t += step
        plt.plot(x_list, y_list)

# This function is used to plot the bezier curve itself
# I used De Casteljau's Algorithm to create bezier curve
def plot_curve(points):
    # plot control polygon of bezier curve
    plot_control_polygon(points)
    # from here I start to code bezier curve
    t = 0
    step = 0.03
    x_list = []
    y_list = []
    list_ = []
    while t <= 1:
        points = list_of_points
        for i in range(len(points) - 1):
            j = len(points) - 1
            for k in range(j):
                x = (1 - t) * points[k].x + t * points[k + 1].x
                y = (1 - t) * points[k].y + t * points[k + 1].y
                list_.append(Point(x, y))

            points = list_
            list_ = []

        x_list.append(points[0].x)
        y_list.append(points[0].y)

        t += step
    plt.scatter(x_list, y_list)
    first_x, first_y = x_list[0], y_list[0]
    last_x, last_y = x_list[-1], y_list[-1]
    print('first_x = ', first_x, '  first_y = ',first_y);
    print('last_x = ', last_x, '  last_y = ',last_y);
    plt.show()

plot_curve(points)
