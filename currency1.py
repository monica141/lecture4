import requests

def main():
    #getting the requestr
    res = requests.get("https://api.fixer.io/latest?base=USD&symbols=EUR")
    #if anyerror show
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    #asking the data to just show the rates from the given information and save it in rate
    rate = data["rates"]["EUR"]
    #printing rate
    print(f"1 USD is equal to {rate} EUR")

if __name__ == "__main__":
    main()


#RESPONSE OF THIS+
#1 USD is equal to 0.81169 EUR
