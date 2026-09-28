import requests

def generate_email(sender_name, recipient, purpose, tone, keypoints):

    prompt = f"""You are an email AI writer. Create a complete email using the following information.

    Sender Name: {sender_name}
    Recipient Name: {recipient}
    Purpose: {purpose}
    Key Points: {keypoints}
    Tone: {tone}

    Instructions:Create a suitable subject.Include a greeting.Write a clear email.Use the provided key points.
    Do not invent information.Keep the mail concise.Include a professional closing.Sign using the sender name.Return only the email."""
    url="http://localhost:11434/api/generate"
    data={
        "model":"llama3.2:3b",
        "prompt":prompt,
        "stream":False
    }
    response=requests.post(url,json=data)
    result=response.json()
    return result["response"]
print("=======================")
print("AI EMAIL WRITER")
print("=======================")
sender_name=input("Your Name: ")
recipient=input("Recipient: ")
purpose=input("Purpose: ")
keypoints = input("Key point: ")
tone = input("tone: ")
email = generate_email(sender_name, recipient, purpose, tone, keypoints)
print("=======================")
print("generate email")
print("=======================")
print(email)
with open("generate_email.txt","w",encoding="utf-8") as file:
    file.write(email)
print("\n Email Generated To generated email.txt")
