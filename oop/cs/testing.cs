using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter an integer: ");
        int n = Convert.ToInt32(Console.ReadLine());

        int count = 0;
        do
        {
            count++;
            n /= 10;
        } while (n != 0);

        Console.WriteLine("Number of digits: " + count);
    }
}