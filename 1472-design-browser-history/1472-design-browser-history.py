class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.currPage = ListNode(homepage)

    def visit(self, url: str) -> None:
        newPage = ListNode(url)
        self.currPage.next = newPage
        newPage.prev = self.currPage
        self.currPage = newPage
        
    def back(self, steps: int) -> str:
        while self.currPage.prev and steps > 0:
            self.currPage = self.currPage.prev
            steps -= 1
        return self.currPage.val 

    def forward(self, steps: int) -> str:
        while self.currPage.next and steps > 0:
            self.currPage = self.currPage.next
            steps -= 1
        return self.currPage.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)