# Define room types and their nightly rates
room_types = ["Single", "Double", "Suite"]
nightly_rates = [100, 150, 250]

# Additional services and their costs
additional_services = {"breakfast": 20, "wifi": 10, "parking": 15}


def calculate_cost(room_type, num_rooms, check_in, check_out, services):
    # Calculate the total cost based on room type, number of rooms, and duration of stay
    total_cost = nightly_rates[room_types.index(room_type)] * num_rooms * (check_out - check_in).days

    # Add the cost of additional services
    for service in services:
        total_cost += additional_services.get(service, 0)

    return total_cost


def main():
    print("Welcome to the ABC Hotel Reservation System")

    # Input check-in and check-out dates
    check_in = input("Enter check-in date (YYYY-MM-DD): ")
    check_out = input("Enter check-out date (YYYY-MM-DD): ")

    try:
        check_in = datetime.datetime.strptime(check_in, "%Y-%m-%d")
        check_out = datetime.datetime.strptime(check_out, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    # Input room type and number of rooms
    print("Room types available:")
    for room_type, rate in zip(room_types, nightly_rates):
        print(f"{room_type}: ${rate} per night")

    room_type = input("Select room type: ")
    if room_type not in room_types:
        print("Invalid room type.")
        return

    num_rooms = input("Enter number of rooms: ")
    if not num_rooms.isdigit() or int(num_rooms) <= 0:
        print("Invalid number of rooms.")
        return
    num_rooms = int(num_rooms)

    # Select additional services
    print("Additional services available: ", ", ".join(additional_services.keys()))
    selected_services = input("Select additional services (comma-separated): ").split(",")
    selected_services = [service.strip().lower() for service in selected_services]

    # Calculate total cost
    total_cost = calculate_cost(room_type, num_rooms, check_in, check_out, selected_services)

    # Display reservation details
    print("\nReservation Details:")
    print(f"Check-in: {check_in.strftime('%Y-%m-%d')}")
    print(f"Check-out: {check_out.strftime('%Y-%m-%d')}")
    print(f"Room type: {room_type}")
    print(f"Number of rooms: {num_rooms}")
    print("Additional services: ", ", ".join(selected_services))
    print(f"Total cost: ${total_cost}")

    # Confirmation
    confirm = input("Confirm reservation (yes/no): ").lower()
    if confirm == "yes":
        print("Reservation confirmed. Thank you!")
    else:
        print("Reservation cancelled.")


if __name__ == "__main__":
    import datetime

    main()
