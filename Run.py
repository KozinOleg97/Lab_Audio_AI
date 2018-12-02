import glob
import Main

files = glob.glob('./*.wav')
for ele in files:
    Main.f(ele)
quit()