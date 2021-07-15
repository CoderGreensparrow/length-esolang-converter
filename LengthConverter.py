from sys import argv
def len_to_semi(input_code):
    '''Converts length code to semi-length code. If a string is set as the value of code, then the program will split by \n-s.'''
    if type(input_code) == type(''):
        code = input_code.split('\n')
    else:
        code = input_code
    new_code = []
    line = 0
    commands = {9:'inp', 10:'add', 11:'sub', 12:'dup', 13:'cond', 14:'gotou', 15:'outn', 16:'outa', 17:'rol', 18:'swap',
                20:'mul', 21:'div', 23:'pop', 24:'gotos', 25:'push', 27:'ror'}

    while line < len(code):
        line_length = len(code[line])
        new_code.append(commands[line_length])
        if line_length == 14 or line_length == 25:
            line += 1
            line_length = len(code[line])
            new_code[-1] = new_code[-1] + ' %s'%str(line_length)
        line += 1

    return new_code

def semi_to_len(input_code):
    '''Converts length code to semi-length code. If a string is set as the value of code, then the program will split by \n-s.'''
    if type(input_code) == type(''):
        code = input_code.split('\n')
    else:
        code = input_code
    new_code = []
    line = 0
    commands = {'inp':9, 'add':10, 'sub':11, 'dup':12, 'cond':13, 'gotou':14, 'outn':15, 'outa':16, 'rol':17, 'swap':18,
                'mul':20, 'div':21, 'pop':23, 'gotos':24, 'push':25, 'ror':27}

    while line < len(code):
        line_content = code[line]
        try:
            new_code.append('1' * int(commands[line_content]))
        except KeyError:
            if line_content[0:5] == 'gotou':
                new_code.append('1' * int(commands['gotou']))
                new_code.append('1' * int(line_content[6:]))
            elif line_content[0:4] == 'push':
                new_code.append('1' * int(commands['push']))
                new_code.append('1' * int(line_content[5:]))
        line += 1

    return new_code

def main():
    file = open(argv[2], 'r')
    if argv[1] == 'semi_to_len':
        converted = semi_to_len(file.read())
    elif argv[1] == 'len_to_semi':
        converted = len_to_semi(file.read())
    for i in converted:
        print(i)
if __name__ == '__main__':
    main()