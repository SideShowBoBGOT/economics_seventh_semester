from pathlib import Path
import os
import functools

SCRIPT_PATH = Path(os.path.abspath(__file__))
SCRIPT_DIR_PATH = SCRIPT_PATH.parent

def main() -> None:
    with open(SCRIPT_DIR_PATH / 'data.csv', 'w') as data_file, \
        open(SCRIPT_DIR_PATH / 'count_lines.csv') as count_lines_file, \
        open(SCRIPT_DIR_PATH / 'repos.csv') as repos_file:
        data_file.write('Назва проекту,Нескоригована кількість функціональних точок,Скоригована кількість функціональних точок,Мова програмування,Тисячі рядків коду,Зусилля\n')
        for (count_row, repo_row) in zip(count_lines_file.readlines(), repos_file.readlines()):
            count_parts = count_row.split(',')
            repo_parts = repo_row.split(',')
            code_lines = int(count_parts[1]) / 1000
            effort = 2.4 * code_lines ** 1.05
            line = ','.join([count_parts[0], repo_parts[1], repo_parts[2], repo_parts[3].rstrip(), str(code_lines), f'{effort:.2f}'])
            data_file.write(line + '\n')

if __name__ == '__main__':
    main()