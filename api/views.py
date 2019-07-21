from django.shortcuts import render
from django.views.generic import TemplateView
import telebot



class Page(TemplateView):
	def get(self, request, **kwargs):
		bot = telebot.TeleBot("670299637:AAFm_IQBb4H0AQtGXwNjO_F_vlhEZ1XQuac")

		@bot.message_handler(content_types=['text'])
		def send_welcome(message):
			bot.reply_to(message, "Howdy, how are you doing?")
		bot.polling(none_stop = True)
		return render(request, "page.html", {"hi": "hi"})

	def post(self, request, **kwargs):
		pass

