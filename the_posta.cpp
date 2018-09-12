#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <map>

// TODO: Add defs.
// TODO: childrenFormat is never used. Fix it.

using namespace std;

#define forsn(i, s, n) for(int i = (int) s; i < (int) n; i++)
#define forn(i, n) forsn(i, 0, n)

int varsCardinality = 1;
int farsCardinality = 4;

struct Type {
  string name;
};

struct Symbol {
  string drawing;
  Type type;
  vector<Type> childrenFormat;
};

struct Node {
  Symbol symbol;
  vector<Node> children;
};

map<string, Type> types;
map<string, Symbol> alphabet;

vector<Node> formulas;
vector<Node> whatWeKnow;

string writeNode(Node node) {
  string s = "";
  s += node.symbol.drawing + (node.children.size() > 0 ? "(" : "");

  forn(i, node.children.size()) {
    s += writeNode(node.children[i]);
    s += i != node.children.size() - 1 ? ", " : "";
  }

  s += node.children.size() > 0 ? ")" : "";
  return s;
} // DONE

bool nodeExistsInVector(Node n, vector<Node> v) {
	forn(i, v.size()) if (n.symbol.drawing == v[i].symbol.drawing) return true;
	return false;
}

bool isStatement(Node n, vector<Node> jailOfVars) {
	vector<Node> newJailOfVars;
	newJailOfVars = jailOfVars;

	if (n.symbol.drawing == alphabet["exists"].drawing) {
		newJailOfVars.push_back(n.children[0]);
	} else if (n.symbol.type.name == types["variable"].name) {
		if (!nodeExistsInVector(n, jailOfVars)) return false;
	}

	forn(i, n.children.size()) {
		if (!isStatement(n.children[i], newJailOfVars)) {
			return false;
		}
	}

	return true;
}

int getFarIndex(Node far) {
	string indexAsText = far.symbol.drawing.substr(2);
	return stoi(indexAsText);
}

void showFormulas() {
	vector<Node> v;

  forn(i, formulas.size()) {
		string text = "\tNO ENUNCIADO";
		if (isStatement(formulas[i], v)) text = "\tENUNCIADO";
    cout << i << ") "<< text << ": \t" << writeNode(formulas[i]) << endl;
  }
}

void showWhatWeKnow() {
  forn(i, whatWeKnow.size()) {
    cout << i << ") " << writeNode(whatWeKnow[i]) << endl;
  }
}

Node selectVariable() {
  int x = -1;

  while (!(x >= 0 && x < varsCardinality)) {
    cout << "Elegí una variable entre 0 y " + to_string(varsCardinality - 1);
    cout << " inclusive. Danos el número:" << endl;
    cin >> x;

    if (!(x >= 0 && x < varsCardinality)) {
      cout << "Tu mamá tiene cara de rana." << endl;
    }
  }

  if (x == varsCardinality - 1) {
    Symbol var;
    var.drawing = "v_" + to_string(varsCardinality);
    var.type = types["variable"];
    alphabet["v_" + to_string(varsCardinality)] = var;
    varsCardinality++;
  }

  Node node;
  node.symbol = alphabet["v_" + to_string(x)];
  return node;
}

Node selectFormula() {
  int x = -1;

  while (!(x >= 0 && x < formulas.size())) {
    cout << "Elegí una formula entre 0 y " + to_string(formulas.size() - 1);
    cout << " inclusive de la siguiente lista:" << endl;
    showFormulas();
    cin >> x;

    if (!(x >= 0 && x < formulas.size())) {
      cout << "Tu mamá tiene cara de rana." << endl;
    }
  }

  // TODO: change to compare structs
  Symbol lastFariable = alphabet["F_" + to_string(farsCardinality - 1)];

  if (formulas[x].symbol.drawing == lastFariable.drawing) {
    Symbol far;
    far.drawing = "F_" + to_string(farsCardinality);
    far.type = types["formula"];
    alphabet["F_" + to_string(farsCardinality)] = far;
    Node node;
    node.symbol = far;
    formulas.push_back(node);
    farsCardinality++;
  }

  return formulas[x];
}

