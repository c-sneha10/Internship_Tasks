#Problem name:String Formatting
#Hacker Rank Link: https://www.hackerrank.com/challenges/python-string-formatting/problem
def print_formatted(number):
    width = len(format(number, 'b'))

    for i in range(1, number + 1):
        decimal = str(i)
        octal = format(i, 'o')
        hexadecimal = format(i, 'X')
        binary = format(i, 'b')

        print(decimal.rjust(width), octal.rjust(width),
              hexadecimal.rjust(width), binary.rjust(width))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
