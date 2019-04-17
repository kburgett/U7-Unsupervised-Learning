
def main():
    header = ["level", "lang", "tweets", "phd", "interviewed_well"]
    table = [
            ["Senior", "Java", "no", "no", "False"],
            ["Senior", "Java", "no", "yes", "False"],
            ["Mid", "Python", "no", "no", "True"],
            ["Junior", "Python", "no", "no", "True"],
            ["Junior", "R", "yes", "no", "True"],
            ["Junior", "R", "yes", "yes", "False"],
            ["Mid", "R", "yes", "yes", "True"],
            ["Senior", "Python", "no", "no", "False"],
            ["Senior", "R", "yes", "no", "True"],
            ["Junior", "Python", "yes", "no", "True"],
            ["Senior", "Python", "yes", "yes", "True"],
            ["Mid", "Python", "no", "yes", "True"],
            ["Mid", "Java", "yes", "no", "True"],
            ["Junior", "Python", "no", "yes", "False"]
        ]

    # task: Define a function that prepends the 
    # attribute label and "=" before each attribute value in the table
    prepend_attribute_labels(table, header)
    for row in table:
        print(row)
    # why did we do this?
    # if we treat each row (instance) as a set
    # we will lose a no and/or a yes if tweets and phd
    # have the same value
    # summary: sets have no order and have no duplicates

    # unsupervised learning
    # we are going to cover association rule
    # mining (ARM) and k means clustering
    # we don't have a special attribute whose
    # value we are trying predict
    # so no more "class label"
    # looking for patterns, groups, associations
    # etc.

    # ARM
    # recall: decision trees give us classification rules
    # IF att1 = val1 AND att2 = val2 ... THEN class = classlabel1
    # let the "left hand side" or LHS be 
    # everything to the left of the THEN
    # let the RHS be everything to the right of the THEN
    # classification rules only have on "term"
    # attribute/value pair in its RHS
    # and at least one term in its LHS
    # for ARM we relax the constraint of one term in RHS
    # for ARM we have at least on term in LHS and
    # at least one term in RHS
    # for example
    # IF att1 = val1 AND att2 = val2 ... 
    # THEN att10 = val10 AND att11 = val11 AND ...
    # how to generate these rules?
    # one approach... brute force combinations
    # VERY computationally expensive
    # the approach we are going to use is Apriori
    # a few notes about ARM/Apriori
    # 1. even with tricks STILL VERY computationally expensive
    # 2. association does not imply causality
    # 3. we need to define new ways to evaluate
    # our rules... with apriori we will get 
    # alot of rules... some are super weak
    # some are super rare

    # our game plan for learning ARM
    # 1. given some rules, use them/evaluate them
    # 2. introduce apriori via lab examples
    # 3. starter code for apriori
    # 4. full implementation of apriori (PA8 :) last one)

    # Rule 1: interviewed_well=False => tweets=no
    # Rule 2: phd=no AND tweets=yes => interviewed_well=True
    # how to represent rules in Python?
    rule1 = {"lhs": ["interviewed_well=False"], "rhs": ["tweets=no"]}
    rule2 = {"lhs": ["phd=no", "tweets=yes"], "rhs": ["interviewed_well=True"]}
    # task: what are the confidence, support, and completeness measures
    # for these two rules? desk check then code it up!
    # Nleft, Nright, Nboth, Ntotal, confidence, support, completeness
    # rule1 desk check: 5, 7, 4, 14, 4/5, 4/14, 4/7
    # rule2 desck check: 4, 9, 4, 14, 4/4, 4/14, 4/9
    for rule in [rule1, rule2]:
        compute_rule_interestingness(rule, table)
        print(rule)

    # set theory basics
    # set: an unordered list with no duplicates
    # python has a set type
    # for example
    transaction = ["eggs", "milk", "milk", "sugar"]
    transaction_set = set(transaction)
    print(transaction_set)
    # note: order was lost, but we could just use a list
    # with no duplicates as a set
    transaction = list(transaction_set)
    print(transaction)
    # A union B: set of all items in A or B or both
    # A intersect B: set of all items in both A and B
    # can use set methods union() and intersection()
    # we need union for apriori
    # lets say we have an LHS set and and RHS set
    # LHS intersect RHS should be 0
    # LHS union RHS is sorted(LHS + RHS)
    # A is a subset of B: if all elements in A are also in B
    # check_row_match(A, B) will return 1 if A is a subset of B, 0 otherwise
    # powerset of A: the set of all possible subsets of A, including 0 and A
    import itertools
    powerset = []
    for i in range(0, len(transaction) + 1):
        # i represnets the size of our subsets
        subsets = list(itertools.combinations(transaction, i))
        powerset.extend([s for s in subsets])
    print(powerset)

    # intro to market basket analysis (MBA)
    # find associations between products customers buys
    # IF {"milk=true", "sugar=true"} THEN {"eggs=true"}
    # we are only interested in products purchased, not products not purchased
    # e.g. =true not the =false
    # for shorthand we can drop the =true
    # IF {"milk", "sugar"} THEN {"eggs"}
    # {"milk", "sugar"} -> {"eggs"}
    # terminology
    # each row in our dataset is now called a "transaction"
    # a transaction is an "itemset" 

    transactions = [
        ["b", "c", "m"],
        ["b", "c", "e", "m", "s"],
        ["b"],
        ["c", "e", "s"],
        ["c"],
        ["b", "c", "s"],
        ["c", "e", "s"],
        ["c", "e"]
    ]
    I = compute_unique_values(table)
    print(I)
    I = compute_unique_values(transactions)
    print(I)

    subsets = compute_k_1_subsets(transactions[3])
    print(subsets)

    rules = apriori(transactions, 0.25, 0.8)
    print(rules)