vector<bool> getAllFariables(Node n) {
	vector<bool> isFarOn;
	forn(i, farsCardinality) isFarOn.push_back(false);

	if (n.symbol.drawing[0] == 'F') {
		isFarOn[getFarIndex(n)] = true;
	}

	forn(i, n.children.size()) {
		vector<bool> tempIsFarOn;
		tempIsFarOn = getAllFariables(n.children[i]);
		forn(j, farsCardinality) isFarOn[j] = isFarOn[j] || tempIsFarOn[j];
	}

	return isFarOn;
}

vector<int> boolToIndex(vector<bool> b) {
	vector<int> v;

	forn(i, b.size()){
		if(b[i]){
			v.push_back(i);
		}
	}

	return v;
}

vector<Node> subformulasWithReps(Node x) {
  vector<Node> result;

  forn(i, x.children.size()) {
    result.push_back(x.children[i]);
    vector<Node> partialResult = subformulasWithReps(x.children[i]);
    forn(j, partialResult.size()) result.push_back(partialResult[j]);
  }

  return result;
}

void useInferenceRule() {
	int index;

	cout << "Elegí una verdad de la forma A=>B:" << endl;
	showWhatWeKnow();

	cin >> index;

	if(!(index < whatWeKnow.size()) || whatWeKnow[index].symbol.drawing != alphabet["implies"].drawing){
		cout << "Tu viejo también." << endl;
	} else {
		forn(i, whatWeKnow.size()){
			if(writeNode(whatWeKnow[index].children[0]) == writeNode(whatWeKnow[i])){
				whatWeKnow.push_back(whatWeKnow[index].children[1]);
				formulas.push_back(whatWeKnow[index].children[1]);
			}
		}
	}
}

Node replaceAllSubnodesWithNode(Node formula, Node far, Node statement) {
  Node newFormula;
  newFormula = formula;

  forn(i, newFormula.children.size()) {
    Node newChild;
    newChild = newFormula.children[i];

    if (writeNode(newChild) == writeNode(far)) {
      newChild = statement;
    } else {
      newChild = replaceAllSubnodesWithNode(newChild, far, statement);
    }

    newFormula.children[i] = newChild;
  }

  return newFormula;
}

bool formulaIsInFormulas(Node f) {
  forn(i, formulas.size()) {
    if (writeNode(formulas[i]) == writeNode(f)) {
      return true;
    }
  }

  return false;
}

void addAllSubformulasToFormulas(Node x) {
  vector<Node> repeatedSubformulas = subformulasWithReps(x);

  forn(i, repeatedSubformulas.size()) {
    if (!formulaIsInFormulas(repeatedSubformulas[i])) {
      formulas.push_back(repeatedSubformulas[i]);
    }
  }
}

void plugStatement() {
	int indexOfFirstStatement, indexOfFariable, indexOfSecondStatement;
	Node truth;

	cout << "Elegí una verdad que tenga fariables:" << endl;
	showWhatWeKnow();

	cin >> indexOfFirstStatement;
	truth = whatWeKnow[indexOfFirstStatement];
  vector<int> listOfFariables = boolToIndex(getAllFariables(truth));

	if(!(indexOfFirstStatement < whatWeKnow.size())){
		cout << "Tu viejo también." << endl;
	} else {
		cout<<"elegiiiiiil una de las fariables que aparecen: "<<endl;

		forn(i, listOfFariables.size()){
			cout<<i<<") F_"<< listOfFariables[i] <<endl;
		}

		cin >> indexOfFariable;

    cout<<"elegiiiiiil una de les enunciades que aparecen: "<<endl;
    showFormulas();
    cin >> indexOfSecondStatement;

    vector<Node> v;

    if (isStatement(formulas[indexOfSecondStatement], v)) {
      Node newTruth;
      Node far;
      far.symbol = alphabet["F_" + to_string(listOfFariables[indexOfFariable])];

      newTruth = replaceAllSubnodesWithNode(
        truth,
        far,
        formulas[indexOfSecondStatement]
      );

      whatWeKnow.push_back(newTruth);
      formulas.push_back(newTruth);

      addAllSubformulasToFormulas(newTruth);
    }
	}
}

void initiateTypes() {
  // FORMULA
  Type FORMULA;
  FORMULA.name = "formula";
  types["formula"] = FORMULA;

  // VARIABLE
  Type VARIABLE;
  VARIABLE.name = "variable";
  types["variable"] = VARIABLE;
} // DONE

