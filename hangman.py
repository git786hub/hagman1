# Hangman game
import random
WORDLIST_FILENAME = "words.txt"
def loadWords():   
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):   
    return random.choice(wordlist)
wordlist = loadWords()
def isWordGuessed(secretWord, lettersGuessed):
   
    if(secretWord==lettersGuessed):
        return True
    else:
        return False
   
def getGuessedWord(secretWord, lettersGuessed):
  
    lettersGuessed =list(lettersGuessed)
    secretWord =list(secretWord)
    len1=len(secretWord)
    copy7=secretWord
    print(" ")
    for k in range(0,len1):
        if secretWord[k] not in lettersGuessed:
               copy7[k]="_"
               
             
    copy7="".join(copy7)
    return copy7                
                            
def getAvailableLetters_All(lettersGuessed):
    
    keys="abcdefghijklmnopqrstuvwxyz"
    lettersGuessed =list(lettersGuessed)
    secretWord1 =list(keys)
    len1=len(secretWord1)
    copy4=list(" ")
    for k in range(0,len1):
        if secretWord1[k]  not in lettersGuessed:
            j=secretWord1[k]
            copy4.append(j)
    copy4=" ".join(copy4)        
    return copy4 

def hangman(secretWord):
  
    COUNT=1
    length= len(secretWord)
    print(" ")
    print(" ")
    print("      ...........WELCOME.............")
    print(" ")
    print("         SECRET WORD IS OF LENGTH          ",length)
    print(" ")
    lettersGuessed=input("       PLEASE ENTER ONE LETTER           ")
    k=isWordGuessed(secretWord, lettersGuessed) 
    
    
    while k!=True: 
         print("----------------------------------------------------------")
         #print("         SECRET WORD IS OF LENGTH............",length)
         x=input("     PLEASE ENTER ONE MORE LETTER        ")
         lettersGuessed += x         
         print("")
         print("* GUESSED LETTERS ARE...............",lettersGuessed)
         copy2=getGuessedWord(secretWord, lettersGuessed)
         print("")
         print("* PARTIALLY GUESSED WORD SO FAR                  ",copy2)
         if copy2==secretWord:
             k=True
         print("")
         print("* The guess matches ?   ",k) 
         '''copy5=getAvailableLetters(secretWord,lettersGuessed)
         print("")
         
           print("* letters that the user has not yet guessed       ",copy5)'''
         copy6=getAvailableLetters_All(lettersGuessed)
         print("")
         
         print("* letters that the user has not yet guessed       ",copy6)
         
         COUNT+=1
         k=isWordGuessed(secretWord, lettersGuessed)
         if copy2==secretWord:
             k=True
    print("")
    print("")
    print("----------------------------------------------------------")
    print("              DONE        ")
    print(" YOU Guess The Word in  " ,COUNT, "Chance" )
    print("----------------------------------------------------------")
         
         


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
