using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CommandSystem.Model;

public class Alerts
{
    //{
    //"alert_id": "b3f1c2e4-5a6d-4e8f-9a0b-1c2d3e4f5a6b",
    //"source": "pikud-haoref",
    //"title": "ירי רקטות וטילים",
    //"content": "ירי רקטות וטילים לעבר קריית שמונה. יש להיכנס למרחב המוגן תוך 15 שניות.",
    //"priority": "CRITICAL",
    //"classification": "UNCLASSIFIED",
    //"lat": 33.2051,
    //"lon": 35.5712,
    //"timestamp": "2026-09-29T11:03:23.108Z",
    //"status": "WAITING"
    //}

    public string alert_id { get; set; } = string.Empty;
    public string source { get; set; } = string.Empty;
    public string title { get; set; }  = string.Empty;
    public string content { get; set; }  = string.Empty;
    public string priority { get; set; }  = string.Empty;
    public string classification { get; set; }  = string.Empty;
    public double lat { get; set; } 
    public double lon { get; set; } 
    public DateTime timestamp { get; set; } 
    public string status { get; set; }  = string.Empty;
    public string region { get; set; } = string.Empty;


}
