import numpy as np 
import matplotlib.pyplot as plt


ST1 = np.array([[17.0 ,12 ,13 ,15 ,15 ,20 ,20],[ 10 ,12 ,14 ,15 ,20 ,15 ,20]]) # class 1 
ST2 = np.array([4, 7.5, 10 ,11, 5 ,5 ,6, 8, 5, 0, 5, 0, 10, 6]).reshape(2,7) # class 2 
Xstudents = np.concatenate((ST1,ST2),axis=1)

Ystudents = np.ones(14)
Ystudents[7:] = 0



def plot2DBinaryDataSet(D1, D2, xmin, xmax, ymin, ymax,st1='go',st2="ro"):
    """Plot a dataset made of 2D points. 
    The dataset is provided in 2 parts for the 2 classes: D1 and D2
        Args: 
            - D1: numpy array of size (2,N), N the number of points in the 1st class
            - D2: numpy array of size (2,M), M the number of points in the 2nd class
            - xmin,xmax,ymin,ymax : numbers to define the plot domain
            - st1 and st2: resp. the style for class 1 and 2
        
        Return: 
            None

    Assume : import matplotlib.pyplot as plt
    """
        # Create the axis: 
    plt.axis([xmin,xmax,ymin,ymax])
    plt.grid(True);
    plt.plot(D1[0,:],D1[1,:],st1)
    plt.plot(D2[0,:],D2[1,:],st2)
    
    




def plotLine(u,b,xmin, xmax, ymin, ymax, linestyle = "-", color="k" ):
    """Plot a line in the "box" defined by xmin, xmax, ymin, ymax
    
    Args: 
        - u : The line is defined by its normal vector u, a numpy array of size 2
        - b : the constant term
        - the "box" is defined by xmin, xmax, ymin, ymax
        
    The line has the equation:     u[0]*x + u[1]*y + b = 0 
    """
    if (u[1]==0):
        if (u[0] == 0):
            sys.stdout.write("WARNING cannot plot such line ...")
            return
        x1=-b/u[0]
        y1=ymax
        x2=x1
        y2=ymin
    else:
        x1=xmax
        y1=-(b+u[0]*x1)/u[1]
        x2=xmin
        y2=-(b+u[0]*x2)/u[1]
    plt.axis([xmin,xmax,ymin,ymax])
    plt.grid(True)
    plt.plot([ x1 , x2 ] , [ y1 , y2 ], linestyle=linestyle, color=color)


def testPlot():
    plot2DBinaryDataSet(Xstudents[:,Ystudents==1],Xstudents[:,Ystudents==0],  xmin = -1.0, xmax=21 , ymin = -1, ymax = 21)
    plotLine([0.5, 0.5],-10, xmin = -1.0, xmax=21 , ymin = -1, ymax = 21,color="b")

if __name__ == "__main__":
    testPlot()
    plt.show()

    
