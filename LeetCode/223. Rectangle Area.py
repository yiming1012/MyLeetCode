
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        rec1 = (C - A) * (D - B)
        rec2 = (G - E) * (H - F)

        x1 = max(A, E)
        y1 = max(B, F)
        x2 = min(C, G)
        y2 = min(D, H)
        if x1 < x2 and y1 < y2:
            area = (x2 - x1) * (y2 - y1)
            return rec1 + rec2 - area
        else:
            return rec1 + rec2