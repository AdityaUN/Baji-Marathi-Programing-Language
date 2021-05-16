
# ---------PARSE_RESULT------------
class ParseResult:
    def __init__(self):
        self.error = None
        self.node = None
        self.advance_count =0 

    def register_advancement(self):
        self.advance_count+=1

    def register(self, res):
        self.advance_count += res.advance_count
        if res.error:
            self.error= res.error
        return res.node

    def success(self, node):
        self.node = node
        return self

    def failure(self, error):
        if not self.error or self.advance_count==0:
            self.error = error
        return self

#------------Runtime Result---------------
class RTResult:
    def __init__(self):
        self.value = None
        self.error = None

    def register(self, res):
        if res.error: self.error = res.error
        return res.value

    def success(self, value):
        self.value = value
        return self

    def failure(self, error):
        self.error = error
        return self
