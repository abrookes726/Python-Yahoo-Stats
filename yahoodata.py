

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests, lxml
from lxml import html
import time

table_list = []

company_name = []

num_list0 = [0,1,2,3,4,5,6,7,8]
num_list1 = [0,1,2,3,4,5,6]
num_list2 = [0,1,2,3,4,5,6,7,8,9,10]
num_list3 = [0,1,2,3,4,5,6,7,8,9]
num_list4 = [0,1]
num_list5 = [0,1]
num_list6 = [0,1]
num_list7 = [0,1,2,3,4,5,6,7]
num_list8 = [0,1,2,3,4,5]
num_list9 = [0,1]

# Each of the tables has a number of data items, and that number will be used in the loops below


ticker_list = ["SLG", "SNA", "SO", "LUV", "SWK", "SBUX", "STT", "STE", "SYK", "SIVB", "SYF", "SNPS", "SYY", "TMUS", "TROW", "TTWO", "TPR", "TGT", "TEL", "FTI", "TDY", "TFX", "TER", "TSLA", "TXN", "TXT", "TMO", "TJX", "TSCO", "TT", "TDG", "TRV", "TRMB", "TFC", "TWTR", "TYL", "TSN", "UDR", "ULTA", "USB", "UAA", "UA", "UNP", "UAL", "UNH", "UPS", "URI", "UHS", "UNM", "VLO", "VAR", "VTR", "VRSN", "VRSK", "VZ", "VRTX", "VFC", "VIAC", "VTRS", "V", "VNT", "VNO", "VMC", "WRB", "WAB", "WMT", "WBA", "DIS", "WM", "WAT", "WEC", "WFC", "WELL", "WST", "WDC", "WU", "WRK", "WY", "WHR", "WMB", "WLTW", "WYNN", "XEL", "XRX", "XLNX", "XYL", "YUM", "ZBRA", "ZBH", "ZION", "ZTS"]



#"ABT", "ABBV", "ABMD", "ACN", "ATVI", "ADBE", "AMD", "AAP", "AES", "AFL", "A", "APD", "AKAM", "ALK", "ALB", "ARE", "ALXN", "ALGN", "ALLE", "LNT", "ALL", "GOOGL", "GOOG", "MO", "AMZN", "AMCR", "AEE", "AAL", "AEP", "AXP", "AIG", "AMT", "AWK", "AMP", "ABC", "AME", "AMGN", "APH", "ADI", "ANSS", "ANTM", "AON", "AOS", "APA", "AAPL", "AMAT", "APTV", "ADM", "ANET", "AJG", "AIZ", "T", "ATO", "ADSK", "ADP", "AZO", "AVB", "AVY", "BKR", "BLL", "BAC", "BK", "BAX", "BDX", "BRK-B", "BBY", "BIO", "BIIB", "BLK", "BA", "BKNG", "BWA", "BXP", "BSX", "BMY", "AVGO", "BR", "BF-B", "CHRW", "COG", "CDNS", "CPB", "COF", "CAH", "KMX", "CCL", "CARR", "CTLT", "CAT", "CBOE", "CBRE", "CDW", "CE", "CNC", "CNP", "CERN", "CF", "SCHW", "CHTR", "CVX", "CMG", "CB", "CHD", "CI", "CINF", "CTAS", "CSCO", "C", "CFG", "CTXS", "CLX", "CME", "CMS", "KO", "CTSH", "CL", "CMCSA", "CMA", "CAG", "COP", "ED", "STZ", "COO", "CPRT", "GLW", "CTVA", "COST", "CCI", "CSX", "CMI", "CVS", "DHI", "DHR", "DRI", "DVA"

# "DE", "DAL", "XRAY", "DVN", "DXCM", "FANG", "DLR", "DFS", "DISCA", "DISCK", "DISH", "DG", "DLTR", "D", "DPZ", "DOV", "DOW", "DTE", "DUK", "DRE", "DD", "DXC", "EMN", "ETN", "EBAY", "ECL", "EIX", "EW", "EA", "EMR", "ENPH", "ETR", "EOG", "EFX", "EQIX", "EQR", "ESS", "EL", "ETSY", "EVRG", "ES", "RE", "EXC", "EXPE", "EXPD", "EXR", "XOM", "FFIV", "FB", "FAST", "FRT", "FDX", "FIS", "FITB", "FE", "FRC", "FISV", "FLT", "FLIR", "FLS", "FMC", "F", "FTNT", "FTV", "FBHS", "FOXA", "FOX", "BEN", "FCX", "GPS", "GRMN", "IT", "GD", "GE", "GIS", "GM", "GPC", "GILD", "GL", "GPN", "GS", "GWW", "HAL", "HBI", "HIG", "HAS", "HCA", "PEAK", "HSIC", "HSY", "HES", "HPE", "HLT", "HFC", "HOLX", "HD", "HON", "HRL", "HST", "HWM", "HPQ", "HUM", "HBAN", "HII", "IEX", "IDXX", "INFO", "ITW", "ILMN", "INCY", "IR", "INTC", "ICE", "IBM", "IP", "IPG", "IFF", "INTU", "ISRG", "IVZ", "IPGP", "IQV", "IRM", "JKHY", "J", "JBHT", "SJM", "JNJ", "JCI", "JPM", "JNPR", "KSU", "K", "KEY", "KEYS", "KMB", "KIM", "KMI", "KLAC",

