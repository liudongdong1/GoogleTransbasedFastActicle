# from google_trans import google_translator  
  
# def singleThreadTran():
#     translator = google_translator()  
#     # <Translate text=สวัสดีจีน lang_tgt=th lang_src=zh>  
#     #  default parameter : lang_src=auto lang_tgt=auto 
#     #  API can automatically identify the src translation language, so you don’t need to set lang_src
#     translate_text = translator.translate('สวัสดีจีน',lang_tgt='en')  
#     print(translate_text)


# from multiprocessing.dummy import Pool as ThreadPool
# import time
# pool = ThreadPool(8) # Threads
# def request(text):
#     lang = "zh"
#     t = google_translator(timeout=5)
#     translate_text = t.translate(text.strip(), lang)
#     return translate_text

# if __name__ == "__main__" :
#     time1 = time.time()
#     with open("./test.txt",'r') as f_p:
#       texts = f_p.readlines()
#       try:
#           results = pool.map(request, texts)
#       except Exception as e:
#           raise e
#       pool.close()
#       pool.join()

#       time2 = time.time()
#       print("Translating %s sentences, a total of %s s"%(len(texts),time2 - time1))