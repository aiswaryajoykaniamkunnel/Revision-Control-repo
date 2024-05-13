from flask import Flask, render_template

app = Flask(__name__)

BOX_STYLE='''
<style>
    .box {
        border: 1px solid #ccc;
        padding: 20px;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        width: 1000px;
        margin: 10px;
        margin-top: 50px;
        position`: absolute;
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

    .small-button{
        width: 100px;
        height: 80px;
        border: 1px solid #000;
        display: inline-block;
        margin: 10px;
        box-shadow: 0 0 10px rgba(100, 100, 100, 0.8);
        position: relative; /* Position relative for status text */
        text-align: center;
        line-height: 50px; /* Center align the text vertically */
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

</style>
'''

# Define routes for different pages
@app.route("/", methods=["POST"])
def login():
    return render_template("login.html")

@app.route("/status")
def status():
    return render_template("status.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
