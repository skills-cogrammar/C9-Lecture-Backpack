class Movie:
    def __init__(self, title, review, rating):
        self.title = title
        self.review = review
        self.rating = rating

    def update_review(self, new_review):
        if new_review:
            self.review = new_review

    def update_rating(self, new_rating):
        if new_rating:
            self.rating = new_rating
        
    def __str__(self):
        return f"{self.title} - {self.rating}/10\n{self.review}"
