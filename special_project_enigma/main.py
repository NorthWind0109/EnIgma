import string
import eel

abc = list(string.ascii_uppercase)#Весь английский алфавит ввиде списка


class thirdRotor:
    def __init__(self):
        self.dictionary = [(3, 7), (19, 2), (11, 8), (5, 17 ), (14, 25),
                           (21, 12), (16, 18 ), (22, 20 ), (18, 16), (24, 14),
                           (9, 23), (23, 3), (8, 4), (13, 10), (1, 21), (12, 26),
                           (6, 15 ), (10, 22), (17, 6), (15, 13 ),
                           (2, 9), (7, 19), (25, 24 ), (20, 5), (4, 11), (26, 1)]#Пример начального соеденения букв,
        # конечно же примеры соединений могут различаться, НО для того чтобы кодировать и декодировать у машин подобный список должен быть одинаковым
        self.code_position = 0  #Стартовая позиция шифровки
        self.decode_position = 0 #Стартовая позиция дешифровки

    def code(self, input, direction): #direction - направление
        self.code_position = self.code_position + 1 #поворот ротора после кодировки
        if self.code_position > 26:
            self.code_position = self.code_position - 26#поворот ротора если он больше 26
        search = self.cykleSearch((input + self.code_position))# переменная говорит о том под каким номером букву нам надо искать для шифровки
        result = 0
        for i in range(0, 26):
            if self.dictionary[i][switchDirection(direction)] == search:
                result = self.dictionary[i][direction]
        return result

    def decode(self, input, direction):
        self.decode_position = self.decode_position + 1
        if self.decode_position > 26:
            self.decode_position = self.decode_position - 26
        real_position = self.decode_position
        if direction == 0:
            real_position = real_position + 1
        else:
            real_position = real_position - 1
            #конструкция расшифровает 2ую позицию для нахождения 1
        for i in range(0, 26):
            if self.dictionary[i][switchDirection(direction)] == input:
                result = self.dictionary[i][direction] - real_position
                while result <= 0:
                    result = result + 26
        return result

    def cykleSearch(self, search):
        while search > 26:
            search = search - 26
        return search


class stator:
    def __init__(self):
        self.dictionary = [(5, 24), (14, 19), (9, 23), (26, 13), (22, 7),
                           (20, 12), (17, 1), (21, 25), (16, 2), (18, 3),
                           (11, 8), (10, 6), (4, 15), (24, 5), (19, 14),
                           (23, 9), (13, 26), (7, 22), (12, 20), (1, 17),
                           (25, 21), (2, 16), (3, 18), (8, 11), (6, 10), (15, 4)]#Пример начального соеденения букв,
        # конечно же примеры соединений могут различаться, НО для того чтобы кодировать и декодировать у машин подобный список должен быть одинаковым

    def find(self, input):#в статоре 13 пар, но для удобства мы используем 26, чтобы не работать над направлением
        for i in range(0, 26):
            if self.dictionary[i][0] == input:
                return self.dictionary[i][1]


class secondRotor: #Аналогично как и с 1 ротором
    def __init__(self):
        self.dictionary = [(18, 8), (4, 6), (13, 5), (23, 24), (12, 25),
                           (19, 21), (2, 14), (24, 16), (3, 19), (7, 1),
                           (10, 23), (6, 2), (20, 13), (15, 12), (14, 10),
                           (5, 20), (17, 3), (16, 17), (9, 22),
                           (25, 15), (11, 18), (8, 26), (1, 7),
                           (21, 9), (22, 11), (26, 4)]
        self.code_position = 0
        self.decode_position = 0

    def code(self, input, direction): #Кодирует букву
        self.code_position = self.code_position + 1
        real_position = self.code_position

        search = self.cykleSearch(input + self.cycleItterator(real_position))
        result = 0
        for i in range(0, 26):
            if self.dictionary[i][switchDirection(direction)] == search:
                result = self.dictionary[i][direction]
        return result

    def decode(self, input, direction):#декодирует букву
        self.decode_position = self.decode_position + 1

        real_position = self.decode_position
        if direction == 0:
            real_position = real_position + 1
        else:
            real_position = real_position - 1
        for i in range(0, 26):
            if self.dictionary[i][switchDirection(direction)] == input:
                result = self.dictionary[i][direction] - self.cycleItterator(real_position)
                while result <= 0:
                    result = result + 26
        return result

    def cycleItterator(self, itterator):#второй ротор будет вращаться при соблюдении условий, то есть каждый 26 прокрут 1 ротора
        while itterator > 26:
            itterator = itterator // 26
        return itterator

    def cykleSearch(self, search):
        while search > 26:
            search = search - 26
        return search


