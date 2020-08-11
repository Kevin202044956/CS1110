def unhide(x):
    a = x.replace(" at ","@")
    b = a.replace(" AT ","@")
    c = b.replace(" (at) ","@")
    d = c.replace(" dot ",".")
    e = d.replace(" DOT ",".")
    f = e.replace(" (dot) ",".")
    print(f)

unhide("mst3k@virginia.edu")
unhide("mst3k at virginia.edu")
unhide("mst3k (at) virginia (dot) edu")
unhide("mst3k AT virginia DOT edu")
unhide("mst3k@virginia dot edu")