# SpamFilterBypass

Came across this a while back. Some vendors implemented fixes, some haven't, some said it's a non-issue, some weren't tested. Obivously, can depend on configuration of product you're facing. Number of prompts make it less that ideal...

The script will null the first 2 bytes of a word document. 

- Create new word document
- Add macro
- run script (or open in text editor and manually delete first 2-bytes)
- Save
- Open the document
- Repair it
- Execute macro
