//
// Created by aichao on 2024/7/12.
//
#include <iostream>
#include "MyLibrary.h"

using namespace std;

int MyLibrary::add(int x, int y) {
    return x + y;
}

int MyLibrary::sub(int x, int y) {
    return x - y;
}

void MyLibrary::say_hi() {
    std::cout << "hi zhu" << std::endl;
}

int MyLibrary::get_y() const {
    return y_;
}

std::string MyLibrary::get_name() const {
    return name_;
}

void MyLibrary::set_name(const std::string &name) {
    name_ = name;
}
