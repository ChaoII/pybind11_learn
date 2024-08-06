//
// Created by aichao on 2024/7/12.
//

#pragma once
#include <iostream>
#include "exports.h"

class WHEELBIND_EXPORT Base {
public:
    explicit Base(int x) : x_(x) {
    }

    virtual ~Base() {
    }

    virtual void say_hi() {
    }

    virtual int get_x() const {
        return x_;
    }

private:
    int x_;
};


class WHEELBIND_EXPORT MyLibrary : public Base {
public:
    explicit MyLibrary(int x, int y) : Base(x), y_(y) {
    }

    void say_hi() override;

    int add(int x, int y);

    int sub(int x, int y);

    int get_y() const;

    std::string get_name() const;

    void set_name(const std::string &name);

private:
    int y_;
    std::string name_;
};
