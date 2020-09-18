from models.dbcontext import DbContext

class Cart(DbContext):
    def getCarts(self, id)
        sql = '''Select Cart.*, Price, ImageUrl, ProductName from Cart Join production.Product
            On Cart.ProductId = production.Product.ProductId and CartId = ? '''
        return self.fetchAll(sql, (id, ))
    
    