void initiateAlphabet() {
  // AND
  Symbol AND;
  AND.drawing = "∧";
  AND.type = types["formula"];
  AND.childrenFormat.push_back(types["formula"]);
  AND.childrenFormat.push_back(types["formula"]);
  alphabet["and"] = AND;

  // NOT
  Symbol NOT;
  NOT.drawing = "¬";
  NOT.type = types["formula"];
  NOT.childrenFormat.push_back(types["formula"]);
  alphabet["not"] = NOT;

  // EXISTS
  Symbol EXISTS;
  EXISTS.drawing = "∃";
  EXISTS.type = types["formula"];
  EXISTS.childrenFormat.push_back(types["variable"]);
  EXISTS.childrenFormat.push_back(types["formula"]);
  alphabet["exists"] = EXISTS;

  // EQUALS
  Symbol EQUALS;
  EQUALS.drawing = "=";
  EQUALS.type = types["formula"];
  EQUALS.childrenFormat.push_back(types["variable"]);
  EQUALS.childrenFormat.push_back(types["variable"]);
  alphabet["equals"] = EQUALS;

  // BELONGS TO
  Symbol BELONGS_TO;
  BELONGS_TO.drawing = "∈";
  BELONGS_TO.type = types["formula"];
  BELONGS_TO.childrenFormat.push_back(types["variable"]);
  BELONGS_TO.childrenFormat.push_back(types["variable"]);
  alphabet["belongsTo"] = BELONGS_TO;

  // IMPLIES
  Symbol IMPLIES;
  IMPLIES.drawing = "⇒";
  IMPLIES.type = types["formula"];
  IMPLIES.childrenFormat.push_back(types["formula"]);
  IMPLIES.childrenFormat.push_back(types["formula"]);
  alphabet["implies"] = IMPLIES;

  // FIRST VARIABLES
  forn(i, 3) {
    Symbol var;
    var.drawing = "v_" + to_string(i);
    var.type = types["variable"];
    alphabet["v_" + to_string(i)] = var;
  }

  // FIRST FARIABLES
  forn(i, farsCardinality) {
    Symbol far;
    far.drawing = "F_" + to_string(i);
    far.type = types["formula"];
    alphabet["F_" + to_string(i)] = far;
  }
} // DONE

void initiateFormulas() {
  forn(i, farsCardinality) {
    Node node;
    node.symbol = alphabet["F_" + to_string(i)];
    formulas.push_back(node);
  }
} // DONE

void runInterface() {
  cout << "Bienvenido, gilcito! Gracias por el audio! ¿Todo bien?" << endl;

  while (true) {
    cout << "Apretá 1 para crear una fórmula." << endl;
    cout << "Apretá 2 para ver todas las fórmulas armadas." << endl;
    cout << "Apretá 3 para ver todas las verdades." << endl;
    cout << "Apretá 4 para jugar." << endl;

    int x = 0;
    cin >> x;

    if (x >= 1 && x <= 4) {
      if (x == 1) {
        cout << "Apretá 1 para crear una fórmula atómica." << endl;
        cout << "Apretá 2 para negar una fórmula." << endl;
        cout << "Apretá 3 para unir dos fórmulas." << endl;
        cout << "Apretá 4 para decir que existe una variable que cumple una fórmula." << endl;

        cin >> x;

        if (x >= 1 && x <= 4) {
          if (x == 1) {
            cout << "Apretá 1 para una fórmula atómica de la forma \"x = y\"." << endl;
            cout << "Apretá 2 para una fórmula atómica de la forma \"x ∈ y\"." << endl;

            cin >> x;

            Node node;

            if (x >= 1 && x <= 2) {
              if (x == 1) {
                node.symbol = alphabet["equals"];
              } else if (x == 2) {
                node.symbol = alphabet["belongsTo"];
              }

              node.children.push_back(selectVariable());
              node.children.push_back(selectVariable());
              formulas.push_back(node);
            } else {
              cout << "Tu mamá tiene cara de rana." << endl;
            }
          } else if (x == 2) {
            Node node;
            node.symbol = alphabet["not"];
            node.children.push_back(selectFormula());
            formulas.push_back(node);
          } else if (x == 3) {
            Node node;
            node.symbol = alphabet["and"];
            node.children.push_back(selectFormula());
            node.children.push_back(selectFormula());
            formulas.push_back(node);
          } else if (x == 4) {
            Node node;
            node.symbol = alphabet["exists"];
            node.children.push_back(selectVariable());
            node.children.push_back(selectFormula());
            formulas.push_back(node);
          }
        } else {
          cout << "Tu mamá tiene cara de rana." << endl;
        }
      } else if (x == 2) {
        showFormulas();
      } else if (x == 3) {
        showWhatWeKnow();
      } else if (x == 4) {
				cout << "Apretá 1 para usar lo de A, A=>B, entonces B." << endl;
        cout << "Apretá 2 para enchufar enunciados en fariables." << endl;

        cin >> x;

        if (x >= 1 && x <= 2) {
					if (x == 1) {
						useInferenceRule();
					} else if (x == 2) {
						plugStatement();
					}
				}
			}
    } else {
      cout << "Tu mamá tiene cara de rana." << endl;
    }
  }
}

