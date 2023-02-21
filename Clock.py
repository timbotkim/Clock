# importing whole module
from tkinter import Label, Tk 
# retrieve system's time
import time

# introduce Tk() to app window, define app title and geometry
app_window = Tk() 
app_window.title("Digital Clock") 
app_window.geometry("420x150") 
app_window.resizable(1,1)

# specify font 
text_font= ("Times New Roman", 68, 'bold')
background = "#004225"
foreground= "#C4A484"
border_width = 25

# add labels to app window
label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

# add clock definition and introduce format
def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, digital_clock)

digital_clock()
app_window.mainloop()
