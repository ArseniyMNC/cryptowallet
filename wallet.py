import blockchane as bc
import naming

class Wallet:

    balance_usd = 0
    balance_coin = 0.00

    def __init__(self, balance_usd: int, balance_coin: float):
        self.balance_usd = balance_usd
        self.balance_coin = balance_coin
        self.name = naming.name_ganerate(20)



    def addUSD(self, count: int):
        self.balance_usd += count
        bc.blockchane(f"added {count} usd to {self.name}")

    def addCoin(self, count: float):
        self.balance_coin += count
        bc.blockchane(f"added {count} coin(s) to {self.name}")

    

    def setUSD(self, count: int):
        self.balance_usd = count if count > 0 else 0
        bc.blockchane(f"seted {count} usd to {self.name}")

    def setCoin(self, count: float):
        self.balance_count = count if count > 0 else 0.00
        bc.blockchane(f"seted {count} coin(s) to {self.name}")

    

    def usd_to_wallet(self, wallet, count: int):
        if count > self.balance_usd:
            raise Exception("...")
        else:
            self.addCoin(-1*count)
            wallet.addCoin(count)
        bc.blockchane(f"transfered {count} usd from {self.name} to {wallet.name}")
    
    def coin_to_wallet(self, wallet, count: float):
        if count > self.balance_coin:
            raise Exception("...")
        else:
            self.addCoin(-1*count)
            wallet.addCoin(count)
        bc.blockchane(f"transfered {count} coin(s) from {self.name} to {wallet.name}")