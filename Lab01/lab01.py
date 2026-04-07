#! /usr/bin/python3

# ********************************************************
# Нэр: Dagiimaa Batjargal (23B1NUM1527)
# И-мэйл хаяг: dagiimaaba89@gmail.com
# ********************************************************

# Энэ файлыг Python 3 дээр нээж ажиллуулна.
# # тэмдэгтээр эхэлсэн мөрүүд нь тайлбар (comment).

# Хэрвээ та функц/процедур бичих даалгавартай бол:
# - Заасан НЭР-ээр нь (function name)
# - Заасан тоо, дарааллын аргументтайгаар нь бичээрэй.
# Албан аргументын нэр (formal argument) нь жишээн дээрхтэй адил байх албагүй.

# Даалгавар бүр дээр оруулах утгуудын төрөл заагдсан байдаг
# (жишээ нь “эерэг бүхэл тоо”). Өөр төрлийн/хэмжээний утга өгвөл
# оновчтой ажиллах шаардлагагүй.

# Та нэмэлт туслах функцууд бичиж болно.
# Туслах функц бүрийн хувьд:
# - юу хийдгийг нь тайлбарласан comment
# - 1–2 жишээ нэмээрэй.

# Өмнөх лаборатори/даалгавраар бичсэн функцээ энэ файл дотор ашиглаж болно.
# Зөвхөн нэг удаа энэ файл дотор тодорхойлогдсон байхад хангалттай.

'''
Зорилго: Python хэлний суурь ойлголтууд дээр хурдан дадлага хийх.

Хэрэгтэй үед унших материалууд:
- Learning Python
- Python Cookbook
- Effective Python
- Google Python Class (онлайн)
'''

# ********************************************************
# ** бодлого 0 ** (1 амархан оноо)
# Доорх функц доторх 0 (эсвэл тоо)-г солиж,
# энэ даалгаварт зарцуулсан цагаа (цаг нэгжээр) оруулна уу.
# Аравтын бутархай тоо байж болно (жишээ: 6.237).
# Уншиж судалсан хугацааг бүү тооцоорой.

def hours():
    return 3.5


# ********************************************************
# ** бодлого 1 ** (9 оноо)
# sum_digits(n) нэртэй функц бич.
# Оролт: эерэг бүхэл тоо n
# Гаралт: n тооны цифрүүдийн нийлбэр

# Жишээ:
# sum_digits(13) => 4
# sum_digits(1000000) => 1
# sum_digits(123456789) => 45
# sum_digits(9) => 9

# ********************************************************
# pass мөрийг өөрийн хэрэгжүүлэлтээр солино.
def sum_digits(n):
    if (n < 0):
        print("eyreg too oruul!")
    else:
        sum = 0
        while n > 0:
            remainder = n % 10
            sum = sum + remainder
            n = n // 10;
        return sum

# ********************************************************
# ** бодлого 2 ** (10 оноо)
# reduce(n) нэртэй РЕКУРСИВ функц бич.
# Оролт: эерэг бүхэл тоо n
# n-ийн цифрүүдийн нийлбэрийг давтан бодсоор үр дүн нь 10-аас бага болтол
# үргэлжлүүлнэ.
# Зөвлөмж: reduce дотроо sum_digits-ийг дуудах нь тохиромжтой.

# Жишээ:
# reduce(123455667888) => 9
# reduce(9999) => 9
# reduce(8888) => 5
# reduce(10101010019999) => 5

# ********************************************************
def reduce(n):
    if n < 0:
        print("eyreg too oruul!")
        return
    else:
        s = sum_digits(n)
        if s < 10:
            return s
        else:
            return reduce(s)

# ********************************************************
# ** бодлого 3 ** (10 оноо)
# removep(lst, pred) нэртэй функц бич.
# Оролт:
# - lst: жагсаалт
# - pred: predicate функц (lambda эсвэл өөр функц)
# Гаралт: pred нөхцлийг ХАНГАСАН элементүүдийг хассан шинэ жагсаалт.

# Жишээ:
# removep([1,2,3,4,5,6], lambda x: x % 2 == 0) => [1,3,5]
# removep([1,2,3,4,5,6], lambda x: x % 2) => [2,4,6]
# removep([1,2,3,4,5,6], lambda a: a > 3) => [1,2,3]
# removep([1,2,3,4,5,6], lambda a: a < 3) => [3,4,5,6]

