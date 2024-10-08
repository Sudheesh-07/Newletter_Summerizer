import requests as Req , bs4
from urllib.parse import urljoin
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
# from transformers import pipeline

# ref_link = []
# def head_function():
#     global ref_link
#     url = "https://www.bbc.com/"
#     response = Req.get(url).text
#     soup = bs4.BeautifulSoup(response, "html.parser")
#     tag_a = soup.select('a')
#     head = []
#     para = []
#     image = []
#     for elements in tag_a:
#         h2 = elements.select("h2")
#         p = elements.select("p")
#         img = elements.select('img[src]')
#         if h2 and p:
#             head.append(h2[0].getText())
#             para.append(p[0].getText())
#             ref_link.append(elements.get('href'))
#             if img:
#                 image.append(img[1]['src'])
#             else:
#                 image.append(r"https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg")
#
#     # Concatenating link to open to scrape and summarize
#     for x in range(0, len(ref_link)):
#         if not ref_link[x].startswith("http"):
#             ref_link[x] = urljoin(url, ref_link[x])
#
#
#
#     # Combining news and summaries
#     news = zip(head, para, image)
#
#     context = {
#         "news_items": news
#     }
#     return context


# def summarize(link_list):
#     summaries = []
#     for x in link_list:
#         response = Req.get(x).text
#         nest_soup = bs4.BeautifulSoup(response, "html.parser")
#         nest_para = nest_soup.select('article')  # 'article' tag should be in lowercase
#
#         if nest_para:  # Ensure there is an article tag
#             full_news = nest_para[0].findAll('p')
#
#             # Extract the text from all paragraphs
#             news = [x.getText() for x in full_news]
#
#             # Merge all paragraphs into a single string
#             text = " ".join(news)
#
#             # Summarize the merged text
#             parser = PlaintextParser.from_string(text, Tokenizer("english"))
#             summarizer = TextRankSummarizer()
#             summary = summarizer(parser.document, 5)  # Summarize into 5 sentences
#
#             # Convert the summarized sentences into a single string
#             summary_sentences = [str(sentence) for sentence in summary]
#             summary_sentences = " ".join(summary_sentences)
#             # Store the summary in a dictionary
#             con_text = {"summary": summary_sentences}
#
#             summaries.append(summary_sentences)
#         else:
#             summaries.append("Summary not available.")  # If no article found
#
#         # Final context with all summaries
#     context = {
#         "data_sum": summaries
#     }
#     return context


































# def head_function():
#     global ref_link
#     url = "https://www.bbc.com/"
#     response = Req.get(url).text
#     soup = bs4.BeautifulSoup(response, "html.parser")
#     tag_a = soup.select('a')
#     head = []
#     para = []
#     image = []
#     for elements in tag_a:
#         h2 = elements.select("h2")
#         p = elements.select("p")
#         img = elements.select('img[src]')
#         if h2 and p:
#             head.append(h2[0].getText())
#             para.append(p[0].getText())
#             ref_link.append(elements.get('href'))
#             if img:
#                 image.append(img[1]['src'])
#             else:
#                 image.append(r"https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg")
#
#     #concating link to open to scrape and summarize
#     for x in range(0, len(ref_link)):
#         if not ref_link[x].startswith("http"):
#             ref_link[x] = urljoin(url, ref_link[x])
#
#
#     news = zip(head, para, image)
#     context = {
#         "news_items":news
#     }
#     return context

#















# def summarize_function():
#     summarizer = pipeline("summarization")
#     article ="""# put int he paragraph"""
#     summary = summarizer(article,max_length=120, min_length=80, do_sample=False)
#     return summary

# def summarize_text(text, sentence_count=5):
#     parser = PlaintextParser.from_string(text, Tokenizer("english"))
#     summarizer = TextRankSummarizer()
#     summary = summarizer(parser.document, sentence_count)
#     summary_sentences = [str(sentence) for sentence in summary]
#     return " ".join(summary_sentences)

