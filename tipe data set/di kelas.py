english = {'desi', 'tono', 'evan', 'miko', 'takashi', 'chaewon'}
korean = {'chaewon', 'yeona', 'erika', 'miko'}

# hanya bisa satu bahasa (manual)
one_language = english.union(korean) - english.intersection(korean)
print("Hanya bisa satu bahasa:", one_language)
# output: Hanya bisa satu bahasa: {'yeona', 'tono', 'desi', 'erika', 'evan', 'takashi'}

