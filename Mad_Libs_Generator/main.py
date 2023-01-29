# import json
# import os
#
# class Madlibs:
#     def __init__(self,word_desc,template):
#         self.word_desc=word_desc
#         self.template=template
#     def from_json(tname, path="./templates"):
#         fpath = os.path.join(path, tname)
#         with open(fpath, "r") as f:
#             data = json.load(f)
#         mad_lib =Madlibs(**data)
#         return mad_lib
# #user input
# def get_words_from_user(words):
#     word=[]
#     print("provide word: ")
#     for i in words:
#         r=input(i+" ")
#         word.append(r)
#     return word
#
# def build_story(template,words):
#     story=template.format(*words)
#     return story
#
# #H:\Python\Mad_Libs_Generator\templates\day at zoo.json
#
#
#
# temp_name="day at zoo.json"
# madlibs=Madlibs.from_json(temp_name)
# words=get_words_from_user(madlibs.word_desc)
# story=build_story(madlibs.template,words)
# print(story)
#
#
#
#
#
#
#
#
# #Build the story






import json
import os


class MadLibs:
    path = "templates"
    def __init__(self, word_desc, template):
        self.template = template
        self.word_desc = word_desc
        self.user_input = []
        self.story = None

    @classmethod
    def from_json(cls, name, path=None):
        if not path:
            path = cls.path
        fpath = os.path.join(path, name)
        with open(fpath, "r") as f:
            data = json.load(f)
        mad_lib = cls(**data)
        return mad_lib

    def get_words_from_user(self):
        print("Please provide the following words: ")
        for desc in self.word_desc:
            ui = input(desc + " ")
            self.user_input.append(ui)
        return self.user_input

    def build_story(self):
        self.story = self.template.format(*self.user_input)
        return self.story

    def show_story(self):
        print(story)


def select_template():
    print("Select a Mad Lib from the following list:")
    templates = os.listdir(MadLibs.path)
    template = input(str(templates) + " ")
    return template


temp_name = select_template()
# temp_name = "day_at_the_zoo.json"
mad_lib = MadLibs.from_json(temp_name)
words = mad_lib.get_words_from_user()
story = mad_lib.build_story()
mad_lib.show_story()

