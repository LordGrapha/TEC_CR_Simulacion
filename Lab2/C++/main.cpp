// C++ program to demonstrate
// the use of rand()
#include <iostream>
#include <fstream>
#include <string.h>

int main()
{
    //to_string(d); es para convertir de double a string
    int random_limit = 10*15;
    std::fstream cRandomFile;
    std::string allNumbers = "";
    cRandomFile.open("cRandom.txt", std::ios::out);
	for (int i = 0; i < random_limit; i++){
        float random = rand() % random_limit;
        random = random/10.0*15.0;
        cRandomFile << std::to_string(random) << " ";
    }
    cRandomFile.close();
	return 0;
}
