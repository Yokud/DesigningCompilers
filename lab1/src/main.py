from regularExpression import convertRegexToDesiredFormat, ALPHABET
from parseTree import ParseTree
from dfa import DFA
from minDfa import MinDFA
from chain import inputСhainСheckСorrespondence


MSG = f"""
    \tМеню\n
    1. Синтаксическое дерево для регулярного выражения;
    2. Значения функций firstpos и lastpos в узлах синтаксического дерева;
    3. Ориентированный граф для функции followpos;
    4. ДКА для регулярного выражения;
    5. Минимизированный ДКА алгоритмом Хопкрофта;
    6. Проверка входной цепочки на соответсвие регулярному выражению;

    0. Выход.\n
    Выбор: """


def inputOption():
    try:
        option = int(input(MSG))
    except:
        option = -1
    
    if option < 0 or option > 6:
        print("%s\nОжидался ввод целого числа от 0 до 6%s" %(RED, BASE))

    return option


def main():
    regex = input(f"\nВведите регулярное выражение: ")
    # regex = "(a|b)*abb"
    # regex = "((abba)|(baab)|(baba)|(abab)|(bb)|(aa))*"
    # regex = "((0110)|(1001)|(1010)|(0101)|(11)|(00))*1((0110)|(1001)|(1010)|(0101)|(11)|(00))*"
    # regex = "((0|1)(0|1)(0|1))*"
    # regex = "((0*00)|1)*"
    convertedRegex = convertRegexToDesiredFormat(regex)
    if convertedRegex is None:
        return

    parseTree = ParseTree(convertedRegex)
    parseTree.printTree()
    
    dfa = DFA(parseTree)
    dfa.printFirstposLastpos()
    dfa.printFollowpos()
    dfa.printDFA()

    minDFA = MinDFA(dfa, ALPHABET)
    minDFA.printGroupList()
    minDFA.printMinDFA()

    option = -1
    while option != 0:
        option = inputOption()
        match option:
            case 1:
                parseTree.buildGraph(view=True)
            case 2:
                dfa.buildFirstposLastposGraph(view=True)
            case 3:
                dfa.buildFollowposGraph(view=True)
            case 4:
                dfa.buildDFAGraph(view=True)
            case 5:
                minDFA.buildMinDFAGraph(view=True)
            case 6:
                inputСhainСheckСorrespondence(regex, minDFA)


if __name__ == '__main__':
    main()
