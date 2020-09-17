from collections import defaultdict

class Solution:
    def highFive(self, items):
        id_to_scores = defaultdict(list)
        
        for _, item in enumerate(items):
            id_to_scores[item[0]].append(item[1])
        for k in id_to_scores.keys():
            id_to_scores[k].sort(reverse=True)
            id_to_scores[k] = sum(id_to_scores[k][:5])//5
        return [[id, score] for id, score in id_to_scores.items()]
        