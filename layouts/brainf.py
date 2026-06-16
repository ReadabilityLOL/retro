import sys

data = [0] * 30000

def parse(instructions):
    datapointer = 0
    instructionPointer = 0
    while instructionPointer < len(instructions):
        match instructions[instructionPointer]:
            case "+":
                data[datapointer] += 1
                data[datapointer] %= 256

            case "-":
                data[datapointer] -= 1
                data[datapointer] %= 256

            case "<":
                datapointer -= 1

            case ">":
                datapointer += 1

            case ".":
                print(chr(data[datapointer]),end="")

            case ",":
                data[datapointer] = ord(input()[0])
            case "[":
                if data[datapointer] == 0:

                    foundRBrackets = 0
                    foundLBrackets = 1

                    while foundLBrackets > foundRBrackets:
                        instructionPointer += 1

                        if instructions[instructionPointer] == "]":
                            foundRBrackets += 1

                        elif instructions[instructionPointer] == "[":
                            foundLBrackets += 1

            case "]":
                if data[datapointer] != 0:

                    foundLBrackets = 0
                    foundRBrackets = 1

                    while foundLBrackets < foundRBrackets:
                        instructionPointer -= 1

                        if instructions[instructionPointer] == "]":
                            foundRBrackets += 1

                        elif instructions[instructionPointer] == "[":
                            foundLBrackets += 1

            case _:
                pass
        instructionPointer += 1

if len(sys.argv) > 1:
    for x in sys.argv[1:]:
        with open(x, "r") as file:
            parse(file.read())
        data = [0] * 30000

else:
    while True:
        parse(input("brainf> "))
        print()
        data = [0] * 30000
