#My list
my_list= ["motor",1, "mobil", "toyota"]
my_list.append("suzuki")
my_list.remove(1)
my_list.insert(2, "honda")
print(my_list)

#List
my_list = [1,2,3,4]
my_poplist = my_list.pop(3)
print(my_list)
print(my_poplist)

#Tuple
my_tuple = (1,2,3,4)
print(my_tuple[1])

#Tuple Error
#my_tuple[3] = 2
#print(my_tuple)

#Dictionary 
my_dictionary= {"nama" : "Yurida Yahsya", "nim" : "0110224100", "rombel" : "TI-11"}
print(my_dictionary)
print(my_dictionary["rombel"])
print(type("nim"))
print(type("my_dictionary"))

my_list = [1,2,3,4]
my_tuple = [1,2,3,4]
my_dictionary = {
        "kendaraan" : "motor",
        "warna" : "putih"
    }

print(type(my_list))
print(type(my_tuple))
print(type(my_dictionary))