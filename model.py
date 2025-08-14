"""Imports"""
import google.generativeai as genai
from google.generativeai.types import GenerationConfig
from prompt import build_prompt
from test_file import extract_text
from tools import write_to_docx


def get_response(prompt_, mode_name='gemini-1.5-flash'):
    """Getting response"""
    prompt = prompt_

    model = genai.GenerativeModel(
        model_name=mode_name,
        system_instruction="Siz 'Rəy və Təklif Asistantı' — Azərbaycan Respublikası dövlət idarəetmə orqanlarında və hüquq sistemində"
                           "25 ildən artıq zəngin və çoxşaxəli təcrübəyə malik, strateji düşüncə qabiliyyəti yüksək, müasir hüquqi"
                           "normativləri dərindən mənimsəmiş, nüfuzlu və tanınmış ali səviyyəli dövlət analitiki və hüquq eksperti kimi"
                           "fəaliyyət göstərirsiniz."
    )

    generation_config = GenerationConfig(
        temperature=0.2
    )


    try:

        response = model.generate_content(
            contents=[
                {"role": "user", "parts": [{"text": prompt}]}
            ],
            generation_config=generation_config
        )

        if response.candidates and response.candidates[0].content and response.candidates[0].content.parts:
            return response.candidates[0].content.parts[0].text
        else:
            print("Error: Model did not return expected content structure.")
            return "Content generation failed."


    except Exception as e:
        print('An error occurred during content generation:' + e.__str__())
        return "Error: " + e.__str__()


def parse_response(response_text):
    """Parsing response"""
    text = """**ÜMUMİ RƏY**

                "Rəqəmsal İnnovasiya və Kibertəhlükəsizlik Şöbəsi"nin yaradılması təklifi, Azərbaycanın rəqəmsal transformasiya strategiyasına uyğun olaraq, əhəmiyyətli və zəruri bir addımdır. Lakin, təklifin maliyyə və təşkilati aspektləri daha dəqiq araşdırılmalı, həmçinin mövcud qanunvericiliyə tam uyğunluğunun təmin edilməsi vacibdir.
                
                **REGULYATİV VƏ STRATEJİ UYĞUNLUQ**
                
                Təklif "Rəqəmsal Azərbaycan" strategiyasının məqsədlərinə uyğundur və kibertəhlükəsizlik sahəsində mövcud qanunvericiliyə (məsələn, "İnformasiya təhlükəsizliyi haqqında" Qanun) əsaslanır.  Lakin, nazirliyin strukturuna yeni şöbənin əlavə edilməsi ilə bağlı "Dövlət qulluğu haqqında" Qanuna uyğunluğun təmin edilməsi və əməkdaşların seçimi üçün müvafiq prosedurların tətbiqi vacibdir.  Oxşar təcrübələr digər dövlət qurumlarının təcrübələrini araşdırmaqla müqayisə edilməlidir.  Məsələn, Rabitə Nazirliyinin kibertəhlükəsizlik strukturu və fəaliyyəti ilə müqayisəli təhlil aparılmalıdır.  Ziddiyyətli məqamlar aşkar edilərsə, uyğunlaşdırma tədbirləri görülməlidir.
            """

    parts = {
        "ÜMUMİ RƏY" : "",
        "REGULYATİV VƏ STRATEJİ UYĞUNLUQ": "",
        "GÜCLÜ TƏRƏFLƏR": "",
        "ZƏİF VƏ PROBLEMLİ SAHƏLƏR": "",
        "TƏKLİFLƏR": "",
        "HÜQUQİ QEYDLƏR": "",
        "MALİYYƏ ƏSASLARI": "",
        "YEKUN QİYMƏTLƏNDİRMƏ": ""
    }

    header = ""

    for ind, char in enumerate(text):

        pass
        # if header ==
        # pass

    pass


def main():

    # Gemini API config
    genai.configure(api_key="AIzaSyAjLpSkv_e9a5rLf-Efl90l2JEkh7ZWzMI")

    text = extract_text()
    prompt = build_prompt(text=text)

    response = get_response(prompt)


    write_to_docx(response)

    # with open(r"../results/result.txt", "w", encoding="utf-8") as file:
    #     file.write(response)
    #     print("Completed!")

    print(response)



if __name__ == "__main__":
    main()




