"""
#FUNCTION 2 : Register for the event
    1. Choose the event >> Output: Show Capacity
    2. User register >> capacity of that event decrease -1
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
# FUNCTION 2: Register for the event

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
register_for_event(event_database)