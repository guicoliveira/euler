

class Line:

    def __init__(self, depth):
        self.depth = depth
        self.nodes = []
    
    def appendNode(self, node):
        self.nodes.append(node)

    def getNodesAsArray(self):
        nodeValues = []
        for node in self.nodes:
            nodeValues.append(node.getValue())
        return nodeValues
    
    

    def __str__(self):
        strRet = ""
        for node in self.nodes:
            strRet += node.getValue()
            strRet += " "
        return strRet

class Tree:
    
    def __init__(self, allNumbers):
        self.root = Node(allNumbers, 0, 0, 0)

    def addNode(self, line):
        self.lines.append(line)
 
    def getBiggerValue(self):
        print(self.root.getBiggerValue())

    def getRightNodeValuesSummed(self):
        print( self.root.getRightNodeValuesSummed())

    def getDepth(self):
        return len(self.lines)

    def __str__(self):
        strRet = ""
        for line in self.lines:
            strRet += line.__str__()
            strRet += "\n"
        return strRet

class TreeOld:
    
    def __init__(self):
        self.lines = []

    def addLine(self, line):
        self.lines.append(line)
    
    def getLine(self, depth):
        return self.lines[depth]

    def getDepth(self):
        return len(self.lines)

    def __str__(self):
        strRet = ""
        for line in self.lines:
            strRet += line.__str__()
            strRet += "\n"
        return strRet

class Node:
    def __init__(self, allNumbers, line, pos, parentValue):
        self.value = int(allNumbers[line][pos])
        self.line = line

        if line < (len(allNumbers)-1):
            self.leftNode = Node(allNumbers, line+1, pos, self.value)
            self.RightNode = Node(allNumbers, line+1, pos+1, self.value)
        
    
    def getRightNodeValuesSummed(self):
        try:
            return self.value + self.RightNode.getRightNodeValuesSummed()
        except AttributeError:
            return self.value

    def getValue(self):
        return self.value

    def getBiggerValue(self):

        try:
            rightV = self.value + self.RightNode.getBiggerValue()
            leftV = self.value + self.leftNode.getBiggerValue()
        except AttributeError:
            return self.value
        
        return rightV if rightV > leftV else leftV


