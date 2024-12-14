import os
from pathlib import Path

SCRIPT_PATH = Path(os.path.abspath(__file__))
SCRIPT_DIR_PATH = SCRIPT_PATH.parent
EXTERNAL_PATH = SCRIPT_DIR_PATH / 'external'
SUFFIXES: list[str] = ['h', 'hpp', 'c', 'cpp', 'cpp2', 'h2', 'cxx', 'sh']

def main() -> None:
    total_lines = 0
    for cppfront_dir in ['source', 'include']:
        for dir, _, src_file_names in os.walk(EXTERNAL_PATH / 'cppfront' / cppfront_dir):
            for src_file_name in src_file_names:
                if any(src_file_name.endswith('.' + suffix) for suffix in SUFFIXES):
                    src_file_path = Path(dir) / src_file_name
                    with open(src_file_path, 'r') as src_file:
                        total_lines += len(src_file.readlines())
    print(total_lines)
        

if __name__ == '__main__':
    main()
