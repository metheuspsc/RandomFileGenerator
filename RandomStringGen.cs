using System;

namespace RandomString
{
    class RandomStringGen
    {
        static void Main() {
            for (int i = 0; i <= 100; i++) 
            {
                Console.WriteLine(RandomStringGen()); 
            }
        }
        public static string RandomStringGen()
        {
            var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
            var stringChars = new char[60];
            var random = new Random();

            for (int i = 0; i < stringChars.Length; i++)
            {
                stringChars[i] = chars[random.Next(chars.Length)];
            }

            var finalString = new String(stringChars);
            return finalString;
            
        }
    }
}
