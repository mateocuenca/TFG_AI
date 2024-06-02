from openai import OpenAI
from dotenv import dotenv_values
from langchain_community.document_loaders import PyPDFLoader
from constants import system_instructions

# 1. Carga el PDF
loader = PyPDFLoader(
    r"/home/matecuenca/Documentos/Ingenieria-en-Software/Defensa-Oral/CVs/RodriguezCuencaMateo_CV_160224_español.pdf")

# 2. Extrae el contenido de la primer página del PDF
pdf_page_content = loader.load_and_split()[0].page_content


# 3. Guarda token de OPEN AI
OPENAI_API_KEY = dotenv_values(".env").get("OPENAI_API_KEY")

# 4. Crea un objeto cliente de OPEN AI
client = OpenAI(api_key=OPENAI_API_KEY)

# 5. Crea un prompt y guarda la respuesta
response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    response_format={"type": "json_object"},
    messages=[
        {
          "role": "system",
          "content": [
              {
                  "type": "text",
                  "text": f"{system_instructions}"
              }
          ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"{pdf_page_content}"
                }
            ]
        },
    ],
    temperature=1,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

# 6. Imprime la respuesta por consola
print(response.choices[0].message.content)
