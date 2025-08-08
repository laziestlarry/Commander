<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Dashboard</title>
  <link rel="stylesheet" href="/static/css/bootstrap.min.css" />
</head>
<body>
  <div class="container mt-5">
    <h1>Dashboard</h1>
    <form action="/launch_commander" method="post">
      <button type="submit" class="btn btn-primary">Launch Commander</button>
    </form>

    <div class="card mt-4">
      <div class="card-header">
        📊 Mission Execution Log
      </div>
      <div class="card-body">
        <pre id="mission-log">Launch the Commander to see live log output...</pre>
      </div>
    </div>
  </div>

  <script>
    document.querySelector('form[action="/launch_commander"]').addEventListener('submit', async function (e) {
      e.preventDefault();
      const response = await fetch("/launch_commander", { method: "POST" });
      const data = await response.json();
      document.getElementById("mission-log").textContent = data.log.join("\n");
    });
  </script>
</body>
</html>
