
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
    

def compute_rule_interestingness(rule, table):
    compute_rule_counts(rule, table)
    rule["confidence"] = rule["Nboth"] / rule["Nleft"]
    rule["support"] = rule["Nboth"] / rule["Ntotal"]
    rule["completeness"] = rule["Nboth"] / rule["Nright"]

def compute_rule_counts(rule, table):
    Nleft = Nright = Nboth = 0
    Ntotal = len(table)

    for row in table:
        Nleft += check_row_match(row, rule["lhs"])
        Nright += check_row_match(row, rule["rhs"])
        Nboth += check_row_match(row, rule["lhs"] + rule["rhs"])

    rule["Nleft"] = Nleft
    rule["Nright"] = Nright
    rule["Nboth"] = Nboth
    rule["Ntotal"] = Ntotal

def check_row_match(row, terms):
    for term in terms:
        if term not in row:
            return 0
    return 1

def prepend_attribute_labels(table, header):
    for row in table:
        for i in range(len(row)):
            label = header[i]
            row[i] = label + "=" + row[i]

if __name__ == "__main__":
    main()