void defineLogicAxioms() {
  // Fariables
  Node f0;
  f0.symbol = alphabet["F_0"];
  Node f1;
  f1.symbol = alphabet["F_1"];
  Node f2;
  f2.symbol = alphabet["F_2"];

  // 1
  Node axiom1;
  axiom1.symbol = alphabet["implies"];
  axiom1.children.push_back(f0);
  Node tempForAxiom1;
  tempForAxiom1.symbol = alphabet["implies"];
  tempForAxiom1.children.push_back(f1);
  tempForAxiom1.children.push_back(f0);
  axiom1.children.push_back(tempForAxiom1);
  formulas.push_back(tempForAxiom1);
  formulas.push_back(axiom1);
  whatWeKnow.push_back(axiom1);

  // 2
  Node axiom2;
  axiom2.symbol = alphabet["implies"];
  Node temp1ForAxiom2;
  temp1ForAxiom2.symbol = alphabet["implies"];
  Node temp2ForAxiom2;
  temp2ForAxiom2.symbol = alphabet["implies"];
  Node temp3ForAxiom2;
  temp3ForAxiom2.symbol = alphabet["implies"];
  Node temp4ForAxiom2;
  temp4ForAxiom2.symbol = alphabet["implies"];
  Node temp5ForAxiom2;
  temp5ForAxiom2.symbol = alphabet["implies"];
  temp5ForAxiom2.children.push_back(f0);
  temp5ForAxiom2.children.push_back(f2);
  temp4ForAxiom2.children.push_back(f0);
  temp4ForAxiom2.children.push_back(f1);
  temp3ForAxiom2.children.push_back(f1);
  temp3ForAxiom2.children.push_back(f2);
  temp2ForAxiom2.children.push_back(temp4ForAxiom2);
  temp2ForAxiom2.children.push_back(temp5ForAxiom2);
  temp1ForAxiom2.children.push_back(f0);
  temp1ForAxiom2.children.push_back(temp3ForAxiom2);
  axiom2.children.push_back(temp1ForAxiom2);
  axiom2.children.push_back(temp2ForAxiom2);
  formulas.push_back(axiom2);
  formulas.push_back(temp1ForAxiom2);
  formulas.push_back(temp2ForAxiom2);
  formulas.push_back(temp3ForAxiom2);
  formulas.push_back(temp4ForAxiom2);
  formulas.push_back(temp5ForAxiom2);
  whatWeKnow.push_back(axiom2);

  // 3
  Node axiom3;
  axiom3.symbol = alphabet["implies"];
  Node temp1ForAxiom3;
  temp1ForAxiom3.symbol = alphabet["implies"];
  Node temp2ForAxiom3;
  temp2ForAxiom3.symbol = alphabet["not"];
  Node temp3ForAxiom3;
  temp3ForAxiom3.symbol = alphabet["not"];
  temp3ForAxiom3.children.push_back(f1);
  temp2ForAxiom3.children.push_back(f0);
  temp1ForAxiom3.children.push_back(temp2ForAxiom3);
  temp1ForAxiom3.children.push_back(temp3ForAxiom3);
  axiom3.children.push_back(temp1ForAxiom3);
  axiom3.children.push_back(tempForAxiom1);
  formulas.push_back(axiom3);
  formulas.push_back(temp1ForAxiom3);
  formulas.push_back(temp2ForAxiom3);
  formulas.push_back(temp3ForAxiom3);
  whatWeKnow.push_back(axiom3);
}

void defineMathAxioms() {
  // ...
}

int main() {
  initiateTypes();
  initiateAlphabet(),
  initiateFormulas();
  defineLogicAxioms();
  defineMathAxioms();

  runInterface();
  return 0;
}
