# Import libraries 
import sys
sys.path.insert(0, 'src/data')
from  dataset import process_data

def main(targets):
    if 'target' in targets:
        return process_data()

if __name__ == '__main__':
    targets = sys.argv[1:]
    print(main(targets))