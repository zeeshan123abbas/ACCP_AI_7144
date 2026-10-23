// Run as an admin user. On a local server, enable authorization afterwards to enforce these users.
const campus = db.getSiblingDB("campus");

campus.createRole({
  role: "studentViewer",
  privileges: [{ resource: { db: "campus", collection: "students" }, actions: ["find"] }],
  roles: []
});

campus.createUser({ user: "report_user", pwd: passwordPrompt(), roles: ["studentViewer"] });
campus.createUser({ user: "app_user", pwd: passwordPrompt(), roles: [{ role: "readWrite", db: "campus" }] });

campus.grantRolesToUser("report_user", [{ role: "read", db: "campus" }]);
printjson(campus.getUsers());
printjson(campus.getRole("studentViewer", { showPrivileges: true }));

campus.revokeRolesFromUser("report_user", [{ role: "read", db: "campus" }]);
// campus.changeUserPassword("app_user", passwordPrompt());
// campus.dropUser("report_user"); campus.dropRole("studentViewer");
