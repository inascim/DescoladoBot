import socket, subprocess, json
import time
import os.path


from telegram.ext import Updater

updater = Updater(token='247860137:AAE3nBl0PV5f7SaEEWGT3DEZ4Xub8O25Byk')

dispatcher = updater.dispatcher

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="Bem vindo ao desColado Bot! Alguém deixou cair um Tanenbaum?")

from telegram.ext import CommandHandler

start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)

def echo(bot, update):
        bot.sendMessage(chat_id=update.message.chat_id, text="Experimente um de nossos comandos: \n /octEval para avaliar uma sentença no octave \n /mathgraph para receber o output grafico de uma função no Matlab")

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler([Filters.text], echo)
dispatcher.add_handler(echo_handler)

def caps(bot, update, args):
        text_caps = ' '.join(args).upper()
        bot.sendMessage(chat_id=update.message.chat_id, text=text_caps)
        
caps_handler = CommandHandler('caps', caps, pass_args=True)
dispatcher.add_handler(caps_handler)

from telegram import InlineQueryResultArticle, InputTextMessageContent
def inline_caps(bot, update):
        query = update.inline_query.query
        if not query:
                return
        results = list()
        results.append(
                InlineQueryResultArticle(
                        id=query.upper(),
                        title='Caps',
                        input_message_content=InputTextMessageContent(query.upper())
                )
        )
        bot.answerInlineQuery(update.inline_query.id, results)

from telegram.ext import InlineQueryHandler
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)



'''def sum(bot, update, args):
        text_sum = ' '.join(args)
        
        proc = subprocess.Popen('octave --eval {}'.format(text_sum),stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
        cmdOutput = proc.communicate()
        cmdOutput = cmdOutput[0].decode('UTF-8').rstrip()
        print(cmdOutput)
        bot.sendMessage(chat_id=update.message.chat_id, text=cmdOutput)
'''


def mathgraph(bot, update, args):
        print('Calling cmd')
        text_mathgraph = ' '.join(args)
        print(mathgraph)
        arq = open('DescoladoBlindado.m', 'w')
        print(text_mathgraph)
        
        arq.write('figure;'+text_mathgraph+"print('FOTO.png','-dpng','-r0')")
        arq.close()
        
        #proc1 = subprocess.Popen('echo {} >> DescoladoBlindado.m'.format(text_sum),stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
        proc = subprocess.Popen('matlab -nodisplay -nodesktop -nosplash -r DescoladoBlindado ',stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
        #proc = subprocess.Popen('octave DescoladoBlindado.m',stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
        
        time.sleep(20)
        #while not os.path.exists("FOTO.png"):
        #        time.sleep(0.01)
        
        if(os.path.exists("FOTO.png")):
                #bot.sendMessage(chat_id=update.message.chat_id, text=cmdErr)
                #proc4 = subprocess.Popen('del /f DescoladoBlindado.m'.format(text_sum),stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
                bot.sendPhoto(chat_id=update.message.chat_id, photo=open('FOTO.png', 'rb'))
                
        else:
                bot.sendMessage(chat_id=update.message.chat_id, text=" Gráfico não foi encontrado. \n Tenha certeza de que seu programa imprima algo! ")
                #time.sleep(5)
                #bot.sendPhoto(chat_id=update.message.chat_id, photo=open('FOTO.png', 'rb'))
                #proc3 = subprocess.Popen('del /f DescoladoBlindado.m'.format(text_sum),stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
                
        proc4= subprocess.Popen('TASKKILL /f /IM matlab.exe'.format(text_mathgraph),stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True) 
        proc8 = subprocess.Popen('del /f FOTO.png',stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
mathgraph_handler = CommandHandler('mathgraph', mathgraph, pass_args=True)
dispatcher.add_handler(mathgraph_handler)





def octEval(bot, update, args):
        print('Calling cmd')
        text_octEval = '\n'.join(args)
        print(args)
        arq = open('DescoladoBlindado.m', 'w')
        print(text_octEval)
        
        arq.write(text_octEval)
        arq.close()

        #proc1 = subprocess.Popen('echo {} >> DescoladoBlindado.m'.format(text_sum),stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
        #proc = subprocess.Popen('matlab -nodisplay -nodesktop -nosplash -r DescoladoBlindado ',stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
        proc = subprocess.Popen('octave DescoladoBlindado.m',stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
        (cmdOutput, cmdErr) = proc.communicate()
        try:
                cmdOutput = cmdOutput.decode('UTF-8').rstrip()
        except:
                pass
        try:
                cmdErr = cmdErr.decode('UTF-8').rstrip()
        except:
                pass
        
        print(cmdErr)
        print(cmdOutput)
        if (len(cmdOutput) < 4):
                cmdOutput=None;
        
        if (len(cmdErr) < 4):
                cmdErr=None;

                
        if ( cmdOutput is None):
                bot.sendMessage(chat_id=update.message.chat_id, text=cmdErr)
                proc4 = subprocess.Popen('del /f DescoladoBlindado.m',stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True)
                time.sleep(5)
                #bot.sendPhoto(chat_id=update.message.chat_id, photo=open('FOTO.png', 'rb'))
                
        else:
                bot.sendMessage(chat_id=update.message.chat_id, text=cmdOutput)
                time.sleep(5)
                #bot.sendPhoto(chat_id=update.message.chat_id, photo=open('FOTO.png', 'rb'))
                proc3 = subprocess.Popen('del /f DescoladoBlindado.m',stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True)

        #proc4= subprocess.Popen('TASKKILL /f /IM matlab.exe'.format(text_sum),stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=True) 
octEval_handler = CommandHandler('octEval', octEval, pass_args=True)
dispatcher.add_handler(octEval_handler)

def unknown(bot, update):
        bot.sendMessage(chat_id=update.message.chat_id, text=" Comando não reconhecido. Tente novamente !")

unknown_handler = MessageHandler([Filters.command], unknown)
dispatcher.add_handler(unknown_handler)

updater.start_polling()
