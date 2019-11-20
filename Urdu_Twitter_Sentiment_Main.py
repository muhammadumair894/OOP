from urdu_sentiment_NLP_analysis_lib import get_urdu_sentiment
urdu_input_sentence="""
دونوں بھائیوں کو اور تو کوئی کھلونا اتنا پسند آیا نہیں تھا   
"""
urdu_sentiment_output=get_urdu_sentiment(urdu_input_sentence)
print(urdu_sentiment_output)