# ********************************************************
def removep(lst, pred):
    result = []

    for i in lst:
        if pred(i) == False:
            result.append(i)

    return result

# Дээрхтэй адил функцийг list comprehension ашиглан бич:
def lcremovep(lst, pred):
    return [x for x in lst if not pred(x)]

# ********************************************************
# ** бодлого 4 ** (10 оноо)
# collectp(lst, pred) нэртэй функц бич.
# Оролт:
# - lst: жагсаалт
# - pred: predicate функц
# Гаралт: pred нөхцлийг ХАНГАСАН элементүүдийг л агуулсан шинэ жагсаалт.

# Жишээ:
# collectp([1,2,3,4,5,6], lambda x: x%2 == 0) => [2,4,6]
# collectp([1,2,3,4,5,6], lambda x: x % 2) => [1,3,5]
# collectp([1,2,3,4,5,6], lambda a: a > 3) => [4,5,6]
# collectp([1,2,3,4,5,6], lambda a: a < 3) => [1,2]

# ********************************************************
def collectp(lst, pred):
    result = []
    for i in lst:

        if pred(i) == True:
            result.append(i)

    return result

# Дээрхтэй адил функцийг list comprehension ашиглан бич:
def lccollectp(lst, pred):
    return [i for i in lst if pred(i)]

# ********************************************************
# ** бодлого 5 ** (10 оноо)
# power_set(lst) нэртэй функц бич.
# lst-ийг set шиг (давхардалтай байж болно гэдгийг анхаар) авч үзээд
# боломжит бүх subset-үүдийг (дэд олонлог) жагсаалт хэлбэрээр буцаана.

'''
Жишээ:
power_set([]) => [[]]
power_set([1]) => [[], [1]]
power_set([1,2]) => [[], [2], [1], [1,2]]
power_set([1,2,3]) => [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
power_set([1,2,3,4]) =>
[[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 4], [1, 3], [1, 3, 4],
 [1, 4], [2], [2, 3], [2, 3, 4], [2, 4], [3], [3, 4], [4]]
power_set([2,2]) => [[], [2], [2], [2, 2]]
'''
# itertools модулийг ашиглаж болно.
def power_set(lst):
    result = [[]] 

    for item in lst:
        new_subsets = []

        for existing_subset in result:
            new_subset = existing_subset + [item]
            new_subsets.append(new_subset)

        result = result + new_subsets

    try:
        result.sort()
    except TypeError:
        pass

    return result

# ********************************************************
# ** бодлого 6 ** (10 оноо)
# sumtree(tree) нэртэй функц бич.
# Оролт: nested list (мод хэлбэрийн жагсаалт) tree
# Гаралт: хамгийн доод түвшний (leaf) бүхэл тоонуудын нийлбэр.
# Анхаар: leaf бүр заавал int байх албагүй — int биш бол үл тооцно.

# Жишээ:
# sumtree([1, 2, 3]) => 6
# sumtree([1, [2, [3]]]) => 6
# sumtree([[[]]]) => 0
# sumtree([[[[2]]]]) => 2
# sumtree([1,"2","3",4, False, []]) => 5

# ********************************************************
def sumtree(tree):
    total = 0

    for i in tree:
        if type(i) == list:
            total += sumtree(i)
        elif type(i) == int and type(i) != bool:
            total += i

    return total

# ********************************************************
# ** бодлого 7 ** (10 оноо)
# doubletree(tree) нэртэй функц бич.
# Оролт: nested list tree
# Гаралт: бүтэц нь ижил боловч leaf бүрийг 2-оор үржүүлсэн (давхарласан) шинэ tree.
# Анхаар: leaf бүр int байх албагүй — int биш бол өөрчлөхгүйгээр буцаана.

# Жишээ:
# doubletree([1, 2, 3]) => [2,4,6]
# doubletree([1, [2, [3]]]) => [2, [4, [6]]]
# doubletree([1, 2, 3, "4", ["6"], True]) => [2, 4, 6, '4', ['6'], True]

# ********************************************************
def doubletree(tree):
    result = []

    for i in tree:
        if type(i) == list:
            result = result + [doubletree(i)]
        elif type(i) == int and type(i) != bool:
            result = result + [i * 2]
        else:
            result = result + [i]

    return result

# ********************************************************
# ** бодлого 8 ** (10 оноо)
# types(tree) нэртэй функц бич.
# Оролт: nested list tree
# Гаралт: leaf node-уудын дата төрлүүдийн нэрсийг (type нэр)
# давхардалгүйгээр авч, цагаан толгойн дарааллаар буцаана.

