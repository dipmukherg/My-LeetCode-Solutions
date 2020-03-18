class Solution:
    def longestPalindrome(self, s: str) -> str:
        #str1 = 'dipapidn'
        max_tuple=None

        table = [[0 for _ in range(len(s))] for _ in range(len(s))]
        if s=="":
            return ""
        elif len(s)==1:
            return s
        
        else:
            for i in range(len(s)):
                table[i][i]=1
                max_tuple=(i,i)

            for i in range(len(s)-1):

                if s[i] == s[i+1]:
                    #print(i,i+1)
                    table[i][i+1] = 1
                    #print(table[i][i+1])
                    max_tuple=(i,i+1)
                else:
                    table[i][i+1] = 0


            for j in range(2,len(s)):
                for i in range(len(s)):
                    if (i+j)<(len(s)):
                        if table[i+1][i+j-1]==0:
                            table[i][i+j]=0
                        else:
                            if s[i]==s[i+j]:
                                table[i][i+j] = 1
                                max_tuple=(i,i+j)
                            else:
                                table[i][i+j] = 0
                    else:
                        continue

            return (s[max_tuple[0]:max_tuple[1]+1])
