import tkinter as tk

HEIGHT = 500
WIDTH = 600

#depth = input("Enter desired depth in meters (1 - 42):")
def get_time(depth):
    try:
        maxTime = [219, 219 , 219 ,219, 219, 219 , 219 ,219, 219, 219 , 147, 147, 98, 98, 72, 72, 56, 56, 45, 45, 37, 37, 29, 29,29,20,20,20,20,20,14,14,14,14,14,9,9,9,9,9,8,8]
        time = maxTime[int(depth) -1]
    except:
        print("depth not avalible")
        
    countdown(time*60)

def countdown(count):
    # change text in label
    label['text'] = count

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Max time for Depth", font=40, command=lambda: get_time(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)




root.mainloop()
