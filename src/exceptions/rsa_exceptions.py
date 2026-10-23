class MessageIsTooLong(Exception):
    """Luokka käsittelee ilmoituksia poikkeustilanteessa, 
        jossa viesti on liian pitkä.
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
