import requests
import tkinter
from tkinter import Tk, Label, Button, Entry

window = tkinter.Tk()

url = "https://currency23.p.rapidapi.com/exchange"

headers = {
    'x-rapidapi-host': "currency23.p.rapidapi.com",
    'x-rapidapi-key': "2484d4ac9emsh68d6b4141d1dd21p1084d4jsn78a0eebf4683"
}

window.title("Currency Converter")

Title = Label(window, text="Currency Converter", font=("Arimo", 32))
Title.pack()

Description = Label(window, text="Please enter the base currency code, target code and amount of money to convert. (Currently we don't support cryptocurrencys).")
Description.pack()

BaseCurrencyEntry = Entry(window)
BaseCurrencyEntry.pack()

TargetCurrencyEntry = Entry(window)
TargetCurrencyEntry.pack()

AmountEntry = Entry(window)
AmountEntry.pack()

def Convert():
    BaseCurrency = BaseCurrencyEntry.get()
    TargetCurrency = TargetCurrencyEntry.get()
    Amount = AmountEntry.get()

    querystring = {"int":f"{Amount}","base":f"{BaseCurrency}","to":f"{TargetCurrency}"}

    response = requests.request("GET", url, headers=headers, params=querystring)

    result = response.json()["result"]["data"][0]["calculatedstr"]

    Label(window, text=f"Currently {Amount} {BaseCurrency} is worth {result} {TargetCurrency}.").pack()

ConvertButton = Button(window, text="Convert!", command=Convert)
ConvertButton.pack()

window.mainloop()