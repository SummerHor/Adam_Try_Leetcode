class Solution:
    def capitalizeTitle(self, title: str) -> str:
        splitted_title = title.split(" ")
        org_title = []
        for i, word in enumerate(splitted_title):
            if len(word) > 2:
                for index, char in enumerate(word):
                    if index == 0:
                        org_title.append(char.upper())
                    else:
                        org_title[i] += char.lower()
            else:
                for index, char in enumerate(word):
                    if index == 0:
                        org_title.append(char.lower())
                    else:
                        org_title[i] += char.lower()
        title = " ".join(org_title)
        return title

