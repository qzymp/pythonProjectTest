class Pager:
    def __init__(self, current_page):
        # 用户请求的页码
        self.current_page = current_page
        # 每页的数据数
        self.per_items = 10

    # 每页第一条的数据
    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items + 1
        return val

    # 每页最后一条数据
    @property
    def end(self):
        val = self.current_page * self.per_items
        return val

p = Pager(8)
print(p.start)
print(p.end)