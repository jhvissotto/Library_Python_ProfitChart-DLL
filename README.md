# Neologica ProfitChart DLL


## Ecosystem

⭐ Portal:     https://bit.ly/finance_analytics  
📊 Blog:       https://slashpage.com/jh-analytics  

📈 Softrader:  https://pypi.org/project/softrader

🐍 Python:     https://github.com/jhvissotto/Project_Finance_Api_Python  
🐍 Pypi:       https://pypi.org/project/jh-finance-api  

🟦 TScript:    https://github.com/jhvissotto/Project_Finance_Api_TScript  
🟦 NPM:        https://www.npmjs.com/package/finance-analytics-api  

🧮 PyHelpers:  https://github.com/jhvissotto/Library_Python_Helpers  

🔌 Server:     https://bit.ly/jh_finance_api  
🔌 Swagger:    https://bit.ly/jh_finance_api_swagger  


## Library

- Description: This library was developed to trade in brazilian exchange B3 via ProfitChart homebroker from Neologica  
- Descrição: Esta biblioteca foi desenvolvida para negociar na bolsa brasileira B3 via homebroker ProfitChart da Neologica  


### Start
```py
def dllStart(key:str, user:str, password:str):
```

### Account Login
```py
def wait_login():
def getAccount():
def getAccountDetails(accountId: TConnectorAccountIdentifier):
```

### Pub/Sub
```py
def subscribeOffer(asset:str, bolsa:str):
def subscribeTicker(asset:str, bolsa:str):
def unsubscribeTicker(asset:str, bolsa:str):
```

### Submit
```py
def sendBuyMarketOrder(brokerId:int, accountId:str, subAccountId:str, password:str, ticker:str, exchange:str, amount:int):
def sendSellMarketOrder(brokerId:int, accountId:str, subAccountId:str, password:str, ticker:str, exchange:str, amount:int):
def buyStopOrder(brokerId:int, accountId:str, subAccountId:str, password:str, ticker:str, exchange:str, price:float, stopPrice:float, amount:int):
def sellStopOrder(brokerId:int, accountId:str, subAccountId:str, password:str, ticker:str, exchange:str, price:float, stopPrice:float, amount:int):
def sendSellOrder(qnt:int, price:float):
```

### Orders
```py
def getOrders(brokerId:str, accountId:str):
def getOrder(cl_ord_id:str, profit_id:int):
def cancelOrder(brokerId:int, accountId:str, subAccountId:str, password:str, cl_ord_id:str):
def cancelAllOrders(brokerId:int, accountId:str, subAccountId:str, password:str):
def changeOrder(brokerId:int, accountId:str, subAccountId:str, cl_ord_id:str, password:str, price:float, amount:int):
def doHasOrdersInInterval(brokerId:int, accountId:str):
```

### Positions
```py
def printLastAdjusted(ticker:str, tick:Lit['A','B']):
def printPosition(ticker:str, exchange:str, brokerId:int, accountId:str, subAccountId:str, positionType:int):
def doZeroPosition(ticker:str, exchange:str, brokerId:int, accountId:int, subAccountId:str, password:str, positionType:int):
```

### Close
```py
def dllEnd():
```