class headersAnocris():

    def __init__(self) -> None:
        
        self.host = "int43.anocris.com"
        self.rest = "https://int43.anocris.com/rest"
        
        self.content_length = { "city" : 143, "limestone" : 162, "obsidian" : 161, "cacao" : 158, "corn" : 157}
        self.referer = {"city" : "city"}

        self.getHEADERS = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "cs,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
            "Connection": "keep-alive",
            "Cookie": "osu=int_int43; PHPSESSID=86lfsqutg8p8fu03l6ceuqp449; osl=int_int43; os=3787%3B0e225af8eb3f03ecf46d1a823b390cac%3B713b7bfcfe3a328f145eba00e0a1cfdded7ba5ff",
            "Host": self.host,
            "Referer": "https://" + self.host + "/", # pro každý požadavek jiné směrování
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"127\", \"Chromium\";v=\"127\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Windows"}
        
        self.postHEADERS = {
            "Content-Length": None, # pro každý produkt jiná délka
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://" + self.host}
        
    def get(self, referer : str) -> dict:
        self.getHEADERS["Referer"] += referer # pro každý požadavek jiné směrování
        return self.getHEADERS
    
    def post(self, referer : str, content_length : str) -> dict:
        self.getHEADERS["Referer"] += self.referer[referer] # pro každý požadavek jiné směrování
        self.postHEADERS["Content-Length"] = self.content_length[content_length]
        return self.getHEADERS | self.postHEADERS
    
    def referer(self, content_length = str):
        pass