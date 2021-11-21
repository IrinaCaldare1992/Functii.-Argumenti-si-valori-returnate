def euro_to_usd( amount ):
    eur_to_usd = 1.2
    result = amount * eur_to_usd
    return result

def usd_to_euro( amount ):
    usd_to_eur = 1.2
    result = amount / usd_to_eur
    return result


print("\n", euro_to_usd(1000))
print("\n", usd_to_euro(1200)) 
