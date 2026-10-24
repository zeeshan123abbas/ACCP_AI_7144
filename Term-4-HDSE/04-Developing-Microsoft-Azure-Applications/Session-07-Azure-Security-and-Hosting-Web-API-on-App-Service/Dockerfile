# Session 07 - Example 4: container image for the Students API
# Copy this file into the Session-06 folder (next to StudentsApi.csproj).

# Stage 1: build with the full SDK
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build
WORKDIR /src
COPY . .
RUN dotnet publish StudentsApi.csproj -c Release -o /app

# Stage 2: run with the small runtime image
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build /app .
# .NET 8 images listen on port 8080 by default
EXPOSE 8080
ENTRYPOINT ["dotnet", "StudentsApi.dll"]
