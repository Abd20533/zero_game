

x = str(input("enter please levele 1 to 4 : "))
if (x == "1"):
    import level1 as l1
if (x == "2"):
    import level2 as l2
if (x == "3"):
    import level3 as l3
if (x == "4"):
    import level30 as l4
if (x != "1" and x != "2" and x != "3" and x != "4"):
    print("error")
    print(f"on level {x}")
