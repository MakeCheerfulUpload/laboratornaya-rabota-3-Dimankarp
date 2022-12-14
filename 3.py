import re

isuNum = 367597
print(f" ISU {isuNum}: %5 = {isuNum%5};")

unitTests = [
"2+2=4",
"Вышло, что работу должны были выполнить 1.5 землекопа. Почему 1.5? Откуда я знаю! В конце концов, какое мне дело, сколько землекопов рыли эту самую траншею? Кто теперь вообще роет землекопами?",
"Жили у бабуси\
\n2 весёлых гуся,\
1 - серый, другой - белый,\
\n2 весёлых гуся.\
1 - серый, другой - белый,\
\n2 весёлых гуся!",
"Пушкин:\
\
\n17 30 48\
\
\n140 10 01\
\
\n126 138\
\
\n140 3 501",
"Список покупок на завтра:\
\n10 яиц\
\n2 бутылки молока\
\n3-4 луковички\
\n3 килограмма картошки\
\nшоколадки, штуки 2-3\
\nсыра много понадобится,\
\nпрямо много - 3 кусочка по 200 грамм"]
#p = re.compile(r'\b(\w+)(\s+(\1)\b)+')
p = re.compile(r'\d+[.,]?\d*')
for test in unitTests:
    print(f'Пример: {test}')
    print(re.sub(p, lambda x: str(int(float(x.group())**2 * 4 - 7)), test))
    print()
while True:
    line = input("Хотите протестировать строчечку? Вводите:")
    print(re.sub(p, lambda x: str(int(float(x.group())**2 * 4 - 7)), line))