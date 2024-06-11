import os

class ScoreManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.scores = self._load_scores()

    def _load_scores(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, 'r') as file:
            scores = [line.strip().split(',') for line in file.readlines()]
            if len(scores) > 0:
                scores = [(name, int(score)) for name, score in scores]
                return sorted(scores, key=lambda x: x[1], reverse=True)
            return []

    def add_score(self, name, score):
        self.scores.append((name, score))
        self.scores = sorted(self.scores, key=lambda x: x[1], reverse=True)
        self._save_scores()

    def _save_scores(self):
        with open(self.file_path, 'w') as file:
            for name, score in self.scores:
                file.write(f"{name},{score}\n")

    def get_highest_score(self):
        return self.scores[0] if self.scores else None

    def get_top_five_scores(self, n=5):
        return self.scores[:n]