from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name, expires):
        self.name = name
        self.expires = expires

    expired = property(NOW > expires)
