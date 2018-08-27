#ifndef KNOWLEDGE_H
#define KNOWLEDGE_H

#include "../type/type.cpp"
#include "../symbol/symbol.cpp"
#include "../node/node.cpp"

class Knowledge {
  private:
    int farsCardinality;
    void initiateTypes();
    void initiateAlphabet();
    void initiateFormulas();
    void defineLogicAxioms();
    void defineMathAxioms();

  public:
    map<string, Type> types;
    map<string, Symbol> alphabet;
    vector<Node> formulas;
    vector<Node> whatWeKnow;
    Knowledge();
    void useInferenceRule(); // Is mixed with interface
    void plugStatement();
    bool formulaIsInFormulas(Node f);
    void addAllSubformulasToFormulas(Node x); // Change
};

#endif
