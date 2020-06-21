from telegram.ext import(Updater, CommandHandler)
from make_requests import get_memes_urls
from dictionary_requests import get_meanings
from insult_req import get_insult
from google_search import get_query_links
from word_does_not_exist import this_word_does_not_exist
import logging
import random
import os

NEWLINE = "\n"
WHITESPACE = " "

TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

##########################################################################################
#insult getting triggered by what's there in the text automatically

# with open("hi_en_bad_words.txt", "r") as f:
#     bad_words = f.readlines()
#     bad_words = [words.replace("\n", "") for words in bad_words]
#     print(len(bad_words))
# def insult_func(update, context):
#     msg = update.message.text
#     msg = msg.replace("\n", "")
#     msg_list = msg.split(" ")
#     for word in msg_list:
#         bad_word_list = [bad_word.lower() == word.lower() for bad_word in bad_words]
#         if (sum(bad_word_list)) and (len(word) > 2):    
#             context.bot.send_message(chat_id=update.effective_chat.id, text=update.effective_user.name + " " + get_insult())
#             break

# from telegram.ext import MessageHandler, Filters
# insult_handler = MessageHandler(Filters.text & (~Filters.command), insult_func)
# dispatcher.add_handler(insult_handler)
############################################################################################

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = 'Hi! welcome to Bot-O-Meme :) \
                                                                        \n\nThese are the available commands - \
                                                                        \n\n/meme - Shows a meme. \
                                                                        \n/toss - Tosses a coin. \
                                                                        \n/means <word> - Gets you the definitions. \
                                                                        \n/google <query string> - Gets you the top 10 google search results. \
                                                                        \n/fake_word - It will show you a fake word with detailed info which looks real. \
                                                                        \n\n/insult <tag> - insults the tagged user.')




def meme(update, context):
    url_caption_list = get_memes_urls(limit=1)
    for url_caption in url_caption_list:
        url = url_caption[0]
        img_url = url_caption[2]
        img_caption = url_caption[1]
        context.bot.send_photo(chat_id=update.effective_chat.id, photo = img_url, caption = img_caption + '\nSource - ' + url)



def toss(update, context):
    coin = {0 : "Heads", 1 : 'Tails'}
    index = random.randint(0, 1)
    context.bot.send_message(chat_id=update.effective_chat.id, text= coin[index].upper() + '!!')


def means(update, context):
    meaning_to_find_text = ' '.join(context.args).lower()
    try:
        meaning = get_meanings(meaning_to_find_text)
    except KeyError:
        meaning = ["Sorry no definitions found."]

    if len(meaning) > 1:
        meaning = '.\n\nor\n'.join(meaning)
    else:
        meaning = meaning[0]

    context.bot.send_message(chat_id=update.effective_chat.id, text=meaning_to_find_text + " means -\n\n" + meaning + ".")



def insult(update, context):
    try:
        person_tag = ' '.join(context.args)
        insult_text = get_insult()
        context.bot.send_message(chat_id=update.effective_chat.id, text= person_tag + " " + insult_text)
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, an unknown error occurred...")



def google(update, context):
    search_query = ' '.join(context.args)
    try:
        links = get_query_links(search_query)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Google results for " + search_query + " :\n\n" + "\n\n".join(str(i) + ". " + link for i, link in enumerate(links)))
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, an unknown error occurred...")


def fake_word(update, context):
    fake_word_data = this_word_does_not_exist()
    
    word = fake_word_data['word']
    definition = fake_word_data['definition']
    example = fake_word_data['example']
    exists = fake_word_data['exists']
    
    if exists is False:
        exists = "This word probably doesn't exists"
    else:
        exists = "This word probably exists"

    context.bot.send_message(chat_id=update.effective_chat.id, text="Word: " + word + NEWLINE + "Definition: " + definition + NEWLINE + "Example: " + example + NEWLINE + NEWLINE + exists)


if __name__ == '__main__':
    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context = True)
    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    meme_handler = CommandHandler('meme', meme)
    dispatcher.add_handler(meme_handler)

    toss_handler = CommandHandler('toss', toss)
    dispatcher.add_handler(toss_handler)

    meaning_handler = CommandHandler('means', means)
    dispatcher.add_handler(meaning_handler)

    insult_command_handler = CommandHandler('insult', insult)
    dispatcher.add_handler(insult_command_handler)

    google_handler = CommandHandler('google', google)
    dispatcher.add_handler(google_handler)

    fake_word_handler = CommandHandler('fake_word', fake_word)
    dispatcher.add_handler(fake_word_handler)

    updater.start_polling()