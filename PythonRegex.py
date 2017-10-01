import re
if re.search("ape", "The ape was at the apex"):
    print("there is an ape")
	
allApes = re.findall("ape.", "the ape in apex")

for i in allApes:
    print(i)
	
	
animalStr = "Cat rat mat pat"

allAnimals = re.findall("[crmfp]at", animalStr)

for i in allAnimals:
    print(i)
    
# after ^ anything but those character which start with given after ^	
allAnimals = re.findall("[^mp]at", animalStr)

for i in allAnimals:
    print(i)
	
owlFood = "rat cat mat pat"
regex = re.compile("[cr]at")
owlFood = regex.sub("owl", owlFood)
print(owlFood)

# r is the raw string which helps in matching \\ if you don't use r then \\ will be taken as special character
randStr = "Here is \\stuff"
print("hmm", re.search(r'\\stuff', randStr))


randStr = '''This is a long
string that goes
on for many lines
'''
regex = re.compile('\n')
randStr = regex.sub('', randStr)