
def rendremonnaie(systeme,somme):
    reponse=[]
    for i in systeme:
        t=0
        while(somme >= i):
            t = t+1
            somme = somme - i
        if(somme < i):
            reponse.append(t)
    return reponse




# def toutrendremonnaie(systeme,somme):
#     toutreponse = []
#     while(systeme != ()):
#         toutreponse.append(rendremonnaie(systeme,somme))
#         systeme = systeme[1:]
#     return toutreponse
#########################################################################################    
#cache = {}

# def howmany(amount, coins):
#     prob = tuple([amount] + coins) # Problem signature
#     if prob in cache:
#         return cache[prob] # We computed this before
#     if amount == 0:
#         return 1 # It's always possible to give an exact change of 0 cents
#     if len(coins) == 1:
#         if amount % coins[0] == 0:
#             return 1 # We can match prescribed amount with this coin
#         else:
#             return 0 # It's impossible
#     total = 0
#     n = 0
#     while n * coins[0] <= amount:
#         total += howmany(amount - n * coins[0], coins[1:])
#         n += 1
#     cache[prob] = total # Store in cache to avoid repeating this computation
#     return total

# print(howmany(50, [15, 10, 6, 2]))
#################################################################################################
#1 2 5 10


# 10 5 1
# 20

# 10 10
# 10 5 5
# 10 5 11111
# 10 11111 11111
# 5 5 11111 11111
# 5 11111 11111 11111
# 11111 11111 11111 11111
#



#def combinations(systeme , somme):


def crossprod (list1, list2):
    output = 0
    for i in range(0,len(list1)):
        output += list1[i]*list2[i]

    return output

def breakit(target, coins):
    resultat = []
    coinslimit = [int(target / coins[i]) for i in range(0,len(coins))]
    count = 0
    temp = []
    for i in range(0,len(coins)):
        temp.append([j for j in range(0,coinslimit[i]+1)])


    r=[[]]
    for x in temp:
        t = []
        for y in x:
            for i in r:
                t.append(i+[y])
        r = t

    for targets in r:
        if crossprod(targets, coins) == target:
            resultat.append(targets)
            #print(targets)
            count +=1
    return resultat





print("Rendre monnaie")
print(rendremonnaie((100,50,20,10,5,1),153))
print("###################")
print("Toutes les methodes")
print(breakit(10000, [10000,5000,1000]))


#print(toutrendremonnaie((100,50,20,10,5,1),153))
#print(combinations((100,50,20,10,5,1),5))



