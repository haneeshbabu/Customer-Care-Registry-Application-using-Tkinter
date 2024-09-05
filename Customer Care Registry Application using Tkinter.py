import tkinter as tk
from tkinter import ttk

# Function to handle the submit button
def submit():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    warranty = warranty_entry.get()
    date_of_purchase = date_of_purchase_entry.get()
    accepted = accept_var.get()

    if accepted == 1:
        with open('customer_records.txt', 'a') as file:
            file.write(f"{first_name},{last_name},{email},{phone},{address},{warranty},{date_of_purchase}\n")
        clear_entries()
    else:
        result_label.config(text="Please accept the terms and conditions.")

# Function to retrieve data from the file
def retrieve_data():
    search_email = search_entry.get()
    with open('customer_records.txt', 'r') as file:
        for line in file:
            data = line.strip().split(',')
            if data[2] == search_email:
                display_search_result(data)
                break
        else:
            result_label.config(text="No record found.")

# Function to display search result in a new window
def display_search_result(data):
    result_window = tk.Toplevel()
    result_window.title("Search Result")
    result_window.geometry("400x300")

    # Create Labels
    labels = ["First Name:", "Last Name:", "Email:", "Phone:", "Address:", "Warranty Period:", "Date of Purchase:"]
    for i, label_text in enumerate(labels):
        label = ttk.Label(result_window, text=label_text)
        label.grid(row=i, column=0, padx=20, pady=10, sticky=tk.W)

    # Create Labels for corresponding data
    data_labels = [data[0], data[1], data[2], data[3], data[4], data[5], data[6]]
    for i, data_text in enumerate(data_labels):
        data_label = ttk.Label(result_window, text=data_text)
        data_label.grid(row=i, column=1, padx=20, pady=10, sticky=tk.W)

# Function to handle the update button
def update_data():
    update_email = update_email_entry.get()
    new_warranty = new_warranty_entry.get()
    new_date_of_purchase = new_date_of_purchase_entry.get()

    with open('customer_records.txt', 'r') as file:
        lines = file.readlines()
    with open('customer_records.txt', 'w') as file:
        for line in lines:
            data = line.strip().split(',')
            if data[2] == update_email:
                data[5] = new_warranty
                data[6] = new_date_of_purchase
                line = ','.join(data) + '\n'
            file.write(line)
    update_email_entry.delete(0, tk.END)
    new_warranty_entry.delete(0, tk.END)
    new_date_of_purchase_entry.delete(0, tk.END)

# Function to clear entry fields
def clear_entries():
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    warranty_entry.delete(0, tk.END)
    date_of_purchase_entry.delete(0, tk.END)


# Create the main window
root = tk.Tk()
root.title("Customer Care Registry")
root.geometry("600x600")

# Configure style
style = ttk.Style(root)
style.theme_use('clam')

# Create Frames
entry_frame = ttk.Frame(root)
search_frame = ttk.Frame(root)
divider = ttk.Separator(root, orient='vertical')

# Create Labels
first_name_label = ttk.Label(entry_frame, text="First Name:")
last_name_label = ttk.Label(entry_frame, text="Last Name:")
email_label = ttk.Label(entry_frame, text="Email:")
phone_label = ttk.Label(entry_frame, text="Phone:")
address_label = ttk.Label(entry_frame, text="Address:")
warranty_label = ttk.Label(entry_frame, text="Warranty Period (months):")
date_of_purchase_label = ttk.Label(entry_frame, text="Date of Purchase (YYYY-MM-DD):")
search_label = ttk.Label(search_frame, text="Search Email:")
update_email_label = ttk.Label(entry_frame, text="Update Email:")
new_warranty_label = ttk.Label(entry_frame, text="New Warranty Period (months):")
new_date_of_purchase_label = ttk.Label(entry_frame, text="New Date of Purchase (YYYY-MM-DD):")

