def main():
    exp = input("Expression: ").strip()
    parts = exp.split(" ")
    sign = parts[1]
    match sign:
        case "+":
            print(float(parts[0]) + float(parts[2]))
        case "-":
            print(float(parts[0]) - float(parts[2]))
        case "*":
            print(float(parts[0]) * float(parts[2]))
        case "/":
            print(float(parts[0]) / float(parts[2]))


main()