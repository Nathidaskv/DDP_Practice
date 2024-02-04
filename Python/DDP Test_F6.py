"""
#FUNCTION 1 : Event creation and management functions
    1. def : view event detail
    2. def : create event detail            >> as date, time, topic, speaker, capacity
    3. def : modify event detail (Delete)
    4. def : modify event detail (Update)
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
