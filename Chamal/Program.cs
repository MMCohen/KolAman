
using Chamal.Data;
using Chamal.Handler;
using Chamal.Model;

var alertHandler = new AlertHandler();

while (true)
{
    var context = new ChamalDbContext(); 


    Alert? alert = context.Alerts
        .FirstOrDefault(a => a.status == "WAITING");

    if (alert == null)
    {
        Console.WriteLine("waiting to get alerts..");
        await Task.Delay(2);
        continue;
    }

    Console.WriteLine("proccesing alert..");
    await Task.Delay(1);

    HandlerResult result = await AlertHandler.HandleAsync(alert);

    Console.WriteLine(result._msg);
    context.SaveChanges();
    context.Dispose();

}

//var context = new ChamalDbContext();

////var x = context.Alerts.Find("00488bb1-dbc2-431e-9521-b38f8599031c");

//List<Alert> x = context.Alerts.ToList();
//foreach (Alert y in x)
//{
//    y.status = "WAITING";
//}
////x.status = "WAITING";

//context.SaveChanges(); .