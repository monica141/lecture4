import requests

def main():
    #taking the input(url) to get the rrequest and get back the https request
    res = requests.get("https://www.google.com/")
    #printing the response that came back
    print(res.text)

if __name__ == "__main__":
    main()
