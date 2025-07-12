import tkinter as tk
import datetime

# Path to the icon image
icon_path = "images/icon-py.ico"

# create main window
root = tk.Tk()
root.title("Milestone monitor")
root.configure(bg="#d8f3dc")
root.iconbitmap(icon_path)

def center_screen(window, width=1800, height=350):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


center_screen(root)

# Get today's day
today = datetime.date.today()

# get the original day of the year
day_of_year = today.timetuple().tm_yday

# progress stages colors
progress_stages = ["#b7efc5", "#6ede8a", "#25a244", "#1a7431", "#04771c"]

# month names
months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "July",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]

# list to hold button
buttons = []


# function create a row of buttons for a week
def create_row(week):
    # display month labels
    for i in range(0, 12):
        month = tk.Label(root, text=months[i], font=("Helvetica", 10), bg="#d8f3dc")
        month.grid(row=0, column=(1 + i) * 4, padx=2, pady=2)

    # buttons each day of the week
    for i in range(1, 8):
        color_btn = tk.Button(root, bg="#ffffff", width=1, height=0)
        color_btn.bind("<Button-1>", change_btn_color)
        color_btn.grid(row=i, column=week, padx=6, pady=2)
        buttons.append(color_btn)


# function change the color of a button
def change_btn_color(event):
    # get button widget and current background color
    btn = event.widget
    bg_color = btn.cget("background")
    # Iterate through the progess stages
    for idx, item in enumerate(progress_stages):
        # Change color if current color matches and index is within range
        if bg_color == item and idx < 4:
            btn.configure(bg=progress_stages[idx + 1])
            break
        # set color to first stage if not found in progress stages
        if bg_color not in progress_stages:
            btn.configure(bg=progress_stages[0])
            break


def save_btns():
    with open("buttons_data.txt", "w") as file:
        for btn in buttons:
            bg_color = btn.cget("background")
            file.write(bg_color + "\n")
        root.destroy()


# function to load buttons colors from file
def load_buttons():
    colors = []
    try:
        with open("buttons_data.txt", "r") as file:
            for line in file:
                bg_color = line.strip()
                colors.append(bg_color)
            return colors
    except FileNotFoundError:
        pass  # do nothing if the file is not found
    return colors


# variable to track edit node
edit = False


# function to toggle edit node
def button_edit_on_off():
    global edit
    btn_idx = 0
    if not edit:
        # Enable edit node
        for b in buttons:
            if btn_idx == day_of_year:
                btn_idx += 1
                bg_color = b.cget("background")
                if bg_color in progress_stages:
                    pass
                else:
                    b.configure(bg="#252422")
            else:
                b.configure(state="disabled")
                b.unbind("<Button-1>")
                btn_idx += 1
        edit = True  # Update edit node
    else:
        # disable edit node
        for b in buttons:
            b.configure(state="disabled")
            b.bind("<Button-1>", change_btn_color)
        edit = False


# create rows of buttons
for i in range(1, 52):
    create_row(i)

# loop existing button colors from file
existing_colors = load_buttons()
# Apply existing colors to buttons
for btn, colors in zip(buttons, existing_colors):
    btn.configure(bg=colors)

# toggle edit mode
button_edit_on_off()

# display labels for progress stages
label_less = tk.Label(root, text="Less", font=("Helvetica", 12), bg="#d8f3dc")
label_less.grid(row=10, column=0, padx=2, pady=2)

for idx, stage_color in enumerate(progress_stages):
    example_color = tk.Button(root, state="disabled", bg=stage_color, width=1, height=0)
    example_color.grid(row=10, column=idx + 1, padx=2, pady=2)


# Button to exit and save
exit_btn = tk.Button(root, command=save_btns, text="Exit and Save", bg="#f07167")
exit_btn.grid(row=9, column=54, padx=6, pady=2)

# button to toggle edit node
edit_btn = tk.Button(root, command=button_edit_on_off, text="Edit", bg="#f07167")
edit_btn.grid(row=9, column=53, padx=6, pady=2)

# run the application
root.mainloop()
