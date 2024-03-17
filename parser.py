from functools import partial


# non recursive but nicer to read the policyText spec than the JSON?
def parseTextPol(policyText: str) -> dict:
    destpolicy = {}
    destpolicy["OR"] = []
    for line in policyText.split("\n"):
        if line == "":
            continue
        andPolicy = {"AND": []}
        for expr in line.split(";"):
            expr = cleanupExpr(expr)
            andPolicy["AND"].append(parseExpr(expr))
        destpolicy["OR"].append(andPolicy)

    return destpolicy


def cleanupExpr(expr: str) -> str:
    return expr.strip()


# parseExpr takes a string and returns a function
def parseExpr(expr: str) -> callable:
    cmd = expr.split(" ")[0]
    args = expr.split(" ")[1:]
    if cmd == "CheckLengthV1":
        if len(args) != 1:
            raise Exception("CheckLengthV1: Invalid expression, length")
        num = args[0]
        if not num.isdigit():
            raise Exception("CheckLengthV1: Invalid expression, arg not number")
        num = int(num)
        return partial(CheckLengthV1, minLength=num)
    elif cmd == "CheckSpecialsV1":
        if len(args) != 1:
            raise Exception("CheckSpecialsV1: Invalid expression")
        num = args[0]
        if not num.isdigit():
            raise Exception("CheckSpecialsV1: Invalid expression")
        num = int(num)
        return partial(CheckSpecialsV1, minNumSpecials=num)
    else:
        raise Exception("Invalid expression", expr)


# Policy "Library" functions

def CheckLengthV1(password: str, minLength: int):
    return len(password) >= minLength


# CheckSpecialsV1 has hardcoded specials
def CheckSpecialsV1(password: str, minNumSpecials: int):
    specials = "!@#$%^&"
    numSpecials = 0
    for char in password:
        if char in specials:
            numSpecials += 1

    return numSpecials >= minNumSpecials
