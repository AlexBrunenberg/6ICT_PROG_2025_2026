def seconden_per_dag(aantal):
    """ return het aantal seconden in aantal dagen 
            Tip! een dag is 24u, een uur 60min, een minuut 60s
    """
    return aantal * 24*60*60

print( seconden_per_dag(1) )    # 86400
print( seconden_per_dag(3) )    # 259200
print( seconden_per_dag(7) )    # 604800
