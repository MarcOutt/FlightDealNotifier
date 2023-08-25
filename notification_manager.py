import smtplib


class NotificationManager:
    def __init__(self, sender_email, sender_password, recipient_email):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_email = recipient_email
        self.email_content = None

    def create_email_content(self, flight_data):
        email_subject = "Offre de vol interessante"
        self.email_content = f"""Subject:{email_subject}\n\n
        - Prix : {flight_data.price}
        - Ville de départ : {flight_data.departure_city}
        - Code IATA de départ : {flight_data.departure_iata_code}
        - Ville d'arrivée : {flight_data.arrival_city}
        - Code IATA d'arrivée : {flight_data.arrival_iata_code}
        - Date de départ : {flight_data.departure_date}
        - Date de retour : {flight_data.return_date}\n\n"""

    def send_notification_email(self):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=self.sender_email, password=self.sender_password)
            connection.sendmail(from_addr=self.sender_email,
                                to_addrs=self.recipient_email,
                                msg=self.email_content.encode('utf-8'))
