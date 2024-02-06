#7.1 Make a list called year_list.
years_list = [1980, 1981, 1982, 1983, 1984, 1985]

#7.2 in which year on the year_list was my third birthday?
print(years_list[3])

#7.3 in which year_list was I the oldest.
print(years_list[5])

#7.4 Make a list called things with this strings: mozzarella, cinderella, salmonella.
things = ["mozzarella", "cinderella", "salmonella"]

#7.5 Capitalize things with person.
things[1] = things[1].capitalize()
print(things)
#question: did it change in list? YES
#BUG REPORT: took me a little while to figure out how to print that specific item.
# first couple tries will print all elements capitalized.

#7.6 Make the cheesy elements in list capitalize.
things[0] = things[0].capitalize()
print(things)
# BUG REPORT: this one I got it at first try.

#7.7 Delete the the disease element in list.
things.remove("salmonella")
print(things)

#9.1 Define the function called good that returns list.

def good():
    print(["Harry", "Ron", "Hermione"])
good()
# BUG REPORT: I don't know if this is correct, I still get confuse using return vs print!
# if I use return< it prints nothing 
  
    
    
#9.2 define a generator function called get_odds and return odd numbers from range 10
def odd_numbers(numbers) :
    new_list = []
    for i in range(0,len(numbers)-1) :
        if i % 2 != 0 :
            new_list.append(i)
    return new_list
l = [1,2,3,4,5,6,7,8,9,10]
print(odd_numbers(l))
#BUG REPORT, It took a couple of tries, first couple rins wouldn print anything
     
