'''
This algorithm checks where a string is a palindrome.

Considering only the letters 1a2b3c '*l* 23 c_B_A' is a palindrome! 

They gave me this task at my job interview for mercedes. I thought long about it and idk why but I think the solution is beautiful:)
'''

string = '1a2b3c   *l* 23 c_B_A'

def is_palin(string):

    i, j = 0, len(string)-1

    while i < j:

        while not string[i].isalpha():
            i += 1
        
        while not string[j].isalpha():
            j -= 1

        if string[i].lower() != string[j].lower():
            return False

        i += 1
        j -= 1
    
    return True


is_palin(string)
        


    
