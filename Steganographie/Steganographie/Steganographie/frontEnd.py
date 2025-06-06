import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np
from PIL import Image

# Colors
BG_COLOR = "#1A1A2E"
BUTTON_COLOR = "#E94560"
TEXT_COLOR = "#FFFFFF"
HOVER_COLOR = "#0F3460"

# main Tkinter window
root = tk.Tk()
root.title("Steganography ")
root.geometry("500x400")
root.config(bg=BG_COLOR)



#Moving text

moving_text = tk.Label(root, text="🔥 Venera Software 🔥", font=("Arial", 16, "bold"), fg="#E94560", bg="#1A1A2E")
moving_text.place(x=10, y=350)  # Move text closer to the bottom

# Function to move text horizontally
def move_text():
    x = moving_text.winfo_x()
    if x < 400:  # Move right until reaching the edge
        moving_text.place(x=x+5, y=350)  # Keep the same Y position (bottom)
    else:
        moving_text.place(x=10, y=350)  # Reset position
    root.after(100, move_text)  # Call function again after 100ms

# Start animation
move_text()


btn_exit = tk.Button(root, text="Quitter ❌", font=("Arial", 12, "bold"), bg="red", fg="white", command=root.quit)
btn_exit.pack(pady=20)



# Function to hide message inside image
def hide_message():
    msg = entry_message.get()
    image_path = filedialog.askopenfilename(title="Select Image")

    if not msg or not image_path:
        messagebox.showerror("Error", "Please enter a message and select an image.")
        return

    image = Image.open(image_path)
    data = np.asarray(image).copy()

    # Convert message to binary
    final_msg = "".join([bin(ord(char))[2:].zfill(8) for char in msg])

    # Encode message length
    msg_length = bin(len(final_msg))[2:].zfill(16)
    result_message = msg_length + final_msg

    # Modify image pixels
    tour = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            for rgb in range(3):  # Iterate over RGB channels
                if tour < len(result_message):
                    binary_pixel = list(bin(data[y][x][rgb])[2:].zfill(8))
                    binary_pixel[-1] = result_message[tour]  # Replace LSB
                    data[y, x, rgb] = int("".join(binary_pixel), 2)
                    tour += 1

    # Save modified image
    saved_path = "SECRET.png"
    Image.fromarray(data).save(saved_path)
    messagebox.showinfo("Success", f"Hidden message saved inside {saved_path}!")

# Function to extract message
def discover_message():
    image_path = filedialog.askopenfilename(title="Select Image")

    if not image_path:
        messagebox.showerror("Error", "Please select an image to decode.")
        return

    image = Image.open(image_path)
    data = np.asarray(image).copy()

    # Extract message length
    tour = 0
    msg_length_bin = ""
    message_bin = ""

    for y in range(len(data)):
        for x in range(len(data[y])):
            for rgb in range(3):
                if tour < 16:
                    msg_length_bin += bin(data[y][x][rgb])[2:].zfill(8)[-1]
                elif tour < 16 + int(msg_length_bin, 2):
                    message_bin += bin(data[y][x][rgb])[2:].zfill(8)[-1]
                tour += 1

    # Convert binary message back to text
    message_chars = [message_bin[i:i+8] for i in range(0, len(message_bin), 8)]
    result_message = "".join([chr(int(char, 2)) for char in message_chars])

    # Save extracted message
    with open("Hidden_Message.txt", "w", encoding="utf-8") as file:
        file.write(result_message)

    messagebox.showinfo("Decoded", f"Hidden Message:\n{result_message}")

# Hover effect function
def on_hover(button, color):
    button.config(bg=color)
def off_hover(button, color):
    button.config(bg=color)

                                            # UI Components

tk.Label(root, text="Enter Message to Hide:", fg=TEXT_COLOR, bg=BG_COLOR, font=("Arial", 12, "bold")).pack(pady=5)
entry_message = tk.Entry(root, width=40, font=("Arial", 12))
entry_message.pack(pady=5)

btn_hide = tk.Button(root, text="Hide Message ", font=("Arial", 12, "bold"), bg=BUTTON_COLOR, fg=TEXT_COLOR, command=hide_message)
btn_hide.pack(pady=10)
btn_hide.bind("<Enter>", lambda e: on_hover(btn_hide, HOVER_COLOR))
btn_hide.bind("<Leave>", lambda e: off_hover(btn_hide, BUTTON_COLOR))

btn_discover = tk.Button(root, text="Discover Message", font=("Arial", 12, "bold"), bg=BUTTON_COLOR, fg=TEXT_COLOR, command=discover_message)
btn_discover.pack(pady=10)
btn_discover.bind("<Enter>", lambda e: on_hover(btn_discover, HOVER_COLOR))
btn_discover.bind("<Leave>", lambda e: off_hover(btn_discover, BUTTON_COLOR))


root.mainloop()