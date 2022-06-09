#tuple prac
'''
def sumdiff(a,b):
    sum = a + b
    diff = a - b
    return (sum, diff)
print("Sum: " + str(sumdiff(2,1)[0]))
print("Diff: " + str(sumdiff(2,1)[1]))
print(max(sumdiff(2,1)))
'''

#dict prac
''''
favic = {}
favic["choc"] = "chocolate"
favic["van"] = "vanilla"
favic["sb"] = "strawberry"
print(favic)
value_removed = favic.pop('sb')
del favic['van']
print(value_removed)
print(favic.values())
'''
#class attributes
'''
class User:
    all_accounts = []
    def __init__(self, name, age):
        self.name = name
        self.age = age
        User.all_accounts.append(self)
    #class methods do not have access to instance attributes
    @classmethod
    def get_all_info(cls):
        info = ""
        for account in cls.all_accounts:
            info = info + account.name + " " + str(account.age)
        return info
    #static methods do not have access to either instance or class attributes

student = User("Albert", 20)
print(student.name + str(student.age))
print(student.get_all_info())
'''
#use super. for inheritance
#modules = file(s); access them with keyword import
#packages = folder(s)
#slice with [:]




