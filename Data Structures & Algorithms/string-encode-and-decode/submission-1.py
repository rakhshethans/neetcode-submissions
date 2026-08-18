class Solution:

    def encode(self, strs: List[str]) -> str:
        # how the encoder works:
        # find the length of every string
        # an element is encoded by having its length followed by the element
        # we know where the next element starts because we add the length to where the string starts
        # this is combined together to form the whole encoded string

        encodedString = ""
        for element in strs:
            length = len(element)
            # [length][element]
            encodedString = encodedString +  str(length) + "#" + element
        
        return encodedString


    def decode(self, s: str) -> List[str]:
        # how the decoder works:
        # start at first char, which is a length
        # next char is start of first word, add length to starting index to get last element
        # that is the whole word
        # next element is the length of the next word
        # repeat till end of string

        decodedList = []
        isLength = True

        i = 0
        while i < len(s):
            length = ""
            currentChar = s[i]
            while currentChar != "#":
                length += currentChar
                i += 1
                currentChar = s[i]
            
            length = int(length)
            start = i + 1
            end = start + length
            element = s[start:end]
            decodedList.append(element)
            i = i + length + 1
        
        return decodedList

