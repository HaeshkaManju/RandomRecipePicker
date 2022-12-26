import tkinter as tk
from PIL import ImageTk

# initiallize app
root = tk.Tk()
# title method places this in the window pane, top-left.
root.title("Recipe Picker")
# "tcl" method.  Moves opening window to center of user's screen.
# root.eval("tk::PlaceWindow . center")
'''
Apparently, this is a way to more precisely control where "the center" of the
    screen is understood to be.
    obviously the //2 and the *0.01 are just specifics from the tutorial, but
        this can be modified and improved further.
'''
x = root.winfo_screenwidth() // 2
y = int(root.winfo_screenheight() * 0.1)
root.geometry('500x600+' + str(x) + '+' + str(y))
'''
Frames are grouped components.  Pass in either root or the frame in which you
    need the new frame associated.
These are classes, so we need to make objects from those classes.  Thus: frame1
'''
# create a frame widget.
frame1 = tk.Frame(root, width=500, height=600, bg="#3d6466")
frame1.grid(row = 0, column = 0)
# Setting propoage to false prevents from the children from pack_propagatting
# "upward" to the other elements.
frame1.pack_propagate(False)

# frame1 widgets
logo_img = ImageTk.PhotoImage(file="assets/RRecipe_logo.png")
logo_widget = tk.Label(frame1, image=logo_img, bg="#3d6466")
# Seems like a weakness in Tkinter to require "double setting" to get a value
## to equal another value.
logo_widget.image = logo_img
logo_widget.pack()

# run app
root.mainloop()