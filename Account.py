import hashlib
import hmac
import secrets
class Account:
    def __init__(self, owner_name, balance=0.0):
        if not owner_name or not owner_name.strip():
            raise ValueError("Owner name cannot be empty")

        if balance < 0:
            raise ValueError("Starting balance cannot be negative")

        self.owner_name = owner_name
        self._balance = balance
        self._pin_salt = None
        self._pin_hash = None

    def set_pin(self, pin):
        if not isinstance(pin, str) or len(pin) != 4 or not pin.isdigit():
            return False

        salt = secrets.token_bytes(16)
        self._pin_salt = salt
        self._pin_hash = hashlib.pbkdf2_hmac(
            "sha256",
            pin.encode("utf-8"),
            salt,
            300_000
        )
        return True

    def verify_pin(self, entered_pin):
        if not isinstance(entered_pin,str):
            return False
        if self._pin_salf is None or self._pin_hash is None:
            return False

        entered_hash = hashlib.pbkdf2_hmac(
            "sha256",
            entered_pin.encode("utf-8"),
            self._pin_salt,
            300_000
        )
        return hmac.compare_digest(entered_hash, self._pin_hash)

    def pin_storage_record(self):
        if self._pin_salt is None or self._pin_hash is None:
            return None

        return {
            "pin_salt": self._pin_salt.hex(),
            "pin_hash": self._pin_hash.hex()
        }

    def load_pin_storage_record(self, record):
        self._pin_salt = bytes.fromhex(record["pin_salt"])
        self._pin_hash = bytes.fromhex(record["pin_hash"])

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            return False
        self._balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self._balance:
            return False

        self._balance -= amount
        return True

