def rgb(html):
    def hextodec(n): #funkcja zamieniająca system 16 na jedną część trypletu rgb
        d = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
        result = ''
        x = n[0] #bierzemy literę lub cyfrę leżącą na 1. miejscu n
        y = n[1] #bierzemy literę lub cyfrę leżącą na 2. miejscu n
        result = d[x]*16 + d[y] #zamiana na system dziesiętny
        return result
    red = html[1:3] #ucinamy poszeczególne fragmenty html na tryplet rgb
    green = html[3:5]
    blue = html[5:7]
    rgb = f'{hextodec(red)},{hextodec(green)},{hextodec(blue)}' 
    return rgb
print(rgb('#FF0005'))
    