# Жишээ:
# types([1, [2.3, "a"], True, 3]) => ['bool', 'float', 'int', 'str']
# types([1,2,3,4, True, "hello", 1.2, {}, (1,2,3)]) => ['bool', 'dict', 'float', 'int', 'str', 'tuple']

# ********************************************************
def types(tree):
    found_types = []

    for item in tree:
        if isinstance(item, list):
            inner_types = types(item)
            for t in inner_types:
                if t not in found_types:
                    found_types.append(t)
        else:
            type_name = type(item).__name__
            if type_name not in found_types:
                found_types.append(type_name)

    found_types.sort()
    return found_types

# ********************************************************
# Класс ашиглалтын нийтлэг жишээ: өгөгдлийн бүтэц (data structure) хэрэгжүүлэх.
# Доорх нь stack-ийн (LIFO — last in, first out) жишээ.
# Элемент нэмэх: push
# Элемент авах: pop
# -----------------------------------------------------------
class stack:

    def __init__(self, stuff=[]):
        self.items = stuff[:]
        self.size = len(stuff)

    def __repr__(self):
        return "stack({})".format(list(self.items))

    def isempty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        self.size += 1

    def peek(self):
        if self.isempty():
            return "Error: stack is empty"
        else:
            return self.items[-1]

    def pop(self):
        if self.isempty():
            return "Error: stack is empty"
        else:
            self.size -= 1
            return self.items.pop()

    # Дээд талын 2 элементийг солих
    def rotate(self):
        if self.size < 2:
            return "Error: stack has fewer than 2 elements"
        else:
            self.items[-1], self.items[-2] = self.items[-2], self.items[-1]

    # Итератор тодорхойлолт (for / list comprehension дээр ашиглагдана)
    def __iter__(self):
        """Stack-ийн iterator."""
        if self.isempty():
            return None
        else:
            index = self.size - 1
            while index >= 0:
                yield self.items[index]
                index -= 1

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.items == other.items

    # Copy constructor — одоогийн instance-ийг хуулбарлах
    def copy(self):
        return stack(self.items)


# Iterator тест
def itest(s):
    for i in s:
        print(i)
    return [x for x in s]


# stack ашиглан string-г урвуу болгох
def revstr(str):
    s = stack()
    for c in str:
        s.push(c)
    result = []
    while not s.isempty():
        result.append(s.pop())
    return ''.join(result)


# ********************************************************
# ** бодлого 9 ** (10 оноо)
# balanced(string) нэртэй функц бич.
# string доторх хаалтнууд ( ) тэнцвэртэй (balanced) эсэхийг шалгана.
# Зөвлөмж:
# - Зүүн хаалт '(' таарвал stack руу push
# - Баруун хаалт ')' таарвал stack-аас pop хийгээд таарч байгаа эсэхийг шалга
# Эцэст нь stack хоосон байвал balanced гэж үзнэ.

def balanced(string):
    s = stack()
    for ch in string:
        if ch == '(':
            s.push(ch)
        elif ch == ')':
            if s.isempty():
                return False
            s.pop()
    return s.isempty()

# ********************************************************
# ** бодлого 10 ** (10 оноо)
# queue өгөгдлийн бүтцийг stack-тай төстэй байдлаар хэрэгжүүл.
# Stack нь LIFO бол queue нь FIFO (first in, first out).
# Skiena номын 71-р хуудас руу лавлаж болно.

class queue:
    def __init__(self, stuff=[]):
        self.data = stuff[:] 

    def __str__(self):
        return "queue({})".format(self.data)

    def __repr__(self):
        return "queue({})".format(self.data)

    def isempty(self):
        # Queue хоосон эсэхийг шалгана
        return self.data == []

    def enqueue(self, item):
        # Queue-ийн сүүл талд шинэ элемент нэмнэ
        self.data.append(item)

    def dequeue(self):
        # Queue-ийн эхний элементийг авна (устгана)
        if self.isempty():
            return 'queue is empty'
        return self.data.pop(0)  # pop(0) = эхний элементийг авна

    def peek(self):
        # Queue-ийн эхний элементийг харна (авахгүй)
        if self.isempty():
            return 'queue is empty'
        return self.data[0]

    def __iter__(self):
        # Элемент бүрийг дарааллаар гаргана
        for item in self.data:
            yield item

    def __eq__(self, other):
        if type(other) != type(self):
            return False
        return self.data == other.data

    def copy(self):
        return queue(self.data)


