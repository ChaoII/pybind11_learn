//
// Created by aichao on 2024/7/12.
//

#pragma once

#include "exports.h"

class WHEELBIND_EXPORT MyLibrary {

public:
    explicit MyLibrary() {};

    int add(int x, int y) {
        return x + y;
    }

    int sub(int x, int y) {
        return x - y;
    }
};


