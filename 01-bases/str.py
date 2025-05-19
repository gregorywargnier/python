import random
text = 'Bonjour'

print(text.upper())
text = text.strip()
print(len(text))
print(text.replace('jour', 'soir'))


print(any(c.isupper() for c in text)) #[true, False, false]
print(all([True, False, True]))
print([c.isupper() for c in text])

print(random.randint(1,10))