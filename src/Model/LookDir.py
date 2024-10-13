import argparse
from pathlib import Path

class LookDir:
    def __init__(self) -> None:
        self.url: str = ""
        self.path: Path = ""

    def set_param(self) -> None:
        parser = argparse.ArgumentParser(description='Search Dir')
        parser.add_argument('-u', '--url', help='URL Target', required=True)  
        parser.add_argument('-w', '--wordlist', help='Wordlist dir', required=True) 
        args = parser.parse_args()

        self.url = args.url
        self.path = args.wordlist

        
        
