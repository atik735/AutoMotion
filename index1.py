import argparse
import itertools
import json

def main():
    parser = argparse.ArgumentParser(description='Custom Wordlist Generator')
    parser.add_argument('-b', '--base', nargs='+', required=True, help='Base words (space-separated)')
    parser.add_argument('-y', '--years', nargs='+', required=True, help='Years to include')
    parser.add_argument('-s', '--special', nargs='+', default=['!','@','#'], help='Special characters')
    parser.add_argument('-o', '--output', default='custom_wordlist.txt', help='Output filename')
    parser.add_argument('-c', '--config', help='JSON config file (overrides CLI)')
    
    args = parser.parse_args()
    
    if args.config:
        with open(args.config) as f:
            config = json.load(f)
        base = config['base']
        years = config['years']
        special = config.get('special', ['!','@','#'])
    else:
        base = args.base
        years = args.years
        special = args.special
    
    combinations = []
    # ... (rest of generation logic from previous implementation) ...
    
    print(f"Generated {len(combinations)} passwords in {args.output}")

if __name__ == "__main__":
    main()