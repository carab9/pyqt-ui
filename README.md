# pyqt-ui

The program runs in two parts, with an input argument 1 or 2. 

The first part displays a red square in a QtWidget. The user can click on the red square and drag it around inside the border of the QtWidget, but the red square can't be dragged outside of the QtWidget, regardless of the current size of the QtWidget. When the user double clicks on the square, a color dialog box will pop up and allow the user to change the color of the square.

The second part displays a color ball bouncing around inside the border of the QtWidget. The default color of the bouncing ball is red, but the color of the ball can be changed via the optional input arguments. For example, the input arguments will be "2 0 0 255" to run a bouncing blue ball in the second part. The QtWidget spawns a QThread, which uses a QTimer, to help create an animation of a ball bouncing around inside a window.

## Requirements

Python, PyQt5, QApplication, QWidget, QColorDialog, QPainter, QColor, QThread, QTimer, random.randint

## Techical Skills:

Python, PyQt5 for GUI (QApplication, QWidget, QColorDialog, QPainter, QColor), QColorDialog for the user to change the color of the square, QThread and QTimer for animating the bouncing ball, random.randint for initializing the random location of the red square.

## Results

Part 1

![image](https://github.com/carab9/pyqt-ui/blob/main/pyqt_ui1.png?raw=true)

![image](https://github.com/carab9/pyqt-ui/blob/main/pyqt_ui4.png?raw=true)

Part 2

![image](https://github.com/carab9/pyqt-ui/blob/main/pyqt_ui2.png?raw=true)

![image](https://github.com/carab9/pyqt-ui/blob/main/pyqt_ui3.png?raw=true)

