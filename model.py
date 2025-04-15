
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
    # Disable scientific notation for clarity
def finder():
    np.set_printoptions(suppress=True)
    model = load_model("keras_Model.h5", compile=False)
    class_names = open("labels.txt", "r").readlines()
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open("<IMAGE_PATH>").convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    if class_name == "👋 Merhaba":
        print("Oh Sanada merhaba") or print("Oh Birileri gelmis Merhaba!")
    elif class_name == "🤘 Rock’n Roll":
        print("Birileri Metalci Sanirim") or print("Rap mi Rock mi?")
    elif class_name == "❤️ Kalp Eller":
        print("Bende seni seviyorum") or print("Cok tatlisin!")
    elif class_name == "👌 Tamam":
        print("Tamam..") or print("Hadi ama bu kadar sade olma")
    elif class_name == "✊ Yumruk":
        print("Kagit! Ben Kazandim") or print("Demek boks ha ama benim ellerim yok :( )")
    elif class_name == "✌️ Barış":
        print("Savas") or print("Bu gunlerde zor bulunuyor Ama sen yinede pozitif kal!")
    elif class_name == "👍 Başparmak Yukarı":
        print("Guzell") or print("Aklina gelen ilk el haraketi sanirim")
    elif class_name == "🤜🤛 Çarpan Yumruklar":
        print("Cak bakalim") or print("Dostuz galiba")
    elif class_name == "Arkaplan":
        print("Ummm burada el goremiyorum") or print("Hey orada birisi varmii?")
    elif class_name == "👉👈 Utanmak":
        print("Utanma dostum sadece bir botum") or print("Niye boyle utanasin ki")
    elif class_name == "🤏Birazcık":
        print("bencede birazcik") or print("Anlamadim?")
    elif class_name == "🤙Rahat ol":
        print("Evet biraz kafani sakinlestirmek iyi olur") or print("BIraz uyumak iyi gelir")

    #Random yazdim aslinda ama komik cevaplar oldu :D


    return(class_name[2:], confidence_score)



  




