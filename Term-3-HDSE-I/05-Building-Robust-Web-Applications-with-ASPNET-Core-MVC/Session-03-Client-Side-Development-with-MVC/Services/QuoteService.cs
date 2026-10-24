namespace ClientSide.Services;

// The interface says WHAT the service can do
public interface IQuoteService
{
    string GetQuote();
}

// The class says HOW it does it
public class QuoteService : IQuoteService
{
    private readonly string[] _quotes =
    {
        "Practice makes progress.",
        "Small steps every day.",
        "Read the error message first."
    };

    public string GetQuote()
    {
        int index = Random.Shared.Next(_quotes.Length);
        return _quotes[index];
    }
}
