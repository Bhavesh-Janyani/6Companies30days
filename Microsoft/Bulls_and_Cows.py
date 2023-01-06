# Runtime = 31ms (81.32%) 
# Memory = 13.9MB (8.16%)

class Solution(object):
    def getHint(self, secret, guess):
        counts = Counter(secret)
        cow = 0
        bull = 0
        for pos in range(len(secret)):
            # if bull
            if secret[pos] == guess[pos]:
                if counts[guess[pos]] > 0:
                    bull += 1
                    counts[guess[pos]] -= 1
                else:
                    cow -= 1
                    bull += 1
            # if cow
            elif guess[pos] in counts:
                if counts[guess[pos]] > 0:
                    counts[guess[pos]] -= 1
                    cow += 1
        return str(bull) + "A" + str(cow) + 'B'