from flask import Flask, request, render_template

import model
from utils import testfun


app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "<h1>Hello Flask!</h1>"


# URL/<username>  example URL/Allen URL/Ted
@app.route("/<username>")
def greeting(username):
    output_html = f"""
    <h1>
        Hello {username}
    </h1>
    """
    return output_html


# [GET] URL/api/v2/department/dep_id/<dep_id: str>/emp_id/<emd_id: str>
@app.route("/api/v2/department/dep_id/<string:dep_id>/emp_id/<int:emd_id>")
def get_employee(dep_id: str, emd_id: int):
    query_sql = f"""
    select
        emp_name,
        emp_id,
        emp_seat
    from emp
    where dep_id = '{dep_id}'
    and emp_id = {emd_id}
    """
    print(type(dep_id))
    print(type(emd_id))
    # db_connect(query_sql)
    return {
        "emp_name": "Allen Shi",
        "emp_id": "123",
        "emp_seat": "B2",
    }


# [GET] URL/hello?username=Allen&age=22
@app.route("/hello")
def hello():
    username = request.args.get("username")  # returns None if user do not give the parameter
    age = request.args.get("age")

    if not username:
        return "What's your name?"
    if not age:
        return f"Hello {username}."

    return f"Hello {username}, you are {age} years old."


# [POST] URL/hello_post  form_data = {"username": "Allen"}
@app.route("/hello_post", methods=["GET", "POST"])
def hello_post():
    form_html = """
    <form method="post" action="/hello_post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username">
        <input type="submit" value="Submit">
    </form>
    """

    request_method = request.method
    username = request.form.get("username")

    if request_method == "POST":
        form_html += f"""
        <h1>Hello {username}</h1>
        """

    return form_html

# URL/tow_sum/<int:x>/<int:y>
@app.route("/two_sum/<int:x>/<int:y>")
def two_sum(x: int, y: int) -> str:
    return str(testfun(x, y))


@app.route('/show_staff')
def hello_google():
    staff_data = model.getStaff()
    column = ['ID', 'Name', 'DeptId', 'Age', 'Gender', 'Salary']
    return render_template('show_staff.html', staff_data=staff_data,
                                              column=column)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
