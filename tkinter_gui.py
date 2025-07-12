import tkinter as tk
import random
import string


def password_generator(
    length=12,
    uppercase=True,
    lowercase=True,
    digits=True,
    special_chars=True,
) -> str | None:
    characters = ""

    if uppercase:
        characters += string.ascii_uppercase

    if lowercase:
        characters += string.ascii_lowercase

    if digits:
        characters += string.digits

    if special_chars:
        characters += string.punctuation

    if not characters:
        print("Error: At least one character type must be selected")
        return None

    password = "".join(
        random.choice(characters) for _ in range(length)
    )  # list comprehension

    # enable text widget for editing
    result_text.config(state="normal")

    # clear previous content
    result_text.delete("1.0", tk.END)

    # insert new text:
    result_text.insert(tk.END, password)

    # disable text widget again to make it read only
    result_text.config(state="disabled")


def start():
    # retrieve text from the entry field
    length_password = int(length_entry.get())

    # retrieve the state of the checkbox
    password_generator(
        length=length_password,
        uppercase=checkbox_uppercase_var.get(),
        lowercase=checkbox_lowercase_var.get(),
        digits=checkbox_digits_var.get(),
        special_chars=checkbox_special_chars_var.get(),
    )


# create the main window
root = tk.Tk()
root.title("Password Generator")


# set initial size
def center_window(window, width=400, height=300):
    sreen_width = window.winfo_screenwidth() # lấy kích thước màn hình
    screen_height = window.winfo_screenheight()
    x = (sreen_width - width) // 2
    y = (screen_height - height) // 2
    # x, y là tọa độ góc trên bên trái của cửa sổ → tính sao cho nằm giữa màn hình
    window.geometry(f"{width}x{height}+{x}+{y}")


# Gọi hàm căn giữa
center_window(root)

# widgets

# label for entry field
length_lable = tk.Label(root, text="Enter the password's length")
length_lable.pack()

# entry field for user input
length_entry = tk.Entry(root)
length_entry.pack()

# button
button = tk.Button(root, text="Generate", command=start)
button.pack()

# checkbox uppercase
checkbox_uppercase_var = tk.BooleanVar(value=False)
checkbox_uppercase = tk.Checkbutton(
    root, text="Include uppercase letters", variable=checkbox_uppercase_var
)
checkbox_uppercase.pack()

# checkbox lowcase
checkbox_lowercase_var = tk.BooleanVar(value=False)
checkbox_lowercase = tk.Checkbutton(
    root, text="Include lowercase letters", variable=checkbox_lowercase_var
)
checkbox_lowercase.pack()

# checkbox digits
checkbox_digits_var = tk.BooleanVar(value=False)
checkbox_digits = tk.Checkbutton(
    root, text="Include digits letters", variable=checkbox_digits_var
)
checkbox_digits.pack()

# checkbox special characters
checkbox_special_chars_var = tk.BooleanVar(value=False)
checkbox_special_chars = tk.Checkbutton(
    root, text="Include special characters", variable=checkbox_special_chars_var
)
checkbox_special_chars.pack()

# test widget
result_text = tk.Text(root, wrap="word", height=5, state="disabled")
result_text.pack()

# run application
root.mainloop()
