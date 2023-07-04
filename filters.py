from itertools import filterfalse

orders = [
    {"id":1, "status":"pago", "quantity":5},
    {"id":2, "status":"pago", "quantity":2},
    {"id":3, "status":"cancelado", "quantity":3},
    {"id":4, "status":"cancelado", "quantity":4}
]

def foi_pago(orden):
    return orden["status"] == "pago"

def n_foi_pago(orden):
    return orden["status"] == "cancelado"

orders_pagos = filter(foi_pago, orders)
list(orders_pagos)

orders_nao_agos = filter(n_foi_pago, orders)
list(orders_nao_agos)

orders_nao_agos_usingff = filterfalse(foi_pago, orders)

list(filter(None, [ 0,0,1,None,False,True,2])) # [1, True, 2]

list(filterfalse(None, [ 0,0,1,None,False,True,2])) # [0, 0, None, False]