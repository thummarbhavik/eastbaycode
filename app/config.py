class Config:
    def __init__(self):
        if False:
            self.dbhost = "mlbh2h.ccr2bbshqt2i.us-west-1.rds.amazonaws.com"
            self.dbuser = "barrybonds"
            self.dbpw = "UShhjkY6"
            self.dbname = "eastbaycode"
            self.dbport = 3306
        else:
            self.dbhost = "localhost"
            self.dbuser = "root"
            self.dbpw = "Hanoi123"
            self.dbname = "eastbaycode"
            self.dbport = 3306
