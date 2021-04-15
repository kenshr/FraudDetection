from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer,PorterStemmer
from nltk.corpus import stopwords
import re
lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()


class preprocess:
    def __init__(self, dataframe):
        self.df = dataframe.copy()

    def set_classes(self):
        self.df.acct_type = self.df.acct_type.map({'premium': 0, 'fraudster_event': 1, 'fraudster': 1, 'spammer_limited': 0,
                                                   'spammer_warn': 0, 'tos_warn': 0, 'spammer_noinvite': 0, 'tos_lock': 0, 'locked': 0,
                                                   'fraudster_att': 1, 'spammer_web': 0, 'spammer': 0})
        self.df.acct_type = self.df.acct_type.fillna(0)

    def scale(self):
        scaler = StandardScaler()

        scaled_columns = self.df[['approx_payout_date', 'body_length', 'channels',
                                  'event_created', 'event_end', 'event_published',
                                 'event_start', 'gts', 'sale_duration', 'sale_duration2', 'user_age', 'venue_latitude', 'venue_longitude']]
        column_names = scaled_columns.columns.tolist()

        self.df.drop(scaled_columns, axis=1, inplace=True)

        scaled_data = scaler.fit_transform(scaled_columns)
        scaled_df = pd.DataFrame(data=scaled_data, columns=column_names)
        self.df = pd.concat([self.df, scaled_df], axis=1)

    def get_dum(self):
        dum_cols = self.df[['country', 'currency', 'listed', 'venue_country', 'venue_state', 'payout_type']]

        dum_df = pd.get_dummies(dum_cols, drop_first=True)

        self.df = pd.merge(self.df, dum_df, left_index=True, right_index=True)

    def drop(self):
        self.df.drop(['country', 'currency', 'listed', 'object_id', 'previous_payouts',
                      'ticket_types', 'venue_country', 'venue_state', 'payout_type', 'user_created'], axis=1, inplace=True)

    def drop_nlp_cols(self):
        self.df.drop(['description', 'email_domain', 'venue_address', 'venue_name',
                      'name', 'org_desc', 'org_name', 'payee_name'], axis=1, inplace=True)

#     def nlp(self, sentence):
#         sentence=str(sentence)
#         sentence = sentence.lower()
#         sentence=sentence.replace('{html}',"")
#         cleanr = re.compile('<.*?>')
#         cleantext = re.sub(cleanr, '', sentence)
#         rem_url=re.sub(r'http\S+', '',cleantext)
#         rem_num = re.sub('[0-9]+', '', rem_url)
#         tokenizer = RegexpTokenizer(r'\w+')
#         tokens = tokenizer.tokenize(rem_num)
#         filtered_words = [w for w in tokens if len(w) > 2 if not w in stopwords.words('english')]
#         stem_words=[stemmer.stem(w) for w in filtered_words]
#         lemma_words=[lemmatizer.lemmatize(w) for w in stem_words]
#         return " ".join(filtered_words)

#     def nlp_process(self):
#         description, email_domain, venue_address, venue_name, name, org_desc, org_name
#         self.df['description_clean'] = self.df.description.map(lambda x: self.nlp(x))

    def fillnans(self):
        self.df = self.df.fillna(0)






    def prep(self):
        self.set_classes()
        self.scale()
        self.get_dum()
        self.drop_nlp_cols()
        self.drop()
        self.fillnans()
        return self.df

if __name__=='__main__':
    print('main')