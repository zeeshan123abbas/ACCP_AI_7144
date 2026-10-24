namespace Modern.Models;

// A record: short immutable data type, perfect for JSON
public record Student(int Id, string FullName, DateOnly JoinDate);

// Used with [AsParameters] to group query-string values
public record SearchQuery(string? Name, int Page = 1, int PageSize = 10);
