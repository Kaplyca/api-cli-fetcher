import requests
import argparse
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fetch", action="store_true")
    parser.add_argument("--url", type=str)
    args = parser.parse_args()

    if args.fetch and args.url:
        response = requests.get(args.url)
        data = response.json()
        with open("output.json", "w") as f:
            json.dump(data, f)
        print("Dane zapisano do output.json!")

if __name__ == "__main__":
    main()