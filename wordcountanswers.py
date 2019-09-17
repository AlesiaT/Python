# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def creation(text):
  for i in range(len(text)):
    text[i] = text[i].lower()
  answer = {}
  sortedtext = sorted(text)
  count = [1]
  i = 1
  a = len(sortedtext)
  while i < a:
    if sortedtext[i] == sortedtext[i-1]:
      count[i-1] += 1
      sortedtext.pop(i)
      a = len(sortedtext)
    else:
      count.append(1)
      i += 1
      a = len(sortedtext)
  for b in range(a):
    key = sortedtext[b]
    answer[key] = count[b]
  return answer

def print_words(text):
  answer = creation(text)
  for k, v in answer.items():
    print (k, ' ', v)
  print ('')

def print_top(text):
  answer = creation(text)
  sortedvalues = sorted(answer.values(), reverse = True)
  sortedkeys = sorted(answer, key=answer.__getitem__, reverse = True)
  print_top = {}
  for i in range(30):
    if i < len(sortedkeys):
      print_top.update( {sortedkeys[i] : sortedvalues[i]} )
  for k, v in print_top.items():
    print (k)
  

  



###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  print ('wordcount.py {--count | --topcount} file')

  filename = ['pensil', 'ShirT', 'word', 'pen', 'pensil', 'shirt', 'Word', 'shirt', 'shirt', 'PenSil', 'pensil', 'Frog', 'pen', 'word', 'shirt']

  print_words(filename)
  print_top(filename)
   
if __name__ == '__main__':
  main()