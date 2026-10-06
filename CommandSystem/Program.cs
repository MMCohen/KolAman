using CommandSystem.Data;
using CommandSystem.Model;
using RabbitMQ.Client;
using RabbitMQ.Client.Events;
using System.Text;
using System.Text.Json;
using System.Text.Json.Nodes;


// create mysql database if not exist
var context = new CommandDbContext();
context.Database.EnsureCreated();

// conection to rabbit
var factory = new ConnectionFactory { HostName = "localhost" };
using var connection = await factory.CreateConnectionAsync();
using var channel = await connection.CreateChannelAsync();



await channel.QueueDeclareAsync(queue: "CENTER", durable: true, exclusive: false, autoDelete: false,
    arguments: new Dictionary<string, object?> { { "x-queue-type", "quorum" } });

Console.WriteLine(" [*] Waiting for messages.");

var consumer = new AsyncEventingBasicConsumer(channel);
consumer.ReceivedAsync += (model, ea) =>
{
    var body = ea.Body.ToArray();
    var message = Encoding.UTF8.GetString(body);

    try
    {
        Alerts? alert = JsonSerializer.Deserialize<Alerts>(message);

        if (message != null && alert != null)
        {
            alert.region = ea.RoutingKey;
            Console.WriteLine(message);
            var context = new CommandDbContext();
            context.Alerts.Add(alert);
            context.SaveChanges();

        }
    }
    catch
    {
        throw;
    }


    Console.WriteLine($" [x] Received {message}");
    return Task.CompletedTask;
};

await channel.BasicConsumeAsync("CENTER", autoAck: true, consumer: consumer);
await channel.BasicConsumeAsync("NORTH", autoAck: true, consumer: consumer);
await channel.BasicConsumeAsync("SOUTH", autoAck: true, consumer: consumer);
await channel.BasicConsumeAsync("OVERSEAS", autoAck: true, consumer: consumer);

Console.WriteLine(" Press [enter] to exit.");
Console.ReadLine();






//Alerts alert = new Alerts
//{
//    alert_id = "sdfs",
//    classification = "df",
//    content = "sdfs",
//    lat = 12.1,
//    lon = 22.5,
//    priority = "sfd",
//    source = "dfd",
//    status = "sdfds",
//    timestamp = DateTime.Now,
//    title = "sdfsd"
//};

//context.Alerts.Add(alert);
//context.SaveChanges();

