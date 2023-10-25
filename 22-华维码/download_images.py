import json
import os
import sys

import requests


def main() -> None:
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} path_to_json dest')
        exit(1)
    with open(sys.argv[1], 'r', encoding='utf8') as f:
        o = json.load(f)
    game = o['data']['game']
    dest = sys.argv[2]
    os.makedirs(dest, exist_ok=True)
    with requests.Session() as s:
        for row in game:
            for path in row:
                if path is None:
                    continue
                url = f'https://prob19.geekgame.pku.edu.cn/{path}'
                r = s.get(url, timeout=10, cookies={'session': 'Your session here'})
                with open(os.path.join(dest, os.path.basename(path)), 'wb') as f:
                    f.write(r.content)


if __name__ == "__main__":
    main()
