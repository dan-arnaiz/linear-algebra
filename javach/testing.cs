using System;

class Program
{
    static void Main()
    {
        int sum = 0;
        int input;
        Console.Write("Enter an integer: ");
        do
        {
            input = Convert.ToInt32(Console.ReadLine());
            sum += input;
        } while (input != 0);

        Console.WriteLine("Total Sum: " + sum);
    }
}