def apriori(table, minsup, minconf):
    supported_itemsets = []
    # implement apriori here
    # call your compute_unique_values() to get I
    # create L1, the list of singletons for each item in I
    k = 2
    # implement the while loop
    # remember: 1 task = 1 algorithm = 1 function
    # have fun :) last PA!!

    rules = generate_apriori_rules(table, supported_itemsets, minconf)
    return rules

def generate_apriori_rules(table, supported_itemsets, minconf):
    rules = []
    # for each itemset S in supported_itemsets
    # start with 1-item RHS, move on to 2-item RHS, etc.
    # for each rule, the remanining items not in RHS become LHS
    # LHS -> RHS

    return rules

def compute_k_1_subsets(itemset):
    subsets = []
    for i in range(len(itemset)):
        subsets.append(itemset[:i] + itemset[i + 1:])
    return subsets

def compute_unique_values(table):
    unique_values = set()
    for row in table:
        for value in row:
            unique_values.add(value)

    return sorted(list(unique_values))

def check_row_match(terms, row):
    for term in terms:
        if term not in row:
            return 0
    return 1
    

def compute_rule_interestingness(rule, table):
    compute_rule_counts(rule, table)
    rule["confidence"] = rule["Nboth"] / rule["Nleft"]
    rule["support"] = rule["Nboth"] / rule["Ntotal"]
    rule["completeness"] = rule["Nboth"] / rule["Nright"]

def compute_rule_counts(rule, table):
    Nleft = Nright = Nboth = 0
    Ntotal = len(table)

    for row in table:
        Nleft += check_row_match(rule["lhs"], row)
        Nright += check_row_match(rule["rhs"], row)
        Nboth += check_row_match(rule["lhs"] + rule["rhs"], row)

    rule["Nleft"] = Nleft
    rule["Nright"] = Nright
    rule["Nboth"] = Nboth
    rule["Ntotal"] = Ntotal



def prepend_attribute_labels(table, header):
    for row in table:
        for i in range(len(row)):
            label = header[i]
            row[i] = label + "=" + row[i]

if __name__ == "__main__":
    main()