import random
import re
import signal
import time

import requests

_interrupted = False
L = 64
Good = '🟩'
Wrong_position = '🟨'
Bad = '🟥'
Delay = 1


def handler(_, __):
    global _interrupted
    _interrupted = True
    print('Interrupt received. Press again for emergent exit.')
    signal.signal(signal.SIGINT, _saved_handler)


_saved_handler = signal.signal(signal.SIGINT, handler)


def main() -> None:
    with open('../token.txt', 'r') as f:
        token = f.read().strip()
    start_url = f'https://prob14.geekgame.pku.edu.cn/?token={token}'
    level_url = 'https://prob14.geekgame.pku.edu.cn/level{}'
    with requests.Session() as s:
        # r = s.get(start_url)
        # How many possible emojis are there?
        # r = s.get(level_url.format(1))
        # print(r)
        # print(r.headers)
        # print(r.content)
        # if r.status_code != requests.codes.ok:
        #     print('Error starting game')
        #     exit(1)
        r = s.get(level_url.format(3))
        play_session = s.cookies.get('PLAY_SESSION')

        # Can one emoji be in multiple positions?
        seen_emojis = {'👵', '👬', '🐷', '🐐', '🐝', '👈', '🐕', '👌', '👇', '👳', '👥', '🐱', '👕', '🐞', '👦', '👸', '🐚', '🐿', '👨', '🐟', '🐠', '💍', '💆', '👒', '👺', '👙', '👂', '🐧', '👃', '👘', '👜', '👋', '💏', '🐓', '👖', '👚', '👗', '👠', '🐒', '👾', '🐖', '🐤', '👰', '💁', '👝', '👲', '🐛', '🐽', '👯', '👟', '👀', '🐪', '🐙', '🐮', '🐼', '👻', '👎', '🐴', '💎', '👣', '👿', '🐫', '👧', '🐣', '🐘', '💉', '🐩', '👁', '👔', '👹', '👢', '🐳', '🐢', '👱', '💈', '👑', '👤'}
        known = [None] * L
        tried = [set() for _ in range(L)]
        wrongly_positioned = set()
        bad = set()

        if _interrupted:
            print(seen_emojis)
            print(known)
            print(tried)
            print(wrongly_positioned)
            print(bad)
            return

        while True:
            s.cookies.clear()
            s.cookies.set('PLAY_SESSION', play_session)
            attempt = []
            for i in range(L):
                if known[i]:
                    attempt.append(known[i])
                    continue
                candidates = wrongly_positioned - tried[i]
                if len(candidates) > 0:
                    attempt.append(random.choice(list(candidates)))
                else:
                    attempt.append(random.choice(list(seen_emojis - bad - tried[i])))
            print(''.join(attempt))

            r = s.get(
                level_url.format(3),
                params={'guess': ''.join(attempt)},
            )
            print(r)
            print(r.headers)
            print(r.content)

            placeholder = eval(re.search('placeholder=("[^"]+?")', r.text).group(1))
            seen_emojis.update(placeholder)
            result = eval(re.search('push\(("[^"]+?")', r.text).group(1))
            # print(placeholder)
            print(result)

            for i in range(L):
                if result[i] == Good:
                    known[i] = attempt[i]
                elif result[i] == Wrong_position:
                    wrongly_positioned.add(attempt[i])
                    tried[i].add(attempt[i])
                elif result[i] == Bad:
                    bad.add(attempt[i])

            print(known)
            if None not in known:
                # print(''.join(known))
                break

            time.sleep(Delay)


if __name__ == "__main__":
    main()
