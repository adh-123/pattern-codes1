arr={"id":1,"name":"Chiranjeevi","gmail":"abc@gmail.com","phno":9059311637}
arr1={"id":2,"name":"Chandyu","gmail":"chandu@gmail.com","phno":1234567891}
arr2={"id":3,"name":"vasudev","gmail":"vasudev@gmail.com","phno":231456789}
# arr.update({"id":4,"name":"ravi","gmail":"xyzc@gmail.com","phno":9652217968})
# # print(arr)
# # arr.clear()
# # print(arr)
# arr["gender"]="male"
# print("create:",arr)
users=[arr,arr1,arr2]
def create(userdetails):
    users.append(userdetails)
def get():
    return users
def update(id,userdetails):
    for i in users:
        if i["id"]==id:
            i.update(userdetails)
def getByid(id):
    for i in users:
        if i["id"]==id:
            return i
def delete(id):
    for i in users:
        if i["id"]==id:
            users.remove(i)
create({"id":4,"name":"ravi","gmail":"xyzc@gmail.com","phno":9652217968})
Create()
update(4,({"name":"suri"}))
print(get())
print(getByid(2))
delete(3)
print("after delete:",get())





    



