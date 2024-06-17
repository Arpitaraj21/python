import pywhatkit as pw

txt = """ Python is an interpreted high-level general-purpose programming"""

pw.text_to_handwriting(txt, "optional.png", [0,0,138])
print("END")