import subprocess
import csv
import os
from pathlib import Path

SCRIPT_PATH = Path(os.path.abspath(__file__))

def main() -> None:
    with open('repos.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            subprocess.run([
                'git',
                'submodule',
                'add',
                row[0],
                f'external/{row[0].split("/")[-1]}'
            ])

if __name__ == '__main__':
    main()