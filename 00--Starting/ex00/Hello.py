ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here

ft_list[1] = "World!"

# --------------------------------------------
#unchanchble
tmp = list(ft_tuple)
tmp[1] = "UAE"
ft_tuple = tmp

# --------------------------------------------

ft_set.discard("tutu!")
ft_set.add("Abu Dhabi")

# --------------------------------------------

ft_dict['Hello'] = "42AbuDhabi"

# --------------------------------------------
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)