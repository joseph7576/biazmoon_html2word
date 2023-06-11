import platform
import PySimpleGUI as psg
from docx import Document
from bs4 import BeautifulSoup

psg.theme('DarkBlue')
layout = [[psg.T("")],
          [psg.T("-"), psg.Text("Please choose your downloaded biazmoon's question html file: ")],
          [psg.T(""), psg.Input(), psg.FileBrowse(key="-htmlfile-", file_types=(('HTML Files', '*.html'),)), psg.Button("Convert")],
          [psg.T(""), psg.Quit("Exit")]]
window = psg.Window('Biazmoon html2word', layout, size=(550,150))


def create_word_doc(file, directory):
    document = Document()
    
    with open(file) as fp: # you should replace your file with mine
        soup = BeautifulSoup(fp, 'html.parser')
        question_and_choices_list  = list(soup.find_all(['p', 'span']))

    CHOICE_LIST = ['الف) ', 'ب) ', 'ج) ', 'د) '] # choice list for questions

    qn = 1 # question number
    cn = 0 # choice number(index)
    for tag in question_and_choices_list:
        if tag.name == 'p': # if it's question
            line = f'\n{qn}- {tag.text.strip()}'
            run = document.add_paragraph(line) # write to doc file
            qn += 1
        elif tag.name == 'span': # if it's choice
            run = document.add_paragraph()
            if cn >= len(CHOICE_LIST): # reset choice index
                cn = 0
            if tag.has_attr('style'):
                # \033[1mBOLD\033[0m -> BOLD ANSI code
                run.add_run('BOLD -> ' + CHOICE_LIST[cn]).bold = True
            else:
                run.add_run(CHOICE_LIST[cn])
            run.add_run(tag.text.strip())
            cn += 1
    
    sysinfo = platform.system()
    if sysinfo == "Linux":
        filepath = directory + '/needtofix.docx'
    elif sysinfo == "Windows":
        filepath  = directory + '\\needtofix.docx'
        
    document.save(filepath)


while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED or event=="Exit" or event=="Quit":
        break
    elif event == "Convert":
        directory = psg.popup_get_folder("Choose a directory to save your docx file.", title='Where to save?')
        create_word_doc(values['-htmlfile-'], directory)
        psg.popup("needtofix.docx has created. Now go and fix that doc.", title=':D')