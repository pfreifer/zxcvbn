from src import zxcvbn_functions as zx

results = zx.zxcvbn('immeuble')

for x in results:
    try:
        k = x + " : "
        for y in results[x]:
            d = results[x][y]
            if k != "":
                print("\n", k)
                k = ""
            print("\t", y, ":", d)
    except:
        print("\n", x, ":", results[x])
