class resourcesAnocris():
    
    def __init__(self) -> None:
        self.products = [ "limestone", "obsidian", "cacao", "corn"]
        self.amount = 0
        self.limit = 0
        self.pending = False
        self.progress = False
        self.queued = 0
        self.runout = 0
        self.tick = 0
        
        self.rest = "https://int43.anocris.com/rest"
        self.resourceProductionFormfk = {
            "limestone" : "a126fc6a456be854b1f018a3d6a16a88b7e90ea1e541371d6a53ba69c052f335aafb3b896a8a3d26f14bbc0d03c819749ada5e59fe658ebce044265be4d0e65b",
            "obsidian" : "78113a18ae9fd32fd59de1bfad463d91566f5910000f85efd39d78ec01d08da1e358e5b2f84c66f082ddc298af97e05543d8004fcacd9777424c299a9e49c741",
            "cacao" : "d59e913c4008baf47a4eb234f73ee629515b5abd4ed2b45a6acfe4c9db20888a68c05d2302ad020cff30f53cccb05610ea99e3b88562ddc278f5e3a693e6ab23",
            "corn" : "3711e2c717314ad2e484dda6f686152e4b119cb184f8a563b22e524ec29cf6324568707a3cbe24ac6fb0f3a3119cbbfd8ac669c418bf45f0f7fba7988a1fea55"
        }
        
        self.durations = [600, 3600, 14400, 28800]
        
    def collectproduction(self, product : str) -> str:
        return self.rest + "/" + self.collectproduction.__name__ + "/" + product
    
    def startproduction(self, product : str, dutation : int) -> str:
        return self.rest + "/" + self.startproduction.__name__ + "/" + product + "/" + dutation
    
    def resourceProductionForm(self, product : str) -> hex:
        return self.resourceProductionFormfk[product]