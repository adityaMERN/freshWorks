import threading 
from threading import*
import time
d={} 

#"create(key_name,value,timeout_value)" function is defined. Timeout is optional we can continue by passing two arguments without timeout

def create(key,value,timeout=0):
    if key in d:
        #error message1
        print("error: this key already exists") 
    else:
        if(key.isalpha()):
            #constraints for file size less than 1GB and Jsonobject value less than 16KB
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024):  
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                #constraints for input key_name capped at 32chars
                if len(key)<=32:
                    d[key]=l
            else:
                #error message2
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#error message3

# "read(key_name)"
            
def read(key):
    if key not in d:
        #error message4
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        b=d[key]
        if b[1]!=0:
            #comparing the present time with expiry time
            if time.time()<b[1]: 
                #to return the value in the format of JsonObject i.e.,"key_name:value"
                stri=str(key)+":"+str(b[0]) 
                return stri
            else:
                #error message5
                print("error: time-to-live of",key,"has expired") 
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#for delete operation
#"delete(key_name)"

def delete(key):
    if key not in d:
        #error message4
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        b=d[key]
        if b[1]!=0:
            #comparing the current time with expiry time
            if time.time()<b[1]: 
                del d[key]
                print("key is successfully deleted")
            else:
                #error message5
                print("error: time-to-live of",key,"has expired") 
        else:
            del d[key]
            print("key is successfully deleted")

