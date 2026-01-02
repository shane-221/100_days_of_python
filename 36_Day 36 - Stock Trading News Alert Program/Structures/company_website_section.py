class CompanyWebsiteSection:
    def __init__(self, **kwargs):
        self.stock =kwargs ["stock"]
        self.price_change = kwargs["price_change"]
        self.articles = kwargs["articles"]
        self.article_number=-1

    def structure (self):
        articles_html = ""
        for a in self.articles:
            articles_html += f"<li>{a[0]} -- {a[1]} -- {a[2]}\n</li>"

        print(articles_html)

        return f"""
            <div>
                <h3>Company Stock ID: {self.stock}</h3>
                <h3>Company Price Change: {self.price_change}</h3>
                <h3>Articles</h3>
                <ul style="margin-left: 20px;" >
                    {articles_html}
                </ul>
            </div>
        """
