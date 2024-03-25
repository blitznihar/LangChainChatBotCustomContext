# LangChain ChatBot Custom Context

##### Simple Fact document is being loaded using langchain text loader and embedded and stored in the vector database (used chroma for ease of testing) and based on the query it retrieves the relevant text from the vector database

#### _Step to run the project_

Add Environment file. Create a .env file and add below configurations
```sh
OPENAI_API_KEY=""
```
Fill the OPENAI_API_KEY values

In the Terminal 
```sh
pipenv install
pipenv shell
```

Once the app is running type below command in the Terminal
```sh
python .
```

Ask your question. for e.g.
```sh
what is the interesting fact about ostrich
```

Or
```sh
what is the interesting fact about english
```

##### References:
[Configurations](https://www.lambdatest.com/blog/python-configuration-file/)

[OpenAI](https://platform.openai.com/docs/introduction)

[GoogleAI](https://aistudio.google.com/app/apikey)

[LangChain](https://python.langchain.com/docs/get_started/introduction)