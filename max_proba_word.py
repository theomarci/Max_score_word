import random
import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

#The objective of my project is to select the word wich has the most occurence in a latin text
# For resolve this problem, I decide to use the simulated algorithm
# I starting with a latin text
# Then I split the text to isolate each word and store them inside a list
# My next step is to determine the number of occurence for each words. 
# Then I calculate the probabilities for each words comparing with the length of my set
# Next I store the score in a dictionnaries
# Now I can to start my simulated algorithm
# I need before write the algorithm function to determibe some parameter :
# I fix the temperature to 100,
# I determine The cooling rate (0.95 for example)
# then I selected my starting point in selecting a random word and his value 
# finally a add my dictionnaries as my range set
# Now it's time to create the algorithm function
# In my function, a selected a word randomly and compare his score with the score of the current point
# If new one is superior to the current I replace the it with the new words
# If not then I must to calculate the acceptance of the new word
# Finally before recall the function I decrease the temperature by an multiplication cooling rate (for example : current_temp *= 0.95)
# When my temperatue is eaqual to 0 I stop my function and return the value found

# ------------------------------------------------------------Functions--------------------------------------------------------------------------------

# return a dictionnary listing all words of my text and his score (the probability of a word appearing multiply times in the text)
def Latin_text_dictionnary (text) :
    text = text.lower()
    text = ''.join([" " if i in [ ",", '"', ".", "!", ":", '\n', '?', '(', ')', '-'] else i for i in text])
    word_list = text.split(" ")
    words_score_dict = {}

    for i in word_list :
        if i not in words_score_dict and len(i)>3:
            score = word_list.count(i)
            words_score_dict[i] = score
    return words_score_dict

# Now I create a new function which take in parameter the dictionnary of the previous function and return a other dictionnary whith words in key and 
# their probabilities.
def Pobability(dictionnary) :
    proba_Glossarium = {}
    total_word = len(dictionnary)
    for i in dictionnary:
        # I decided to calculate the percentage of each word because otherwise the values is too small. 
        proba_word = round((dictionnary[i] / total_word), 4)
        proba_Glossarium[i] = proba_word
    return proba_Glossarium


        
# Now it's time to build the simulated annealing algorithm
def simulated_annealing(dictionnary, cooling_rate, temperature, iteration) :
        
        current_word = random.choice(list(dictionnary.keys()))
        
        while temperature > 0 and iteration <= 2500 :
             current_value = dictionnary[current_word]
             new_word = random.choice(list(dictionnary.keys()))
             new_value = dictionnary[new_word]

             difference = new_value - current_value

             if difference > 0 :
                  current_word = new_word
             else :
                  acceptance = math.exp(difference / temperature)
                  random_num = random.random()

                  if random_num < acceptance :
                       current_word = new_word
                  else :
                       current_word = current_word

             temperature *= cooling_rate     
             iteration += 1

        return current_word

# I create here a function which return a dataframe

def words_data(Gloss):
     dataframe = {}
     words = []
     in_text = []

     for i in Gloss :
          word = i
          value = Gloss[i]
          words.append(word)
          in_text.append(value)

     dataframe["Word"] = words
     dataframe["Number"] = in_text

     df = pd.DataFrame(dataframe)

     return df

def graph_top_words(dataframe) :
     sorted_value = dataframe.sort_values(by = 'Number', ascending = False)
     top_20 = sorted_value.head(20)
     plt.barh(top_20['Word'], top_20['Number'], color='red')
     plt.title('The 20 most frequently repeated words', fontstyle='italic', fontweight='bold', color='blue')
     plt.xlabel('occurences', fontweight='bold', color='blue')
     plt.ylabel('Words', fontweight='bold', color='blue')
     plt.show()