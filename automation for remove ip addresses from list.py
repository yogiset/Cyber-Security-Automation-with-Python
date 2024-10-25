def update_file(import_file, remove_list):
    # Build `with` statement to read in the initial contents of the file
    with open(import_file, "r") as file:
        # Use `.read()` to read the imported file and store it in a variable named `ip_addresses`
        ip_addresses = file.read()

    # Use `.split()` to convert `ip_addresses` from a string to a list
    ip_addresses = ip_addresses.split()

    # Use list comprehension to remove elements in `remove_list`
    ip_addresses = [ip for ip in ip_addresses if ip not in remove_list]

    # Convert `ip_addresses` back to a string so that it can be written into the text file 
    ip_addresses = " ".join(ip_addresses)       

    # Build `with` statement to rewrite the original file
    with open(import_file, "w") as file:
        # Rewrite the file, replacing its contents with `ip_addresses`
        file.write(ip_addresses)

# Call `update_file()` and pass in the correct file path and a list of IP addresses to be removed
update_file("E:/Cyber Security Automation with Python/allow_list.txt", ["192.168.25.60", "192.168.140.81", "192.168.203.198"])

# Build `with` statement to read in the updated file
with open("E:/Cyber Security Automation with Python/allow_list.txt", "r") as file:
    # Read in the updated file and store the contents in `text`
    text = file.read()

# Display the contents of `text`
print(text)
