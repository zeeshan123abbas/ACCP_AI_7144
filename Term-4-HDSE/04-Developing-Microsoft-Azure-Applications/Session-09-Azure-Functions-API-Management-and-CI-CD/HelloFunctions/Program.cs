// Session 09 - Program.cs: start the Functions host (isolated worker model)
using Microsoft.Extensions.Hosting;

var host = new HostBuilder()
    .ConfigureFunctionsWorkerDefaults()
    .Build();

host.Run();
