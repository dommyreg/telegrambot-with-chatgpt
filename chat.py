
import openai
import telebot

openai.api_key = "la tua chiave API"
bot = telebot.TeleBot("IL TUO TOKEN TELEGRAM")

def chatgpt3(message):
	res = openai.Completion.create(
	    model = "text-davinci-003",
	    prompt = message,
	    max_tokens = 200
	)
	return res.choices[0].text
	
@bot.message_handler(func=lambda message: True)
def chat(message):
	res = chatgpt3(message.text)
	bot.reply_to(message, res)
		
bot.infinity_polling()
		
