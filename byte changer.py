def join_bytes(text):
    """
    OBJ: join bytes, without spaces
    str->str
    PRE:

    """
    final_text=""
    for character in text:
        if character!=" ":
            final_text+=character #with this we delete spaces 
    return final_text
        

def check_text():
    """
    OBJ: check if the bytes are multiples of 8, this is for , bytes lines, if you want 8 bytes change 8 for 16, etc
    none->bool
    PRE:
    """
    join_text=join_bytes(your_input)
    return len(join_text)%8==0


def split_by_lines():
    """
    OBJ: split bytes in lines, for making easier put in your game or whatever
    None->list
    PRE:
    """
    text=join_bytes(your_input)
    lines=""
    list_of_lines=[]
    len_text=len(text)
    counter=1

    while counter<=len_text:
        for letter in text: #change 8 for 16 of you want obtain lines of 8 bytes instead of 4,etc
            lines+=letter
            if counter%8==0:
                list_of_lines.append(lines)
                lines=""
                counter+=1
            else:
                counter+=1
    return list_of_lines

def reverse_bytes():
    """
    
    """

    lines=split_by_lines()
    #print(lines)
    text=""
    text2=""
    text3=""
    new_list=[]

    for bytes in lines: #iterates bytes in each line
        bytes=bytes[::-1]
        #print(bytes)
        counter=0  #counts the elements in the line (if u have 4 bytes line, it'll be until 8, if u have 8 bytes line, it'll be until 16...)
        for byte in bytes:
            if counter%2==0:
                text2+=byte
                counter+=1
                #print(text)
            elif counter%2!=0:
                text+=byte
                counter+=1
                #print(text2)
            if counter==8: #if u have 4 bytes line, it'll be until 8, if u have 8 bytes line, it'll be until 16...
                for i in range (counter//2):
                    text3+=text[i]+text2[i]
                new_list.append(text3.upper())
                counter=0
                text=""
                text2=""
                text3=""
    return new_list

def hex_calculator(initial_address, total_addresses):
    """
    OBJ: calculate the addresses that correspond to the bytes
    str,int->list
    PRE:
    """
    list_adresses=[initial_address.upper()] 
    b = "4" #if you want to sum 8 bytes remove 4 and write 8, if you want to sum 16 bytes remove 4 and write 10,etc  the corresponding decimal number in hexadecimal
    sum = (int(initial_address, 16) + int(b, 16)) 
    #print(hex(sum).upper())
    #print(list_adresses)
    #print(str(sum)[2:])
    for i in range(total_addresses):
        list_adresses.append((hex(sum).upper())[2:])
        sum += (int(b, 16)) 

    return list_adresses


print("---------------")
print(" BYTE CHANGER")
print("---------------")
print("")
print("1.-  Byte Changer")
print("2.-  Hex Address Calculator")
print("3.-  Both (Byte Changer & Hex Address Calculator)")
print("")

option=int(input("Choose an option: "))

if option==1:
    your_input=input("\nIntroduce bytes: ")
    if check_text():
    #print(split_by_lines())
        bytes_list=reverse_bytes()
        print("")
        for bytes in bytes_list:
            print(bytes)
        print("")
    else:
        print ("\nError, write a suitable number of bytes")
        print("")
elif option==2:
    your_address=input("\nEnter the address from which the following will be created: ")
    try:
        number_of_addresses=int(input("Number of adresses you want to generate without counting the initial address(if u want to start from this address check line 90): "))#if u want to start from this address check line 90: "))
        hex_adresses=hex_calculator(your_address,number_of_addresses)
        print("")
        for address in hex_adresses:
            print(address)
        print("")
    except:
        print("Error, your input is not valid. Try to put a INT number")
elif option==3:
    your_input=input("\nIntroduce bytes: ")
    if check_text():
        bytes_list=reverse_bytes()
        your_address=input("\nEnter the address from which the following will be created (if u want to start from this address check line 90): ")#if u want to start from this address check line 90
        print("")
        number_of_addresses=len(bytes_list)
        hex_adresses=hex_calculator(your_address,number_of_addresses)
        for i in range(len(bytes_list)):
            print(f"00{hex_adresses[i]} {bytes_list[i]}") #you can add number u want like "0" to the left of {hex_adresses[i]} like print(f"00{hex_adresses[i]} {bytes_list[i]}")
    else:
        print ("\nError, write a suitable number of bytes")
        print("")

    

        




