import tkinter as tk

HEIGHT = 200
WIDTH = 600



def get_time(depth):
    if int(depth) < 0 or int(depth) > 42:
        instruction['text'] = "depth not avalible"
    elif int(depth) < 30 and int(depth) > 0:
        instruction['text'] = " A safety stop for 3 to 5 minutes at 5 metres is recommended"
    else:
        instruction['text'] = " A safety stop for 3 to 5 minutes at 5 metres is required"
    try:
        maxTime = [219, 219 , 219 ,219, 219, 219 , 219 ,219, 219, 219 , 147, 147, 98, 98, 72, 72, 56, 56, 45, 45, 37, 37, 29, 29,29,20,20,20,20,20,14,14,14,14,14,9,9,9,9,9,8,8]
        time = maxTime[int(depth) -1]
    except:
        print("error")
        
    count = time*60
    set_count = count
    countdown(count)

def humanize_time(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    return '%02d:%02d:%02d' % (hours, mins, secs)

def countdown(count):
    # change text in label
    label['text'] = humanize_time(count)

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)

def reset_time():
    count = set_count

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.3, anchor='n')

entry = tk.Entry(frame)
entry.place(relwidth=0.3, relheight=1)

start_button = tk.Button(frame, text="Start", command=lambda: get_time(entry.get()))
start_button.place(relx=0.5, relheight=1, relwidth=0.4)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.45, relwidth=0.8, relheight=0.3, anchor='n')

label = tk.Label(lower_frame)
label.place(rely=0.5,relwidth=1, relheight=0.5)

instruction = tk.Label(lower_frame, text="input depth in meter to start timer countdown")
instruction.place(relwidth=1, relheight=0.5)



root.mainloop()
