class CompanyWebsiteSection:
    def __init__(self, **kwargs):
        self.stock =kwargs ["stock"]
        self.price_change = kwargs["price_change"]
        self.articles = kwargs["articles"]

    def structure (self):
        return f"""
        <div>
            <h3>Company Stock ID: {self.stock}</h3>
            <h3>Company Price Change: {self.price_change}</h3>
            <h3>Articles</h3>
        <div>
    
        """
