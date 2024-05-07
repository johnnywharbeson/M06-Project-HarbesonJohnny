import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


# Function to create the main window for the Ice Cream Delight application.

def main_window():
    window = tk.Tk()
    window.title("Kevin's Ice Cream Delight")

    selected_toppings = []

    # Load and resize images
    cone_image = Image.open("cone.png")
    cone_image = cone_image.resize((30, 30),
                                   3)  # Using the integer value for ANTIALIAS
    cone_photo = ImageTk.PhotoImage(cone_image)

    sundae_image = Image.open("sundae.png")
    sundae_image = sundae_image.resize(
        (30, 30), 3)  # Using the integer value for ANTIALIAS
    sundae_photo = ImageTk.PhotoImage(sundae_image)

    # Functions

    # Function to add a topping to the selected toppings list.
    def add_topping(topping):
        if topping not in selected_toppings:
            selected_toppings.append(topping)

    # Function to remove a topping from the selected toppings list.
    def remove_topping(topping):
        if topping in selected_toppings:
            selected_toppings.remove(topping)

    # Function to confirm the order and display order summary.
    def confirm_order():
        order_type = order_type_var.get()
        ice_cream_type = ice_cream_type_var.get()
        num_scoops = num_scoops_var.get()

        if order_type == "" or ice_cream_type == "" or num_scoops == "":
            messagebox.showerror("Error", "Please fill in all fields")
            return

        summary = f"Order Type: {order_type}\nIce Cream Type: {ice_cream_type}\nNumber of Scoops: {num_scoops}\nToppings: {', '.join(selected_toppings)}"
        messagebox.showinfo("Order Summary", summary)

    # Function to update the ice cream type variable and menu button text.
    def update_ice_cream_type(item):
        ice_cream_type_var.set(item)
        ice_cream_type_menu.config(text=item)

    # Order type variable and dropdown menu
    order_type_var = tk.StringVar()
    order_type_var.set("Pick Up")

    order_type_label = tk.Label(window, text="Order Type:")
    order_type_label.pack()

    order_type_options = ["Pick Up", "Dine-In"]
    order_type_dropdown = tk.OptionMenu(window, order_type_var,
                                         *order_type_options)
    order_type_dropdown.pack()

    # Ice cream type variable and menu button
    ice_cream_type_var = tk.StringVar()
    ice_cream_type_var.set("Cone")

    ice_cream_type_label = tk.Label(window, text="Ice Cream Type:")
    ice_cream_type_label.pack()

    ice_cream_type_menu = tk.Menubutton(window,
                                         text=ice_cream_type_var.get(),
                                         indicatoron=True,
                                         borderwidth=1,
                                         relief="raised")
    ice_cream_type_menu.pack()

    ice_cream_type_menu.menu = tk.Menu(ice_cream_type_menu, tearoff=0)
    ice_cream_type_menu["menu"] = ice_cream_type_menu.menu

    ice_cream_type_menu.menu.add_command(
        label="Cone",
        image=cone_photo,
        compound="left",
        command=lambda: update_ice_cream_type("Cone"))
    ice_cream_type_menu.menu.add_command(
        label="Sundae",
        image=sundae_photo,
        compound="left",
        command=lambda: update_ice_cream_type("Sundae"))

    # Number of scoops and drop down menu
    num_scoops_var = tk.StringVar()
    num_scoops_var.set("One")

    num_scoops_label = tk.Label(window, text="Number of Scoops:")
    num_scoops_label.pack()

    num_scoops_options = ["One", "Two", "Three"]
    num_scoops_dropdown = tk.OptionMenu(window, num_scoops_var,
                                         *num_scoops_options)
    num_scoops_dropdown.pack()

    # Topping checkboxes 
    toppings_list = [
        "Nuts", "Chocolate", "Strawberry Syrup", "Pineapple Syrup",
        "Whip Cream", "Sprinkles", "Sugar Cookies", "Bananas", "Cherry"
    ]

    toppings_label = tk.Label(window, text="Select Toppings:")
    toppings_label.pack()

    for topping in toppings_list:
        var = tk.BooleanVar()
        chk = tk.Checkbutton(
            window,
            text=topping,
            variable=var,
            onvalue=True,
            offvalue=False,
            command=lambda topping=topping, var=var: update_toppings(
                var, topping))
        chk.pack()

    # Function to update selected toppings list based on checkbox state
    def update_toppings(var, topping):
        if var.get():
            add_topping(topping)
        else:
            remove_topping(topping)

    # Images at the bottom
    cone_bottom_image = Image.open("cone.png")
    cone_bottom_image = cone_bottom_image.resize(
        (125, 125), 3)  # Using the integer value for ANTIALIAS
    cone_bottom_photo = ImageTk.PhotoImage(cone_bottom_image)

    sundae_bottom_image = Image.open("sundae.png")
    sundae_bottom_image = sundae_bottom_image.resize(
        (125, 125), 3)  # Using the integer value for ANTIALIAS
    sundae_bottom_photo = ImageTk.PhotoImage(sundae_bottom_image)

    cone_label_bottom = tk.Label(window, image=cone_bottom_photo)
    cone_label_bottom.image = cone_bottom_photo  # Keep a reference to avoid garbage collection
    cone_label_bottom.pack(side=tk.LEFT, padx=10, pady=10)

    sundae_label_bottom = tk.Label(window, image=sundae_bottom_photo)
    sundae_label_bottom.image = sundae_bottom_photo  # Keep a reference to avoid garbage collection
    sundae_label_bottom.pack(side=tk.RIGHT, padx=10, pady=10)

    # Confirm order button
    confirm_button = tk.Button(window,
                               text="Confirm Order",
                               command=confirm_order)
    confirm_button.pack()

    # Exit button
    exit_button = tk.Button(window, text="Exit", command=window.quit)
    exit_button.pack()

    # Start the GUI event loop
    window.mainloop()


if __name__ == "__main__":
    main_window()
