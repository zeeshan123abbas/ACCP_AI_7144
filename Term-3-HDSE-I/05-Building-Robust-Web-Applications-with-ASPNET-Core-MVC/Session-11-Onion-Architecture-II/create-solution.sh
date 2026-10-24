# Run these once to create the 4-project Onion solution from scratch
dotnet new sln -n OnionDemo

dotnet new classlib -n OnionDemo.Domain
dotnet new classlib -n OnionDemo.Service
dotnet new classlib -n OnionDemo.Infrastructure
dotnet new webapi   -n OnionDemo.WebApi --use-controllers

dotnet sln add OnionDemo.Domain OnionDemo.Service OnionDemo.Infrastructure OnionDemo.WebApi

# Dependencies point INWARD
dotnet add OnionDemo.Service        reference OnionDemo.Domain
dotnet add OnionDemo.Infrastructure reference OnionDemo.Domain
dotnet add OnionDemo.WebApi         reference OnionDemo.Service OnionDemo.Infrastructure

dotnet add OnionDemo.Infrastructure package Microsoft.EntityFrameworkCore.Sqlite --version 8.0.11

dotnet run --project OnionDemo.WebApi
