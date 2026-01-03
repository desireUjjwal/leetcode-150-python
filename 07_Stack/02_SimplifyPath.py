71. Simplify Path

# transform this absolute path into its simplified canonical path.

# The rules of a Unix-style file system are as follows:

# A single period '.' represents the current directory.
# A double period '..' represents the previous/parent directory.
# Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
# Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
# The simplified canonical path should follow these rules:

# The path must start with a single slash '/'.
# Directories within the path must be separated by exactly one slash '/'.
# The path must not end with a slash '/', unless it is the root directory.
# The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
# Return the simplified canonical path.

class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split("/")
        stack = []
        for x in components:
            if(x == "" or x == "."):
                continue
            if x == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(x)
        return "/" + "/".join(stack)

# little more optimized approach:
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = ""
        for c in path + "/":
            if c == "/":
                if curr == "..":
                    if stack:
                        stack.pop()
                elif curr != "." and curr != "":
                    stack.append(curr)
                curr = ""
            else:
                curr += c
        return "/" + "/".join(stack)
