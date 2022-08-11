
# Q1 ////////////////////
txt = input("Enter a string: ")
ltter = input("enter the letter that you want to remove: ")

def check(txt, letter):
    
    new_txt = ''
    for i in txt:
        if i not in letter:
            new_txt = new_txt + i
            
    print('The String you entered: ', txt)
    print('After removed the character: ', new_txt)


check(txt, ltter)



# Q2 //////////////////////////////////////////////
first_range = int(input("Enter the first range: "))
last_range = int(input("Enger the last range: "))

for range_number in range(first_range, last_range):
    if range_number > 1:
        for j in range(2, range_number):
            if (range_number % j) == 0:
                break
        else:
            print(range_number)




# Q3 //////////////////////////////////////////
txt = input("Enter a string: ")
ltter = input("enter the letter that you want to count: ")

def count_ltter(txt, letter):
    ltter_count = 0
    for i in txt:
        if i in letter:
            ltter_count += 1
   
    if ltter_count > 0:
        print('The String you entered: ', txt)
        print('The charcter count you enter in the a string: ', ltter_count)
    else:
        print("The charcter you entered is not exist ):")  

count_ltter(txt, ltter)