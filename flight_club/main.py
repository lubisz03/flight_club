from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from config import ORIGIN_CITY_IATA


def main():
    data_manager = DataManager()
    sheet_data = data_manager.get_destination_data()

    if sheet_data[0]["iataCode"] == "":
        for row in sheet_data:
            row["iataCode"] = FlightSearch.get_destination_code(row["city"])
        data_manager.destination_data = sheet_data
        data_manager.update_destination_codes()

    from_time = datetime(2025, 4, 28)
    to_time = datetime(2025, 4, 30)

    for destination in sheet_data:
        print(destination)
        flight = FlightSearch.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=data_manager.convert_date(destination['from']),
            to_time=data_manager.convert_date(destination['to']),
            min_days=destination["minLength"],
            max_days=destination["maxLength"]
        )
        if flight.price < destination["lowestPrice"]:
            NotificationManager.send_email(flight)


if __name__ == "__main__":
    main()
