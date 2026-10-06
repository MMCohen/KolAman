using Chamal.Model;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Chamal.Handler
{
    public class AlertHandler
    {
        public async static Task<HandlerResult> HandleAsync(Alert alert)
        {
            if (alert.classification == "TOP_SECRET")
            {
                return await TopImportentAsync(alert);
            }

            if (alert.classification == "SECRET" 
                || alert.classification == "RESTRICTED")
            {
                return await ImportentAsync(alert);
            }

            else
            {
                return await NotImportentAsync(alert);
            }
        }
        public async static Task<HandlerResult> TopImportentAsync(Alert alert)
        {
            alert.status = "INPROGRESS";

            int delay = alert.content.Length * 10;
            Console.WriteLine($"start timestamp: {DateTime.UtcNow}");
            await Task.Delay(delay);
            Console.WriteLine($"end timestamp: {DateTime.UtcNow}");

            alert.status = "DONE";

            return HandlerResult.Importent("very importent");
        }


        public async static Task<HandlerResult> ImportentAsync(Alert alert)
        {

            alert.status = "INPROGRESS";

            int delay = alert.content.Length * 10;
            Console.WriteLine($"start timestamp: {DateTime.UtcNow}");
            await Task.Delay(delay);
            Console.WriteLine($"end timestamp: {DateTime.UtcNow}");

            alert.status = "DONE";

            return HandlerResult.Importent("importent");
        }

        public async static Task<HandlerResult> NotImportentAsync(Alert alert)
        {
            alert.status = "CANCEL";

            Console.WriteLine($"start timestamp: {DateTime.UtcNow}");
            Console.WriteLine($"end timestamp: {DateTime.UtcNow}");
            return HandlerResult.NotImportent("not importent");
        }
    }
}
