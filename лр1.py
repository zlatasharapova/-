import time
import os
green='\u001b[42m'
red='\u001b[41m'
pink='\u001b[105m'
white='\u001b[107m'
end='\u001b[0m'
def flag():
    height=18
    width=60
    y_center=9
    x_center=30
    radius=6
    for y in range(height):
        row=''
        for x in range(width):
            if (((x-x_center)/2)**2 + (y-y_center)**2)<=radius**2:
                row+= red + ' '
            else:
                row+= green + ' '
        print(row + end)

uzor=[
'####__',
'#__#__',
'#_##__',
'#_#___',
'#_####'
]
def pattern():
    for line in uzor:
        row = ''
        for shtuk in range(2):       #количество штук узоров
            for i in line:
                if i == '#':
                    row += pink + '  ' + end
                else:
                    row += '  '
            row+='   '
        print(row)

def kadr(color):
    for line in uzor:
        row = ''
        for i in line:
            if i == '#':
                row += color + '  ' + end
            else:
                row += '  '
        print(row)

def animation():
    colors=[red,green,pink,white]
    for i in range(4):

        kadr(colors[i])
        print(f'\x1b[12;1HКадр{i+1}/4')
        time.sleep(1)
        os.system("clear")


def sequence():
    numbers = []
    file = open('sequence.txt', 'r')
    for line in file:
        numbers.append(float(line))
    sum1 = 0
    for x in numbers[:125]:
        sum1 += abs(x)
    sum2 = 0
    for x in numbers[125:250]:
        sum2 += abs(x)
    p1 = sum1 / (sum1 + sum2) * 100
    p2 = 100 - p1

    # 1 клетка = 2%
    n1 = round(p1 / 2)
    n2 = 50 - n1

    print(pink + " " * n1 + end + white + " " * n2 + end)
    print(pink + "  " + end, "первые 125:", round(p2, 2), "%")
    print(white + "  " + end, "вторые 125:", round(p2, 2), "%")

def dop():
    esc="\033"
    row0 = 15
    col0 = 5
    for y in range(0, 13):   # ось y (13 строк в высоту)
        print(esc + "[" + str(row0 - y) + ";" + str(col0) + "H|")
    for c in range(0, 25):  # ось x
        print(esc + "[" + str(row0) + ";" + str(col0 + c) + "H-")
    print(esc + "[" + str(row0) + ";" + str(col0) + "H0")   # начало координат
    print(esc + "[" + str(row0 - 13) + ";" + str(col0) + "Hy")  # подписи осей
    print(esc + "[" + str(row0 + 1) + ";" + str(col0 + 25) + "Hx")  # подписи осей

    for c in range(1, 19):  # график y = 2x + 3 (4 столбца = 1 единица x)
        x = c / 4
        y = round(2 * x + 3)
        if y <= 12:
            print(esc + "[" + str(row0 - y) + ";" + str(col0 + c) + "H" + pink + "." + end)
        print(esc + "[" + str(row0 + 3) + ";1H")  # курсор вниз
