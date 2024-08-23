<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="styles.css">
    <title>Login</title>
</head>
<body>
<div class="login-modal" id="loginModal">
<div class="login-content">
    <h1>Register</h1>
    <form action="/register" method="post" class="login-form">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>

        <label for="confirm_password">Confirm Password:</label>
        <input type="password" id="confirm_password" name="confirm_password" required><br>
        <button type="submit">Register Account</button>
    </form>
    <p>Already have an account? <a href="/start">Login</a></p>
    </div>
</div>
</body>
</html>