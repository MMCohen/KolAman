
namespace Chamal.Handler
{
    public class HandlerResult
    {
        public string _msg { get; private set; } = string.Empty;
        public bool isAlertImportent { get; private set; }
        public bool isEmergencyAlertDetected { get; private set; } = false;

        public static HandlerResult NotImportent(string msg)
        {
            return new HandlerResult
            {
                _msg = msg,
                isAlertImportent = false
            };

        }

        public static HandlerResult Importent(string msg)
        {
            return new HandlerResult
            {
                _msg = msg,
                isAlertImportent = true
            };
        }

        public static HandlerResult EmergencyAlert(string msg)
        {
            return new HandlerResult
            {
                _msg = msg,
                isAlertImportent = true,
                isEmergencyAlertDetected = true
            };
        }

    }
}
