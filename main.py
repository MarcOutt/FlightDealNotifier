from notification_manager import NotificationManager
from flight_data import FlightData
from data_manager import DataManager
from flight_search import FlightSearch
from private_infos import my_email, password, email

sender_email = my_email
sender_password = password
recipient_email = email

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

if sheet_data[0]["IATA Code"] == "":
    for row in sheet_data:
        row["IATA Code"] = flight_search.get_iata_code_city(row["City"])
    print(f"sheet_data:\n {sheet_data}")
    data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

for row in sheet_data:
    print(row)
    city_code = row["IATA Code"]
    flights = flight_search.get_flight_price(city_code)
    for flight in flights:
        print(flight['price'],row["Lowest Price"])
        if int(flight['price']) <= int(row["Lowest Price"]):
            flight_data = FlightData(
                price=flight['price'],
                departure_city=flight['cityFrom'],
                departure_iata_code=flight['cityCodeFrom'],
                arrival_city=flight['cityTo'],
                arrival_iata_code=flight['cityCodeTo'],
                departure_date=flight['dTime'],
                return_date=flight['aTime']
            )

            notification_manager = NotificationManager(sender_email, sender_password, recipient_email)
            notification_manager.create_email_content(flight_data=flight_data)
            notification_manager.send_notification_email()

