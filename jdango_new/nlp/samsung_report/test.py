from nlp.samsung_report.services import Controller

key, value = Controller().test()
a = [{'maximum_frequency_word' : key},{'maximum_frequency_count':value}]
print(a)