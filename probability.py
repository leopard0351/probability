import tkinter as tk
from tkinter import font as tkFont
from math import factorial

def calculate_probability():
    try:
        n = int(entry_n.get())
        x = int(entry_x.get())
        p = float(entry_p.get())
        q = 1 - p
       

        # Validate input values
        if not (0 <= p <= 1 and 0 <= q <= 1):
            result_label.config(text="Error: P and Q must be between 0 and 1")
            return
        if p > 1:
            result_label.config(text="Error: P must be 1 or less")
            return
        if not (0 <= x <= n):
            result_label.config(text="Error: X must be between 0 and N")
            return
     

        # Calculate exact probability
        binom_coeff_exact = factorial(n) / (factorial(x) * factorial(n - x))
        probability_exact = binom_coeff_exact * (p ** x) * (q ** (n - x))

        # Calculate probability of at least X successes
        probability_at_least_x = sum(factorial(n) / (factorial(i) * factorial(n - i)) * (p ** i) * (q ** (n - i)) for i in range(x, n + 1))

        result_label.config(text=f"Exact Probability: {probability_exact:.5f}\nProbability of at least {x} successes: {probability_at_least_x:.5f}")
    except ValueError:
        result_label.config(text="Invalid input")

# Setting up the window
window = tk.Tk()
window.title("Probability Calculator")
window.geometry('400x300')  # Width x Height

# Font styling
default_font = tkFont.Font(family="Helvetica", size=12)

# Creating labels
label_n = tk.Label(window, text="N (Number of Trials):", font=default_font)
label_x = tk.Label(window, text="X (Number of Successes):", font=default_font)
label_p = tk.Label(window, text="P (Probability of Success):", font=default_font)



# Creating input widgets
entry_n = tk.Entry(window, font=default_font)
entry_x = tk.Entry(window, font=default_font)
entry_p = tk.Entry(window, font=default_font)

calculate_button = tk.Button(window, text="Calculate", command=calculate_probability, font=default_font)
result_label = tk.Label(window, text="Probability: ", font=default_font)


label_n.pack(anchor='w', padx=10)
entry_n.pack(anchor='center', pady=5)
label_x.pack(anchor='w', padx=10)
entry_x.pack(anchor='center', pady=5)
label_p.pack(anchor='w', padx=10)
entry_p.pack(anchor='center', pady=5)

# Adding widgets to the window
entry_n.pack(anchor='center', pady=5)
entry_x.pack(anchor='center', pady=5)
entry_p.pack(anchor='center', pady=5)

calculate_button.pack(anchor='center', pady=5)
result_label.pack(anchor='center', pady=5)

# Running the application
window.mainloop()