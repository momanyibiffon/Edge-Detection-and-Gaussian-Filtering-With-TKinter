from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter.filedialog
import cv2 as cv


def select_image_gaussian():
    #grab a reference to the image panels
    global panelA, panelB
    # open a file chooser dialog and allow the user to select an input
    # image
    path = tkinter.filedialog.askopenfilename()
    # ensure a file path was selected
    if len(path) > 0:
        # load the image from disk
        img = cv.imread(path)

        # image scaled to get new dimensions
        scale_percent = 20  # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        image = cv.resize(img, dim, interpolation=cv.INTER_AREA)

        # apply gaussian blur on src image
        gaussed = cv.GaussianBlur(image, (9, 9), cv.BORDER_DEFAULT)

        # OpenCV represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

        # convert the images to PIL format...
        image = Image.fromarray(image)
        gaussed = Image.fromarray(gaussed)

        # ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)
        gaussed = ImageTk.PhotoImage(gaussed)

        # if the panels are None, initialize them
        if panelA is None or panelB is None:
            # the first panel will store our original image
            panelA = Label(image=image)
            panelA.image = image
            panelA.pack(side="left", padx=10, pady=10)

            # while the second panel will store the edge map
            panelB = Label(image=gaussed)
            panelB.image = gaussed
            panelB.pack(side="right", padx=10, pady=10)

            # otherwise, update the image panels
        else:
            # update the pannels
            panelA.configure(image=image)
            panelB.configure(image=gaussed)
            panelA.image = image
            panelB.image = gaussed


def select_image():
    # grab a reference to the image panels
    global panelA, panelB
    # open a file chooser dialog and allow the user to select an input
    # image
    path = tkinter.filedialog.askopenfilename()
    # ensure a file path was selected
    if len(path) > 0:
        # load the image from disk
        img = cv.imread(path)

        # image scaled to get new dimensions
        scale_percent = 20  # percent of original size
        width = int(img.shape[1] * scale_percent / 100)
        height = int(img.shape[0] * scale_percent / 100)
        dim = (width, height)
        # resize image
        image = cv.resize(img, dim, interpolation=cv.INTER_AREA)
        # convert it to grayscale
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        # detect edges in it with Canny
        edged = cv.Canny(gray, 50, 100)

        # OpenCV represents images in BGR order; however PIL represents
        # images in RGB order, so we need to swap the channels
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

        # convert the images to PIL format...
        image = Image.fromarray(image)
        edged = Image.fromarray(edged)

        # ...and then to ImageTk format
        image = ImageTk.PhotoImage(image)
        edged = ImageTk.PhotoImage(edged)

        # if the panels are None, initialize them
        if panelA is None or panelB is None:
            # the first panel will store our original image
            panelA = Label(image=image)
            panelA.image = image
            panelA.pack(side="left", padx=10, pady=10)

            # while the second panel will store the edge map
            panelB = Label(image=edged)
            panelB.image = edged
            panelB.pack(side="right", padx=10, pady=10)

            # otherwise, update the image panels
        else:
            # update the pannels
            panelA.configure(image=image)
            panelB.configure(image=edged)
            panelA.image = image
            panelB.image = edged

# initialize the window toolkit along with the two image panels


root = Tk()
panelA = None
panelB = None

# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI

btn = Button(root, text="Edge detection", command=select_image)
btn.pack(side="bottom", expand="yes", padx="10", pady="10")

btn = Button(root, text="Gaussian Filter", command=select_image_gaussian)
btn.pack(side="bottom", expand="yes", padx="10", pady="10")
# kick off the GUI
root.mainloop()





