import os
#menu
def menu():
        choice = input ("\n\tChoose your option \n\tA - Enter RLE \n\tB - Display ASCII \n\tC - Convert to ASCII art \n\tD - Convert to RLE \n\tQ - Quit \n\t")
        if choice == "A":
            enter_rle()
        elif choice == "B":
            display_ascii()
        elif choice == "C":
            convert_to_ascii()
        elif choice == "D":
            convert_to_rle()
        else:
            print("You quit")

######################################################################################################################

#enter rle
def enter_rle():
        lines = int(input("How many lines of RLE compressed data do you want to enter?"))

        #check i they have enter more than 2
        while lines < 2:
                lines = int(input("ERROR \nYou have to enter a value higher that 2 \nHow many lines of RLE compressed data do you want to enter?"))

        #for loop to enter data
        for i in range(0,lines):
                rle = input("Please enter your line of rle code: ")
                #checks wether the rle has been entered correctly
                while (len(rle)%3) != 0:
                        rle = input("ERROR \nPlease enter your line of rle code: ")
                counter = 0
                #sets up an empty string
                array = ""
                #iterates untill there are no more characters
                while (len(rle)-1) >= counter:
                        #splits the string into 3 sets of characters
                        char1 = rle[counter]
                        char2 = rle[counter+1]
                        char3 = rle[counter+2]
                        #adds to the counter so in the next iteration it moves to the next set
                        counter = counter + 3
                        #changes characters to integers
                        char1 = int(char1)
                        char2 = int(char2)
                        #multiplies the 1st character by 10 and adds 1 and 2 together so they can iterate
                        if char1 > 0:
                                char1 = char1*10
                                char2 = char1+char2
                        #adds the ASCII to the string
                        for i in range (0,char2):
                                array= array + char3
                print(array)
        menu()

#######################################################################################################################     

#display ascii
def display_ascii():
        # open and prints file
        file = input("Please enter the name of your ASCII art file: ")
        f = open( file,"r")
        print(f.read())
        f.close()
        #return
        menu()
        
#######################################################################################################################

#convert to ascii
def convert_to_ascii():
        filename = input("Please enter the name of your RLE file: ")
        f = open(filename,"r")
        for x in f:
            #reads line to dencode
            rle = x
            counter = 0
            #conversion
            array = ""
            while (len(rle)-1) > counter:
                    #splits string into sets of 3 charatcers
                    char1 = rle[counter]
                    char2 = rle[counter+1]
                    char3 = rle[counter+2]
                    counter = counter + 3
                    #changes characters to integers
                    char1 = int(char1)
                    char2 = int(char2)
                    #multiplies the 1st character by 10 and adds 1 and 2 together so they can iterate
                    if char1 > 0:
                            char1 = char1*10
                            char2 = char1+char2
                            #adds the ASCII to the string
                    for i in range (0,char2):
                            array = array + char3
            print(array)
            
        menu()
        
#######################################################################################################################

#convert to rle
def convert_to_rle():
        #open file
        file = input("Enter ASCII file to convert: ")
        f = open( file,"r")
        file_rle = open("compressed.txt","w+")
        #finds the total characters
        total = 0
        #cycle through each line
        for x in f:
        #readline
                a = x
                i = len(a)
                character =1
                while i > 1:
                        #loops so it knows the end of the string
                        counter = 1
                        while a[character -1] == a[character]:
                                #counts the loops so it knows how many characters have passed
                                counter = counter +1
                                character = character +1
                        # checks if characters are equal
                        if a[character -1] != a[character]:
                                total = total + counter
                                char1 = a[character -1]
                                char2 = str(counter)
                                finalchar = char2 +char1
                                #make the rle all 3 digits so is easier to decode
                                if counter < 10:
                                        finalchar = "0" + finalchar
                                #writes data to a new file
                                file_rle.write(finalchar)
                                character = character+1
                                #show how many are left
                        i = i -counter
        #closing files
        f.close()
        file_rle.close()
        #open in read mode
        file_rle = open("compressed.txt","r")
        #calculate how many character smaller it is
        a= file_rle.read()
        #finds the amount of characters
        i = len(a)
        #finds the differnce
        diff= total - i
        print("The compressed file is ",diff," charcters smaller")
        #return
        menu()
            
        
        

           
menu()
