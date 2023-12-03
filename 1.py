import functools

f = open("input.txt", "r")


def startsWithConvert(s, word, digit):
    if (s.startswith(word)):
        return digit
    return None


def endsWithWithConvert(s, word, digit):
    if (s.endswith(word)):
        return digit
    return None


def getFirstNumber(s, getStringNumber, getDigit, getRemainder):
    ret = getStringNumber(s, 'one', '1') or \
          getStringNumber(s, 'two', '2') or \
          getStringNumber(s, 'three', '3') or \
          getStringNumber(s, 'four', '4') or \
          getStringNumber(s, 'five', '5') or \
          getStringNumber(s, 'six', '6') or \
          getStringNumber(s, 'seven', '7') or \
          getStringNumber(s, 'eight', '8') or \
          getStringNumber(s, 'nine', '9')
    if ret is not None:
        return ret
    if (getDigit(s).isdigit()):
        return getDigit(s)
    return getFirstNumber(getRemainder(s), getStringNumber, getDigit, getRemainder)


def getFirstAndLastNumbers(i):
    return getFirstNumber(i, startsWithConvert, lambda s: s[0], lambda s: s[1:]) + getFirstNumber(i,
                                                                                                  endsWithWithConvert,
                                                                                                  lambda s: s[-1],
                                                                                                  lambda s: s[:-1])


def addStrings(a, b):
    return int(a) + int(b)


x = functools.reduce(addStrings, map(getFirstAndLastNumbers, f.read().split()))

print(x)
