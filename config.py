#global cards values
cards_val = {str(v) : v for v in range(2,11)}
cards_val["A"] = 11
cards_val["J"] = 10
cards_val["Q"] = 10
cards_val["K"] = 10

#constants
INIT_RDS = 2
WIN = 1
PUSH = 0
SEPARATE_LINE = "--------"

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False