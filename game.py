# Python library imports
import random
import itertools
from collections import OrderedDict

# Function to generate a random sample of cards based on the number of cards,
# number of dimensions for each card and size of each dimension
def sample_cards(dims, dim_size, n_cards):
    s = dims * [range(dim_size)]
    try:
        return random.sample(list(itertools.product(*s)),n_cards)
    except ValueError:
        print "The sample number of cards should not be greater than %s" %len(list(itertools.product(*s)))

# Function to find the appropriate third card in the set given first two cards
# This function is only called for dim_size = 3
def find_third_card(first, second):
    def third_card((a,b)):
        return (-a-b)%3
    return map(third_card,zip(first,second))

# Brute force method to determine a set
def set_brute(first, second, third):
    def same_cards(ca_1,ca_2,ca_3):
        return ca_1==ca_2 and ca_2==ca_3
    def different_cards(ca_1,ca_2,ca_3):
        return len({ca_1,ca_2,ca_3})==3
    return all(same_cards(card1,card2,card3) or different_cards(card1,card2,card3)
               for (card1,card2,card3) in zip(first, second, third))

# Main class
class Sets:

    def __init__(self, dims=4, dim_size=3, n_cards=12):
        # Generate a list of all cards
        self.cards = sample_cards(dims,dim_size,n_cards)

    # Get possible sets in the sample card deck (method only works for dim_size=3)
    def get_sets(self):
        possible_sets = []
        cards_dict = {}
        for card_pos,card in enumerate(self.cards):
            cards_dict[card]=card_pos
        for i,ci in enumerate(self.cards):
            for j,cj in enumerate(self.cards[i+1:],i+1):
                k = cards_dict.get(tuple(find_third_card(ci,cj)))
                if k > j:
                    possible_sets.append((ci,cj,self.cards[k]))
        sets_dict = OrderedDict()
        for i, single_set in enumerate(possible_sets):
            key = "Set {}".format(i+1)
            sets_dict[key] = single_set
        return sets_dict

    # Get possible sets in the sample card deck (method works for any dim_size)
    # This method is computationally more expensive than the previous function
    def getsets_brute(self):
        possible_sets = []
        for i,ci in enumerate(self.cards):
            for j,cj in enumerate(self.cards[i+1:],i+1):
                for k,ck in enumerate(self.cards[j+1:],j+1):
                    if set_brute(ci, cj,ck):
                        possible_sets.append((ci,cj,ck))
        sets_dict = OrderedDict()
        for i, single_set in enumerate(possible_sets):
            key = "Set {}".format(i+1)
            sets_dict[key] = single_set
        return sets_dict





