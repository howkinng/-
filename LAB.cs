Console.Write("Введите строку: ");
string str = Console.ReadLine();

Console.Write("Введите символ для подсчета процента: ");
char ch = Console.ReadKey().KeyChar;

int count = 0;
foreach (char c in str)
{
    if (c == ch)
    {
        count++;
    }
}

double percent = (double)count / str.Length * 100;

Console.WriteLine($"\nПроцент вхождения символа '{ch}' в строку: {percent}%");
