# Gemini API

## install the SDK

```bash
pip install -q -U google-generativeai
```

## initialize the generative model

```Python
import google.generativeai as genai


genai.configure(api_key = "your gemini api key")
model = genai.GenerativeModel('gemini-pro')

```

## generate text

```Python
response = model.generate_content("write a story about ai")
print(response.text)
```
