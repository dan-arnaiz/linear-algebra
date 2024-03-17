class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        element_to_row = {}
        matrix = []
        for num in nums:
            if num in element_to_row:
                if element_to_row[num] + 1 == len(matrix):
                    matrix.append([])
                matrix[element_to_row[num] + 1].append(num)
                element_to_row[num] += 1
            else:
                if len(matrix) == 0:
                    matrix.append([])
                matrix[0].append(num)
                element_to_row[num] = 0
        return matrix

# test    
if __name__ == "__main__":
    s = Solution()
    print(s.findMatrix([1,3,4,1,2,3,1])) 
    print(s.findMatrix([1,2,3,4,5])) 
    print(s.findMatrix([1,1,1,1,1])) 
