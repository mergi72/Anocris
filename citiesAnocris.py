import getHTTPAnocris

class citiesAnocris:
    
    def __init__(self) -> None:
                self.city = { "Litvínov": 3837, "Most": 5490, "Ossegg": 5552}
        
    def get(self, name: str) -> int:
        return self.city[name]