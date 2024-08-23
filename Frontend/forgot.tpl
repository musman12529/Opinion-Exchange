<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" type="text/css" href="styles.css">
    <title>Reset Password</title>
</head>
<body>
<div class="login-modal" id="resetPasswordModal">
    <div class="login-content">
        <h1>Reset Password</h1>
        <form action="/forgot" method="post" class="reset-password-form">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br>
            <label for="newPassword">New Password:</label>
            <input type="password" id="newPassword" name="newPassword" required><br>
            <button type="submit">Reset Password</button>
        </form>
        <p>Already have an account? <a href="/start">Login</a></p>
    </div>
</div>
</body>
</html>