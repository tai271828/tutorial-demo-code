/*
  Demo how to use __FUNCTION__

  This macro helps you to show the called function name
  Usage:
    prompt: g++ function-name.cpp
    prompt: ./a.out
*/

#include <iostream>
using namespace std;

void callFunc(void) {
    cout << __FUNCTION__ << endl;
}

main(void) {
    callFunc();
}
