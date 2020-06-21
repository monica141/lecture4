import requests

def main():
    #link from fixer.io for api to get updated rates
    res = requests.get("https://api.fixer.io/latest?base=USD&symbols=EUR")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    #this is extracting the json code and savind it into variable data
    data = res.json()
    #here we are printing data
    print(data)

if __name__ == "__main__":
    main()


#RESPONSE OF this
#{´base´: 'USD', 'date': '2020-06-21', 'rates': {'EUR: 0.81169'}}
