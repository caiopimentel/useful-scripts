import sys

sentence_counter = 0
paragraph_threshold = 3
output = []

for p in sys.argv[1:]:

    with open(p, encoding='utf8') as f:
        content = ''.join(f.readlines()) # reading file
        content = content.replace('\n', ' ').split('.')  # preprocessing

    for i in content:
        if sentence_counter < paragraph_threshold:
            if sentence_counter == 0:
                output.append(i.lstrip() + '.')
            else:
                output.append(i + '.')
            sentence_counter += 1
        else:
            output.append(i + ('.\n'))
            sentence_counter = 0

    with open(p[2:-4] + '_OUTPUT.txt', "w") as f:
        f.write(''.join(output[:-1]))

else:
    print('\nUsage examples:\n  edx_linebreak_cleaner.py edx_subtitle_00.txt')
    print('  edx_linebreak_cleaner.py edx_subtitle_00.txt edx_subtitle_01.txt edx_subtitle_02.txt\n')