# Runtime = 223ms (100%) 
# Memory = 20MB (55.56%)

class TweetCounts:
    def __init__(self):
        self.words = defaultdict(lambda: [])

    def recordTweet(self, tweetName: str, time: int) -> None:
        insort(self.words[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        idxStart = bisect_left(self.words[tweetName], startTime)
        idxEnd = bisect_right(self.words[tweetName], endTime)
        tmp = self.words[tweetName][idxStart: idxEnd]
        if freq == "minute":        
            div = 60
        elif freq == "hour":
            div = 3600
        else: 
            div = 84600
        maxElem = (endTime - startTime)//div  
        ans = [0 for _ in range(maxElem + 1)]
        for num in tmp: 
            idx = (num - startTime)//div
            ans[idx] += 1
        return ans