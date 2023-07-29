import random
import string
import tkinter as tk

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_and_display_password():
    # Get user inputs
    user_name = username_entry.get()
    password_length = int(password_length_entry.get())

    # Generate a random password of the specified length
    password = generate_password(password_length)
    
    # Display the generated password
    output_label.config(text=f"Password: {password}", bg="lightblue", fg="black")

    # Configure the accept button to display username and password when clicked
    accept_button.config(command=lambda: show_output(user_name, password), bg="green", fg="white")
    
    # Configure the reject button to generate a new password when clicked
    reject_button.config(command=generate_new_password, bg="red", fg="white")

    # Show the accept and reject buttons
    accept_button.pack(pady=10)
    reject_button.pack(pady=10)

def show_output(user_name, password):
    # Display the username and password
    output_label.config(text=f"Username: {user_name}\nPassword: {password}", bg="lightgreen", fg="black")

    # Hide the accept and reject buttons after accepting the password
    accept_button.pack_forget()
    reject_button.pack_forget()

def generate_new_password():
    # Generate a new password when the user rejects the previous one
    password_length = int(password_length_entry.get())
    password = generate_password(password_length)
    
    # Display the new password
    output_label.config(text=f"New password: {password}", bg="lightblue", fg="black")

    # Show the accept and reject buttons for the new password
    accept_button.config(bg="green", fg="white")
    reject_button.config(bg="red", fg="white")
    accept_button.pack(pady=10)
    reject_button.pack(pady=10)

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x500")

# Username input
username_label = tk.Label(root, text="Enter User Name:", font=("Comic Sans MS", 14))
username_label.pack(pady=10)
username_entry = tk.Entry(root, font=("Comic Sans MS", 14))
username_entry.pack(pady=10)

# Password length input
password_length_label = tk.Label(root, text="Enter Password Length:", font=("Comic Sans MS", 14))
password_length_label.pack(pady=10)
password_length_entry = tk.Entry(root, font=("Comic Sans MS", 14))
password_length_entry.pack(pady=10)

# Generate password button
generate_button = tk.Button(root, text="Generate Password", font=("Comic Sans MS", 14), command=generate_and_display_password, bg="blue", fg="white")
generate_button.pack(pady=10)

# Output label
output_label = tk.Label(root, text="", font=("Comic Sans MS", 14), wraplength=300)
output_label.pack(pady=10)

# Accept and Reject buttons
accept_button = tk.Button(root, text="Accept Password", font=("Comic Sans MS", 14))
reject_button = tk.Button(root, text="Reject Password", font=("Comic Sans MS", 14))

root.mainloop()