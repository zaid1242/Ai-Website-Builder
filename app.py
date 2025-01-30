from flask import Flask, request, jsonify
import openai

# Step 1: Initialize Flask app
app = Flask(__name__)

# Step 2: Set OpenAI API Key
openai.api_key = "your-api-key"  # Replace with your OpenAI key

# Step 3: AI Function to Generate Website Code
def generate_website(command):
    prompt = f"Generate an HTML, CSS, and JavaScript code snippet for: {command}. Keep it simple, responsive, and well-structured."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Step 4: API Route to Handle User Requests
@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    command = data["command"]
    website_code = generate_website(command)
    return jsonify({"code": website_code})

# Step 5: Run Flask App
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
