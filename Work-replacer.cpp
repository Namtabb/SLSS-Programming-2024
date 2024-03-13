#include <iostream>

using namespace std;


int main(){

string user;


getline(cin, user);

cout << user.replace("noodles", "ok").replace("100", "no");


    return 0;
}