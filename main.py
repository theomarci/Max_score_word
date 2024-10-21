import Latin_eulogy as Le
import max_proba_word as mpw
import pandas as pd

# ---------------------------------------------------------------------MAIN CODE-------------------------------------------------------------------------

def main() :
     my_dict = mpw.Latin_text_dictionnary(Le.latin_text)
     probability_Glossarium = mpw.Pobability(my_dict)
     sim_ann_alg = mpw.simulated_annealing(probability_Glossarium, 0.95, 100, 1)
     word_dataframe = mpw.words_data(my_dict)
     chart = mpw.graph_top_words(word_dataframe)
     return  sim_ann_alg, word_dataframe

the_best_word, word_dataframe = main()
print(f"""
      I translate three texts in latin with ChatGPT about Punic war.
      After the undesirable tokens eliminations, like space and coma, I have {len(word_dataframe)} words.
      This is the Dataframe of the text vocabulary :

      {word_dataframe}

      In the text, the word which has the most repetition is : {the_best_word}.
""")