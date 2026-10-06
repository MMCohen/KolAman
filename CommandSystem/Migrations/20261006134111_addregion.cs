using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace CommandSystem.Migrations
{
    /// <inheritdoc />
    public partial class addregion : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.AddColumn<string>(
                name: "region",
                table: "Alerts",
                type: "longtext",
                nullable: false)
                .Annotation("MySql:CharSet", "utf8mb4");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropColumn(
                name: "region",
                table: "Alerts");
        }
    }
}
