from network import Network

class Client(Network):
    def __init__(self, name: str, x: int, y: int, standard: str, frequency: str,  support11k: bool, support11v: bool, support11r: bool, min_rssi: int):
        super().__init__(x, y, support11k, support11v, support11r, min_rssi)
        self.name = name
        self.standard = standard
        self.frequency = frequency

me = Client()    