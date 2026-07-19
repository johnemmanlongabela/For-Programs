import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row = len(button_values) #5
column = len(button_values[0]) #4
color_light_gray = "#00FF00"
color_black = "#000000"
color_dark_gray = "#FF0000"
color_orange = "#FF8C00"
color_white = "#FFFFFF"

#Window setup
window = tkinter.Tk()
window.title("Simple Calculator")
window.resizable(width=False, height=False)
window.mainloop()