from __future__ import annotations
from typing import Union

I = 'I'
R = 'R'

# Level : to %, lower bound
LEVELS = {
    '4++'   : (100.0, 99.0),
    '4+'    : ( 97.0, 95.0),
    '4'     : ( 90.5, 87.0),
    '4-'    : ( 83.0, 80.0),
    '3+'    : ( 78.0, 77.0),
    '3'     : ( 74.5, 73.0),
    '3-'    : ( 71.0, 70.0),
    '2+'    : ( 68.0, 67.0),
    '2'     : ( 64.5, 63.0),
    '2-'    : ( 61.0, 60.0),
    '1+'    : ( 58.0, 57.0),
    '1'     : ( 54.5, 53.0),
    '1-'    : ( 51.0, 50.0),
    R       : ( 40.0, 00.0),
    I       : ( 00.0, 00.0)
}

GRADES = dict(map(reversed, LEVELS.items()))

def is_valid_level(level: str) -> bool:
    return level.upper() in LEVELS

def is_valid_grade(grade: str) -> bool:
    try:        
        return 0 <= float(grade) <= 110
    except:
        return False

def to_grade(level: str) -> float:
    return LEVELS[level][0]

def to_level(grade: float) -> str:
    thresholds = sorted(GRADES.keys(), key=lambda g: g[1], reverse=True)
    for thresh in thresholds:
        if grade >= thresh[1]:
            return GRADES[thresh]

def any_to_grade(value: str) -> float:
    if is_valid_level(value):
        return to_grade(value)
    elif is_valid_grade(value):
        return float(value)
    else:
        raise TypeError('Value is not a valid grade or level')

def average() -> tuple[str, float]:
    prompt = 'Enter grade or level; optional space + integer weight (default 1); blank to stop: '
    items = []

    nxt = input(prompt).upper().strip()
    while nxt:
        parts = nxt.split()

        try:
            if len(parts) == 1:
                val, wt = parts[0], 1
            elif len(parts) == 2:
                val, wt = parts[0], int(parts[1])
            else:
                raise Exception('Unrecognized input')
            
            val = any_to_grade(val)
            items.append((val, wt))

        except Exception as e:
            print(repr(e))
 
        nxt = input(prompt).upper().strip()

    if not items:
        return ['I', 0]

    else:
        t = 0
        tw = 0

        for (val, wt) in items:
            t += val * wt
            tw += wt
        a = (t / tw)

        return [to_level(a), a]
    
def mass_average() -> list[tuple[str, float]]:
    rows = []

    nxt = input('Enter weights as integers separated by spaces: ').upper().strip()
    wts = list(int(wt) for wt in nxt.split())

    prompt = 'Enter series of grades or levels; blank to stop: '
    nxt = input(prompt).upper().strip()
    while nxt:
        vals = nxt.split()
        try:
            rows.append(list(any_to_grade(v) for v in vals))
        except Exception as e:
            print(repr(e))
        
        nxt = input(prompt).upper().strip()

    if not rows:
        return []

    else:
        avgs = []
        for row in rows:
            items = zip(row, wts)

            t = 0
            tw = 0
            
            for (val, wt) in items:
                t += val * wt
                tw += wt
            a = (t / tw)

            avgs.append((to_level(a), a))
    
        return avgs

def prog_average() -> None:

    choice = ''
    while choice != 'Q':
        print()
        lv, gr = average()
        print('========')
        print(f'{round(gr):<2} | {lv}')
        print('')
        choice = input('Press Enter to do another or Q to quit: ').upper().strip()

def prog_mass_average() -> None:

    choice = ''
    while choice != 'Q':
        print()
        avgs = mass_average()
        print('========')
        for (lv, gr) in avgs:
            print(f'{round(gr):<2} | {lv}')
        print('')
        choice = input('Press Enter to do another or Q to quit: ').upper().strip()

def run() -> None:
    choices = [prog_average, prog_mass_average]
    choice = input('Enter 0 for average or 1 for mass average: ').strip() # TODO lol
    choices[int(choice)]()

if __name__ == '__main__':
    run()
