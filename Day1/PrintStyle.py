sal=1000
exp=6.5
comp="wipro"
'''
print(type(sal))
print(type(exp))
print(type(comp))

print("My name is Suraj")

#C style
print("Suraj is working in %s from past %.1f years with salary of %d" %(comp,exp,sal))

#formatted style
print(f"Suraj is working in {comp} from past {exp} years with salary {sal}")
print("Suraj is working in {0} from past {1} years with salary {2}".format(comp,exp,sal))
'''
#Unformatted or Python style
print("Suraj is working in",comp," from past ",exp," years with salary ",sal)
#print("Suraj is with sal"+sal)
#print("Suraj is with experience"+exp)
#print("Suraj is with company "+comp)