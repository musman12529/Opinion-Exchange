<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="styles.css">
    <title>Login</title>
</head>
<body>
<div class="login-modal" id="loginModal">
<div class="login-content">
    <h1>Login</h1>
    <form action="/login" method="post" class="login-form">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username" required><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password" required><br>
        <button type="submit">Login</button>
    </form>
    <p>Don't have an account? <a href="/register">Register here</a></p>
    <p>Forgot Password? <a href="/forgot">Reset Password</a></p>
    </div>
</div>
</body>
</html>