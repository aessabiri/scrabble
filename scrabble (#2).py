import nltk , time , random ,itertools , string
from nltk.corpus import brown
from collections import Counter

nltk.download('brown') # Download the Brown corpus from NLTK, which is a collection of text samples in English. will be used to count the frequency of a given word in the brown corpus

words_list = set(nltk.corpus.words.words()) # Create a set called 'words_list' containing all the words from the NLTK corpus 'words'.

nltk.download('words') # frequency calculator source
global score 

alphabets = {
    "a" : 1 ,
    "b" : 2,
    "c" : 2,
    "d" : 2,
    "e" : 1,
    "f" : 2,
    "g" : 2,
    "h" : 2,
    "i" : 1,
    "j" : 3,
    "k" : 3,
    "l" : 2,
    "m" : 2,
    "n" : 2,
    "o" : 1,
    "p" : 4,
    "q" : 6,
    "r" : 3,
    "s" : 3,
    "t" : 1,
    "u" : 1,
    "v" : 4,
    "w" : 4,
    "x" : 6,
    "y" : 3,
    "z" : 6,
# Alphabets with weights of every Alphabets, the weight will be used for scoring
}



def global_word_frequency(word_list): # with help from external sources

    brown_words = brown.words()

    # Create a frequency distribution of each words in the Brown corpus
    brown_freq_dist = nltk.FreqDist(brown_words)

    # Count the frequency of each word in the given list
    word_counter = Counter(word_list)

    # Calculate the global frequency of each word
    global_frequency = {word: brown_freq_dist[word.lower()] for word in word_counter.keys()}

    return global_frequency



def most_common_words(word_list):
    frequency_dict = global_word_frequency(word_list)
    if not frequency_dict: # no word would match 
        print("No common words found.")
        return
    frequency_dict_sorted  = dict(sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True)) # sorted for no reason at all 

    for word, frequency in frequency_dict.items():
        if frequency > 1:
            print('\033[32m'"other possible word:  ",word, "   --> word score",evaluate(word))
            print('\033[0m')
            wait(0.3)
    highest_key = "" # sometimes there is no word in the list and that would raise an error -> highest_key =  null
    highest_key = max(frequency_dict, key=frequency_dict.get) # select the word with the highest frequency in the dictionary
    print ("Most Common word is :      ",highest_key,"       with a frequency of: ",frequency_dict[highest_key]) # print the highest frequency word with the frequency



