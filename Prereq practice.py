def fizzbuzz(start,finish):

    for num in range(start,finish+1):

         if num % 3 == 0 and num % 5==0 :
             print("fizzbuzz")

         elif num % 3 == 0 or "3" in str(num):
            print("fizz")
         elif num % 5 ==0 or "5" in str(num):
            print("buzz")
        
         else:
            print(num)
    return 



def is_anagram(word1, word2):

    length = len(word2)
    changed_word2= word2[::-1]
    if word1 == changed_word2:
        print("True")
    else:
        print("False")
    return


def count_letters(file_name):
    #list= []
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
   # for char in content:
      #  if char == char in list:
           # char += 1
      #  elif 
    return

