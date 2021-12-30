from itertools import zip_longest
# importam fisierul
my_file = open("nationalities.txt", "r")
content = my_file.read()
content_list = content.split("\n")
my_file.close()

# facem pachetul de carti la care adaugam si "Pacalici"
masculin = 'M'
feminin = 'F'
list1 = list(map(lambda orig_string: orig_string + feminin, content_list))
list2 = list(map(lambda orig_string: orig_string + masculin, content_list))
list3 = ['PACALICI']
cards_deck = list1 + list2 + list3


sorted_list = sorted(list1 + list2)




