# We start with an empty list to hold our tickets
active_tickets = []

print("=== Factory Maintenance System Offline ===")

while True:
    action = input("Choose action (add/view/quit): ")
    
    if action == "add":
        issue = input("Enter equipment issue: ")
        active_tickets.append(issue)
        print("Ticket logged successfully.\n")

    elif action == "view":
        print("\n--- Current Active Tickets ---")
        for ticket in active_tickets:
            print(f"- {ticket}")
        print("------------------------------\n")

    # 4. Check if they typed "quit"
    elif action == "quit":
        print("Shutting down system. Goodbye!")
        # Use the magic keyword here to shatter the loop!
        break

    # 5. Catch-all for typos
    else:
        print("Invalid command. Please type add, view, or quit.\n")