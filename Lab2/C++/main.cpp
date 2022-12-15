// C++ program to demonstrate
// the use of rand()
#include <cstdlib>
#include <iostream>
#include <string.h>

using namespace std;

int main()
{
    //to_string(d); es para convertir de double a string
    const int random_limit = 10000;
    double listaRandoms[random_limit];
    ofstream cRandom;
    cRandomFile.open("cRandom.txt");
	for (int i = 0; i < random_limit; i++)
        int random = rand() % random_limit;
        cRandomFile << to_string(random / random_limit);
    cRandomFile.close();
	return 0;
}
