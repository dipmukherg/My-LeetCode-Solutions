class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = 0
        start = 0
        max_len = 0
        lookup = set()
        idx=0
        while idx!=len(s):
        #for idx,i in enumerate(s):
            if idx==0:
                counter = 1
                max_len=1
                lookup.add(s[idx])
                idx+=1
                print(max_len)
            else:
                if s[idx] not in lookup:
                    lookup.add(s[idx])
                    counter+=1
                    if counter>max_len:
                        max_len=counter
                    idx+=1
                    #print(s[idx],counter,'lookup_failed')
                else:
                    counter=0
                    lookup=set()
                    start+=1
                    idx=start
                    #print(s[idx],counter,'lookup_successful')

        return max_len
