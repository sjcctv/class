        for i in range(rg):
    # even index elements are positive
            if i % 2 == 0:
                s += 4/k
            else:
         
                # odd index elements are negative
                s -= 4/k
            # denominator is odd
            k += 2
        return(s)
