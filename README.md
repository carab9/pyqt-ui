# pyqt-ui

The program runs in two parts, with an input argument 1 or 2. The first part displays a red square in a QtWidget. The user can click on the red square and drag it around inside the border of the QtWidget, but the red square can't be dragged outside of the QtWidget, regardless of the current size of the QtWidget.

The second part displays a color ball bouncing around inside the border of the QtWidget. The default color of the bouncing ball is red, but the color of the ball can be changed via the optional input arguments. For example, the input arguments will be "2 0 0 255" to run a bouncing blue ball in the second mode. The QtWidget spawns a QThread, which uses a  QTimer, to help create an animation of a ball bouncing around
inside a window.

Part 1

![image](https://github.com/carab9/pyqt-ui/blob/main/pyqt_ui1.jpg?raw=true)

Part 2

![image](https://github.com/carab9/pyqt-ui/blob/main/pyqt_ui2.jpg?raw=true)

![image](https://github.com/carab9/pyqt-ui/blob/main/pyqt_ui3.jpg?raw=true)

