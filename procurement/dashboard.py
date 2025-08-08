<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Dashboard</title>
    <!-- existing head content -->
</head>
<body>
    <div class="container">
        <!-- existing dashboard layout -->

        <form action="/launch_commander" method="post" id="launch-form">
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

        <script>
          document.getElementById('launch-form').addEventListener('submit', async function (e) {
            e.preventDefault();
            const response = await fetch("/launch_commander", { method: "POST" });
            const data = await response.json();
            document.getElementById("mission-log").textContent = data.log.join("\n");
          });
        </script>

    </div>
</body>
</html>
