import random
import string
message=[]
def add_random_before(temp):
    ch=""
    for i in range(3):
        ch=ch+random.choice(string.ascii_letters)
    ch=ch+temp
    return ch

def add_random_after(temp):
    ch=""
    for i in range(3):
        ch=ch+random.choice(string.ascii_letters)
    ch=temp+ch
    return ch

def encode_message(words):
    for temp in words:
        if(len(temp)<3 and len(temp)>1):
            temp=temp[1]+temp[0]
            message.append(temp)
        elif(len(temp)>=3):
            temp=temp[1:]+temp[0]
            before=add_random_before(temp)
            final=add_random_after(before)
            message.append(final)
        else:
            message.append(temp)
    
def decode_message(message):
    decode_msg=[]
    for item in message:
        if(len(item)<3 and len(item)>1):
            item=item[1]+item[0]
            decode_msg.append(item)
        elif(len(item)>=3):
            item=item[3:]
            item=item[:len(item)-3]
            item=item[len(item)-1:]+item[:len(item)-1]
            decode_msg.append(item)
        else:
            decode_msg.append(item)
    return decode_msg

def print_message(message):
    for msg in message:
        print(msg,end=" ")
    print()

#MAIN
lan=input("Enter your message: ")
words=lan.split()
encode_message(words)
print_message(message)
decode=decode_message(message)
print_message(decode)
   