# ********************************************************
# ** нэмэлт дасгал 11 ** (8 оноо)
# flatten(tree) нэртэй функц бич.
# Оролт: nested list tree
# Гаралт: tree-ийн бүх leaf-үүдийг зүүнээс баруун чиглэлээр шулуужуулж
# нэг түвшний жагсаалт болгон буцаана.
# Анхаар:
# - leaf нь ямар ч төрлийн утга байж болно (int/str/bool/tuple/…).
# - List биш leaf бол шууд үр дүнд орно.

# Жишээ:
# flatten([1, [2, [3, 4]], 5]) => [1, 2, 3, 4, 5]
# flatten([[[]]]) => []
# flatten([1, "a", [True, [2.5]]]) => [1, 'a', True, 2.5]
def flatten(tree):
    result = []

    for item in tree:
        if isinstance(item, list):
            flat_inner = flatten(item)
            for x in flat_inner:
                result.append(x)
        else:
            result.append(item)

    return result

# ********************************************************
# ** нэмэлт дасгал 12 ** (6 оноо)
# countp(lst, pred) нэртэй функц бич.
# Оролт: lst жагсаалт, pred predicate функц
# Гаралт: pred нөхцлийг хангаж буй элементүүдийн тоо

# Жишээ:
# countp([1,2,3,4,5,6], lambda x: x % 2 == 0) => 3
# countp([1,2,3,4], lambda x: x > 10) => 0

def countp(lst, pred):
    count = 0

    for i in lst:
        if pred(i) == True:
            count = count + 1

    return count


# ********************************************************
# ** нэмэлт дасгал 13 ** (6 оноо)
# unique(lst) нэртэй функц бич.
# Оролт: lst жагсаалт
# Гаралт: давхардлыг арилгасан шинэ жагсаалт (анхны эрэмбийг хадгална).

# Жишээ:
# unique([1,1,2,2,3,1]) => [1,2,3]
# unique(["a","b","a","c","b"]) => ['a','b','c']

def unique(lst):
    seen = []

    for i in lst:
        if i not in seen:
            seen.append(i)

    return seen


# ********************************************************
# ** нэмэлт дасгал 14 ** (8 оноо)
# is_palindrome(s) нэртэй функц бич.
# Оролт: тэмдэгт мөр s
# Гаралт: s нь палиндром (урвуугаар нь уншихад ижил) бол True, эс тэгвээс False.
# Том/жижиг үсгийг ялгахгүй (case-insensitive) шалгана.
# Зөвлөмж: revstr эсвэл stack ашиглаж болно.

# Жишээ:
# is_palindrome("level") => True
# is_palindrome("Level") => True
# is_palindrome("hello") => False
# is_palindrome("") => True

def is_palindrome(s):
    s = s.lower()

    reversed_s = ''
    i = len(s) - 1
    while i >= 0:
        reversed_s = reversed_s + s[i]
        i = i - 1

    return s == reversed_s


# ********************************************************
# ** нэмэлт дасгал 15 ** (12 оноо)
# eval_postfix(expr) нэртэй функц бич.
# Оролт: expr нь postfix (Reverse Polish Notation) илэрхийлэл бүхий string.
# Токенууд нь зайгаар тусгаарлагдсан байна.
# Дэмжих операторууд: +  -  *  /
# Гаралт: бодит тоон үр дүн (float эсвэл int).
# Зөвлөмж: stack ашиглах.

# Жишээ:
# eval_postfix("3 4 +") => 7
# eval_postfix("10 2 /") => 5
# eval_postfix("2 3 4 * +") => 14   (2 + 3*4)
# eval_postfix("5 1 2 + 4 * + 3 -") => 14

def eval_postfix(expr):
    s = stack()

    tokens = expr.split()

    for token in tokens:
        if token == '+':
            b = s.pop()
            a = s.pop()
            s.push(a + b)

        elif token == '-':
            b = s.pop()
            a = s.pop()
            s.push(a - b)

        elif token == '*':
            b = s.pop()
            a = s.pop()
            s.push(a * b)

        elif token == '/':
            b = s.pop()
            a = s.pop()
            answer = a / b
            if answer == int(answer):
                s.push(int(answer))
            else:
                s.push(answer)

        else:
            s.push(int(token))

    return s.pop()


