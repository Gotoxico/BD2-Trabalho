# BD2 - Trabalho

## Passos para Execução

### Criar o Ambiente Virtual e Instalar Dependências

No terminal, execute os seguintes comandos:

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

- Rode VideoResizeAndFrameExtractionPrincipal, lembrando sempre de alterar os paths de configuração

- Rode PeopleDetectionWithYoloSavingJSON, lembrando sempre de alterar os paths de configuração

- Link para pasta Google Drive com video utilizados para teste: https://drive.google.com/drive/folders/1jkZbXMNpJvO1UkcK4f8Cjl2jRkXTiwGc?usp=sharing

### Se quiser utilizar versão com LLM 

- Instale o LM Studio

- Instale modelo multi-modal (reconhece imagem)

- Inicie server

- Carregue um modelo e utilize o endereço chat/completions fornecido

- Rode CropPeopleWithYolo para recortar as pessoas nas imagens

- Rode IntegratingLLMButWithCroppedPeople para gerar records JSON
