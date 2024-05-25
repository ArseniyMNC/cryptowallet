import course
import blockchane as bc

def buy_USD(wallet, count: int):
    if wallet.balance_coin < count/course.USD_IN_COIN:
        raise Exception("...")
    else:
        wallet.addCoin(-1*(count/course.USD_IN_COIN))
        wallet.addUSD(count)

def sell_USD(wallet, count: int):
    if wallet.balance_usd < count:
        raise Exception("...")
    else:
        wallet.addCoin(count/course.USD_IN_COIN)
        wallet.addUSD(-1*count)



def buy_coin(wallet, count: float):
    if wallet.balance_usd < count*course.USD_IN_COIN:
        raise Exception("...")
    else:
        wallet.addUSD(-1*(count*course.USD_IN_COIN))
        wallet.addCoin(count)
    bc.blockchane(f"{wallet.name} buyed {count} usd")

def sell_coin(wallet, count: float):
    if wallet.balance_coin < count:
        raise Exception("...")
    else:
        wallet.addCoin(-1*count)
        wallet.addUSD(count*course.USD_IN_COIN)
    bc.blockchane(f"{wallet.name} buyed {count} coin(s)")