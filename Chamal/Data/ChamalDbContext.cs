using Microsoft.EntityFrameworkCore;

using Chamal.Model;
using System.Reflection.Emit;

namespace Chamal.Data;

public class ChamalDbContext : DbContext
{
    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseMySql("server=localhost;port=3306;user=root;password=root;database=CommandSystem",
            ServerVersion.AutoDetect("server=localhost;port=3306;user=root;password=root;database=CommandSystem"));
    }

    public DbSet<Alert> Alerts { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Alert>()
            .HasKey(a => a.alert_id);
    }
}
