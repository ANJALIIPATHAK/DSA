class Solution:
    def minOperations(self, logs: List[str]) -> int:
        logStack = []
        for operation in logs:
            if operation == "../":
                if logStack:
                    logStack.pop()
                else:
                    continue
            elif operation == "./":
                continue
            else:
                logStack.append(operation)
        return len(logStack)