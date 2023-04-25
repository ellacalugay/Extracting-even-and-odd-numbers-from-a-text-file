# Ella Lureen C. Calugay | BSCPE 1-5 | Assignment #4 | PROBLEM 1
# Creating a program that reads a txt file then extract the even and odd numbers then place it in a two additional text files: "even.txt" with even numbers, and "odd.txt" with odd numbers.

#Pseudocode
# Import the necessary module 
import tkinter as tk

# Create a tkinter window
root = tk.Tk()
root.title("PROBLEM 1")

# Open the file "numbers.txt" for reading.
with open ("numbers.txt", "r") as numbers:

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
    else:
        odds.append(num)

# If the number is even, add it to the list of even numbers (even.txt).
with open("even.txt", "w") as even:
    for num in evens:
        even.write(str(num) + '\n')

# If the number is odd, add it to the list of odd numbers (odd.txt).
with open("odd.txt", "w") as odd:
    for num in odds:
        odd.write(str(num) + '\n') 
        
# End of the code.