#"KHC", "KR", "LB", "LHX", "LH", "LRCX", "LW", "LVS", "LEG", "LDOS", "LEN", "LLY", "LNC", "LIN", "LYV", "LKQ", "LMT", "L", "LOW", "LUMN", "LYB", "MTB", "MRO", "MPC", "MKTX", "MAR", "MMC", "MLM", "MAS", "MA", "MKC", "MXIM", "MCD", "MCK", "MDT", "MRK", "MET", "MTD", "MGM", "MCHP", "MU", "MSFT", "MAA", "MHK", "TAP", "MDLZ", "MNST", "MCO", "MS", "MOS", "MSI", "MSCI", "NDAQ", "NTAP", "NFLX", "NWL", "NEM", "NWSA", "NWS", "NEE", "NLSN", "NKE", "NI", "NSC", "NTRS", "NOC", "NLOK", "NCLH", "NOV", "NRG", "NUE", "NVDA", "NVR", "ORLY", "OXY", "ODFL", "OMC", "OKE", "ORCL", "OTIS", "PCAR", "PKG", "PH", "PAYX", "PAYC", "PYPL", "PNR", "PBCT", "PEP", "PKI", "PRGO", "PFE", "PM", "PSX", "PNW", "PXD", "PNC", "POOL", "PPG", "PPL", "PFG", "PG", "PGR", "PLD", "PRU", "PEG", "PSA", "PHM", "PVH", "QRVO", "PWR", "QCOM", "DGX", "RL", "RJF", "RTX", "O", "REG", "REGN", "RF", "RSG", "RMD", "RHI", "ROK", "ROL", "ROP", "ROST", "RCL", "SPGI", "CRM", "SBAC", "SLB", "STX", "SEE", "SRE", "NOW", "SHW", "SPG", "SWKS",

#"SLG", "SNA", "SO", "LUV", "SWK", "SBUX", "STT", "STE", "SYK", "SIVB", "SYF", "SNPS", "SYY", "TMUS", "TROW", "TTWO", "TPR", "TGT", "TEL", "FTI", "TDY", "TFX", "TER", "TSLA", "TXN", "TXT", "TMO", "TJX", "TSCO", "TT", "TDG", "TRV", "TRMB", "TFC", "TWTR", "TYL", "TSN", "UDR", "ULTA", "USB", "UAA", "UA", "UNP", "UAL", "UNH", "UPS", "URI", "UHS", "UNM", "VLO", "VAR", "VTR", "VRSN", "VRSK", "VZ", "VRTX", "VFC", "VIAC", "VTRS", "V", "VNT", "VNO", "VMC", "WRB", "WAB", "WMT", "WBA", "DIS", "WM", "WAT", "WEC", "WFC", "WELL", "WST", "WDC", "WU", "WRK", "WY", "WHR", "WMB", "WLTW", "WYNN", "XEL", "XRX", "XLNX", "XYL", "YUM", "ZBRA", "ZBH", "ZION", "ZTS"]


df = pd.DataFrame(list())
df.to_csv("yahoo.csv")

for y in range(0,len(ticker_list)):
    page = requests.get("https://finance.yahoo.com/quote/" + ticker_list[y] + "/key-statistics?p=" + ticker_list[y])
    soup = BeautifulSoup(page.content, "lxml")
    source_code = soup.find_all("table")

# "table" is the piece of html code withint the website that the program is looking for

    for x in range(0, len(source_code)):
        table_list.append(pd.read_html(str(source_code[x])))

# The first forloop adds the data from the yahoo finance table to the csv file.
# The second forloop adds a number of tickers for lines of data the company has.

    for i, table in enumerate(table_list[0]):
        table.to_csv("yahoo.csv".format(i)," ",mode="a", header=False)
    for item in range(0, len(num_list0)):
         company_name.append(ticker_list[y])

    for i, table in enumerate(table_list[1]):
        table.to_csv("yahoo.csv".format(i)," ",mode="a", header=False)
    for item in range(0, len(num_list1)):
         company_name.append(ticker_list[y])

    for i, table in enumerate(table_list[2]):
        table.to_csv("yahoo.csv".format(i)," ",mode="a", header=False)
    for item in range(0, len(num_list2)):
         company_name.append(ticker_list[y])

    for i, table in enumerate(table_list[3]):
        table.to_csv("yahoo.csv".format(i)," ",mode="a", header=False)
    for item in range(0, len(num_list3)):
         company_name.append(ticker_list[y])

    for i, table in enumerate(table_list[4]):
        table.to_csv("yahoo.csv".format(i)," ",mode="a", header=False)
    for item in range(0, len(num_list4)):
         company_name.append(ticker_list[y])

    for i, table in enumerate(table_list[5]):
        table.to_csv("yahoo.csv".format(i)," ",mode="a", header=False)
    for item in range(0, len(num_list5)):
         company_name.append(ticker_list[y])

    for i, table in enumerate(table_list[6]):
        table.to_csv("yahoo.csv".format(i)," ",mode="a", header=False)
    for item in range(0, len(num_list6)):
         company_name.append(ticker_list[y])

    for i, table in enumerate(table_list[7]):
        table.to_csv("yahoo.csv".format(i)," ",mode="a", header=False)
    for item in range(0, len(num_list7)):
         company_name.append(ticker_list[y])

    for i, table in enumerate(table_list[8]):
        table.to_csv("yahoo.csv".format(i)," ",mode="a", header=False)
    for item in range(0, len(num_list8)):
         company_name.append(ticker_list[y])

    for i, table in enumerate(table_list[9]):
        table.to_csv("yahoo.csv".format(i)," ",mode="a", header=False)
    for item in range(0, len(num_list9)):
         company_name.append(ticker_list[y])

    print(ticker_list[y])
    table_list = []
    time.sleep(1)

# The program outputs two csv files, one for the company tickers and one for the scraped data.
# The ticker list is separate from the rest of the data because there are two
# columns outputted into the yahoo csv.

df2 = pd.DataFrame(list())
df2["Company Ticker"] = company_name
df2.to_csv("yahootickers.csv", index=False)
