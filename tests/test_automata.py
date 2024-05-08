from algorithms.automata import DFA


import unittest


class TestDFA(unittest.TestCase):
    def test_DFA(self):
        transitions = {
            'a': {'1': 'a', '0': 'b'},
            'b': {'1': 'b', '0': 'a'}
        }

        final = ['a']
        start = 'a'

        self.assertEqual(False, DFA(transitions, start, final, "000111100"))
        self.assertEqual(True, DFA(transitions, start, final, "111000011"))

        transitions1 = {
            '0': {'0': '1', '1': '0'},
            '1': {'0': '2', '1': '0'},
            '2': {'0': '2', '1': '3'},
            '3': {'0': '3', '1': '3'}
        }

        final1 = ['0', '1', '2']
        start1 = '0'

        self.assertEqual(False, DFA(transitions1, start1, final1, "0001111"))
        self.assertEqual(True, DFA(transitions1, start1, final1, "01010101"))

        transitions2 = {
            '0': {'a': '0', 'b': '1'},
            '1': {'a': '0', 'b': '2'},
            '2': {'a': '3', 'b': '2'},
            '3': {'a': '3', 'b': '3'}
        }

        final2 = ['3']
        start2 = '0'

        self.assertEqual(False, DFA(transitions2, start2, final2, "aaabbb"))
        self.assertEqual(True, DFA(transitions2, start2, final2, "baabba"))
 #added : 
    def test_DFA_empty_string(self):
        transitions = {'a': {'0': 'a', '1': 'a'}}
        final = ['a']
        start = 'a'
        self.assertTrue(DFA(transitions, start, final, ""))  # Assuming empty string should be accepted

    def test_DFA_invalid_character(self):
        transitions = {'a': {'0': 'a'}}
        final = ['a']
        start = 'a'
        with self.assertRaises(KeyError):  # Assuming exception for undefined transition
            DFA(transitions, start, final, "01")

    def test_DFA_no_transitions_defined(self):
        transitions = {'a': {}}
        final = ['a']
        start = 'a'
        with self.assertRaises(KeyError):  # Assuming exception if no transition exists
            DFA(transitions, start, final, "0")

    def test_DFA_single_state(self):
        transitions = {'a': {'0': 'a', '1': 'a'}}
        final = ['a']
        start = 'a'
        self.assertTrue(DFA(transitions, start, final, "000"))
        self.assertTrue(DFA(transitions, start, final, "111"))


if __name__ == '__main__':
    unittest.main()
