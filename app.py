# from flask import Flask, render_template, request
# import subprocess

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/execute', methods=['POST'])
# def execute():
#     code = request.form['code']
#     result = execute_python(code)
#     return result

# def execute_python(code):
#     try:
#         # Execute Python code using subprocess
#         process = subprocess.Popen(['python', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#         output, error = process.communicate(timeout=5)
#         if error:
#             return error
#         return output
#     except subprocess.TimeoutExpired:
#         return "Timeout: Execution took too long."
#     except Exception as e:
#         return str(e)

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute():
    code = request.form['code']
    result = execute_python(code)
    return jsonify({'output': result})

def execute_python(code):
    try:
        # Execute Python code using subprocess
        process = subprocess.Popen(
            ['python', '-c', code],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        output, error = process.communicate(timeout=5)
        if process.returncode != 0:
            return error.strip() if error else "Unknown error occurred."
        return output.strip() if output else "No output."
    except subprocess.TimeoutExpired:
        return "Timeout: Execution took too long."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)


# import streamlit as st
# import subprocess
# import shlex

# def execute_python(code):
#     try:
#         # Execute Python code using subprocess
#         process = subprocess.Popen(
#             ['python', '-c', code],
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE,
#             text=True,
#             encoding='utf-8',
#             errors='replace'
#         )
#         output, error = process.communicate(timeout=5)
#         if process.returncode != 0:
#             return error.strip() if error else "Unknown error occurred."
#         return output.strip() if output else "No output."
#     except subprocess.TimeoutExpired:
#         return "Timeout: Execution took too long."
#     except Exception as e:
#         return f"Error: {str(e)}"

# def main():
#     st.title('Online Python Compiler')
#     code = st.text_area("Enter your Python code here", height=200)
#     if st.button("Execute"):
#         result = execute_python(code)
#         st.subheader("Output:")
#         st.code(result, language='python')

# if __name__ == "__main__":
#     main()

