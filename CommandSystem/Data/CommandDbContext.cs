using CommandSystem.Model;
using Microsoft.EntityFrameworkCore;


namespace CommandSystem.Data;

public class CommandDbContext : DbContext
{
    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        optionsBuilder.UseMySql("server=localhost;port=3306;user=root;password=root;database=CommandSystem",
            ServerVersion.AutoDetect("server=localhost;port=3306;user=root;password=root;database=CommandSystem"));
    }

    public DbSet<Alerts> Alerts { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Alerts>()
            .HasKey(a => a.alert_id);
    }
}
