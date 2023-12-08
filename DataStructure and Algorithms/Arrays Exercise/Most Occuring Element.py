# Find the Most Occuring Element  output: [('a',4), ('b',3)]

L1 = ['a', 'b','c','d','e','b','a','a','a','b']

def majority(elements):


    results = []

    for i in elements:
        cnt = elements.count(i)

        if (i,cnt) not in results:
            results.append((i,cnt))

    return results

print(majority(L1))



