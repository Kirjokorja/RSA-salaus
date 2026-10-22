import sys


class UI:

    def __init__(self, crypto_service):
        self._crypto_service = crypto_service

    def _generate_keys(self):
        keys = self._crypto_service.generate_keys()
        print(f"\nJulkinen avainpari:\n{keys["public"]}\n")
        print(f"\nYksityinen avainpari:\n{keys["secret"]}\n")

    def _encrypt_message(self):
        public_key_e = input("\nAnna julkisen avainparin ensimmäinen avain: ")
        public_key_n = input("\nAnna julkisen avainparin toinen avain: ")
        try:
            key_pair = (int(public_key_e), int(public_key_n))
        except ValueError:
            print("\nAvainparien on oltava kokonaislukuja.\n")
            return
        message = input("\nKirjoita salattava viesti: ")
        try:
            encrypted = self._crypto_service.encrypt_text(key_pair, message)
            print(f"\nSalattu viesti: {encrypted}\n")
        except self._crypto_service.get_exceptions().MessageIsTooLong as e:
            print(f"\n{e.message}\n")

    def _decrypt_message(self):
        secret_key_e = input("\nAnna yksityisen avainparin ensimmäinen avain: ")
        secret_key_n = input("\nAnna yksityisen avainparin toinen avain: ")
        try:
            key_pair = (int(secret_key_e), int(secret_key_n))
        except ValueError:
            print("\nAvainparien on oltava kokonaislukuja.\n")
            return
        message = input("\nKirjoita salattu viesti: ")
        try:
            decrypted = self._crypto_service.decrypt_text(key_pair, message)
        except ValueError:
            print("\nSalatun viestin on oltava kokonaisluku.\n")
            return
        print(f"\nPurettu viesti:\n{decrypted}\n")

    def start(self):
        print("Luo uudet avainparit: syötä 'a'.")
        print("Salaa viesti: syötä 's'.")
        print("Pura salaus: syötä 'p'.")
        print("Lopeta: syötä 'Lopeta'.")
        command = input()

        if command == "a":
            self._generate_keys()
            print("--------------------")
        if command == "s":
            self._encrypt_message()
            print("--------------------")
        if command == "p":
            self._decrypt_message()
            print("--------------------")
        if command == "Lopeta":
            sys.exit()

        self.start()
