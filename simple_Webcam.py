# demo

import tkinter as tk
import cv2
import pyttsx3
from tkinter import filedialog

engine = pyttsx3.init()

def take_picture():
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    cv2.imshow("picture", frame)
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
    cv2.imwrite(file_path, frame)
    camera.release()
    engine.say("picture taken")
    engine.runAndWait()


def on_speak():
    engine.say("Say Cheese")
    engine.runAndWait()
    take_picture()

root = tk.Tk()
root.geometry("200x200")

speak_button = tk.Button(root, text="Speak", command=on_speak)
speak_button.pack()

root.mainloop()
