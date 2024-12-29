import tkinter as tk
from tkinter import messagebox
from sympy import symbols, Eq, solve
from owlready2 import get_ontology

# Load the OWL ontology
ontology_path = r"C:\Users\Asus\Desktop\AI_ITS_Assignment\Ontology_file\AlgOntology.owl"
ontology = get_ontology(ontology_path).load()

class AddItem:
    def __init__(self, root):
        self.root = root  # main window
        self.root.title("Algebra Tutor")  # window title
        self.root.geometry("600x400")  # the size
        self.root.minsize(400, 300)  # minimum size
        self.root.resizable(True, True)  # resizing the window
        self.root.configure(background="Silver")  # background color

        # Grid layout configuration
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # input instruction for user
        self.asas = tk.Label(
            root, text="Enter a Single Algebra Equation (e.g., 23x + 4 + y = 2):",
            font=("Arial", 16), anchor="center", background="Silver"
        )
        self.asas.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

        # input field equation
        self.equation_entry = tk.Entry(root, font=("Arial", 14))
        self.equation_entry.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=10)

        # solve button
        self.solve_button = tk.Button(
            root, text="Solve", command=self.solve_equation, font=("Arial", 18), bg="green", fg="white"
        )
        self.solve_button.grid(row=2, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        self.solve_button.bind("<Configure>", self.adjust_button_width)  # Adjust button width on resize

        # Label displaying the result
        self.result_label = tk.Label(root, text="", font=("Arial", 12), wraplength=500, justify="left", anchor="nw")
        self.result_label.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)

    # Adjust button
    def adjust_button_width(self, event):
        self.solve_button.config(width=self.root.winfo_width() // 2)

    # Function to solvation
    def solve_equation(self):
        equation = self.equation_entry.get().strip()  # Get the equation from the input field
        if not equation:  # Check if the equation is empty
            messagebox.showerror("Error", "Please Enter an Algebra Equation.")  # Show error if no equation
            return
        question = ontology.search_one(iri="*Equation1")

        x, y = symbols("x y")  # define variables for solving

        try:
            # split equation
            left, right = equation.split("=")
            eq = Eq(eval(left), eval(right))  # create the sympy equation

            # solve the equations for both x and y
            solutions_x = solve(eq, x)
            solutions_y = solve(eq, y)

            # display the solution
            solution_text = f"Solutions:\n"
            if solutions_x:
                solution_text += f"x = {solutions_x}\n"
            if solutions_y:
                solution_text += f"y = {solutions_y}\n"

            self.result_label.config(text=solution_text)  # lable for update result
            messagebox.showinfo("Solution", solution_text)  # showing solution

        except Exception as e:  # handle errors
            messagebox.showerror("Error", f"Invalid input or equation format. Error: {e}")


# start application
if True:
    root = tk.Tk()  # create the main window
    app = AddItem(root)  # initialize app with root window
    root.mainloop()  # start tkinter event loop
