# keyword arguments

# def sum_nums(*args):
#     print(args) # printing arguments
#     print(type(args)) # its gonna be 'tuple'

#     print(args[0]) # printing index
#     return(sum(args)) # returning sum

# print(sum_nums(5, 2, 20, 10, 3, 4))

# another example of positional arguments
# def get_posts_info(name, posts_qty):
#     info = f"{name} wrote {posts_qty} posts"
#     return info

# info = get_posts_info("Artem", 25)
# print(info)

#####################
# ** means that function takes an arbitrary number of named arguments (key=value)
# and converts them into dictionary
def get_posts_info(**person):  
    print(person) # {'posts_qty': 30, 'name': 'Artem', 'id': 1348}
    info = f"{person['name']} wrote {person['posts_qty']} posts"
    return info

info = get_posts_info(posts_qty = 30, name = "Artem", id = 1348)
# Literally those arguments converts into this:
# person = {
#     'posts_qty': 30,
#     'name': 'Artem',
#     'id': 1348
# }
print(info)

####### one more example 
def parsing_some_info(**pc_specs):
    print(pc_specs) # printing all specs | key=value
    specs = (
        f"CPU: {pc_specs['CPU']}\nMotherboard: {pc_specs['Motherboard']}\n"
        f"RAM: {pc_specs['RAM']}\nGPU: {pc_specs['GPU']}\nPSU: {pc_specs['PSU']}\n"
        f"Storage: {pc_specs['Storage']}\nCooler/AIO: {pc_specs['cool_sys']}\n"
        f"Case: {pc_specs['Case']}"
    )
    return specs

pc_specs = parsing_some_info(CPU = "Intel Core i7 11700KF", Motherboard = "Z590i Vision-D", 
                             RAM = "DDR4 HyperX 2x16Gb 3200 Mhz", GPU = "RTX 3070ti FE",
                             PSU = "Corsair 600W Platinum", 
                             Storage = "Samsung 980Evo 1tb/Crucial P3 2Tb",
                             cool_sys = "Be quiet Silent Loop 280mm",
                             Case = "Cooler Master NR200P")
print(f"\nFINAL PC SPECS:\n{pc_specs}")