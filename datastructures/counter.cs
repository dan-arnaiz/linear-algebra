using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter first integer: ");
        int x = Convert.ToInt32(Console.ReadLine());

        Console.Write("Enter second integer: ");
        int y = Convert.ToInt32(Console.ReadLine());

        Console.Write("Enter third integer: ");
        int z = Convert.ToInt32(Console.ReadLine());

        for (int i = x; i <= y; i++)
        {
            if (i % z == 0)
            {
                continue;
            }
            Console.WriteLine(i);
        }
    }
}