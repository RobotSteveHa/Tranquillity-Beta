import sys

class Tree:
    def __init__(self):
        # The code contained in the tree structure
        self.code   = None 
        # The lexical type of the included code
        self.type   = None
        
        # Branch information of Tree
        self.branchCount = 0
        self.branch      = []

    def set(self, code, type):
        """
        * Set basic data in tree. *
        """
        self.code = code
        self.type = type

    def addBranch(self, tree):
        """
        * Create a new branch *
        In essence, "create" is to add a new Tree to the branch list.
        """
        self.branch.append(tree)
        self.branchCount += 1
    
def showTree(mainTree):
    print('=' * 20)
    print("The id of the Tree:", id(mainTree))
    print("The code of the Tree: \n"+'-'*5+'\n'+str(mainTree.code)+'\n'+'-'*5)
    print("The type of the Tree: "+str(mainTree.type))
    print("The id of the Tree included: ", end='')
    for i in mainTree.branch:
        print(id(i), end='')
    print("\n"+'='*20)

class matchToken:
    """
    Find the location of the specified Token.
    This is equivalent to marking the Token.
    """
    def __init__(self, string, targetString):
        self.string           = string

        self.targetString     = targetString
        self.status           = []
    
    def find(self):
        pos             = None
        stringMode      = False 
        targetStringPos = 0

        for i in range(len(self.string)):
            if self.string[i] == '"' or self.string[i] == '\'':
                if stringMode == False:
                    stringMode = self.string[i] 
                else: 
                    stringMode == False
            if stringMode == False and self.targetString[targetStringPos] == self.string[i]: 
                for j in range(len(self.targetString)):
                    if self.targetString[j] != self.string[i+j]:
                        i += j
                        break
                self.status = [i, j+len(self.targetString)-1]
            
        print(self.status)

    def execution(self):
        self.find()
        return self.status

class astCreation:
    """
    * Creation of a preliminary AST structure *
    
    Parse the source code into AST.
    Token the source code through the token information.
    Then, it is parsed step by step through the token tag.
    Gradually improve ast from overall to detailed.
    """
    def __init__(self, sourceCode, syntaxInfo):
        self.sourceCode = sourceCode
        self.syntaxInfo = syntaxInfo

        self.mainAst       = Tree()
        self.endSymbolList = None

        # Token
        self.tokenType = None
        self.tokenEnd  = None

        self.tokenSign = None
    
    def checkResourceIntegrity(self):
        """
        * Check resource integrity. *

        Check if the required resources are missin.
        Note: check the integrity of resources generally.
        """
        try:
            # Statement Terminator
            self.endSymbolList = list(self.syntaxInfo["endSymbol"]["symbolList"])

            if (len(self.endSymbolList) == 0) or (not len(self.endSymbolList) == len(self.syntaxInfo["endSymbol"]["symbolList"])):
                print("OSError2: Lack of resource integrity.")
                sys.exit(0)
        except:
            print("OSError3: Lack of resource integrity.")
            sys.exit(0)

    def getToken(self):
        print(self.syntaxInfo)
        print(self.syntaxInfo["endSymbol"])
        print(self.syntaxInfo["endSymbol"]["symbolList"])

        for symbol in self.endSymbolList:
            self.tokenType = self.syntaxInfo["endSymbol"][symbol]["type"]
            if self.tokenType == "codeBlock": 
                self.tokenEnd  = self.syntaxInfo["endSymbol"][symbol]["end"]

            print(self.tokenType, self.tokenEnd)
            print(matchToken(self.sourceCode, self.tokenType).execution())

            self.tokenEnd = None
    
    def execution(self):
        self.checkResourceIntegrity()
        self.getToken()

