import zxcvbn as zx
import json

results = zx.zxcvbn('hello world')

for x in results:
    try :
        k = x + " : "
        for y in results[x]:
            d = results[x][y]
            if k != "":
                print(k)
                k = ""
            print("\t", y, ":", d)
    except:
        print(x, ":", results[x])

    print("\n")
