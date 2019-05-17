cat_speech = input("Enter a text you want the cat to say")

text_length = len(cat_speech)

print('{} {0:>4}'.format('^'))
print('  {0:4}'.format('_' * text_length))
print('< {0:4} >'.format(cat_speech))
print('  {}'.format('--' * text_length))