# ********************************************************
# Google Python course-оос авсан энгийн test() функц
# main() дотор expected-тэй харьцуулж хэвлэнэ.
def test(got, expected):
    if hasattr(expected, '__call__'):
        ok = expected(got)
    else:
        ok = (got == expected)
    prefix = ' OK ' if ok else '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# ********************************************************
# main() — тестүүдийг ажиллуулна.
def main():
    print('hours')
    print('# 0-ээс их эсэх?')
    test(hours(), lambda x: x > 0)

    print('sum_digits')
    test(sum_digits(10), 1)
    test(sum_digits(13), 4)
    test(sum_digits(1000000), 1)
    test(sum_digits(123456789), 45)
    test(sum_digits(9), 9)

    print('reduce')
    test(reduce(123455667888), 9)
    test(reduce(9999), 9)
    test(reduce(8888), 5)
    test(reduce(10101010019999), 5)

    print('removep')
    test(removep(range(7), lambda x: x % 2 == 0), [1, 3, 5])
    test(removep(range(7), lambda x: x % 2), [0, 2, 4, 6])
    test(removep(range(7), lambda x: x > 3), [0, 1, 2, 3])
    test(removep(range(7), lambda x: x < 3), [3, 4, 5, 6])

    print('lcremovep')
    test(lcremovep(range(7), lambda x: x % 2 == 0), [1, 3, 5])
    test(lcremovep(range(7), lambda x: x % 2), [0, 2, 4, 6])
    test(lcremovep(range(7), lambda x: x > 3), [0, 1, 2, 3])
    test(lcremovep(range(7), lambda x: x < 3), [3, 4, 5, 6])

    print('collectp')
    test(collectp(range(7), lambda x: x % 2 == 0), [0, 2, 4, 6])
    test(collectp(range(7), lambda x: x % 2), [1, 3, 5])
    test(collectp(range(7), lambda x: x > 3), [4, 5, 6])
    test(collectp(range(7), lambda x: x < 3), [0, 1, 2])

    print('lccollectp')
    test(lccollectp(range(7), lambda x: x % 2 == 0), [0, 2, 4, 6])
    test(lccollectp(range(7), lambda x: x % 2), [1, 3, 5])
    test(lccollectp(range(7), lambda x: x > 3), [4, 5, 6])
    test(lccollectp(range(7), lambda x: x < 3), [0, 1, 2])

    print('power_set')
    test(power_set([]), [[]])
    test(power_set([1]), [[], [1]])
    test(sorted(power_set([1, 2])), sorted([[], [2], [1], [1, 2]]))
    test(sorted(power_set([1, 2, 3])),
         sorted([[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]))
    test(power_set([1, 2, 3, 4]),
         [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 4], [1, 3], [1, 3, 4],
          [1, 4], [2], [2, 3], [2, 3, 4], [2, 4], [3], [3, 4], [4]])
    test(power_set([2, 2]), [[], [2], [2], [2, 2]])

    toppings = ['onion', 'peppers', 'bacon', 'sausage', 'mushroom']
    test(power_set(toppings),
         [[], ['bacon'], ['bacon', 'mushroom'], ['bacon', 'sausage'],
          ['bacon', 'sausage', 'mushroom'], ['mushroom'], ['onion'],
          ['onion', 'bacon'], ['onion', 'bacon', 'mushroom'],
          ['onion', 'bacon', 'sausage'], ['onion', 'bacon', 'sausage', 'mushroom'],
          ['onion', 'mushroom'], ['onion', 'peppers'],
          ['onion', 'peppers', 'bacon'], ['onion', 'peppers', 'bacon', 'mushroom'],
          ['onion', 'peppers', 'bacon', 'sausage'],
          ['onion', 'peppers', 'bacon', 'sausage', 'mushroom'],
          ['onion', 'peppers', 'mushroom'], ['onion', 'peppers', 'sausage'],
          ['onion', 'peppers', 'sausage', 'mushroom'], ['onion', 'sausage'],
          ['onion', 'sausage', 'mushroom'], ['peppers'], ['peppers', 'bacon'],
          ['peppers', 'bacon', 'mushroom'], ['peppers', 'bacon', 'sausage'],
          ['peppers', 'bacon', 'sausage', 'mushroom'], ['peppers', 'mushroom'],
          ['peppers', 'sausage'], ['peppers', 'sausage', 'mushroom'], ['sausage'],
          ['sausage', 'mushroom']])

    print('sumtree')
    test(sumtree([1, 2, 3]), 6)
    test(sumtree([1, [2, [3]]]), 6)
    test(sumtree([[[]]]), 0)
    test(sumtree([[[[2]]]]), 2)
    test(sumtree([1, 2, 3, 4]), 10)
    test(sumtree([1, "2", "3", 4]), 5)
    test(sumtree([1, "2", "3", 4, False]), 5)
    test(sumtree([1, "2", "3", 4, False, []]), 5)

    print('doubletree')
    test(doubletree([1, 2, 3]), [2, 4, 6])
    test(doubletree([1, [2, [3]]]), [2, [4, [6]]])
    test(doubletree([]), [])
    test(doubletree([[[[8, 8, 8]]]]), [[[[16, 16, 16]]]])
    test(doubletree([1, 2, 3, "4", "5", ["6"]]), [2, 4, 6, '4', '5', ['6']])
    test(doubletree([1, 2, 3, "4", "5", ["6"], True]), [2, 4, 6, '4', '5', ['6'], True])

    print('types')
    test(types([1, [2.3, "a"], True, 3, 4, 5]), ['bool', 'float', 'int', 'str'])
    test(types([1, 2, 3, 4]), ['int'])
    test(types([1, 2, 3, 4, True, "hello"]), ['bool', 'int', 'str'])
    test(types([1, 2, 3, 4, True, "hello", 1, 2]), ['bool', 'int', 'str'])
    test(types([1, 2, 3, 4, True, "hello", 1.2]), ['bool', 'float', 'int', 'str'])
    test(types([1, 2, 3, 4, True, "hello", 1.2, {}]), ['bool', 'dict', 'float', 'int', 'str'])
    test(types([1, 2, 3, 4, True, "hello", 1.2, {}, (1, 2, 3)]),
         ['bool', 'dict', 'float', 'int', 'str', 'tuple'])

    print('stack')
    s = stack()
    s.push(1); s.push(2); s.push(3); s.push(4)
    test(s, stack([1, 2, 3, 4]))
    test(s == s.copy(), True)
    test([x for x in s], [4, 3, 2, 1])
    test(s.peek(), 4)
    test(3 in s, True)
    test(5 in s, False)
    test(s.pop(), 4)
    test(s.pop(), 3)
    test(s.peek(), 2)
    test(revstr('abcdef'), 'fedcba')
    test(revstr(''), '')

    print('balanced')
    test(balanced('dkdk'), True)
    test(balanced('()()()()'), True)
    test(balanced('()()()())'), False)
    test(balanced('()()()()(('), False)
    test(balanced('(a)s(d)f(g)gh(h)j(k'), False)

    print('queue')
    d = queue()
    d.enqueue(9); d.enqueue(1); d.enqueue(2)
    test(d == d.copy(), True)
    test(d.peek(), 9)
    test(d.data, [9, 1, 2])
    test([x for x in d], [9, 1, 2])
    test(2 in d, True)
    test(5 in d, False)
    test(d.dequeue(), 9)
    test(d.dequeue(), 1)
    test(d.dequeue(), 2)
    test(2 in d, False)
    test(d.dequeue(), 'queue is empty')

    # ----- Нэмэлт дасгалуудын тест -----
    print('flatten')
    test(flatten([1, [2, [3, 4]], 5]), [1, 2, 3, 4, 5])
    test(flatten([[[]]]), [])
    test(flatten([1, "a", [True, [2.5]]]), [1, 'a', True, 2.5])

    print('countp')
    test(countp([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0), 3)
    test(countp([1, 2, 3, 4], lambda x: x > 10), 0)

    print('unique')
    test(unique([1, 1, 2, 2, 3, 1]), [1, 2, 3])
    test(unique(["a", "b", "a", "c", "b"]), ['a', 'b', 'c'])

    print('is_palindrome')
    test(is_palindrome("level"), True)
    test(is_palindrome("Level"), True)
    test(is_palindrome("hello"), False)
    test(is_palindrome(""), True)

    print('eval_postfix')
    test(eval_postfix("3 4 +"), 7)
    test(eval_postfix("10 2 /"), 5)
    test(eval_postfix("2 3 4 * +"), 14)
    test(eval_postfix("5 1 2 + 4 * + 3 -"), 14)


if __name__ == '__main__':
    main()