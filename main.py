import Latin_eulogy as Le
import max_proba_word as mpw

# ---------------------------------------------------------------------MAIN CODE-------------------------------------------------------------------------

def main() :
     my_dict = mpw.Latin_text_dictionnary(Le.latin_text)
     probability_Glossarium = mpw.Pobability(my_dict)
     sim_ann_alg = mpw.simulated_annealing(probability_Glossarium, 0.95, 100, 1)
     return sim_ann_alg

the_best_word = main()
print(f"In the text, the word which recurs multiple times is : {the_best_word}")