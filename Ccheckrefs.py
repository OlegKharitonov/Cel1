
def checknew(all_refs, reffile):

    newitems = []

    with open(reffile, 'r') as itfi:
        cont = itfi.read()

    for elem in all_refs:
        if elem not in cont:
            newitems.append(elem)

    return newitems