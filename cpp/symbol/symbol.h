#ifndef SYMBOL_H
#define SYMBOL_H

#include "../type/type.h"

class Symbol {
  public:
    string drawing;
    Type type;
    vector<Type> childrenFormat;
};

#endif
