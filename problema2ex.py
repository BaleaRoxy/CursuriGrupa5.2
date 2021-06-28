string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
#atches = [[5, 14, "Conquistador"], [26, 31, "King"], [43, 49, "Palace"]]

# def replace_text (start: int,  text: str) -> str:
#     word = string.split(" ")
#     word[start] = text
#     return word
#
# print(replace_text(2, "ala"))

def function(string, patches):
    patches=reversed(patches)
    string=[string.replace(string[item[0]-1:item[1]], item[2]) for item in patches]
    # for item in patches:
    #     print(item)
    #     start = item[0]
    #     end = item[1]
    string = string.replace(string[item[0]-1:item[1]], item[2])
    #     word = item[2]
    #     print(string, string[start-1:end])
    return string
print(function(string, [5,14, "Conquistador"], [26, 31, "king"], [43, 49, "palace"]))