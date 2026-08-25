
# Rag-demo
 
Small Django API that talks to a local LLM (running through LM Studio) and answers questions using a basic RAG setup over a few text files. Built this to understand how RAG and OpenAI-style API integration work under the hood, so no LangChain, no vector DB, just plain Python.
 
### How works
 
You send a question to `/assistant/ask/`. It searches through the .txt files in `assistant/docs/` for whichever one shares the most words with the question (just splitting text into sets and checking overlap, nothing fancy), then sends that document's content plus your question to the local model. The model answers using that context instead of just guessing.
 
## Stack
 
Django + DRF, the `openai` python library pointed at my local LM Studio server instead of actual OpenAI, running qwen2.5-coder-1.5b-instruct locally. No embeddings or vector search, just word overlap for now.
 
## Setup ist3malo the below commands :D
 
```bash
python -m venv venv
source venv/bin/activate
pip install django djangorestframework openai python-dotenv
python manage.py runserver
```
 
Also need LM Studio running with the server started and the model loaded, serving on http://127.0.0.1:1234.
 
## Testing
 
Quick check that routing works, no LLM involved:
 
```bash
curl -X POST http://127.0.0.1:8000/assistant/ask/ \
  -H "Content-Type: application/json" \
  -d '{"question": "does this work"}'
```
 
Should pull from the shipping doc:
 
```bash
curl -X POST http://127.0.0.1:8000/assistant/ask/ \
  -H "Content-Type: application/json" \
  -d '{"question": "how long does shipping take"}'
```
 
Should pull from the returns doc:
 
```bash
curl -X POST http://127.0.0.1:8000/assistant/ask/ \
  -H "Content-Type: application/json" \
  -d '{"question": "what is your return policy"}'
```
 
If the Django endpoint throws a connection error, this checks whether LM Studio itself is actually up, skips Django entirely: LET ME SAY CLAUDE 3AZAMA FOR PROVIDING THESE TESTING COMMANDS :D
 
```bash
curl -X POST http://localhost:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen2.5-coder-1.5b-instruct",
    "messages": [{"role": "user", "content": "does this work"}],
    "temperature": 0.7
  }'
```
 
## Limitations
 
Retrieval is just keyword overlap, no real understanding of meaning. Ask something totally unrelated like "what's the weather today" and it'll still confidently hand back whichever doc happens to share the most words, even if none of them are actually relevant. Real RAG would use embeddings and cosine similarity, and probably a minimum score threshold so it can say "nothing relevant found" instead of forcing a bad match.
 
Also no memory between requests, every question is handled fresh with no history. And it only ever returns one document, doesn't combine info from multiple files :p.

Currently on the tool calling - smaller models do struggle with providing the correct output although they do know how to use the tool. Models I've tried are qwen2.5-coder-7b-instruct and qwen2.5-coder-1.5b-instruct. They where useless as they did not give the out put in the correct way/ formatting. If you want to try it, try using the Qwen3-Coder-30B-A3B in Lm studio as that model is more capable, i did not try it yet lol but you can if you want.
 
## Next up
 
Still need to add tool/function calling so the model can actually call a function like check_order_status instead of just answering from text. After that, package the whole thing with Docker so it can run anywhere. Might swap the retrieval for real embeddings if I have time, you may ask where i got the shipping and delivery thing from yeah got it from the current job I have lol so yeah no judgin please :)).


## All done now but I skipped a couple of things - not sure if I'll add anything as this took way more time than it should've but view the repo if you're interested in rag - materials I used for studying is AWS what is rag and a couple of random sites and articles with some claude for explanation of difficult or unclear topics :D