import tkinter
from tkinter import ttk

import yfinance

tickersymbol1 = 'AMC'
tickersymbol2 = 'GME'

tickerData1 = yfinance.Ticker(tickersymbol1)
tickerData2 = yfinance.Ticker(tickersymbol2)

tickerDf1 = tickerData1.history(interval='1m')
tickerDf2 = tickerData2.history(interval='1m')

#main application window
root = tkinter.Tk()
root.title("stonks")


#creates a content frame
mainframe = ttk.Frame(root, padding="1 1 10 10")
mainframe.grid(column=0, row=0, sticky=("N", "W", "E", "S"))
root.columnconfigure(1, weight=2)
root.rowconfigure(1, weight=2)

#content within window
ttk.Label(mainframe, text="AMC").grid(column=1, row=1, sticky=tkinter.W)
ttk.Label(mainframe, text=tickerDf1).grid(column=2, row=1, sticky=tkinter.W)
ttk.Label(mainframe, text='GME').grid(column=1, row=2, sticky=tkinter.W)
ttk.Label(mainframe, text=tickerDf2).grid(column=2, row=2, sticky=tkinter.W)


#tells Tk to start events
root.mainloop()
