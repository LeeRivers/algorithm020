class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = len(s)
        lt = len(t)
        if ls != lt:
            return False
        stas = {}
        stat = {}
        for ch in s:
            stas[ch] = stas.get(ch,0)+1
        for ch in t:
            stat[ch] = stat.get(ch,0) + 1
            
        if stas == stat:
            return True
        else:
            return False