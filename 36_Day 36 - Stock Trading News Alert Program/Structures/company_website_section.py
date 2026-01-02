class CompanyWebsiteSection:
    def __init__(self, **kwargs):
        self.stock =kwargs ["stock"]
        self.price_change = kwargs["price_change"]
        self.articles = kwargs["articles"]
        self.article_number=-1

    def structure (self):
        return f"""
        <div>
            <h3>Company Stock ID: {self.stock}</h3>
            <h3>Company Price Change: {self.price_change}</h3>
            <h3>Articles</h3>
            <ul style="margin-left: 20px;">
                <li>{self.articles[self.article_number+1][0]} I {self.articles[self.article_number+1][1]} I {self.articles[self.article_number+1][2]}/li>
        <div>
    
        """
