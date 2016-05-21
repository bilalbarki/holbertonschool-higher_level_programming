from family import Person, Baby, Teenager, Adult, Senior
from family import load_from_file, save_to_file

#my_family = load_from_file("my_family.json")
#print "I have %d members in my family" % len(my_family)
b=[0,1]
# new baby!
b[0] = Person(3, "Tony", [7, 4, 2015], "Male", "Green")
b[0].last_name = "Rod"
b[1] = Baby(3, "jjjj", [7, 4, 2015], "Male", "Green")
b[1].last_name = "Foto"
#my_family.append(b)

save_to_file(b, "my_family.json")
