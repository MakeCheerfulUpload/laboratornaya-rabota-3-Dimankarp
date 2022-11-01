import re

isuNum = 367597
print(f" ISU {isuNum}: %6 = {isuNum%6};")

unitTests = [
"Вот-вот и стрельнет мне вот   вот такой возраст возраст, когда ни ни есть не не хочется, ни пить   пить",
"Раз раз раз раз раз раз два два раз два три три три четыре пять пять шесть, два, два, три, три, семь.семь семь семь",
"Приём пс-сс пс-сс, как как слы слы слышно? Свя свя связь     рвё рвё тся тся тся связь ",
"Покемоны покемоны покемоны...вам ВАМ они ещё не надоели? Ну, может-может может-может как-нибудь уже перестанем джигли джигли паффлить паффлить и прочие пика пика чу?",
"Здра-здра-здра вствуйте! Н-н-н е подск-подск-подск ажите, к-к-к ак добр-добр-добр-добр аться до ме-ме-ме тро."]
#p = re.compile(r'\b(\w+)(\s+(\1)\b)+')
p = re.compile(r'\b([a-zA-zа-яёА-яё0-9_-]+)([\s-]+(\1)\b)+', re.I)
for test in unitTests:
    print(f'Пример: {test}')
    print(re.sub(p, r'\1', test))
    print()
while True:
    line = input("Хотите протестировать строчечку? Вводите:")
    print(re.sub(p, r'\1', line))