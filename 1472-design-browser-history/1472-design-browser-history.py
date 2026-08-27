class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)

    def visit(self, url: str) -> None:
        newPage = ListNode(url)
        self.curr.next = newPage
        newPage.prev = self.curr
        self.curr = newPage
        
    def back(self, steps: int) -> str:
        count = 0
        while count != steps:
            if not self.curr.prev:
                return self.curr.val
            self.curr = self.curr.prev
            count += 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        count = 0
        while count != steps:
            if not self.curr.next:
                return self.curr.val
            self.curr = self.curr.next
            count += 1
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)