from duckduckgo_search import DDGS 

def fetch_search_results(topic, num_results=3):
     """ Search the web for topic and then return snippet """ 
     results = [] with DDGS() as ddgs: 
          for r in ddgs.text(topic, max_results = num_results): 
            results.append(r["body"]) return results