"""Print out all the melons in our inventory."""


from melons import new_melon_dict # importing the new_melon_dict dictionary of dictionaries
# key = melon as string
# value = dictionary of melon attributes

def print_melon(melon_file):
    """Print each melon."""
    for melon in new_melon_dict: #for each index, which is each melon name
        print melon.upper() # print name of the melon as key
        for attribute in new_melon_dict[melon]: #iterate through dictionary value of each melon
            print '  ' + str(attribute) + ' : ' + str(new_melon_dict[melon][attribute])
            #print "  seedless: " + str(new_melon_dict[melon]["melon_seedlessness"])
            #print "  price: " + str(new_melon_dict[melon]["melon_price"])
"""   
    have_or_have_not = 'have'
    if seedless:
        have_or_have_not = 'do not have'

    print "{}s {} seeds and are ${:.2f}".format(name, have_or_have_not, price)
"""

"""
for i in melon_names:
    print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
"""

print_melon(new_melon_dict)