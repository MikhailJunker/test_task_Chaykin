# Реализация кольцевого буфера на основе линейного списка (использование стандартного типа - list)
class BufferByLinearList:

    __MAX_SIZE = 16

    def __init__(self):
        self.__size = 0
        self.__buffer = [-1 for c in range(BufferByLinearList.__MAX_SIZE)]
        self.__indexToWrite = 0
        self.__indexToRead = 0

    def push(self, value):
        self.__buffer[self.__indexToWrite] = value
        if self.__size == BufferByLinearList.__MAX_SIZE:
            self.__indexToRead = (self.__indexToRead + 1) % BufferByLinearList.__MAX_SIZE
        else:
            self.__size += 1
        self.__indexToWrite = (self.__indexToWrite + 1) % BufferByLinearList.__MAX_SIZE

    def pop(self):
        if self.__size == 0:
            return None
        popElement = self.__buffer[self.__indexToRead]
        self.__indexToRead = (self.__indexToRead + 1) % BufferByLinearList.__MAX_SIZE
        self.__size -= 1
        return popElement

    def isEmpty(self):
        return self.__size == 0

    def show(self):
        if self.__indexToRead >= self.__indexToWrite and self.__size > 0:
            print(self.__buffer[self.__indexToRead:] + self.__buffer[:self.__indexToWrite])
        else:
            print(self.__buffer[self.__indexToRead:self.__indexToWrite])


# Реализация элемента кольцевого списка
class Element:

    def __init__(self):
        self.__value = -1
        self.__next = None

    def setValue(self, value):
        self.__value = value

    def setNext(self, link):
        self.__next = link

    def getValue(self):
        return self.__value

    def getNext(self):
        return self.__next


# Реализация кольцевого буфера в виде одностороннего кольцевого списка, где каждый элемент содержит 2 поля:
# 1) Value - значение элемента
# 2) Next - указатель на следующий элемент в кольцевом списке (последний элемент в списке указывает на первый элемент)
class BufferByRingList:

    __MAX_SIZE = 16

    def __init__(self):
        self.__size = 0
        self.__linkToWrite = Element()
        self.__linkToRead = self.__linkToWrite
        lastEl = self.__linkToWrite
        for i in range(BufferByRingList.__MAX_SIZE - 1):
            el = Element()
            lastEl.setNext(el)
            lastEl = el
        lastEl.setNext(self.__linkToWrite)

    def push(self, value):
        self.__linkToWrite.setValue(value)
        if self.__size == BufferByRingList.__MAX_SIZE:
            self.__linkToRead = self.__linkToRead.getNext()
        else:
            self.__size += 1
        self.__linkToWrite = self.__linkToWrite.getNext()

    def pop(self):
        if self.__size == 0:
            return None
        popElement = self.__linkToRead.getValue()
        self.__linkToRead = self.__linkToRead.getNext()
        self.__size -= 1
        return popElement

    def isEmpty(self):
        return self.__size == 0

    def show(self):
        currentLink = self.__linkToRead
        buffer = []
        while currentLink != self.__linkToWrite or (len(buffer) == 0 and self.__size == BufferByRingList.__MAX_SIZE):
            buffer.append(currentLink.getValue())
            currentLink = currentLink.getNext()
        print(buffer)



# bufferByLinearList = BufferByLinearList()
# bufferByLinearList.show()
# for i in range(20):
#     bufferByLinearList.push(i)
# bufferByLinearList.show()
# for i in range(40):
#     bufferByLinearList.pop()
# bufferByLinearList.show()

# bufferByRingList = BufferByRingList()
# bufferByRingList.show()
# for i in range(20):
#     bufferByRingList.push(i)
# bufferByRingList.show()
# for i in range(40):
#     bufferByRingList.pop()
# bufferByRingList.show()



######################################################################
#
# Реализация в виде линейного списка:
#   +:
#     1) Простота реализации (достаточно использовать стандартный тип - list)
#
#   -:
#     1) Требуются преобразования индексов (взятие по модулю размера буфера)

# Реализация в виде кольцевого списка:
#   +:
#     1) Интуитивно понятна (КОЛЬЦЕВОЙ буфер логично реализовывать КОЛЬЦЕВЫМ списком)
#     2) Не требует преобразований индексов элементов (взятие по модулю размера буфера). Работа ведется только
#        с указателями на следующий элемент
#
#   -:
#     1) Требуется дополнительная реализация класса элемента кольцевого списка
#     2) Список реализуется самостоятельно, что менее предпочтительно в сравнении с готовой реализацией стандартного
#        типа - list
#
######################################################################