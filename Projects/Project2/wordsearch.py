# Name: Jacob Wren
# Course:       CPE 101
# Instructor:   Irene Humer
# Assignment:   WordSearch Project
# Term:         Winter 2020

def main():
    chars = str(input() )
    width = int(len(chars) ** .5)
    search = str(input() ) + " "
    w = ""
    L = ""
    for j in range(0, len(chars), width):
        for i in range(j, width + j):
            L = L + chars[i]
        print(L)
        L = ""
    print()
    for t in search:
        if t != " ":
            w = w + t
        if t == " ":
            search = w
            print_(chars, search, width)       
        if t == " ":
            w = ""

            
def print_(chars, search, width):
    if forward(chars, search) is not None:
        print("{0:>{2}}: [FF] ({1})".format(search, forward(chars, search), width ))
    if backward(chars, search) is not None:
        print("{0:>{2}}: [BB] ({1})".format(search, backward(chars, search), width ))        
    if upward(chars, search) is not None:
        print("{0:>{2}}: [UU] ({1})".format(search, upward(chars, search) , width)   )
    if downward(chars, search) is not None:
        print("{0:>{2}}: [DD] ({1})".format(search, downward(chars, search), width ))
    if DD(chars, search) is not None:
        print("{0:>{2}}: [FD] ({1})".format(search, DD(chars, search), width ))
    if DU(chars, search) is not None:
        print("{0:>{2}}: [BU] ({1})".format(search, DU(chars, search), width ))
    if Rev_DD(chars, search) is not None:
        print("{0:>{2}}: [BD] ({1})".format(search, Rev_DD(chars, search), width ))
    if Rev_DU(chars, search) is not None:
        print("{0:>{2}}: [FU] ({1})".format(search, Rev_DU(chars, search), width ))       
               
    
def forward(chars, search):
    index = chars.find(search)
    width = int((len(chars)) ** (1 / 2))
    if index != -1:
        row = index // width
        col = index % width
        return str(row) + ", " + str(col)


def backward(chars, search):
    width = int((len(chars)) ** (1 / 2))
    Rev_string = ""
    for i in chars:
        Rev_string = i + Rev_string 
    #Rev_string = chars[::-1]
    index = Rev_string.find(search)
    Og_index = len(chars) - index - 1
    if index != -1:
        row = Og_index // width
        col = Og_index % width
        return str(row) + ", " + str(col)


def upward(chars: str, search: str) -> str:
    width = int((len(chars)) ** (1 / 2))
    n = int( len(chars) / width)
    t = 0
    L = ""
    for i in range(width):
        for j in range(t, len(chars), width):
            L = chars[j] + L  
        index = L.find(search)
        if index != -1:
            return str(width - 1 - index) + ", " + str(t)
        L = ""
        t = t + 1


def downward(chars: str, search: str) -> str:
    width = int((len(chars)) ** (1 / 2))
    n = int( len(chars) / width)
    t = 0
    L = ""
    for i in range(width):
        for j in range(t, len(chars), width):
            L = L + chars[j] 
        index = L.find(search)
        if index != -1:
            return str(index) + ", " + str(t)
        L = ""
        t = t + 1


def DD_right(chars: str, search: str) -> str:
    width = int((len(chars)) ** (1 / 2))
    n = int( len(chars) / width)
    t = 1
    L = ""
    end = len(chars)
    for i in range(width - 2):   
        for j in range(t, end, width + 1):
            L = L + chars[j] 
        index = L.find(search)
        end = end - width
        if index != -1:
            return str(index) + ", " + str(t + index)
        L = ""
        t = t + 1


def DD_left(chars: str, search: str) -> str:
    width = int((len(chars)) ** (1 / 2))
    n = int( len(chars) / width)
    L = ""
    j = 0
    for i in range(width - 1):    
        for k in range(j, len(chars), width + 1):
            L = L + chars[k] 
        index = L.find(search)
        if index != -1:
            return str(index + i) + ", " + str(index)
        L = ""
        j = j + width


def DD(chars: str, search: str) -> str:
    if DD_right(chars, search) is not None:
        return DD_right(chars, search)
    if DD_left(chars, search) is not None:
        return DD_left(chars, search)


def DU_right(chars: str, search: str) -> str:
    width = int((len(chars)) ** (1 / 2))
    n = int( len(chars) / width)
    t = 1
    L = ""
    end = len(chars)
    for i in range(width - 2):   
        for j in range(t, end, width + 1):
            L = chars[j] + L
        index = L.find(search)
        end = end - width
        if index != -1:
            return str(len(L) - 1 - index) +  ", " + str(width - 1 - index)
        L = ""
        t = t + 1


def DU_left(chars: str, search: str) -> str:
    width = int((len(chars)) ** (1 / 2))
    n = int( len(chars) / width)
    L = ""
    j = 0
    for i in range(width - 1):    
        for k in range(j, len(chars), width + 1):
            L = chars[k] + L
        index = L.find(search)
        if index != -1:
            return str(width - index - 1) + ", " + str(len(L) - index - 1)
        L = ""
        j = j + width


def DU(chars: str, search: str) -> str:
    if DU_right(chars, search) is not None:
        return DU_right(chars, search)
    if DU_left(chars, search) is not None:
        return DU_left(chars, search)



def Rev_DD_right(chars: str, search: str) -> str:
    width = int((len(chars)) ** (1 / 2))
    t = width - 2
    L = ""
    end = len(chars) - width - 1
    for i in range(width - 2):   
        for j in range(t, end, width - 1):
            L = L + chars[j] 
        index = L.find(search)
        if index != -1:
            return str(index) + ", " + str(t - index)
        end = end - width
        L = ""
        t = t - 1


def Rev_DD_left(chars: str, search: str) -> str:
    width = int((len(chars)) ** (1 / 2))
    n = int( len(chars) / width)
    L = ""
    j = width - 1
    end = len(chars) - width + 1
    for i in range(width - 1):    
        for k in range(j, end, width - 1):
            L = L + chars[k] 
        index = L.find(search)
        if index != -1:
            return str(index + i) + ", " + str(width - 1 - index)
        L = ""
        j = j + width 
        end = end + 1


def Rev_DD(chars: str, search: str) -> str:
    if Rev_DD_right(chars, search) is not None:
        return Rev_DD_right(chars, search)
    if Rev_DD_left(chars, search) is not None:
        return Rev_DD_left(chars, search)


def Rev_DU_right(chars: str, search: str) -> str:
    width = int((len(chars)) ** (1 / 2))
    t = width - 2
    L = ""
    end = len(chars) - width - 1
    for i in range(width - 2):   
        for j in range(t, end, width - 1):
            L = chars[j] + L
        index = L.find(search)
        if index != -1:
            return str(len(L) - 1 - index) + ", " + str(index)
        end = end - width
        L = ""
        t = t - 1


def Rev_DU_left(chars: str, search: str) -> str:
    width = int((len(chars)) ** (1 / 2))
    n = int( len(chars) / width)
    L = ""
    j = width - 1
    end = len(chars) - width + 1
    for i in range(width - 1):    
        for k in range(j, end, width - 1):
            L = chars[k] + L
        index = L.find(search)
        if index != -1:
            return str(width - index - 1) + ", " + str(i + index)
        L = ""
        j = j + width 
        end = end + 1


def Rev_DU(chars: str, search: str) -> str:
    if Rev_DU_right(chars, search) is not None:
        return Rev_DU_right(chars, search)
    if Rev_DU_left(chars, search) is not None:
        return Rev_DU_left(chars, search)


if __name__ == "__main__":
    main()
