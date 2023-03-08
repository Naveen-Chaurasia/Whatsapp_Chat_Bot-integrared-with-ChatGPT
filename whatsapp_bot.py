
#https://www.pragnakalp.com/automate-messages-using-whatsapp-business-api-flask-part-1/
#https://www.pragnakalp.com/build-an-automated-ai-powered-whatsapp-chatbot-with-chatgpt-using-flask/
#https://www.pragnakalp.com/automate-messages-using-whatsapp-business-api-flask-part-1/


from flask import Flask, request
import requests
import openai

openai.api_key = 'sk-hT**************************************************uBo'

app = Flask(__name__)
 
def send_msg(msg,receiver_number):

  headers = {
       'Authorization': 'Bearer EAADOtBAbT*********************************************ISJxX4yb8NTmjC9ClEgZB3uQySMGUahx1e4ZAAq39RWFhiZAkZBrZAQ888CVBB8gTKAZCgM8iRZBNPm2WYxh2PtVQZDZD',
   }

  response = requests.post('https://graph.facebook.com/v16.0/1035Phone_ID*************2/messages',
                            json={
        "messaging_product": "whatsapp",
        "to": ***************,
        "type": "text",
        "text": {
            "body": msg
        }
    },
                            headers=headers)

  print("Status code: ", response.status_code)

# response_Json = response.json()
# print("Printing Post JSON data")
# print(response_Json['data'])

# print("Content-Type is ", response_Json['headers']['Content-Type'])
  print(response)

@app.route('/receive_msg', methods=['POST','GET'])
def webhook():
   res = request.get_json()
   print(res)
   try:
       if res['entry'][0]['changes'][0]['value']['messages'][0]['id']:
            chat_gpt_input=res['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
            completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": chat_gpt_input}]
            )
            response = completion['choices'][0]['message']['content']
            print("ChatGPT Response=>",response)
            receiver_number=res['entry'][0]['changes'][0]['value']['contacts'][0]['wa_id']
            send_msg(response,receiver_number)
   except:
       pass
   return '200 OK HTTPS.'
 
  
if __name__ == "__main__":
   app.run(debug=True)