
import ast
import openai
openai.api_key = "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"
def apa_highlightsssss(text_2):
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

text_5 = "Utl.: In Kanzlerdirektfrage fällt SPÖ-Chefin Pamela Rendi-Wagner\n deutlich hinter FPÖ-Chef Herbert Kickl zurück =\n\n\nWien (OTS) - In der großen „profil“-Monatsumfrage überholt die FPÖ\nmit 28% (+2) die SPÖ und liegt nun erstmals seit fast sieben Jahren\nauf dem ersten Platz. Die Sozialdemokratie verliert 2%-Punkte auf\n24%. Noch deutlicher fällt SPÖ-Chefin Pamela Rendi-Wagner in der\nfiktiven Kanzlerdirektfrage zurück. Nach 15% im Dezember würden sie\nim Jänner 12% direkt wählen, während FPÖ-Chef Herbert Kickl von 15\nauf 17% zulegt. Bundeskanzler Karl Nehammer liegt mit 20% vorne (+2).\nSeine Partei steigt auf 22% (+2). Der Regierungspartner, die Grünen,\nlegt auf 12% zu (+1). Die NEOs verharren bei 9%. Das geht aus einer\nUmfrage hervor, die das Meinungsforschungsinstitut Unique research\nfür „profil“ durchgeführt.\n\n\n Gefragt nach der Einstellung zu den Verkehrsblockaden der „Letzten\nGeneration“ sprechen sich 42% für Geldstrafen, 31% für\nGefängnisstrafen, 19% gegen jegliche Konsequenzen aus.\n\n\n Die geplante, rasche Aufhebung sämtlicher Corona-Maßnahmen\nbefürworten 60% der Befragten, der Rest will noch zuwarten.\n\n\n (n=800, maximale Schwankungsbreite: +\/- 3,5%, Methode: Kombination\naus Telefon- und Online-Befragung)\n\n\n~\nRückfragehinweis:\n Profil Redaktion GmbH\n online@profil.at\n~\n\n\nDigitale Pressemappe: http:\/\/www.ots.at\/pressemappe\/179\/aom\n\n\n*** OTS-ORIGINALTEXT PRESSEAUSSENDUNG UNTER AUSSCHLIESSLICHER\nINHALTLICHER VERANTWORTUNG DES AUSSENDERS - WWW.OTS.AT ***\n\n\nOTS0006 2023-01-21\/08:00\n\n\n210800 Jän 23\n"

print(apa_highlightsssss(text_5))