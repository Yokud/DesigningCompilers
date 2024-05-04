import unittest
from regularExpression import convertRegexToDesiredFormat, ALPHABET
from parseTree import ParseTree
from dfa import DFA
from minDfa import MinDFA
from chain import checkChain


class TestChains(unittest.TestCase):

    def test_astar_a(self):
        regex = "a*"
        chain = "a"

        convertedRegex = convertRegexToDesiredFormat(regex)
        parseTree = ParseTree(convertedRegex)
        dfa = DFA(parseTree)
        minDFA = MinDFA(dfa, ALPHABET)
        
        self.assertTrue(checkChain(chain, minDFA))

    def test_astar_aaa(self):
        regex = "a*"
        chain = "aaa"

        convertedRegex = convertRegexToDesiredFormat(regex)
        parseTree = ParseTree(convertedRegex)
        dfa = DFA(parseTree)
        minDFA = MinDFA(dfa, ALPHABET)
        
        self.assertTrue(checkChain(chain, minDFA))

    def test_astar_b(self):
        regex = "a*"
        chain = "b"

        convertedRegex = convertRegexToDesiredFormat(regex)
        parseTree = ParseTree(convertedRegex)
        dfa = DFA(parseTree)
        minDFA = MinDFA(dfa, ALPHABET)
        
        self.assertFalse(checkChain(chain, minDFA))

    def test_astar_null(self):
        regex = "a*"
        chain = ""

        convertedRegex = convertRegexToDesiredFormat(regex)
        parseTree = ParseTree(convertedRegex)
        dfa = DFA(parseTree)
        minDFA = MinDFA(dfa, ALPHABET)
        
        self.assertTrue(checkChain(chain, minDFA))

    def test_ab_abb(self):
        regex = "(a|b)*abb"
        chain = "abb"

        convertedRegex = convertRegexToDesiredFormat(regex)
        parseTree = ParseTree(convertedRegex)
        dfa = DFA(parseTree)
        minDFA = MinDFA(dfa, ALPHABET)
        
        self.assertTrue(checkChain(chain, minDFA))

    def test_ab_aaabb(self):
        regex = "(a|b)*abb"
        chain = "aaabb"

        convertedRegex = convertRegexToDesiredFormat(regex)
        parseTree = ParseTree(convertedRegex)
        dfa = DFA(parseTree)
        minDFA = MinDFA(dfa, ALPHABET)
        
        self.assertTrue(checkChain(chain, minDFA))

    def test_ab_babaabb(self):
        regex = "(a|b)*abb"
        chain = "babaabb"

        convertedRegex = convertRegexToDesiredFormat(regex)
        parseTree = ParseTree(convertedRegex)
        dfa = DFA(parseTree)
        minDFA = MinDFA(dfa, ALPHABET)
        
        self.assertTrue(checkChain(chain, minDFA))

    def test_ab_ababbb(self):
        regex = "(a|b)*abb"
        chain = "ababbb"

        convertedRegex = convertRegexToDesiredFormat(regex)
        parseTree = ParseTree(convertedRegex)
        dfa = DFA(parseTree)
        minDFA = MinDFA(dfa, ALPHABET)
        
        self.assertFalse(checkChain(chain, minDFA))

    def test_ab_null(self):
        regex = "(a|b)*abb"
        chain = ""

        convertedRegex = convertRegexToDesiredFormat(regex)
        parseTree = ParseTree(convertedRegex)
        dfa = DFA(parseTree)
        minDFA = MinDFA(dfa, ALPHABET)
        
        self.assertFalse(checkChain(chain, minDFA))

    def test_abc_aabb(self):
        regex = "((aa)|(bb)|c)*"
        chain = "aabb"

        convertedRegex = convertRegexToDesiredFormat(regex)
        parseTree = ParseTree(convertedRegex)
        dfa = DFA(parseTree)
        minDFA = MinDFA(dfa, ALPHABET)
        
        self.assertTrue(checkChain(chain, minDFA))

    def test_abc_bbcccbbc(self):
        regex = "((aa)|(bb)|c)*"
        chain = "bbcccbbc"

        convertedRegex = convertRegexToDesiredFormat(regex)
        parseTree = ParseTree(convertedRegex)
        dfa = DFA(parseTree)
        minDFA = MinDFA(dfa, ALPHABET)
        
        self.assertTrue(checkChain(chain, minDFA))

    def test_abc_aacab(self):
        regex = "((aa)|(bb)|c)*"
        chain = "aacab"

        convertedRegex = convertRegexToDesiredFormat(regex)
        parseTree = ParseTree(convertedRegex)
        dfa = DFA(parseTree)
        minDFA = MinDFA(dfa, ALPHABET)
        
        self.assertFalse(checkChain(chain, minDFA))

    def test_abc_null(self):
        regex = "((aa)|(bb)|c)*"
        chain = "bbcccbbc"

        convertedRegex = convertRegexToDesiredFormat(regex)
        parseTree = ParseTree(convertedRegex)
        dfa = DFA(parseTree)
        minDFA = MinDFA(dfa, ALPHABET)
        
        self.assertTrue(checkChain(chain, minDFA))
    
if __name__ == '__main__':
    unittest.main()
        
