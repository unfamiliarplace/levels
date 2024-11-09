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

def is_valid_grade(grade: float) -> bool:
    return 0 <= grade <= 110

def to_grade(level: str) -> float:
    return LEVELS[level][0]

def to_level(grade: float) -> str:
    thresholds = sorted(GRADES.keys(), key=lambda g: g[1], reverse=True)
    for thresh in thresholds:
        if grade >= thresh[1]:
            return GRADES[thresh]

def average() -> tuple[str, float]:
    pass

def run() -> None:
    pass

if __name__ == '__main__':
    run()
