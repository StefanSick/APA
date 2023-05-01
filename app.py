import ast
import openai
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='templates')

openai.api_key = "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"


def apa_votes(text):
    parties_dict = '''{
    "GRÜNE": "__",
    "Liste Potocnik (Linz)": "__",
    "Bier": "__",
    "Team Kärnten": "__",
    "JETZT": "__",
    "Für Innsbruck": "__",
    "DAÖ": "__",
    "ÖVP": "__",
    "Liste Fritz": "__",
    "FRITZ": "__",
    "Gerechtes Innsbruck": "__",
    "SONSTIGE": "__",
    "SPÖ": "__",
    "FPÖ": "__",
    "BZÖ": "__",
    "ALI": "__",
    "Verantwortung Erde": "__",
    "Tiroler Seniorenbund": "__",
    "MFG": "__",
    "Team HC Strache": "__",
    "TS": "__",
    "NEOS": "__",
    "KPÖ": "__",
    "PIRAT": "__",
    }'''

    prompt = (
        f"take the given Article in German:\n\n{text}\n\n"
        "Collect the vote percentages for each party with medium level of preciseness. The percentages are in text. Give as an output: python dictionary format with following keys and values. __ must become a percentage or NA if not found: \n"
        f'{parties_dict}'
    )
    

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=3020,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    party_dictionary = ast.literal_eval(response.choices[0].text.strip())
    return party_dictionary

def apa_highlight(text_2):
    apa_list=[]

    
    prompt_2 = (f"Given the following text in German:\n\n{text_2}\n\n"
                "Find the passages in the text where the vote percentage for each political party is stated."
                "For each passage, create a string that contains the exact text passage from the article where the information was found. Place each string in a list and return the list as the output."
            f"{apa_list}")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt_2,
        max_tokens=3020,
        n=1,
        stop=None,
        temperature=0.5,
    )
    api_output = response.choices[0].text.strip()
    apa_list = ast.literal_eval(api_output)
    return apa_list



@app.route('/', methods=['GET', 'POST'])
def apa():
    if request.method == 'POST':
        text = request.form['text']
        apa_data = apa_votes(text)
        apa_list_fin = apa_highlight(text)
        return render_template('apa_output.html', apa=apa_data, text_apa = text, apa_list= apa_list_fin)
    return render_template('apa_input.html')


if __name__ == '__main__':
    app.run(debug=True)
