# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #4 | PROBLEM 1
# Creating a program that reads a txt file then extract the even and odd numbers then place it in a two additional text files: "even.txt" with even numbers, and "odd.txt" with odd numbers.

#Pseudocode
# Import the necessary module 
import tkinter as tk

# Create a tkinter window
root = tk.Tk()
root.title("PROBLEM 1")

# Create a frame for the output
frame = tk.Frame(root, bd=2, relief="groove")
frame.pack(padx=10, pady=10)

# Create labels for the output files with border and border color
even_label = tk.Label(frame, text="Even Numbers", font=("Arial", 12, "bold"), bg="yellow", bd=2, relief="groove")
even_label.grid(row=0, column=0, padx=10)

odd_label = tk.Label(frame, text="Odd Numbers", font=("Arial", 12, "bold"), bg="red", bd=2, relief="groove")
odd_label.grid(row=0, column=1, padx=10)

# Add a border to the top of the output
top_border = tk.Frame(frame, bg="blue", height=2, width=300)
top_border.grid(row=1, columnspan=2, pady=(10,0))

# Open the file named numbers.txt for reading, even.xt for write and odd.txt for write
with open ("numbers.txt", "r") as numbers, open("even.txt", "w") as even_file, open("odd.txt", "w") as odd_file:

# Read the contents of the file into a list of strings.
    all_numbers = numbers.readlines()

# Create two new empty lists to store even and odd numbers.
    evens = []
    odds = []

    # Loop through the file "numbers.txt" and check each number.
    for num in all_numbers:
        # Convert the string to an integer.
        num = int(num.strip())
        # Check if the number is even or odd and add it to the corresponding list.
        if num % 2 == 0:
            evens.append(num)
            even_file.write(str(num) + "\n")
        else:
            odds.append(num)
            odd_file.write(str(num) + "\n")

    # Define a function to load and display even numbers from a text file
    def load_evens():
        clear_output()
        # Open the "even.txt" file in read mode
        with open("even.txt", "r") as even_file:
            # Read the contents of the file and store them in a list
            evens = even_file.readlines()
            # Iterate over the even numbers in the list
            for idx, even in enumerate(evens):
                # Create a Tkinter label for each even number
                even_label = tk.Label(frame, text=even, bg="magenta")
                # Add the label to the frame at the appropriate row and column
                even_label.grid(row=idx+3, column=0)

    # Define a function to load and display odd numbers from a text file
    def load_odds():
        clear_output()
        # Open the "odd.txt" file in read mode
        with open("odd.txt", "r") as odd_file:
            # Read the contents of the file and store them in a list
            odds = odd_file.readlines()
            # Iterate over the odd numbers in the list
            for idx, odd in enumerate(odds):
                # Create a Tkinter label for each odd number
                odd_label = tk.Label(frame, text=odd, bg="magenta")
                # Add the label to the frame at the appropriate row and column
                odd_label.grid(row=idx+3, column=1)
    
    # Define a function to load and display either even or odd numbers based on the selected mode
    def load_output():
        # Check the value of the mode variable to determine which function to call
        if mode.get() == "Even Numbers":
            # If "Even Numbers" is selected, call the load_evens() function
            load_evens()
        else:
            # Otherwise, call the load_odds() function
            load_odds()

    # Define a function to close the GUI and terminate the program
    def load_close():
        # Loop over all the children of the frame
        for bye in frame.winfo_children():
            # Check if the child is not one of the three specific widgets
            if bye != top_border and bye != even_label and bye != odd_label:
                # If it's not one of the specific widgets, destroy it
                bye.destroy()       
        # Close the root window, terminating the program
        root.destroy()
    
    # Define a function to clear all the widgets from the frame except for the top border and even/odd labels
    def clear_output():
        # Loop over all the children of the frame
        for child in frame.winfo_children():
            # Check if the child is not one of the three specific widgets
            if child != top_border and child != even_label and child != odd_label:
                # If it's not one of the specific widgets, destroy it
                child.destroy()

# End of the code.
