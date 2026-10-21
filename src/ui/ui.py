import sys

class UI:

    def __init__(self, crypto_service):
        self._crypto_service = crypto_service

    def _generate_keys(self):
        keys = self._crypto_service.generate_keys()
        print(f"Julkinen avainpari: {keys["public"]}\n")
        print(f"Yksityinen avainpari: {keys["secret"]}\n")

    def _encrypt_message(self):
        public_key_e = input("Anna julkisen avainparin ensimmäinen avain: ")
        public_key_n = input("Anna julkisen avainparin toinen avain: ")
        key_pair = (int(public_key_e), int(public_key_n))
        message = input("Kirjoita salattava viesti: ")
        try:
            encrypted = self._crypto_service.encrypt_text(key_pair, message)
            print(f"\n{encrypted}\n")
        except self._crypto_service.get_exceptions().MessageIsTooLong as e:
            print(f"\n{e.message}\n")
    
    def _decrypt_message(self):
        secret_key_e = input("Anna yksityisen avainparin ensimmäinen avain: ")
        secret_key_n = input("Anna yksityisen avainparin toinen avain: ")
        key_pair = (int(secret_key_e), int(secret_key_n))
        message = input("Kirjoita salattu viesti: ")
        decrypted = self._crypto_service.decrypt_text(key_pair, message)
        print(f"\n{decrypted}\n")

    def start(self):
        print("Luo uusi avainpari: syötä 'a'.")
        print("Salaa viesti: syötä 's'.")
        print("Pura salaus: syötä 'p'.")
        print("Lopeta: syötä 'Lopeta'.")
        command = input()
    
        if command == "a":
            self._generate_keys()
        if command == "s":
            self._encrypt_message()
        if command == "p":
            self._decrypt_message()
        if command == "Lopeta":
            sys.exit()

        self.start()
