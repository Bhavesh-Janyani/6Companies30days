# Runtime = 17ms (91.26%) 
# Memory = 13.3MB (98.6%)

class Solution:
    def fractionToDecimal(self, numerator, denominator):
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator < 0 else ''
        integer = sign + str(n)
        if remainder == 0: return integer
    
        rs = {}       
        decimal = ''
        i = 0
        while remainder > 0 and remainder not in rs:
            rs[remainder] = i
            n, remainder = divmod(remainder*10, abs(denominator))
            decimal += str(n)
            i +=  1
        
        if remainder in rs:
            i = rs[remainder]
            return integer + '.' + decimal[:i] + '(' + decimal[i:] + ')'
        else:
            return integer + '.' + decimal[:]