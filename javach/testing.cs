using System;

public class Program
{
    public static void Main(string[] args)
    {
        while(true)
        {
            Console.Write("Enter letter: ");
            char letter = Console.ReadLine()[0];

            if (letter == 'C' || letter == 'O' || letter == 'D' || letter == 'E')
            {
                break;
            }
        }
    }
}