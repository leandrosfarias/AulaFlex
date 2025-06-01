

class Feedback:
    def __init__(self, user_id: str, rating: int, comment: str):
        self.user_id = user_id
        self.rating = rating
        self.comment = comment

    def __repr__(self):
        return f"Feedback(user_id={self.user_id}, rating={self.rating}, comment={self.comment})"
