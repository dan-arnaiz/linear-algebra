using System;

class MainClass {

    static public void Main()
    {
        Console.Write("Enter n: ");
        int n = Convert.ToInt32(Console.ReadLine());

        for (int i = 1; i <= n; i += 2)
        {
            Console.Write(i);
        }
    }
}