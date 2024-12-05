import tkinter as tk
from PIL import Image, ImageTk

# Application Title and Details
print("Welcome to the Learn English Letters in Sign Language application!")
print("Developers: [Team Member Names]")
print("Description: This application helps you learn English letters using sign language.")

# List of English letters
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']

# Dictionary containing the sign language (image) for each letter
sign_language = {
    'A': 'imgs\\image_a.jpg',
    'B': 'imgs\\image_b.jpg',
    'C': 'imgs\\image_c.png',
    'D': 'imgs\\image_d.png',
    'E': 'imgs\\image_e.png',
    'F': 'imgs\\image_f.jpg',
    'G': 'imgs\\image_g.jpg',
    'H': 'imgs\\image_h.jpg',
    'I': 'imgs\\image_i.jpg',
    'J': 'imgs\\image_j.jpg',
    'K': 'imgs\\image_k.jpg',
    'L': 'imgs\\image_l.jpg',
    'M': 'imgs\\image_m.jpg',
    'N': 'imgs\\image_n.jpg',
    'O': 'imgs\\image_o.jpg',
    'P': 'imgs\\image_p.jpg',
    'Q': 'imgs\\image_q.jpg',
    'R': 'imgs\\image_r.jpg',
    'S': 'imgs\\image_s.jpg',
    'T': 'imgs\\image_t.jpg',
    'U': 'imgs\\image_u.jpg',
    'V': 'imgs\\image_v.jpg',
    'W': 'imgs\\image_w.jpg',
    'X': 'imgs\\image_x.jpg',
    'Y': 'imgs\\image_y.jpg',
    'Z': 'imgs\\image_z.jpg',
}


# User class to track user's progress in learning letters
class User:
    def __init__(self, name):
        self.name = name
        self.learned_letters = []

    def learn_letter(self, letter):
        """Learn a new letter and add it to the list of learned letters."""
        if letter not in self.learned_letters:
            self.learned_letters.append(letter)
            print(f"Letter {letter} learned.")
        else:
            print(f"You've already learned the letter {letter}.")

    def show_progress(self):
        """Display the learned letters of the user."""
        print(f"{self.name}'s Progress:")
        for letter in self.learned_letters:
            print(f"Letter {letter} learned.")


# User-defined Functions
def show_letter_sign(letter, image_label):
    """Display the sign language for the letter (using an image)."""
    # Load and display the image for the corresponding letter
    img_path = sign_language[letter]
    try:
        img = Image.open(img_path)
        img = img.resize((200, 200))  # Resize to fit the window
        img = ImageTk.PhotoImage(img)
        image_label.config(image=img)
        image_label.image = img
        print(f"Sign language for letter {letter}: {img_path}")
    except FileNotFoundError:
        print(f"Image for letter {letter} not found at {img_path}")


# GUI (Graphical User Interface) using Tkinter
root = tk.Tk()
root.title("Learn English Letters in Sign Language")
root.geometry("491x700")  # Increased window size
root.configure(bg='#f0f0f0')  # Light gray background

# Label to welcome the user
label = tk.Label(root, text="Learn English Letters in Sign Language",
                 font=('Helvetica', 16, 'bold'),
                 bg='#f0f0f0')
label.grid(row=0, column=0, columnspan=7, pady=20)

# Label to display the sign language image
image_label = tk.Label(root, bg='#f0f0f0')
image_label.grid(row=1, column=0, columnspan=7, pady=10)


# Function to handle button clicks to show letter signs
def on_button_click(letter):
    show_letter_sign(letter, image_label)
    result_label.config(text=f"Displayed sign language for letter: {letter}")


# Create letter buttons in a grid layout
def create_letter_buttons():
    for i, letter in enumerate(letters):
        # Calculate row and column
        row = 2 + (i // 7)  # Start from row 2, move to next row every 7 letters
        col = i % 7

        # Create button with enhanced styling
        button = tk.Button(root,
                           text=letter,
                           width=5,
                           height=2,
                           font=('Helvetica', 12, 'bold'),
                           bg='#4CAF50',  # Green background
                           fg='white',  # White text
                           activebackground='#45a049',  # Slightly darker green when pressed
                           relief=tk.RAISED,  # 3D raised effect
                           command=lambda l=letter: on_button_click(l))
        button.grid(row=row, column=col, padx=5, pady=5)


# Create letter buttons
create_letter_buttons()

# Label to display quiz results
result_label = tk.Label(root,
                        text="Quiz result will appear here.",
                        font=('Helvetica', 10),
                        bg='#f0f0f0')
result_label.grid(row=6, column=0, columnspan=7, pady=10)

# Create a global user object
user = User("Ahmed")  # Initialize user object once


# Button to start the quiz
def start_quiz():
    quiz_window = tk.Toplevel(root)
    quiz_window.title("Start Quiz")
    quiz_window.geometry("300x200")
    quiz_window.configure(bg='#f0f0f0')

    label = tk.Label(quiz_window,
                     text="Choose a letter from A-Z:",
                     font=('Helvetica', 12),
                     bg='#f0f0f0')
    label.pack(pady=10)

    entry = tk.Entry(quiz_window,
                     font=('Helvetica', 12),
                     justify='center')
    entry.pack(pady=10)

    def submit():
        letter = entry.get().upper()
        if letter in letters:
            user.learn_letter(letter)
            show_letter_sign(letter, image_label)
        else:
            print("This is not a valid letter. Try again!")
        quiz_window.destroy()

    submit_button = tk.Button(quiz_window,
                              text="Submit",
                              font=('Helvetica', 12, 'bold'),
                              bg='#2196F3',  # Blue background
                              fg='white',  # White text
                              command=submit)
    submit_button.pack(pady=10)


# Quiz button
quiz_button = tk.Button(root,
                        text="Start Quiz",
                        font=('Helvetica', 12, 'bold'),
                        bg='#2196F3',  # Blue background
                        fg='white',  # White text
                        width=10,
                        command=start_quiz)
quiz_button.grid(row=7, column=2, columnspan=3, pady=10)


# Button to show user progress
def progress():
    user.show_progress()


progress_button = tk.Button(root,
                            text="Show Progress",
                            font=('Helvetica', 12, 'bold'),
                            bg='#FF9800',  # Orange background
                            fg='white',  # White text
                            width=15,
                            command=progress)
progress_button.grid(row=8, column=2, columnspan=3, pady=10)

# Run the application
if __name__ == '__main__':
    root.mainloop()