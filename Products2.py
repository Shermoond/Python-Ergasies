def cost(x):
    cost=[]
    for i in products:
        for j in products[i]:
            cost.append(products[i].get(j))
    t_c=0
    for i in range(0,len(cost)-1):
        t_c=+cost[i]
    t_c=t_c*cost[3]+t_c
    print(t_c)

    
products={
    "goods":{
        "oranges":1.08,
        "apples":10,
        "chocholates":25
    },
    "taxes":{
        "vat":0.24
    }
}
cost(products)