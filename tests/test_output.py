import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from model.Parser import Parser, Node

# test func Node
def test_node(capfd):
    # Create nodes
    root = Node(('ROOT','TBD'))
    verb = Node(('xuất phát','VERB'))
    nsubj = Node(('máy bay','NOUN'))
    det = Node(('nào','WDET'))
    prep1 = Node(('từ','PREP'))
    pobj1 = Node(('thành phố','NOUN'))
    nmod = Node(('hồ chí minh','NAME'))
    prep2 = Node(('lúc','PREP'))
    pobj2 = Node(('14:30HR','NOUN'))
    punc = Node(('?.','EOL'))
    # Build the Tree
    root.add_child(verb,'root')
    verb.add_child(nsubj,'nsubj')
    verb.add_child(prep1,'prep')
    verb.add_child(prep2,'prep')
    verb.add_child(punc,'punc')
    nsubj.add_child(det,'det')
    prep1.add_child(pobj1,'pobj')
    prep2.add_child(pobj2,'pobj')
    pobj1.add_child(nmod,'nmod')
    # Print the Tree
    print(root.buildTree())
    # Capture the stdout
    out, err = capfd.readouterr()
    assert out.split() == ['(ROOT',
    '((root', '(xuất', 'phát',
    '((nsubj', '(máy', 'bay',
    '((det', '(nào))', ')))',
    '(prep', '(từ', '((pobj',
    '(thành', 'phố', '((nmod',
    '(hồ', 'chí', 'minh))', ')))', ')))',
    '(prep', '(lúc', '((pobj', '(14:30HR))', ')))',
    '(punc', '(?.))', ')))', ')))']
