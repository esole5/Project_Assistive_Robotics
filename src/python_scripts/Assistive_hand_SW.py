import os
import time
import tkinter as tk
from tkinter import messagebox
from robodk.robolink import *
from robodk.robomath import *

# Define relative path to the .rdk file
relative_path = "src/roboDK/Assistive_UR5e.rdk"
absolute_path = os.path.abspath(relative_path)

# Start RoboDK with the project file
RDK = Robolink()
RDK.AddFile(absolute_path)

# Retrieve items from the RoboDK station
robot = RDK.Item("UR5e")
base = RDK.Item("UR5e Base")
tool = RDK.Item("Hand")
Init_target = RDK.Item("Init")
Control_1_target = RDK.Item('Control_1')
Pick_target = RDK.Item('Pick')
Control_2_target = RDK.Item('Control_2')
Show_target = RDK.Item('Show')

# Set robot frame, tool and speed
robot.setPoseFrame(base)
robot.setPoseTool(tool)
robot.setSpeed(20)

# Move to initial position
def Init():
    print("Init")
    robot.setSpeed(100)
    robot.MoveJ(Init_target, True)
    print("Init_target REACHED")

# Move to pick up the object
def Pick_object():
    print("")
    robot.setSpeed(100)
    robot.MoveL(Control_1_target, True)
    robot.setSpeed(25)
    robot.MoveL(Pick_target, True)
    # Petit stop per agafar l'objecte
    time.sleep(1)
    robot.setSpeed(80)
    robot.MoveL(Control_1_target, True)
    print("An object has been picked!")

# Move to show the object to the surgeon 
def Show_object():
    robot.setSpeed(100)
    robot.MoveL(Control_2_target, True)
    robot.setSpeed(100)
    robot.MoveL(Show_target, True)
    #stop per ensenyar l'eina al metge
    time.sleep(2)
    print("The object has been gived, FINISHED")

# Main sequence
def main():
    Init()
    Pick_object()
    Show_object()
    Init()

# Confirmation dialog to close RoboDK
def confirm_close():
    root = tk.Tk()
    root.withdraw()
    response = messagebox.askquestion(
        "Close RoboDK",
        "Do you want to save changes before closing RoboDK?",
        icon='question'
    )
    if response == 'yes':
        RDK.Save()
        RDK.CloseRoboDK()
        print("RoboDK saved and closed.")
    else:
        RDK.CloseRoboDK()
        print("RoboDK closed without saving.")

        # Confirmation dialog to close RoboDK

# Run main and handle closing
if __name__ == "__main__":
    main()
    #confirm_close()
