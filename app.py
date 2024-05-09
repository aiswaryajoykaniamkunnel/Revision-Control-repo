from flask import Flask, request, redirect, url_for
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

BOX_STYLE = '''
<style>
    .box {
        border: 1px solid #ccc;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        width: 1000px;
        margin: auto;
        margin-top: 50px;
        position: absolute;
    }

    .input-box {
        margin-top: 100px;
        padding: 20px;
        width: 80px;
        border: 1px solid #ccc;
        height: 20px;
    }

    .input-box label {
        display: block;
        margin-bottom: 5px;
    }

    .input-box input {
        width: 100%;
        padding: 8px;
        top: 100px;
        border: 1px solid #ccc;
        border-radius: 10px;
    }

    input[type="submit"] {
        width: 100%;
        padding: 10px;
        background-color: #007bff;
        color: #fff;
        border: none;
        border-radius: 3px;
        cursor: pointer;
    }

    .small-box {
        width: 80px;
        height: 50px;
        border: 1px solid #000;
        display: inline-block;
        margin: 10px;
        box-shadow: 0 0 10px rgba(100, 100, 100, 0.8);
        position: relative; /* Position relative for status text */
        text-align: center;
        line-height: 50px; /* Center align the text vertically */
    }

    .occupied {
        background-color: cyan; /* pink for occupied rooms */
    }

    .vacant {
        background-color: gray;
    }

    .emergency {
        background-color: red;
    }
</style>'''


# Initialize Flask app
app = Flask(__name__)

# Connect to MongoDB Atlas
client = MongoClient("mongodb+srv://aiswaryajoypp:u1358@cluster0.kddhga6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", server_api=ServerApi('1'))
db = client["LoginData"]
users_collection = db["logindataa"]  # Replace with your collection name

# Route for login page
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if authenticate_user(username, password):
            return redirect(url_for('admin'))  # Redirect to admin page
        else:
            return redirect(url_for('register'))  # Redirect to register page
    else:
        return """
        <div class="box">
            <h2><center>Login</h2>
            <form method="post"><center>
                <div class="input-box">
                    <label for="username">Username:</label>
                    <input type="text" id="username" name="username">
                </div><br>
                <div class="input-box">
                    <label for="password"> Password : </label>
                    <input type="password" id="password" name="password">
                </div><br>
                <input type="submit" value="Submit">
            </form>
        </div>
        """.format(BOX_STYLE)

# Route for Register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not users_collection.find_one({"username": username}):
            users_collection.insert_one({"username": username, "password": password})
            return "Registration successful"
    return """
    <div class="box">
        <h2><center>Register</h2>
        <form method="post"><center>
            <div class="input-box">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username">
            </div>
            <div class="input-box">
                <label for="password">Password :</label>
                <input type="password" id="password" name="password">
            </div>
            <input type="submit" value="Register">
        </form>
    </div>
    """.format(BOX_STYLE)

# Route for admin page
@app.route("/admin", methods=["GET", "POST"])
def admin():
    # Generate HTML content for 100 boxes
    content = '<div class="box">'
    for room_number in range(101, 200):
        # Determine the class based on room status (you can replace this logic with your own)
        inum = room_number-100
        if room_number % inum == 0:
            room_class = "emergency" 
        elif room_number % 6 ==0:
            room_class = "occupied"
        else: 
            room_class = "vacant"
        content += '''
            <div class="small-box {}">F{}</div>
        '''.format(room_class, room_number)
    content += '</div>'  # End of box
    
    return BOX_STYLE + content


# Function to authenticate user
def authenticate_user(username, password):
    user = users_collection.find_one({"username": username, "password": password})
    return user is not None

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)