bookings = []
n = int(input("Enter number of bookings: "))
for i in range (n):
    flight_number = input("Enter flight number: ")
    passenger_name = input("Enter passenger name: ")
    departure = input("Enter departure city: ")
    destination = input("Enter destination city: ")
    seat_number = input("Enter seat number: ")
    bookings.append((flight_number, passenger_name, departure, destination, seat_number))

for a in bookings:
    print(a)

flight_check = input("Enter flight number to check: ")
seat_check = input("Enter seat number to check: ")
seat_booked = any(flight_number == flight_check and seat_number == seat_check for flightnumber, , , , seat_number in bookings)
print(f"Is seat {seat_check} on flight {flight_check} booked? :{seat_booked}")

destination_check = input("Enter destination city to find passengers: ")
passengers = [passengersname for , passengersname, ,  destination, _ in bookings if destination == destination_check]
print(f"Passengers traveling to {destination_check} is :{passengers}")