class firstRotor:#Аналогично как и с 1 ротором
    def __init__(self):
        self.dictionary = [(24, 19), (19, 20), (5, 13), (6, 7), (2, 5),
                           (15, 25), (8, 17), (9, 4), (20, 10), (12, 11),
                           (25, 23), (11, 6), (18, 8), (23, 2), (21, 16),
                           (16, 26), (26, 1), (7, 21), (3, 3), (4, 12),
                           (14, 15), (22, 9), (17, 24), (13, 22), (1, 14), (10, 18)]
        self.code_position = 0
        self.decode_position = 0

    def code(self, input, direction):
        self.code_position = self.code_position + 1
        real_position = self.code_position

        search = self.cykleSearch(input + self.cycleItteratorSqrt(real_position))
        result = 0
        for i in range(0, 26):
            if self.dictionary[i][switchDirection(direction)] == search:
                result = self.dictionary[i][direction]
        return result

    def decode(self, input, direction):
        self.decode_position = self.decode_position + 1

        real_position = self.decode_position
        if direction == 0:
            real_position = real_position + 1
        else:
            real_position = real_position - 1
        for i in range(0, 26):
            if self.dictionary[i][switchDirection(direction)] == input:
                result = self.dictionary[i][direction] - self.cycleItteratorSqrt(real_position)
                while result <= 0:
                    result = result + 26
        return result

    def cycleItteratorSqrt(self, itterator):#третий ротор будет вращаться при соблюдении условий, то есть при 26 прокрутках 2 ротора
        if itterator // (26 * 26) > 1:
            while itterator > (26 * 26):
                itterator = itterator // (26 * 26)
        else:
            itterator = itterator // (26 * 26)
        return itterator

    def cykleSearch(self, search):
        while search > 26:
            search = search - 26
        return search


rotor_3 = thirdRotor()
rotor_2 = secondRotor()
rotor_1 = firstRotor()
stator = stator()


def crypt_word(word):#Сама функция делит слово на буквы и каждой букву кодирует
    result = list()
    for letter in word:
        result.append(codeByRotors(letter))
    return result


def decrypt_word(word):#Функция разбивает слово на буквы, декриптит каждую букву слова
    result = list()
    for letter in word:
        result.append(decodeByRotors(letter))
    return result


def codeByRotors(letter):#вызов методов шифрования
    number = abc.index(letter) + 1
    thirdRtl = rotor_3.code(number, 0)
    secondRtl = rotor_2.code(thirdRtl, 0)
    firstRtl = rotor_1.code(secondRtl, 0)
    statorRtl = stator.find(firstRtl)
    firstLtr = rotor_1.code(statorRtl, 1)
    secondLtr = rotor_2.code(firstLtr, 1)
    thirdLtr = rotor_3.code(secondLtr, 1)
    result = thirdLtr

    return abc[result - 1]


def decodeByRotors(letter):#вызов методов дешифровки
    number = abc.index(letter) + 1
    thirdRtl = rotor_3.decode(number, 0)
    secondRtl = rotor_2.decode(thirdRtl, 0)
    firstRtl = rotor_1.decode(secondRtl, 0)
    statorRtl = stator.find(firstRtl)
    firstLtr = rotor_1.decode(statorRtl, 1)
    secondLtr = rotor_2.decode(firstLtr, 1)
    thirdLtr = rotor_3.decode(secondLtr, 1)
    result = thirdLtr

    return abc[result - 1]


def switchDirection(direction):
    return 0 if direction == 1 else 1


def configureMachine(action, frtRrStart, sndRrStart, trdRrStart):
    if action == '1':
        rotor_1.code_position = frtRrStart
        rotor_2.code_position = sndRrStart
        rotor_3.code_position = trdRrStart
    elif action == '2':
        rotor_1.decode_position = frtRrStart
        rotor_2.decode_position = sndRrStart
        rotor_3.decode_position = trdRrStart


def runMachine(action, stringByWords):
    result = ''
    strg = ''
    if action == '1':
        for word in stringByWords:
            crypted = crypt_word(word)
            result += strg.join(crypted)
            result += ' '
    elif action == '2':
        for word in stringByWords:
            uncr = decrypt_word(word)
            result += strg.join(uncr)
            result += ' '
    return result


@eel.expose
def process(frtRrStart, sndRrStart, trdRrStart, inputString, action):
    inputString = inputString.upper()#принимаем буквы в любом регистре и переводим их в верхний регистр
    stringByWords = inputString.split()#разбиваем текст на слова, делим их пробелами. +сохраняем их в списках
    if action and frtRrStart and sndRrStart and trdRrStart:
        configureMachine(action, int(frtRrStart), int(sndRrStart), int(trdRrStart))
        result = runMachine(action, stringByWords)
        return result
    else:
        return 'Ошибка'


eel.init('interface')
eel.start('enigma.html', size=(1200, 1200))

