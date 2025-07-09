from flask import Flask, render_template_string

app = Flask(__name__)

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Flipkart Clone</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      background: #f1f3f6;
    }
    header {
      background-color: #2874f0;
      padding: 10px;
      color: white;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    header .logo {
      font-size: 24px;
      font-weight: bold;
    }
    header .login-btn {
      background: white;
      color: #2874f0;
      border: none;
      padding: 8px 12px;
      border-radius: 4px;
      cursor: pointer;
    }
    .sidebar {
      background: white;
      width: 250px;
      position: fixed;
      top: 0;
      left: 0;
      height: 100%;
      border-right: 1px solid #ccc;
      padding-top: 60px;
      display: none;
      overflow-y: auto;
    }
    .sidebar ul {
      list-style: none;
      padding: 0;
    }
    .sidebar ul li {
      padding: 12px 16px;
      border-bottom: 1px solid #eee;
      cursor: pointer;
    }
    .main {
      margin-left: 0;
      padding: 20px;
    }
    .categories {
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
    }
    .category {
      background: white;
      padding: 10px;
      text-align: center;
      border-radius: 6px;
      width: 80px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    #loginPopup {
      display: none;
      position: fixed;
      top: 20%;
      left: 50%;
      transform: translateX(-50%);
      background: white;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 5px 10px rgba(0,0,0,0.2);
      z-index: 10;
    }
    #overlay {
      display: none;
      position: fixed;
      top: 0; left: 0;
      width: 100%; height: 100%;
      background: rgba(0,0,0,0.4);
      z-index: 5;
    }
  </style>
</head>
<body>

<header>
  <div class="logo">Flipkart</div>
  <button class="login-btn" onclick="showLogin()">Login</button>
</header>

<div class="sidebar" id="sidebar">
  <ul>
    <li>Login & Signup</li>
    <li>SuperCoin Zone</li>
    <li>Flipkart Plus Zone</li>
    <li>All Categories</li>
    <li>More on Flipkart</li>
    <li>Choose Language</li>
    <li>Offer Zone</li>
    <li>Sell on Flipkart</li>
    <li>My Orders</li>
    <li>Coupons</li>
    <li>My Cart</li>
    <li>My Wishlist</li>
    <li>My Account</li>
    <li>My Notifications</li>
    <li>Notification Preferences</li>
    <li>Help Centre</li>
    <li>Legal</li>
  </ul>
</div>

<div class="main">
  <h2>Explore Categories</h2>
  <div class="categories">
    <div class="category">Mobiles</div>
    <div class="category">Grocery</div>
    <div class="category">Fashion</div>
    <div class="category">Electronics</div>
    <div class="category">Home</div>
    <div class="category">Appliances</div>
    <div class="category">Travel</div>
    <div class="category">Beauty</div>
  </div>
</div>

<!-- Login Popup -->
<div id="overlay" onclick="hideLogin()"></div>
<div id="loginPopup">
  <h3>Log in for the best experience</h3>
  <input type="text" placeholder="Enter phone number" style="padding: 8px; width: 100%; margin-bottom: 10px;">
  <button onclick="hideLogin()" style="background: #2874f0; color: white; border: none; padding: 10px; width: 100%; border-radius: 4px;">Continue</button>
</div>

<script>
  function showLogin() {
    document.getElementById("loginPopup").style.display = "block";
    document.getElementById("overlay").style.display = "block";
  }

  function hideLogin() {
    document.getElementById("loginPopup").style.display = "none";
    document.getElementById("overlay").style.display = "none";
  }
</script>

</body>
</html>
"""

@app.route("/")
def homepage():
    return render_template_string(html_code)

if __name__ == "__main__":
    app.run(debug=True)
