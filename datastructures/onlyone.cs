using System;

class Program
{
    static void Main()
    {
        int sum = 0;
        while (true)
        {
            Console.Write("Enter an integer: ");
            int n = Convert.ToInt32(Console.ReadLine());

            if (n == -1)
            {
                sum += n;
                break;
            }

            if (n >= 10 && n <= 99)
            {
                continue;
            }

            sum += n;
        }

        Console.WriteLine("Sum of Integers: " + sum);
    }
}