import requests
from config import KIWI_API_KEY, KIWI_ENDPOINT
from flight_data import FlightData
from datetime import datetime


class FlightSearch:

    @staticmethod
    def get_destination_code(city_name):
        location_endpoint = f"{KIWI_ENDPOINT}/locations/query"
        headers = {"apikey": KIWI_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint,
                                headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    @staticmethod
    def check_flights(origin_city_code, destination_city_code, from_time, to_time, min_days, max_days):
        headers = {"apikey": KIWI_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": min_days,
            "nights_in_dst_to": max_days,
            "flight_type": "round",
            "max_stopovers": 2,
            "curr": "PLN",
            "sort": "price",
            "limit": 1
        }

        response = requests.get(
            url=f"{KIWI_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )

        try:
            data = response.json()["data"][0]
            print(response.json()["data"])
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        routes = data["route"]
        outbound_flight = routes[0]
        return_flight = routes[-1]
        trip_start_date = outbound_flight["local_departure"].split("T")[0]
        trip_end_date = return_flight["local_arrival"].split("T")[0]

        start_date = datetime.strptime(trip_start_date, "%Y-%m-%d")
        end_date = datetime.strptime(trip_end_date, "%Y-%m-%d")

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["cityFrom"],
            origin_airport=data["flyFrom"],
            destination_city=data["cityTo"],
            destination_airport=data["flyTo"],
            out_date=trip_start_date,
            return_date=trip_end_date,
        )
        print(f"{flight_data.destination_city}: {flight_data.price} PLN - "
              f"From: {flight_data.out_date} To: {flight_data.return_date} "
              )
        return flight_data
