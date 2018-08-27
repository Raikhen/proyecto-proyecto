#include "node.h"

string Node::toString() {
  string s = "";
  s += symbol.drawing + (children.size() > 0 ? "(" : "");

  forn(i, children.size()) {
    s += children[i].toString();
    s += i != children.size() - 1 ? ", " : "";
  }

  s += children.size() > 0 ? ")" : "";
  return s;
}

bool Node::belongsToVector(vector<Node> list) {
	forn(i, list.size()) {
    if (symbol.drawing == list[i].symbol.drawing) {
      return true;
    }
  }

	return false;
}

bool Node::isStatement(vector<Node> jailOfVars) {
	vector<Node> newJailOfVars;
	newJailOfVars = jailOfVars;

	if (n.symbol.drawing == alphabet["exists"].drawing) { // OUCH
		newJailOfVars.push_back(n.children[0]);
	} else if (n.symbol.type.name == types["variable"].name) { // OUCH * 2
		if (!nodeExistsInVector(n, jailOfVars)) return false;
	}

	forn(i, n.children.size()) {
		if (!isStatement(n.children[i], newJailOfVars)) {
			return false;
		}
	}

	return true;
}
