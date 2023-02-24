using System;

class Program {
  static void Main(string[] args) {
    Console.WriteLine("Введите строку:");
    string input = Console.ReadLine();
    int count = 0;
    string[] words = input.Split(' ');
    foreach (string word in words) {
      if (word != "") {
        count++;
      }
    }
    Console.WriteLine("Количество слов: " + count);
    Console.ReadKey();
  }
}
