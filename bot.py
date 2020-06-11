from telegram.ext import Updater, CommandHandler
import logging

updater = Updater(token='1128728650:AAFPELrFHtNnuVpN_0nG___iuzvk7PJyDBo', use_context = True)

dispatcher = updater.dispatcher

# print(dispatcher)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text = 'Hi! use /meme command to see memes :)')

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# def echo(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# from telegram.ext import MessageHandler, Filters
# echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
# dispatcher.add_handler(echo_handler)


# def caps(update, context):
#     text_in_caps = ' '.join(context.args).upper()
#     context.bot.send_message(chat_id=update.effective_chat.id, text=text_in_caps)

# caps_handler = CommandHandler('caps', caps)
# dispatcher.add_handler(caps_handler)


from make_requests import get_memes_urls


def meme(update, context):
    url_caption_list = get_memes_urls(limit=1)
    for url_caption in url_caption_list:
        url = url_caption[0]
        img_url = url_caption[2]
        # print("img_url -", img_url)
        img_caption = url_caption[1]
        # print("img_caption -", img_caption)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo = img_url, caption = img_caption + '\nSource - ' + url)

meme_handler = CommandHandler('meme', meme)
dispatcher.add_handler(meme_handler)


# from telegram import InlineQueryResultArticle, InputTextMessageContent
# def inline_caps(update, context):
#     query = update.inline_query.query
#     if not query:
#         return
#     results = list()
#     results.append(
#         InlineQueryResultArticle(
#             id=query.upper(),
#             title='Caps',
#             input_message_content=InputTextMessageContent(query.upper())
#         )
#     )
#     context.bot.answer_inline_query(update.inline_query.id, results)

# from telegram.ext import InlineQueryHandler
# inline_caps_handler = InlineQueryHandler(inline_caps)
# dispatcher.add_handler(inline_caps_handler)


updater.start_polling()