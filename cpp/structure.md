# Structure idea

Write structs as classes.

Current functions:
  + string writeNode(Node node)
  + bool nodeExistsInVector(Node n, vector<Node> v)
  * isStatement(Node n, vector<Node> jailOfVars)
  * int getFarIndex(Node far)
  * void showFormulas()
  * void showWhatWeKnow()
  * Node selectVariable()
   Node selectFormula()
  * vector<bool> getAllFariables(Node n)
    - vector<int> boolToIndex(vector<bool> b)
  * vector<Node> subformulasWithReps(Node x)
  * void useInferenceRule()
  * Node replaceAllSubnodesWithNode(Node formula, Node far, Node statement)
  * bool formulaIsInFormulas(Node f)
  * void addAllSubformulasToFormulas(Node x)
  * void plugStatement()
  + void initiateTypes()
  + void initiateAlphabet()
  + void initiateFormulas()
  * void runInterface()
  + void defineLogicAxioms()
  + void defineMathAxioms()

Class Knowledge that contains formulas and wwk?
  - void initiateTypes()
  - void initiateAlphabet()
  - void initiateFormulas()
  - void useInferenceRule()
  - void plugStatement()
  - bool formulaIsInFormulas(Node f)
  - void addAllSubformulasToFormulas(Node x) CHANGE
  - void defineLogicAxioms()
  - void defineMathAxioms()

Class Type

Class Symbol

Class Node
  - string writeNode(Node node)
  - bool nodeExistsInVector(Node n, vector<Node> v)
  - isStatement(Node n, vector<Node> jailOfVars)
  - int getFarIndex(Node far)
  - vector<bool> getAllFariables(Node n)
  - vector<Node> subformulasWithReps(Node x)
  - Node replaceAllSubnodesWithNode(Node formula, Node far, Node statement)

Class Interface
  - void showFormulas()
  - void showWhatWeKnow()
  - Node selectVariable()
  - Node selectFormula()
  - void runInterface()
