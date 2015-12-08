import unittest
from itertools import chain
from game import Sets

def unique_sets_length(d):
    seen = {} # dict (value, key)
    result = set() # keys with unique values
    for k,v in d.iteritems():
        if v in seen:
            result.discard(seen[v])
        else:
            seen[v] = k
            result.add(k)
    return len(list(result))

class TestGameofSet(unittest.TestCase):

    # Test for maximum number of sets in the traditional three card Set game
    # Dimensions = 4, Dimension size = 3
    def test_maximum_getsets(self):
        set_object = Sets(dims=4, dim_size=3, n_cards=81)
        result = len(set_object.get_sets())
        self.assertEqual(1080, result, msg="")

    # Test for maximum number of sets in the traditional three card Set game
    # Dimensions = 4, Dimension size = 3 for the alternate computationally
    # slower function that is used for higher dimensions and dimension sizes
    def test_maximum_getsets_brute(self):
        set_object = Sets(dims=4, dim_size=3, n_cards=81)
        result = len(set_object.getsets_brute())
        self.assertEqual(1080, result, msg="")

    # Test for uniqueness of sets in the traditional three card Set game
    # Dimensions = 4, Dimension size = 3
    def test_unique_getsets(self):
        set_object = Sets(dims=4, dim_size=3, n_cards=81)
        result = set_object.get_sets()
        self.assertEqual(1080, unique_sets_length(result), msg="")

    # Test for uniqueness of sets in the traditional three card Set game
    # Dimensions = 4, Dimension size = 3 for the alternate computationally
    # slower function that is used for higher dimensions and dimension sizes
    def test_unique_getsets_brute(self):
        set_object = Sets(dims=4, dim_size=3, n_cards=81)
        result = set_object.getsets_brute()
        self.assertEqual(1080, unique_sets_length(result), msg="")

    # Test to see if "Set definition" is honored in the traditional three card Set game
    # Dimensions = 4, Dimension size = 3
    def test_setdef_getsets(self):
        def same_cards(ca_1,ca_2,ca_3):
            return ca_1==ca_2 and ca_2==ca_3
        def different_cards(ca_1,ca_2,ca_3):
            return len({ca_1,ca_2,ca_3})==3
        set_object = Sets(dims=4, dim_size=3, n_cards=81)
        result = set_object.get_sets().values()
        setdef_flag = False
        for set_tuple in result:
            setdef_flag = all(same_cards(i, j ,k) or different_cards(i, j, k)
                              for i, j, k in zip(set_tuple[0],set_tuple[1],set_tuple[2]))
            if setdef_flag == False:
                break
        self.assertTrue(setdef_flag, msg="")

    # Test to see if "Set definition" is honored in the traditional three card Set game
    # Dimensions = 4, Dimension size = 3 for the alternate computationally
    # slower function that is used for higher dimensions and dimension sizes
    def test_setdef_getsets_brute(self):
        def same_cards(ca_1,ca_2,ca_3):
            return ca_1==ca_2 and ca_2==ca_3
        def different_cards(ca_1,ca_2,ca_3):
            return len({ca_1,ca_2,ca_3})==3
        set_object = Sets(dims=4, dim_size=3, n_cards=81)
        result = set_object.getsets_brute().values()
        setdef_flag = False
        for set_tuple in result:
            setdef_flag = all(same_cards(i, j ,k) or different_cards(i, j, k)
                              for i, j, k in zip(set_tuple[0],set_tuple[1],set_tuple[2]))
            if setdef_flag == False:
                break
        self.assertTrue(setdef_flag, msg="")

if __name__ == '__main__':
    unittest.main()