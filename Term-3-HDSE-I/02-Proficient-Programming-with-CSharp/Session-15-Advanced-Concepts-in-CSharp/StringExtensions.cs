// Session 15: Extension methods add new methods to an existing type
// Rules: a STATIC class, a STATIC method, and "this" before the first parameter.
public static class StringExtensions
{
    // Usage: "ali raza".ToTitle()  ->  "Ali Raza"
    public static string ToTitle(this string text)
    {
        string[] words = text.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        for (int i = 0; i < words.Length; i++)
        {
            // first letter upper case + the rest lower case
            words[i] = char.ToUpper(words[i][0]) + words[i][1..].ToLower();
        }
        return string.Join(" ", words);
    }

    // Usage: 75.IsPass()  ->  true
    public static bool IsPass(this int marks) => marks >= 50;
}
