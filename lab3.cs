using System;

class Program {
  static void Main(string[] args) {
    int[] input = {1, 4, 3, 2, 7, 6, 9, 8, 5, 0};
    int[] even = new int[input.Length];
    int evenIndex = 0;
    int[] odd = new int[input.Length];
    int oddIndex = 0;
    for (int i = 0; i < input.Length; i++) {
      if (input[i] % 2 == 0) {
        even[evenIndex++] = input[i];
      } else {
        odd[oddIndex++] = input[i];
      }
    }
    Array.Resize(ref even, evenIndex);
    Array.Resize(ref odd, oddIndex);
    Array.Sort(even);
    Array.Sort(odd);
    Console.WriteLine("Четные: " + string.Join(", ", even));
    Console.WriteLine("Нечетные: " + string.Join(", ", odd));
    Console.ReadKey();
  }
}
