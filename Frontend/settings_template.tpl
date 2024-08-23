<!-- settings_template.tpl -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>User Settings</title>
</head>
<body>
    <div class="container">
        <h2>User Settings</h2>

        <p>Username: {{ user['username'] }}</p>
        <p>User ID: {{ user['id'] }}</p>


        <form action="/update-password" method="post">
            <label for="old_password">Old Password:</label>
            <input type="password" name="old_password" required><br>

            <label for="new_password">New Password:</label>
            <input type="password" name="new_password" required><br>

            <label for="confirm_password">Confirm New Password:</label>
            <input type="password" name="confirm_password" required><br>

            <input type="submit" value="Update Password">
        </form>

        <br>
        <a href="/home">Back to Home</a>
    </div>
</body>
</html>