# Create Entry Boxes
first_name_entry = ttk.Entry(entry_frame, width=30)
last_name_entry = ttk.Entry(entry_frame, width=30)
email_entry = ttk.Entry(entry_frame, width=30)
phone_entry = ttk.Entry(entry_frame, width=30)
address_entry = ttk.Entry(entry_frame, width=30)
warranty_entry = ttk.Entry(entry_frame, width=30)
date_of_purchase_entry = ttk.Entry(entry_frame, width=30)
search_entry = ttk.Entry(search_frame, width=30)
update_email_entry = ttk.Entry(entry_frame, width=30)
new_warranty_entry = ttk.Entry(entry_frame, width=30)
new_date_of_purchase_entry = ttk.Entry(entry_frame, width=30)

# Create Submit Button
submit_button = ttk.Button(entry_frame, text="Submit", command=submit)
search_button = ttk.Button(search_frame, text="Search", command=retrieve_data)
update_button = ttk.Button(entry_frame, text="Update", command=update_data)

# Create Result Label
result_label = ttk.Label(root, text='', font=('Arial', 12))

# Create Terms & Conditions Checkbox
accept_var = tk.IntVar()
accept_check = ttk.Checkbutton(entry_frame, text="I accept the terms and conditions.", variable=accept_var)

# Grid positioning for frames
entry_frame.pack(padx=20, pady=10, fill='both', expand=True)
search_frame.pack(padx=20, pady=10, fill='both', expand=True)

# Grid positioning for labels
first_name_label.grid(row=0, column=0, padx=20, pady=10, sticky=tk.W)
last_name_label.grid(row=1, column=0, padx=20, pady=10, sticky=tk.W)
email_label.grid(row=2, column=0, padx=20, pady=10, sticky=tk.W)
phone_label.grid(row=3, column=0, padx=20, pady=10, sticky=tk.W)
address_label.grid(row=4, column=0, padx=20, pady=10, sticky=tk.W)
warranty_label.grid(row=5, column=0, padx=20, pady=10, sticky=tk.W)
date_of_purchase_label.grid(row=6, column=0, padx=20, pady=10, sticky=tk.W)
search_label.grid(row=0, column=0, padx=20, pady=10, sticky=tk.W)
update_email_label.grid(row=9, column=0, padx=20, pady=10, sticky=tk.W)
new_warranty_label.grid(row=10, column=0, padx=20, pady=10, sticky=tk.W)
new_date_of_purchase_label.grid(row=11, column=0, padx=20, pady=10, sticky=tk.W)

# Grid positioning for entry boxes
first_name_entry.grid(row=0, column=1, padx=20, pady=10)
last_name_entry.grid(row=1, column=1, padx=20, pady=10)
email_entry.grid(row=2, column=1, padx=20, pady=10)
phone_entry.grid(row=3, column=1, padx=20, pady=10)
address_entry.grid(row=4, column=1, padx=20, pady=10)
warranty_entry.grid(row=5, column=1, padx=20, pady=10)
date_of_purchase_entry.grid(row=6, column=1, padx=20, pady=10)
search_entry.grid(row=0, column=1, padx=20, pady=10)
update_email_entry.grid(row=9, column=1, padx=20, pady=10)
new_warranty_entry.grid(row=10, column=1, padx=20, pady=10)
new_date_of_purchase_entry.grid(row=11, column=1, padx=20, pady=10)

# Grid positioning for terms and conditions
accept_check.grid(row=7, columnspan=2, padx=20, pady=10, sticky=tk.W)

# Grid positioning for buttons
submit_button.grid(row=8, column=0, columnspan=2, padx=20, pady=10)
update_button.grid(row=12, column=0, columnspan=2, padx=20, pady=10)
search_button.grid(row=1, column=1, padx=20, pady=10, sticky=tk.W)

# Grid positioning for result label
result_label.pack(padx=20, pady=10, fill='both', expand=True)

# Place the divider
divider.pack(in_=root, side='left', fill='y', padx=20, pady=10)

# Start the main loop
root.mainloop()
