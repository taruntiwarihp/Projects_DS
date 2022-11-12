import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from nltk.tokenize import RegexpTokenizer # regexp tokenizers use to split words from text  
from nltk.stem.snowball import SnowballStemmer # stemmes words
from sklearn.feature_extraction.text import CountVectorizer # create sparse matrix of words using regexptokenizes  
from sklearn.pipeline import make_pipeline
import pickle# use to dump model 
import warnings # ignores pink warnings 
warnings.filterwarnings('ignore')

def main():
    phish_data = pd.read_csv('phishing_site_urls.csv')
    new_phish_data = pd.read_csv("dataset_phishing.csv")

    # print(phish_data.head())
    # print(new_phish_data.head())
    new_phish_data.columns = phish_data.columns
    print(phish_data.shape, new_phish_data.shape)
    final_df = pd.concat([phish_data, new_phish_data])
    print("New dataframe shape", final_df.shape)
    print("Null Values :",final_df.isnull().sum())

    tokenizer = RegexpTokenizer(r'[A-Za-z]+')

    print('Getting words tokenized ...')
    final_df['text_tokenized'] = final_df.URL.map(lambda t: tokenizer.tokenize(t)) # doing with all rows

    print('Getting words stemmed ...')
    stemmer = SnowballStemmer("english") 
    final_df['text_stemmed'] = final_df['text_tokenized'].map(lambda l: [stemmer.stem(word) for word in l])

    print('Getting joiningwords ...')
    final_df['text_sent'] = final_df['text_stemmed'].map(lambda l: ' '.join(l))

    cv = CountVectorizer()
    feature = cv.fit_transform(final_df.text_sent)
    trainX, testX, trainY, testY = train_test_split(feature, final_df.Label)

    print("Creating Pipeline ...")
    pipeline_ls = make_pipeline(CountVectorizer(tokenizer = RegexpTokenizer(r'[A-Za-z]+').tokenize,stop_words='english'), MultinomialNB())

    print("Training Pipeline ..")
    trainX, testX, trainY, testY = train_test_split(final_df.URL, final_df.Label)
    pipeline_ls.fit(trainX,trainY)
    pipeline_ls.score(testX,testY) 
    print('Training Accuracy :',pipeline_ls.score(trainX,trainY))
    print('Testing Accuracy :',pipeline_ls.score(testX,testY))

    print("Saving model ...")
    pickle.dump(pipeline_ls,open('phishing.pkl','wb'))

    loaded_model = pickle.load(open('phishing.pkl', 'rb'))
    result = loaded_model.score(testX,testY)
    print("Final Accuracy ", result)


if __name__ == "__main__":
    main()