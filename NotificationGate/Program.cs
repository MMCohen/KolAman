using NotificationGate.AlertsWatcher;
using System;
using System.IO;
using Confluent.Kafka;

namespace NotificationGate;

class NotificationGate
{
    static void Main()
    {

        var config = new ProducerConfig
        {
            BootstrapServers = "localhost:9092"
        };

        var producer = new ProducerBuilder<Null, string>(config).Build();


        var alertWatcher = new AlertWatcher(producer);

        producer.Flush();
        producer.Dispose();
    }
}


