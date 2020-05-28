from data.dummy_data import ATMS


class ATM:
    def __init__(self, booth: str, address: str, location: str):
        self.booth = booth
        self.address = address
        self.location = location


def get_locations():
    return map(lambda data: ATM(**data), ATMS)
