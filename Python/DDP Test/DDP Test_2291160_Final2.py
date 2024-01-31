"""
>>>>> PLANNING <<<<<

#**Event Database Dictionary
    #1. Event ID    2. Event name    3. speaker name    4. date    5. Capacity    6. attendees    7.point

#INDEX PAGE
    #1. Greeting
    print("Welcome to E-Business Event Management System (EBEMS)")
    #2. Who are you : 
        1. Admin (go to Function A)
        2. User (Go to function B)

#FUNCTION A : Main menu page : ADMIN
    1. Creating a new event (FUNCTION 1)
    2. Event attendance report (FUNCTION 5)

#FUNCTION B : Main menu page : USER
    1. Register for the event (FUNCTION 2)
    2. Check royalty points (FUNCTION 3)
    3. Post-event feedback (FUNCTION 4)

#**FUNCTION 1 : Event creation and management functions
    1. def : view event detail
    2. def : create event detail            >> as date, time, topic, speaker, capacity
    3. def : modify event detail (Delete)
    4. def : modify event detail (Update)

#FUNCTION 2 : Register for the event
    1. Choose the event >> Output: Show Capacity
    3. User register >> capacity of that event decrease -1


#FUNCTION 3 : Royalty points
    #1. fill in user ID >> then display royalty points

#FUNCTION 4 : Post-event feedback
    #1. fill in event ID
    #2. Input feedback

#FUNCTION 5 : Event Attendance Report
    #1. fill in Event ID >> output : show Event ID, Event name and post-event feedback

"""


# Event Database Dictionary
event_database = {
    1: {
        'event_name': 'Tech Conference',
        'speaker_name': 'John Doe',
        'date': '15-02-2024',
        'capacity': 100,
        'attendees': ['Alice', 'Bob'],
    },
    2: {
        'event_name': 'Data Science Workshop',
        'speaker_name': 'Jane Smith',
        'date': '10-03-2024',
        'capacity': 50,
        'attendees': ['Charlie']
    }
}

# User Database Dictionary
user_database = {
    101: {'user_name': 'Alice', 'loyalty_points': 50},
    102: {'user_name': 'Bob', 'loyalty_points': 30},
    103: {'user_name': 'Charlie', 'loyalty_points': 20}
}

# FUNCTION 1.1: View Event Detail
def view_event_detail(event_id):
    event = event_database.get(event_id)
    if event:
        print(f"\nEvent ID: {event_id}")
        print(f"Event Name: {event['event_name']}")
        print(f"Speaker Name: {event['speaker_name']}")
        print(f"Date: {event['date']}")
        print(f"Capacity: {event['capacity']}")
        print(f"Attendees: {', '.join(event['attendees'])}")
    else:
        print(f"Event with ID {event_id} not found.")

# FUNCTION 1.2: Create Event Detail
def create_event_detail(event_id, event_name, speaker_name, date, capacity):
    if event_id in event_database:
        print("Event ID already exists. Please choose a different ID.")
    else:
        event_database[event_id] = {
            'event_name': event_name,
            'speaker_name': speaker_name,
            'date': date,
            'capacity': capacity,
            'attendees': []
        }
        print(f"Event '{event_name}' added successfully.")

# FUNCTION 1.3: Modify Event Detail (Delete Event)
def modify_event_detail_delete(event_id):
    if event_id in event_database:
        del event_database[event_id]
        print(f"Event with ID {event_id} deleted successfully.")
    else:
        print(f"Event with ID {event_id} not found.")

# FUNCTION 1.4: Modify Event Detail (Update Capacity)
def modify_event_detail_update_capacity(event_id, new_capacity):
    event = event_database.get(event_id)
    if event:
        event['capacity'] = new_capacity
        print(f"Capacity of event '{event['event_name']}' updated to {new_capacity}.")
    else:
        print(f"Event with ID {event_id} not found.")

# FUNCTION 2: Register for the event
def register_for_event(event_database):
    while True:
        print("\nEvent Registration System")
        print("1. Choose an event")
        print("2. Register user")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            event_id = int(input("Enter Event ID: "))
            show_capacity(event_id, event_database)
        elif choice == '2':
            event_id = int(input("Enter Event ID to register for: "))
            register_user(event_id, event_database)
        elif choice == '3':
            print("Exiting Event Registration System.")
            break
        else:
            print("Invalid choice. Please choose again.")

# Helper function to show event capacity
def show_capacity(event_id, event_database):
    event = event_database.get(event_id)
    if event:
        print(f"\nEvent ID: {event_id}")
        print(f"Event Name: {event['event_name']}")
        print(f"Remaining Capacity: {event['capacity'] - len(event['attendees'])}")
    else:
        print(f"Event with ID {event_id} not found.")

