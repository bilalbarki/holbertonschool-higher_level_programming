from family import Person

p = Person(1, "bilal", [12, 31, 1980], "Male", "Blue")
p.last_name = "Dupont"
print "New person %s %s" % (p.get_first_name(), p.last_name)
