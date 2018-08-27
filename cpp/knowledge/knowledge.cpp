#include "knowledge.h"

void Knowledge::initiateTypes() {
  Type FORMULA;
  FORMULA.name = "formula";
  types["formula"] = FORMULA;

  Type VARIABLE;
  VARIABLE.name = "variable";
  types["variable"] = VARIABLE;
}

void Knowledge::initiateAlphabet() {
  Symbol AND;
  AND.drawing = "∧";
  AND.type = types["formula"];
  AND.childrenFormat.push_back(types["formula"]);
  AND.childrenFormat.push_back(types["formula"]);
  alphabet["and"] = AND;

  Symbol NOT;
  NOT.drawing = "¬";
  NOT.type = types["formula"];
  NOT.childrenFormat.push_back(types["formula"]);
  alphabet["not"] = NOT;

  Symbol EXISTS;
  EXISTS.drawing = "∃";
  EXISTS.type = types["formula"];
  EXISTS.childrenFormat.push_back(types["variable"]);
  EXISTS.childrenFormat.push_back(types["formula"]);
  alphabet["exists"] = EXISTS;

  Symbol EQUALS;
  EQUALS.drawing = "=";
  EQUALS.type = types["formula"];
  EQUALS.childrenFormat.push_back(types["variable"]);
  EQUALS.childrenFormat.push_back(types["variable"]);
  alphabet["equals"] = EQUALS;

  Symbol BELONGS_TO;
  BELONGS_TO.drawing = "∈";
  BELONGS_TO.type = types["formula"];
  BELONGS_TO.childrenFormat.push_back(types["variable"]);
  BELONGS_TO.childrenFormat.push_back(types["variable"]);
  alphabet["belongsTo"] = BELONGS_TO;

  Symbol IMPLIES;
  IMPLIES.drawing = "⇒";
  IMPLIES.type = types["formula"];
  IMPLIES.childrenFormat.push_back(types["formula"]);
  IMPLIES.childrenFormat.push_back(types["formula"]);
  alphabet["implies"] = IMPLIES;

  forn(i, 3) { // TODO: Unhardcode this!!!
    Symbol var;
    var.drawing = "v_" + to_string(i);
    var.type = types["variable"];
    alphabet["v_" + to_string(i)] = var;
  }

  // FIRST FARIABLES
  forn(i, 4) { // TODO: Unhardcode this!!!
    Symbol far;
    far.drawing = "F_" + to_string(i);
    far.type = types["formula"];
    alphabet["F_" + to_string(i)] = far;
  }
}

void Knowledge::initiateFormulas() {
  forn(i, farsCardinality) {
    Node node;
    node.symbol = alphabet["F_" + to_string(i)];
    formulas.push_back(node);
  }
}

void Knowledge::defineLogicAxioms() {
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

void Knowledge::defineMathAxioms() {
  // ...
}

Knowledge::Knowledge() {
  farsCardinality = 4;

  initiateTypes();
  initiateAlphabet();
  initiateFormulas();
  defineLogicAxioms();
}