def celebration(): # with help of outside sources
    print("**************************************")
    print("*             YOU WON !!!            *")
    print("*        CELEBRATION TIME!!!         *")
    print("*", name ," with a score of : ",score,"  *")
    print("**************************************")
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[97m']
    fireworks = ['*', '+', '.', 'o', 'O', '0']

    all_characters = list(string.ascii_letters) + fireworks

    for _ in range(1000):
        time.sleep(0.01)
        color = random.choice(colors)
        firework = random.choice(all_characters)
        print(color + firework, end='', flush=True)

    print('\033[0m')  # Reset terminal color to the original



def generate(level,choice): # everytime generate is called, it would only return one letter or the string " invalid letter "
    chosenletter = ""
    vowels = ["a","e","i","o","u"]
    consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

    if level == "1" :
        if choice == "v" or choice == "V":
            chosenletter = random.choice(vowels)
        elif choice == "c" or choice == "C":
            chosenletter = random.choice(consonants)
        elif choice == "r" or choice == "R": 
            if random.random() < 0.4: # 40% chance of generating a vowel to ensure that there will be some vowels in the random ;) generated letters 
                chosenletter = random.choice(vowels)
            else:
                chosenletter = random.choice(consonants)
        else :
            chosenletter = ("invalid choice")
    
        if chosenletter in alphabets: # filter out the letter that have a weight more than 3
            if alphabets[chosenletter] <= 3 :
                return chosenletter
            else :
                return ("invalid choice")
        else :
            return ("invalid choice")
        
    if level == "2" or level == "3" :
        if choice == "v" or choice == "V":
            chosenletter = random.choice(vowels)
        elif choice == "c" or choice == "C":
            chosenletter = random.choice(consonants)
        elif choice == "r" or choice == "R": 
            if random.random() < 0.4: # 40% chance of generating a vowel
                chosenletter = random.choice(vowels)
            else:
                chosenletter = random.choice(consonants)
        else :
            chosenletter = ("invalid choice")
    
        return chosenletter # we just return the chosen letters allowing the letters with weights more than 3



def validate (word,randletter): #returns True or False
    word = word.lower() # lower case
    wordlist = list(word) # turn the word into a list of letters
    randomletter = randletter
    passes = True # Default is True and only becomes False if the letter doesn't exist in the list
    for l in wordlist:
        if l in randomletter:
            randomletter.remove(l) # we remove the letter that is found to avoid using the same letters twice
        else:
            print ('\033[91m'" Letter does not exist: ",l)
            print('\033[0m') 
            passes = False
    return passes



def evaluate(word): # Returns score as Int
    word = word.lower()
    points = 0
    for i in word:
        points = points + (alphabets[i]) # calculate the score using the weights defined in alphabets
    return points



def search(word):

    if word in nltk.corpus.words.words():
        print('\033[32m'f'{word} is in the dictionary  word score ', evaluate(word))
        print('\033[0m')
        return True
    else:
        print('\033[91m'f'{word} is not in the dictionary')
        print('\033[0m')
        return False    



def print_decorated(text): # with help of external sources
    text_length = len(text)
    border_length = text_length + 6  # Account for 2 asterisks and 2 spaces on each side
    border = "*" * border_length

    print(border)
    print(f"*  {text}  *")
    print(border)



def wait(sec):
    time.sleep(sec)


  
def is_valid_word(combination): # checks if the word is in the word_list
        word = "".join(combination)
        return word.lower() in words_list



def generate_combinations_as_words(randletters): # return valid words from the random letters 
    all_combinations = []
    computer_letters = randletters[:]  # Create a copy of randletters for computer's word generation
    for length in range(2, len(computer_letters) + 1):
        permutations = itertools.permutations(computer_letters, length) # create all possible words that can be constructed from the letters
        for perm in permutations:
            word = "".join(perm)
            if is_valid_word(word): # add the word to all_cobination if the word is valid 
                all_combinations.append(word)
    return all_combinations



def best_scoring_word(wordlists):
    best_word = ""
    for word in wordlists: 
        if evaluate(word) > evaluate(best_word):
            best_word = word      
    print ("best scoring word is :  ",best_word , "   word score :" , evaluate(best_word))
    return best_word



def print_big_text(text): # with help of outside sources
    alphabet = {
        "A": ["  #  ", " # # ", "#####", "#   #", "#   #"],
        "B": ["#### ", "#   #", "#### ", "#   #", "#### "],
        "C": [" ####", "#    ", "#    ", "#    ", " ####"],
        "D": ["###  ", "#  # ", "#   #", "#  # ", "###  "],
        "E": ["#####", "#    ", "###  ", "#    ", "#####"],
        "F": ["#####", "#    ", "###  ", "#    ", "#    "],
        "G": [" ####", "#    ", "#  ##", "#   #", " ####"],
        "H": ["#   #", "#   #", "#####", "#   #", "#   #"],
        "I": ["#####", "  #  ", "  #  ", "  #  ", "#####"],
        "J": ["#####", "   # ", "   # ", "#  # ", " ##  "],
        "K": ["#   #", "#  # ", "###  ", "#  # ", "#   #"],
        "L": ["#    ", "#    ", "#    ", "#    ", "#####"],
        "M": ["#   #", "## ##", "# # #", "#   #", "#   #"],
        "N": ["#   #", "##  #", "# # #", "#  ##", "#   #"],
        "O": [" ### ", "#   #", "#   #", "#   #", " ### "],
        "P": ["#### ", "#   #", "#### ", "#    ", "#    "],
        "Q": [" ### ", "#   #", "#   #", "#  ##", " ####"],
        "R": ["#### ", "#   #", "#### ", "#  # ", "#   #"],
        "S": [" ####", "#    ", " ### ", "    #", "#### "],
        "T": ["#####", "  #  ", "  #  ", "  #  ", "  #  "],
        "U": ["#   #", "#   #", "#   #", "#   #", " ### "],
        "V": ["#   #", "#   #", " # # ", " # # ", "  #  "],
        "W": ["#   #", "#   #", "# # #", "## ##", "#   #"],
        "X": ["#   #", " # # ", "  #  ", " # # ", "#   #"],
        "Y": ["#   #", " # # ", "  #  ", "  #  ", "  #  "],
        "Z": ["#####", "   # ", "  #  ", " #   ", "#####"],
        " ": ["     ", "     ", "     ", "     ", "     "],
        "!": ["  #  ", "  #  ", "  #  ", "     ", "  #  "],
        "?": [" ##  ", "#  # ", "  ## ", "     ", "  #  "],
        ".": ["     ", "     ", "     ", "     ", "  #  "],
        ",": ["     ", "     ", "     ", "  #  ", " #   "],
        ":": ["     ", "  #  ", "     ", "  #  ", "     "],
        "-": ["     ", "     ", " ### ", "     ", "     "],
        "'": ["  #  ", "  #  ", "     ", "     ", "     "],
        '"': [" # # ", " # # ", "     ", "     ", "     "],
        "&": [" ##  ", "#  # ", " ##  ", "# # #", " ## #"]
    }

    lines = ["", "", "", "", ""]

    for char in text:
        char_lines = alphabet.get(char.upper(), alphabet[" "])
        for i, line in enumerate(char_lines):
            lines[i] += line + "  "

    for line in lines:
        print(line)
        



while True:
    computer_score = 0 
    score = 0 # Settting score to 0 after each game
    randletter= [] # Settting randletter array to empty after each game
    print ("\n")
    print ("\n")
    print_big_text (" Welcome to ")
    print ("\n")
    print_big_text("  Scrabble") 
    wait(1)
    print ("\n")
    name = input(" Input your Name \n")
    wait(1)
    print ("\n")
    print_big_text("    Hello")
    print ("\n")
    print_big_text("    "+name)
    print_decorated(
        '''
        choose level.

            1 >> Easy
            2 >> Medium
            3 >> Hard
            any key >> Random Difficulty
        numbers only from 1 to 3
        '''
    )
    print ("\n")
    level = input("            ----> ")
    if level != "1" and level != "2" and level != "3":
        level = str(random.randint(1, 3)) # random difficulty assigned if level is > 3

    print ("       level >> ", level)
    print('\033[0m')
    time.sleep(1)
    print_decorated (
        '''
                ....Starting.....
        In Each round you have a choice of 10 letters 
        Press v or V for vowels
        Press c or C for Consonants
        press r or R for Random generation
        
        '''
    )
    tolerance = 0 # if the user enters a wrong value 3 time, we default the number of rounds to 3 

    while True: 
        try:
            rounds = int(input("How many rounds do you want to play? \n"))
            if rounds <= 0:
                print('\033[91m'"Please enter a positive integer value for the number of rounds.")
                print('\033[0m')
                tolerance += 1
                if tolerance >= 3 :
                    rounds = 3 # defaulting to 3 rounds because the user might be drunk
                    wait(1)
                    print (" Defaulting to 3 Rounds")
                    wait(1)
                    break
            else : 
                break
        except ValueError:
            print('\033[91m'"Invalid input. Please enter a valid integer value for the number of rounds.")
            print('\033[0m') 
            tolerance =+ 1
            if tolerance >= 3 :
                rounds = 3 # defaulting to 3 rounds because the user might be drunk
                wait(1)
                print (" Defaulting to 3 Rounds")
                wait(1)
                break
        
        
        
    
    
    while rounds > 0:
        if level == "1":
            while len(randletter) < 10:
                
                vorc = input(" Vowel or Consonants or r for Random \n")

                if vorc == "r" or vorc == "R":
                    while len(randletter) < 10:
                        letter=generate(level, "r")
                        if letter != "invalid choice" and  letter !=  None :
                            randletter.append(letter)
                        else :
                            None
                else :
                    letter=generate(level, vorc)
                    if letter == "invalid choice":
                        print ("you can only press v or c or r\n")
                    elif letter !=  None:
                        randletter.append(letter)
                        print (randletter)
                    time.sleep(1)
        elif level == "2":
            while len(randletter) < 7:  
                vorc = input("Vowel or Consonants or r for Random \n")
                if vorc == "r" or vorc == "R":
                    while len(randletter) < 7:
                        letter=generate(level, "r")
                        randletter.append(letter)
                else :
                    letter=generate(level, vorc)
                    if letter == "invalid choice":
                        print ("you can only press v or c or r\n")
                    else :
                        randletter.append(letter)
                        print (randletter)
                    time.sleep(1)
        elif level == "3":
            while len(randletter) < 5:
                
                vorc = input("Vowel or Consonants or r for Random \n")
                if vorc == "r" or vorc == "R":
                    while len(randletter) < 5:
                        letter=generate(level, "r")
                        randletter.append(letter)
                else :
                    letter=generate(level, vorc)
                    if letter == "invalid choice":
                        print ("you can only press v or c or r\n")
                    else :
                        randletter.append(letter)
                        print (randletter)
                    time.sleep(1)
        computer_letters = randletter[:]
        print (name,"your letters of choice are: \n ",randletter) # printing Randome letters

        start_time = time.time() # start timer 
        word = input("----> Input your word \n")
        end_time = time.time() # end timer
        elapsed_time = round(end_time - start_time) # calculate time it took to answer
        print ("Time taken to input word: ",elapsed_time," seconds")
        print (word," score = ", evaluate(word))
        validateLetter = validate(word,randletter)
        print ("\n")
        checkDict = search(word)
        print ("\n")
        print ("Computer generating a word ...")
        print ("\n")
        valid_word_combination = generate_combinations_as_words(computer_letters)
        best_word =  best_scoring_word(valid_word_combination)
        print ("\n")
        print ("\n")
        most_common_words(valid_word_combination) #retrun a list of other possible word if found
        
        

        scoreBeforeTimeBonus = 0
        if checkDict == True:
            scoreBeforeTimeBonus = evaluate(word) 
        scoreBonus = 0
        if validateLetter == False or checkDict == False:
            print ("Invalid word")
    
        else: 
            if elapsed_time < 10:
                scoreBonus = scoreBeforeTimeBonus + 5
                print ("Bonus score: 5")
            elif elapsed_time < 20:
                scoreBonus = scoreBeforeTimeBonus + 3
                print ("Bonus score: 3")
            elif elapsed_time < 30:
                scoreBonus = scoreBeforeTimeBonus + 1
                print ("Bonus score: 1")
            else:
                scoreBonus = scoreBeforeTimeBonus
                print ("No Bonus score")


        
        computer_score = computer_score + evaluate(best_word)
        print ("word score is: ",scoreBeforeTimeBonus)
        print ("your score for this round: ",scoreBonus, " computer score : " ,computer_score)
        
        score = score + scoreBonus
        rounds = rounds - 1
        randletter.clear()
        computer_letters.clear()
        print ("Rounds left: ",rounds)
        print ("-----------------------------")
    print (name)
    print ("Your overall score is: ",score)
    print ("Overall Computer score is :", computer_score)
    if score > computer_score:
        print ("celebration")
        celebration()
    else:
        print_decorated('\033[91m' ''' Hey, don't sweat the Scrabble loss! Remember,
                        every letter in life is just a 'tile' to success, 
                        and even the best players get stuck with a 'Q' without a 'U'!
                        Embrace the 'blank' tiles in your journey, 
                        and you'll be 'tripling' your victories in no time! 
                        Keep 'shuffling' forward,
                        and the 'double word' of triumph will be yours for the taking!
                        Keep playing, 
                        and let's 'scrabble' our way to greatness! 🎉😄''') # with help of outside sources
        print('\033[0m') # resetting the color
    playagain = input("Do you want to play again ? (y/n) \n")
    if playagain == "y" or playagain == "Y":
        print ("Restarting and Resetting...")
        time.sleep(1)
    else:       
        print ("Game Over")
        break


