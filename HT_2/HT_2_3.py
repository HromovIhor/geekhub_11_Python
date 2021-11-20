#Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

def Remove_Empty(tuples):
    tuples = [i for i in tuples if i]
    return tuples

hard_coded = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
print(Remove_Empty(hard_coded))
