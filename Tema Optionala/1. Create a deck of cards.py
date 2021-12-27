import random

with open('cards.txt', 'r') as reader:
   line = reader.readline()
   while line != '':
         print(line, end='')
         line = reader.readline()


num_lines = sum(1 for line in open('cards.txt'))

if num_lines == 10:
    print("\n\nCarti suficient pt joc")
if num_lines < 10:
    print("Prea putine carti")

def randcard(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print('\nCartea aleasa este...')
print(randcard('cards.txt'))