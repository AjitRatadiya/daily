str = "NORMAL,ADANIGREEN-EQ,BUY,NSE,MARKET,MARGIN,DAY,0.00,0.00,0.00,5,STRN001"
keys = ["variety", "tradingsymbol", "symboltoken", "transactiontype", "exchange",
        "ordertype", "producttype", "duration", "price", "squareoff", "stoploss", "quantity"]
str_list = str.split(",")
print(str_list)
dic = {}
for a in range(len(keys)):
    dic[keys[a]] = str_list[a]
print(dic)