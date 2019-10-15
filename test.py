import zxcvbn as zx
import json

results = zx.zxcvbn('a1b3c5d7e')

for x in results:
    try :
        k = x + " : "
        for y in results[x]:
            d = results[x][y]
            if k != "":
                print("\n", k)
                k = ""
            print("\t", y, ":", d)
    except:
        print("\n", x, ":", results[x])

