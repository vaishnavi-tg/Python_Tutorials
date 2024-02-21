def test(a,b):
    return a+b
print(test(2,3))#here it is addition 
print(test("vaish","navi"))# here it is concatination 
print(test([1,2,3,4,5],[6,7,8,9,0]))



class datascience:
    def syllabus(self):
        print("This is the method for data science")
class webdev:
    def syllabus(self):
        print("This is the method for webdevelopment")
                 
def class_parcer(classobject):
    for i in classobject:
        i.syllabus()


obj_ds=datascience()
obj_wd=webdev()
classobject=[obj_ds,obj_wd]
class_parcer(classobject)


