import smtplib
from config import MY_MAIL, PASSWORD


class NotificationManager:
    def send_email(self, flight):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_MAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_MAIL,
                                to_addrs=MY_MAIL,
                                msg=f"Subject: Low price alert!\n\nOnly {flight.price}GBP to fly from {flight.origin_city} to {flight.destination_city}, from {flight.out_date} to {flight.return_date}.")
