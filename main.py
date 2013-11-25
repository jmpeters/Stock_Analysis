import urllib2
import re
import matplotlib.pyplot as plt
import numpy

__author__ = 'peterj8'


class HypotheticalTime(object):
    # How to store things according to dates.  I would like to keep that data.

    def __init__(self, **kwargs):
        self.dateRange
        self.currentDate


class TradingStrategy(object):
    def __init__(self):
        pass

class SellHighBuyLow(TradingStrategy):
    def __init__(self):
        pass

class Account(object):

    def __init__(self):
        self._stock_owned = 0
        self._liquidity = 0
        self._market = Market()

    def purchaseStock(self, numShares):
        pass

class Market(object):

    def __init__(self):
        pass

    def stockPriceClose(self, stockSymbol):
        pass



def downloadStockCSV(**kwargs):

    yahooQueryInfo = "http://ichart.finance.yahoo.com/table.csv?s=%(stockSymbol)s&d=%(eMonth)s&e=%(eDay)s&f=%(eYear)s" \
                     "&g=d&a=%(sMonth)s&b=%(sDay)s&c=%(sYear)s&ignore=.csv" % kwargs

    webResponse = urllib2.urlopen(yahooQueryInfo)
    stockInfoStorage = open(stockQueryInfo["stockSymbol"] + ".csv", "w")
    stockInfoStorage.writelines(webResponse.read())
    stockInfoStorage.close()
    return

def extractClosingPricesFromCSV(**kwargs):

    stock_info = open(kwargs["stockSymbol"] + ".csv", "r")
    stockPriceInfo = stock_info.readlines()

    priceList = []
    for idx in range(len(stockPriceInfo)):
        info = re.findall(r'\s*[0-9-]+\s*,\s*[0-9.]+\s*,\s*[0-9.]+\s*,\s*[0-9.]+\s*,\s*([0-9.]+)\s*',
                          stockPriceInfo[idx * -1].rstrip())

        if info != []:
            priceList.append(info[0])

    stock_info.close()
    return priceList

# Month is zero based
stockQueryInfo = {"sDay": "1", "sMonth": "0", "sYear": "2010",
                  "eDay": "21", "eMonth": "10", "eYear": "2013",
                  "stockSymbol": "AEG"}

# Download the CSV from the web and store it in a file named from its stock symbol
downloadStockCSV(**stockQueryInfo)

# Extract the closing price information from the CSV file
stockValue = extractClosingPricesFromCSV(**stockQueryInfo)

# Plots are compatible with Numpy arrays
t = numpy.arange(0, len(stockValue), 1)

# Make Fig. 1
myfig = plt.figure(1)    # Specifies which figure number to use

# Add a subplot
mysubplot1 = myfig.add_subplot(111) # 1 row, 1 column, 1st position

# Plot data onto the subplot. 'bo' = blue circle, 'k' = black line
mysubplot1.plot(t, stockValue, 'k')

# Add labels
mysubplot1.set_title("Stock Price")
mysubplot1.set_xlabel("Days")
mysubplot1.set_ylabel("Dollars")

# Show the figure
plt.show()

#prev_value = 36.48
#stock_owned = 50
#net_value = -1 * stock_owned * prev_value
#max_stock_owned = stock_owned
#price_at_max_owned = prev_value

#for price in stockValue:
#    price = float(price)
#    if(prev_value < price):
#        if(stock_owned > 0):
#            stock_owned -= 1
#            net_value += price
#    elif(prev_value > price):
#        stock_owned += 1
#        net_value -= price
#    else:
#        pass
#    prev_value = price
#    if(max_stock_owned < stock_owned):
#        max_stock_owned = stock_owned
#        price_at_max_owned = price

#net_value += stock_owned * prev_value

#print "Value: " + str(net_value)
#print "Max owned: " + str(max_stock_owned) + " valued at " + str(price_at_max_owned * max_stock_owned)

# webscrape (twitter on trending or news articles... need web crawler.  time intensive and need a database)
# SQLite database to keep all this information handy
# graphs from matlab plot
#

# maybe in the future: how to predict EPS
# maybe in the future: understand the entire CAT earnings model
#

