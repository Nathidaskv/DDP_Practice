class CustomerFeedbackSystem:
    def __init__(self):
        self.feedback_data = {}

    def submit_feedback(self, customer_name, feedback):
        if customer_name not in self.feedback_data:
            self.feedback_data[customer_name] = []
        self.feedback_data[customer_name].append(feedback)

    def view_feedback(self):
        if not self.feedback_data:
            print("No feedback found.")
        else:
            for customer_name, feedback_list in self.feedback_data.items():
                print(f"Customer: {customer_name}")
                for index, feedback in enumerate(feedback_list, start=1):
                    print(f"Feedback {index}: {feedback}")
                print("\n")

def main():
    feedback_system = CustomerFeedbackSystem()

    while True:
        print("\nCustomer Feedback System")
        print("1. Submit Feedback")
        print("2. View Feedback")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            customer_name = input("Enter your name: ")
            feedback = input("Enter your feedback: ")
            feedback_system.submit_feedback(customer_name, feedback)
            print("Feedback submitted successfully.")
        elif choice == '2':
            feedback_system.view_feedback()
        elif choice == '3':
            print("Exiting Customer Feedback System.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
