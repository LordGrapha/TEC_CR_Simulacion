using System.Threading.Tasks;
using System.IO;
using System;
class main
{
    static void Main(string[] args)
        {
            Random randomGenerator = new Random();
            string randoms = "";
            for (int i = 0; i < 10000; i++)
            {
                randoms = randoms + (randomGenerator.Next(1, (10*17))/(10.0*17.0)) + " ";
            }
            string fullPath = "./C#Random.txt";
            // Write file using StreamWriter  
            using (StreamWriter writer = new StreamWriter(fullPath))  
            {  
            writer.WriteLine(randoms); 
            }  
        }
}