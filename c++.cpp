#include <iostream>
#include <cmath>

using namespace std;

int main(){

    int x,y;
    char op;

    cout << "What is your first number? ";
    cin >> x;

    cout << "What is your operator? ";
    cin >> op;

    cout << "What is your second number? ";
    cin >> y;

    if(op == '*')
    cout << x * y;

    else if(op == '/')
    cout << x/y;
    
    else if(op == '+')
    cout << x+y;

    else if(op == '-')
    cout << x-y;

    else 
    cout << "Invalid operator";

    return 0;

    


}