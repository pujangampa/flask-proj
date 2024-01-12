# app.py

from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_cipher(text, key, decrypt=False):
    result = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.isupper():
                result += chr((ord(char) - shift - 65) % 26 + 65) if decrypt else chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) - shift - 97) % 26 + 97) if decrypt else chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result_message = None  # Initialize result_message

    if request.method == 'POST':
        file_path = request.form['file_path']
        key = int(request.form['key'])
        operation = request.form['operation']

        try:
            with open(file_path, 'r') as file:
                content = file.read()
                if operation == 'encrypt':
                    result = caesar_cipher(content, key)
                    result_message = "File encrypted successfully"
                elif operation == 'decrypt':
                    result = caesar_cipher(content, key, decrypt=True)
                    result_message = "File decrypted successfully"
                else:
                    return render_template('index.html', error="Invalid operation. Please choose encrypt or decrypt.")

            with open(file_path, 'w') as file:
                file.write(result)

        except Exception as e:
            return render_template('index.html', error=f"An error occurred: {str(e)}")

    return render_template('index.html', result_message=result_message)

if __name__ == '__main__':
    app.run(debug=True)

