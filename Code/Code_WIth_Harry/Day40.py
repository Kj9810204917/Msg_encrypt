# Coder and Decoder for chatting one another
data=[]
i=0
while True:
    print("For Code the Data Choose 1")
    print("For Decode the Data Choose 2")
    
    Data=int(input("Enter the Number For Furthure Function : "))  
    match Data:
        case 1:
            Check_In=0
            while True:
                data1=input(f"Enter the Message : or : terminate the code program as '.' ")
                if data1!=".":
                    data.append(data1)
                else:
                    break
        case 2:
            Check_Out=0
            while True:
                Number_Msg=int(input("Enter the Message Number : "))
                if (Number_Msg)<=len(data):
                    print(data[Number_Msg-1])
                else:
                    break
        case _:
            print("Oops! You choose the wrong Command ")
    print("Write Exit For Terminate the program : or : Any thing You wants to Write ")
    exit=input()
    if exit=="Exit" or exit=="exit":
        break
    i=i+1