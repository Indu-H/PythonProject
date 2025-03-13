import tkinter as tk
from tkinter import messagebox, simpledialog

class EmployeeRelocationAssistant:
    def __init__(self, root):
        self.housing_options = [
            {"rent": 1500, "location": "City Center"},
            {"rent": 1200, "location": "Suburbs"},
            {"rent": 1000, "location": "Downtown"}
        ]
        self.routes = [
            {"route_name": "Highway Route", "cost": 50, "time": 30},
            {"route_name": "Scenic Route", "cost": 40, "time": 45},
            {"route_name": "Express Route", "cost": 60, "time": 25}
        ]
        self.employee_preferences = {}
        self.root = root
        self.root.title("Employee Relocation Assistant")
        self.create_widgets()
    
    def create_widgets(self):
        options = [
            ("Match Housing", self.match_housing),
            ("Optimize Route", self.optimize_relocation_route),
            ("Update Housing", self.update_housing),
            ("Delete Housing", self.delete_housing),
            ("Update Route", self.update_route),
            ("Delete Route", self.delete_route),
            ("Display Housing", self.display_housing),
            ("Display Routes", self.display_routes),
            ("Exit", self.root.quit)
        ]
        
        for text, command in options:
            tk.Button(self.root, text=text, command=command, width=20).pack(pady=5)
    
    def match_housing(self):
        emp_id = simpledialog.askinteger("Input", "Enter Employee ID:")
        budget = simpledialog.askinteger("Input", "Enter Budget:")
        location = simpledialog.askstring("Input", "Enter Preferred Location:")
        
        if emp_id is not None and budget is not None and location:
            self.employee_preferences[emp_id] = {"budget": budget, "location": location}
            suitable_houses = [h for h in self.housing_options if h["rent"] <= budget and h["location"] == location]
            result = min(suitable_houses, key=lambda x: x['rent'], default="No suitable housing found")
            messagebox.showinfo("Recommended Housing", str(result))
    
    def optimize_relocation_route(self):
        if not self.routes:
            messagebox.showinfo("Best Route", "No routes available")
        else:
            best_route = min(self.routes, key=lambda x: (x['cost'], x['time']), default="No suitable route found")
            messagebox.showinfo("Best Route", str(best_route))
    
    def update_housing(self):
        index = simpledialog.askinteger("Input", "Enter housing index to update:")
        if index is not None and 0 <= index < len(self.housing_options):
            rent = simpledialog.askinteger("Input", "Enter new rent:")
            location = simpledialog.askstring("Input", "Enter new location:")
            if rent and location:
                self.housing_options[index] = {"rent": rent, "location": location}
                messagebox.showinfo("Success", "Housing updated successfully.")
        else:
            messagebox.showerror("Error", "Invalid index.")
    
    def delete_housing(self):
        index = simpledialog.askinteger("Input", "Enter housing index to delete:")
        if index is not None and 0 <= index < len(self.housing_options):
            del self.housing_options[index]
            messagebox.showinfo("Success", "Housing deleted successfully.")
        else:
            messagebox.showerror("Error", "Invalid index.")
    
    def update_route(self):
        index = simpledialog.askinteger("Input", "Enter route index to update:")
        if index is not None and 0 <= index < len(self.routes):
            route_name = simpledialog.askstring("Input", "Enter new route name:")
            cost = simpledialog.askinteger("Input", "Enter new cost:")
            time = simpledialog.askinteger("Input", "Enter new travel time:")
            if route_name and cost and time:
                self.routes[index] = {"route_name": route_name, "cost": cost, "time": time}
                messagebox.showinfo("Success", "Route updated successfully.")
        else:
            messagebox.showerror("Error", "Invalid index.")
    
    def delete_route(self):
        index = simpledialog.askinteger("Input", "Enter route index to delete:")
        if index is not None and 0 <= index < len(self.routes):
            del self.routes[index]
            messagebox.showinfo("Success", "Route deleted successfully.")
        else:
            messagebox.showerror("Error", "Invalid index.")
    
    def display_housing(self):
        messagebox.showinfo("Housing Options", str(self.housing_options))
    
    def display_routes(self):
        messagebox.showinfo("Relocation Routes", str(self.routes))

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeRelocationAssistant(root)
    root.mainloop()
