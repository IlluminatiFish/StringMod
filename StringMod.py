###########################
# Project Name: StringMod #
# Version: 0.0.1          #
# Author: IlluminatiFish  #
###########################

class Matcher:

    def __init__(self, string_a, string_b):
        self.string_a = string_a
        self.string_b = string_b

        
    def matches(self):

        # We do not want to include spaces in the matched string counter so we check for this
        chars_a = [char for char in self.string_a if not char.isspace()] 
        chars_b = [char for char in self.string_b if not char.isspace()]

        matched = ""

        for a, b in zip(chars_a, chars_b):
            if a == b:
                matched += b
            else:
                break
            
        return len(matched)
    

    def matched_chars(self):
        chars_a = [char for char in self.string_a]
        chars_b = [char for char in self.string_b]

        matched = ""

        for a, b in zip(chars_a, chars_b):
            if a == b:
                matched += b
            else:
                break

        return matched

matcher = Matcher('test', 'test2')
print('Number of matches made: {}'.format(matcher.matches()))
print('Chars that were matched: {}'.format(matcher.matched_chars()))

