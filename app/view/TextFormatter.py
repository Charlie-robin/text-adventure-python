class TextFormatter:
    @staticmethod
    def pad_text( text, line_width, border_character = "*"):
        amount_to_pad = line_width - len(text) - 4
        padding = " " * amount_to_pad 
        return f"{border_character} {text}{padding} {border_character}"
    
    @staticmethod
    def center_pad_text(text, line_width, border_character = "*"):
        even_text = text if len(text) % 2 == 0 else f"{text} "
        amount_to_pad = int((line_width - len(even_text)) / 2 - 2)
        padding = " " * amount_to_pad
        return f"{border_character} {padding}{even_text}{padding} {border_character}"

    @staticmethod
    def split_oversized_text( text, line_width):
        words = text.split(" ")
        words_to_pad = []
        for word in words:
            if len(words_to_pad) == 0:
                words_to_pad.append(word)
                continue
            if len(word) + len(words_to_pad[-1]) < line_width - 5:
                words_to_pad[-1] += f" {word}"
            else:
                words_to_pad.append(word)    
        return words_to_pad        