# Helper function to register a user for an event
def register_user(event_id, event_database):
    event = event_database.get(event_id)
    if event:
        if len(event['attendees']) < event['capacity']:
            attendee_name = input("Enter Attendee Name: ")
            event['attendees'].append(attendee_name)
            event['capacity'] -= 1  # Decrease the capacity by 1
            print(f"Attendee '{attendee_name}' registered for event '{event['event_name']}'.")
            print(f"Remaining Capacity for event '{event['event_name']}': {event['capacity'] - len(event['attendees'])}")
        else:
            print(f"Event '{event['event_name']}' is at full capacity. Cannot register more attendees.")
    else:
        print(f"Event with ID {event_id} not found.")

# FUNCTION 3: Royalty points
def get_loyalty_points(user_id, user_database):
    user = user_database.get(user_id)
    if user:
        loyalty_points = user.get('loyalty_points', 0)
        print(f"Loyalty points for user '{user['user_name']}': {loyalty_points}")
    else:
        print(f"User with ID {user_id} not found.")

# FUNCTION 4: Post-event feedback
def post_event_feedback(event_id, event_database):
    event = event_database.get(event_id)
    if event:
        feedback = input(f"Provide feedback for the event '{event['event_name']}': ")
        event['feedback'] = feedback
        print("Feedback submitted successfully.")
    else:
        print(f"Event with ID {event_id} not found.")

# FUNCTION 5: Event Attendance Report
def event_attendance_report(event_id, event_database):
    event = event_database.get(event_id)
    if event:
        print("\nEvent Attendance Report")
        print(f"Event ID: {event_id}")
        print(f"Event Name: {event['event_name']}")
        
        # Check if there is post-event feedback
        feedback = event.get('feedback', 'No feedback provided')
        print(f"Post-event Feedback: {feedback}")
    else:
        print(f"Event with ID {event_id} not found.")

# FUNCTION A: Admin Main Menu
def admin_main_menu():
    while True:
        print("\nAdmin Main Menu")
        print("1. Manage events")
        print("2. View event details")
        print("3. Exit")

        admin_choice = input("Enter choice (1/2/3): ")

        if admin_choice == '1':
            manage_event()
        elif admin_choice == '2':
            event_id = int(input("Enter Event ID: "))
            view_event_detail(event_id)
        elif admin_choice == '3':
            print("Exiting Admin Main Menu.")
            break
        else:
            print("Invalid choice. Please choose again.")

# FUNCTION B: User Main Menu
def user_main_menu():
    while True:
        print("\nUser Main Menu")
        print("1. Register for an event")
        print("2. Check loyalty points")
        print("3. Post-event feedback")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            register_for_event(event_database)
        elif choice == '2':
            user_id = int(input("Enter User ID: "))
            get_loyalty_points(user_id, user_database)
        elif choice == '3':
            event_id = int(input("Enter Event ID for feedback: "))
            post_event_feedback(event_id, event_database)
        elif choice == '4':
            print("Exiting User Main Menu.")
            break
        else:
            print("Invalid choice. Please choose again.")

# Index Page
print("Welcome to E-Business Event Management System (EBEMS)")

# Who are you: Admin or User
while True:
    print("\nWho are you:")
    print("1. Admin (Enter 'A')")
    print("2. User (Enter 'U')")
    print("3. Exit (Enter 'E')")

    user_type = input("Enter choice (A/U/E): ")

    if user_type.upper() == 'A':
        admin_main_menu()
    elif user_type.upper() == 'U':
        user_main_menu()
    elif user_type.upper() == 'E':
        print("Exiting EBEMS. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose again.")

#MANAGE FUNCTION 1
def manage_event():
    while True:
        print("\nEvent Management System")
        print("1. View event details")
        print("2. Create new event")
        print("3. Delete event")
        print("4. Update event capacity")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '1':
            event_id = int(input("Enter Event ID: "))
            view_event_detail(event_id)
        elif choice == '2':
            event_id = int(input("Enter Event ID: "))
            event_name = input("Enter Event Name: ")
            speaker_name = input("Enter Speaker Name: ")
            date = input("Enter Date (DD-MM-YYYY): ")
            capacity = int(input("Enter Capacity: "))
            create_event_detail(event_id, event_name, speaker_name, date, capacity)
        elif choice == '3':
            event_id = int(input("Enter Event ID to delete: "))
            modify_event_detail_delete(event_id)
        elif choice == '4':
            event_id = int(input("Enter Event ID to update capacity: "))
            new_capacity = int(input("Enter new capacity: "))
            modify_event_detail_update_capacity(event_id, new_capacity)
        elif choice == '5':
            print("Exiting Event Management System.")
            break
        else:
            print("Invalid choice. Please choose again.")
