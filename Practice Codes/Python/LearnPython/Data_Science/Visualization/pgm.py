import numpy as np
import matplotlib.pyplot as plt

def line_plot():
    x = np.arange(1,1000)
    y = np.square(x)
    plt.xlabel("Numbers")
    plt.ylabel("Squares")
    plt.title("Square of a number")
    plt.plot(x,y)
    plt.show()

def main():
    # Square of a number within a range...
    line_plot()

if __name__ == "__main__":
    main()