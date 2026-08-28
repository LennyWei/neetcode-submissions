class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        can obviously turn into binary with bin(), any other ideas:
        '''

        res = 0

        for i in range(32):

            iIsOne = ((n >> i) & 1)

            if iIsOne:
                res |= (1 << (31 - i))

        return res