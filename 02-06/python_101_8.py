total_bill = float(raw_input("Total bill amount? "))
service = raw_input("Level of service? ")
split = int(raw_input("split how many ways? "))
good = float(0.20 * total_bill)
fair = float(0.15 * total_bill)
bad = float(0.10 * total_bill)
good_bill = float(good + total_bill)
fair_bill = float(fair + total_bill)
bad_bill = float(bad + total_bill)
good_bill_split = float(good_bill / split)
fair_bill_split = float(fair_bill / split)
bad_bill_split = float(bad_bill / split)
if service == "good":
    print "Tip amount: %0.2f" % good
    print "Total amount: %0.2f" % good_bill
    print "Amount per person: %0.2f" % good_bill_split
elif service == "fair":
    print "Tip amount: %0.2f" % fair
    print "Total amount: %0.2f" % fair_bill
    print "Amount per person: %0.2f" % fair_bill_split
elif service == "bad":
    print "Tip amount: %0.2f" % bad
    print "Total amount: %0.2f" % bad_bill
    print "Amount per person: %0.2f" % bad_bill_split
