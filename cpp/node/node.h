#ifndef NODE_H
#define NODE_H

#include "../symbol/symbol.h"

class Node {
  public:
    Symbol symbol;
    vector<Node> children;
    string toString();
    bool belongsToVector(vector<Node> list);
    bool isStatement();
    bool isStatement(vector<Node> jailOfVars);
    int getFarIndex();
    vector<bool> getAllFariables();
    vector<Node> subformulasWithReps();
    Node replaceAllSubnodesWithNode(Node formula, Node far, Node statement);
};

#endif
