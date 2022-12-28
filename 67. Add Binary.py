class Solution:
    def addBinary(self, a: str, b: str) -> str:
        binary = int(a, 2) + int(b, 2)
        return bin(binary)[2:]