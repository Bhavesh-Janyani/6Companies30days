# Runtime = 69ms (74.62%) 
# Memory = 14.1MB (39.9%)

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        count = Counter(senate)
        bans = defaultdict(int)
        z = 0
        while count['D'] > 0 and count['R'] > 0:
            nextSenate = []
            for party in senate:
                oppo = 'R' if party == 'D' else 'D'
                if bans[party]:
                    bans[party] -= 1
                else:
                    bans[oppo] += 1
                    count[oppo] -= 1
                    nextSenate.append(party)
            senate = nextSenate
        return 'Radiant' if count['R'] > 0 else 'Dire'
        
            