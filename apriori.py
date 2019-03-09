import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


def readMatrix(file):
    fd = open(file, 'r')
    dataset = list()
    for itemset in fd:
        dataset.append( list(itemset.strip().split(",")) )
    return dataset


if __name__ == "__main__":
    dataset =readMatrix("route.csv")

    te = TransactionEncoder()
    te_ary = te.fit(dataset).transform(dataset)
    df = pd.DataFrame(te_ary, columns=te.columns_)

    frequent_itemsets = apriori(df, min_support=0.1, use_colnames=True)

    print "\n --------------------------------------------------------------------------------------------------------------"
    print "                                 FREQUENT ITEMSETS GENERATED"
    print "-----------------------------------------------------------------------------------------------------------------"
    print "\n\n\n",frequent_itemsets



    rules=association_rules(frequent_itemsets, metric="support", min_threshold=0.1)
    print "\n --------------------------------------------------------------------------------------------------------------"
    print "                                 ASSOCIATION RULES GENERATED"
    print "-----------------------------------------------------------------------------------------------------------------"
    print "\n\n\n",rules
