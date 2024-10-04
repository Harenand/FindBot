import asyncio
from duckduckgo_search import AsyncDDGS

async def aget_results(word):
    results = await AsyncDDGS(proxy=None).atext(word, max_results=15)
    return results

def print_hrefs(json_data):
    """
    Выводит построчно атрибуты href из JSON-данных.
    """
    if isinstance(json_data, dict):
        for key, value in json_data.items():
    
          if key == "href":
              print(f"{value}\n")              
          elif isinstance(value, (dict, list)):
              print_hrefs(value)
  
    elif isinstance(json_data, list):
        for item in json_data:
            print_hrefs(item)



if __name__ == "__main__":
    res = asyncio.run(aget_results("как приготовить пирог"))
    if isinstance(res, dict):
        for key, value in res.items():
    
          if key == "href":
              print(f"{value}\n")              
          elif isinstance(value, (dict, list)):
              print_hrefs(value)
  
    elif isinstance(res, list):
        for item in res:
            print_hrefs(item)

# https://duckduckgo.com/?t=h_&q=%D0%BA%D0%B0%D0%BA+%D0%BF%D1%80%D0%B8%D0%B3%D0%BE%D1%82%D0%BE%D0%B2%D0%B8%D1%82%D1%8C+%D0%BF%D0%B8%D1%80%D0%BE%D0%B3&ia=web
# results = DDGS().text("как научится играть на гитаре", max_results=10, )
# print_hrefs(results)
# https://html.duckduckgo.com/html/?t=h_&q=как ухаживать за черепахой&ia=web


# import requests
# from bs4 import BeautifulSoup

# def duckduckgo_parse_links(query):
#     """
#     Парсит ссылки на источники с DuckDuckGo.
#     """
#     url = f"https://duckduckgo.com/?q={query}"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')

#     results = soup.find_all('a', class_='result__a')

#     links = []
#     for result in results:
#         links.append(result['href'])

#     return links

# # Пример использования
# results = duckduckgo_parse_links("python programming")
# print(results)




# import ollama
# response = ollama.chat(model='llama2', messages=[
#   {
#     'role': 'user',
#     'content': 'Write a synonym for the word beautiful',
#   },
# ])
# print(response['message']['content'])
