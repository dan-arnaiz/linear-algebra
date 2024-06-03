using System;

class Program
{
    static void Main()
    {
        Console.Write("Enter an integer: ");
        int n = Convert.ToInt32(Console.ReadLine());

        int sum = 0;
        while (n != 0)
        {
            int digit = n % 10;
            if (digit % 3 == 0)
            {
                n /= 10;
                continue;
            }
            sum += digit;
            n /= 10;
        }

        Console.WriteLine("Sum of all digits: " + sum);
    }
}