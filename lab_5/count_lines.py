import os
from pathlib import Path
import csv

SCRIPT_PATH = Path(os.path.abspath(__file__))
SCRIPT_DIR_PATH = SCRIPT_PATH.parent
EXTERNAL_PATH = SCRIPT_DIR_PATH / 'external'
SUFFIXES: list[str] = [
    'h',
    'hpp',
    'c',
    'cpp',
    'hs',
    'cabal',
    'yaml',
    'toml',
    'html',
    'css',
    'json',
    'sh',
    'js',
    'ts',
    'py',
    'sh',
    'java',
    'asm',
]

def main() -> None:
    with open(SCRIPT_DIR_PATH / 'count_lines.csv', 'w') as count_lines_file:
        def count_lines(repo_name: str, crawl_path: Path) -> None:
            total_lines = 0
            for dir, _, src_file_names in os.walk(crawl_path):
                for src_file_name in src_file_names:
                    if any(src_file_name.endswith('.' + suffix) for suffix in SUFFIXES):
                        src_file_path = Path(dir) / src_file_name
                        with open(src_file_path, 'r') as src_file:
                            total_lines += len(src_file.readlines())
            count_lines_file.write(f'{repo_name},{total_lines}\n')

        with open(SCRIPT_DIR_PATH / 'repos.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                repo_name = row[0].split("/")[-1]
                crawl_path = EXTERNAL_PATH / repo_name
                count_lines(repo_name, crawl_path)


if __name__ == '__main__':
    main()