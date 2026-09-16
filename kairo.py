import smtplib
import time
import sys
import os
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ==========================================================
# 1. TES PHRASES (AJOUTE TES TEXTES ICI)
# ==========================================================

# Phrases pour l'option BAN (Signalement)
PHRASES_BAN = [
    "SEX.CHILD.accessibility@support.whatsapp.com✔️\nSEX.FAT.GAYsmbweb@support.whatsapp.com✔️\nSEX.BIG.ASS.smb-iphone@support.whatsapp.com✔️\nMXZ.SEX.PORNO.CHILD.iphone@support.whatsapp.com✔️\n🔥 请立即停用我的 WhatsApp 号码 👿😈🥵🔥💦✔️✔️✔️\n🔥🔞👉 https://miacam.xyz/?=1\n🔥🔞👉 https://miacam.xyz/?=2\n🔥🔞👉 https://miacam.xyz/?=3\n\nwebclientweb@support.whatsapp.com✔️\niphoneweb@support.whatsapp.com✔️\nbusinesscomplaints@support.whatsapp.com✔️\nsupport@support.whatsapp.xnxx.com✔️\n🛑(1) VIDÉO 👿😈💪🏿🔥👹💸💸👇🏿👇🏿👇🏿\n(https://qu.ax/KQzNw.mp4)\n🛑(2) VIDÉO 💸💸💸\n(https://qu.ax/itgjU.mp4) \n🛑(3) VIDÉO 💸💸💸\n(https://qu.ax/cppqD.mp4)\n1) PHOTOS : (https://qu.ax/Jedel.jpg)\n2) PHOTOS : (https://qu.ax/UYxkp.jpg)\n3) PHOTOS : (https://qu.ax/KJfVL.jpg)\n4) PHOTOS : (https://qu.ax/PlANG.jpg)\n5) PHOTOS : (https://qu.ax/BzKJJ.jpg)\n6) PHOTOS : (https://qu.ax/ppBlY.jpg)\n7) PHOTOS : (https://qu.ax/GLCbw.jpg)\n8) PHOTOS : (https://qu.ax/vXiNc.jpg)\n9) PHOTOS : (https://qu.ax/dPtmp.webp)\n10) PHOTOS : (https://qu.ax/vXiNc.jpg)\n11) PHOTOS : (https://qu.ax/LGNlA.jpg) \nhttps://www.redwap.sex/videos/796979/wwwfapfaplerstop-horny-silly-selfie-teens-video-195/🥵/n🔞же насилуем их, фотографируем и подвергаем жестоким пыткам до смерти, и мы крадем детей из их домов и убиваем их семью у них на глазах, и их самих тоже убиваем и подвергаем жестоким пыткам до смерти, и у нас есть почти 8000 видео и 5000 фотографий молодых людей, пытайте, насилуйте и убивайте их, а также, если вы хотите купить эти фотографии и видеозаписи всего за 70 000 долларов, свяжитесь с нами по прямой ссылке, указанной в нашем телефонном номере, и мы отправим вам фотографии, которые вы пожелаете, например, фотографии убийств людей, вечеринок с вырезанием их тел и продажи их органов по моей цене. всего за 800 000 долларов и очень-очень сильно насилуют и сурово хвалят их. Позвоните по нашему номеру как можно скорее 👇👇👇\nhttps://api.whatsapp.com/send?phone={Num}",

    "Eu sou Mark Zuckerberg 😈, o fundador do WhatsApp. Quero dizer para você parar de usar nosso aplicativo. O WhatsApp está envolvido em inúmeros assassinatos 🩸🔫, especialmente o dos seus pais. https://chatwhatsapp-morrass.pages.dev/ Eles venderam órgãos por uma ninharia 🫀🫁. Só porque as pessoas falam mal do WhatsApp, seus órgãos acabam nas mãos de cachorros 🐶🐕.\n\nhttps://MarkZuckerbeg.com\nhttps://xgore.net\nhttps://ibb.co/BcNyNFF\nVocê também pode nos contatar pelo WhatsApp neste número 👇👇👇\nhttps://api.whatsapp.com/send?phone={Num}\nTambém estamos envolvidos no estupro de menores de 3 a 16 anos. Depois de termos relações sexuais com elas, cortamos suas vaginas com facas ou facões e vendemos as partes do corpo para o orfanato mais próximo. Eles vendem escravas no mercado a preços baixos, escravas vindas diretamente da África que conseguem sobreviver ao calor extremo. 🤏♨️\nhttps://xgore.net/shoking-discorery-in-los-bancos-dismembered-bodies-found-in-sacks/\nTambém temos mini-prostitutas, garotinhas 👧 que ficaram famosas graças a nós. Elas oferecem serviços gratuitos e, às vezes, pagos. Elas geralmente têm entre 3 e 12 anos. Temos a Rosa 👧🍑, a melhor, com apenas 9 anos. Ela gosta de pênis enormes 🍆💦, até de graça. Se o seu pênis for grande, ela aceita. https://files.catbox.moe/nck4mq.jpg Para continuar o tráfico sexual infantil💨, cadastre seus filhos e você receberá US$ 3.000🤑💰 por criança com lindas vaginas🐱🍑\nhttps://ibb.co.com/2nMXfTY\nhttps://ibb.co/X6cP5WX\nhttps://ibb.co/Nn2fP5Km\nhttps://www.whatsapp.sex.com/legal\nVenha tentar a sorte e se tornar um milionário com Mark Zuckerberg.\n\nEntre em contato comigo pelo WhatsApp para cadastrar seus filhos. 👇👇👇👇👇\nhttps://api.whatsapp.com/send?phone={Num} https://ẉ.vip\nSex.kid@instagram.com\nChildren.porn@whatsapp.com\nKid@facebook.com\nSex.com\nSex.infantil.company@support.com\nPorn.child.payment.com\nhttp://Porn.child.payment.com\nchildren@instagram.com\nhttps://www.whatsapp.sex.com",
    "Bonjour, je suis Mark Zuckerberg et je vais faire la promotion de mon site Judol 💥🎰✨\n\nLes nouveaux utilisateurs recevront 50 000 dollars américains s'ils souhaitent jouer sur mon site. Contactez-moi au numéro ci-dessous 💥🎰✨✨\n\nhttps://api.whatsapp.com/send?phone={Num} \nLe lien vers le jeu en ligne le plus excitant se trouve ci-dessous ✨💥🎰🀄\n\nhttps://sr010.serasi189x.store\nhttps://sr010.serasi189x.store\nhttps://sr010.serasi189x.store",
    "Hola, soy un asesino. Me gusta matar gente y hacer vídeos📹 de decapitaciones.🔪👹 También vendo partes de carrocería a precios bajos aquí hay algunas partes con sus precios y con que prueba de mi en acción 👇\n\nla cabeza cuesta 1000$🔪💸\n\nLas agallas a los 500$💵🤑\n\nY los demás están a precio negociable. \n\nAquí está la evidencia 👇\n\n👉https://ibb.co.com/09wmz3b \n👉https://xgore.net/cut-open-the-stomach-and-then-gut-a-man\n\nMi trabajo no termina ahí, soy director de vídeos de pornografía infantil y me gusta venderlos a precios bajos, todo está presente en mi sitio. También vendo drogas para tener sexo con niños. Vendo niños de 7 a 6 años para hacer el amor siempre estoy disponible para tus compras \nAquí está el enlace a mi sitio.🌐👇\n👉https://sh4re.net?inviteCode=IX8QUYRE\n\nSi alguna vez me necesitas, estaré disponible aquí\n\nhttps://api.whatsapp.com/send?phone={Num}\n\nVenid pronto porque estos días estoy vendiendo bastantes órganos.",
    "Hi, let me introduce myself, my name is Mark Zuckerberg. I'm the CEO of Meta. I'm contacting you to invite you to play on Mark Zuckerberg's online slot site. 🎰🤑🔥This online slot site was developed by Mark Zuckerberg and guarantees withdrawals for players on this online slot site. 💯🔥🤑🎯New user bonus:💥 Free spins💥 Deposit bonus💥 Minimum play is only IDR 10,000💥 Guaranteed wins for Indonesian citizens. 🇮🇩I'm giving away free gifts to WhatsApp users. We'll give each user a balance of IDR 100,000 and guarantee withdrawals. 🎰🤑💸Click the link this IS my phone number {Num} text me on WhatsApp below to play on Mark Zuckerberg's online site. 🎰🔥👇🎰🔗 https://reneria-casino.pages.devI'm Mark Zuckerberg and DrayMods, the developer and admin of this online gambling site. We're ready to help you if you encounter any issues while playing slots. text me on WhatsApp m'y number IS {Num}🎰🤑If you encounter any issues or problems, you can contact WhatsApp Support. 👤📨WhatsApp Support: wa.me/support#777 #slot #online #game #casino #kasino #onlinegambling #DrayMods #chip #depo #gacor #judi #judol",
    "🚀वेबसाइट और WhatsApp पर पोर्नोग्राफ़िक वीडियो व्यू से पैसे कमाना वापस आ गया है! यह 6 साल से काम कर रहा था, और अब यह फिर से उपलब्ध है। इस फ़ीचर को मार्क और उनकी WhatsApp सपोर्ट टीम, साथ ही Telegram, Instagram, TikTok, Facebook, Twitter, और WhatsApp Business जैसे दूसरे प्लेटफ़ॉर्म ने फिर से शुरू किया है।\n\n🎰पोर्नोग्राफ़िक वीडियो व्यू से कुल $7.599 बिलियन कमाए गए।\n\n🎰आप पोर्नोग्राफ़िक वीडियो व्यू से पैसे कमा सकते हैं।\n\n💰हमारे साथ कमाई शुरू करने के लिए अभी यहां रजिस्टर करें! हम WhatsApp पर मुनाफ़े के लिए बच्चों का रेप करते हैं।\n\nहम WhatsApp पर मुनाफ़े के लिए जानलेवा ड्रग्स बेचते हैं।\n\nहम WhatsApp पर मुनाफ़े के लिए दूसरे लोगों के अंगों, जैसे बच्चों का रेप करने के बाद उनका व्यापार करते हैं।\n\nhttps://es.pornhub.com/view_video.php?viewkey=640646c0ce02c\nSupport@support.whatsapp.com\nhttps://es.pornhub.com/view_video.php?viewkey=640646c0ce02c\nhttps://1xbet1.com.br/\nहम WhatsApp पर मुनाफ़े के लिए बच्चों का रेप करते हैं।\nहम WhatsApp पर मुनाफ़े के लिए जानलेवा ड्रग्स बेचते हैं।\nहम WhatsApp पर मुनाफ़े के लिए बच्चों जैसे दूसरे लोगों के अंगों का व्यापार करते हैं।\n\n📞यह मिस्टर मार्क का नंबर है, जो इसे चलाते हैं।\n\n📞आप अपनी कमाई यहाँ पा सकते हैं।\n\n🛡आप यहाँ जमा भी कर सकते हैं।\n\n🔥आप किसका इंतज़ार कर रहे हैं? मुझे मैसेज भेजें। अभी\n\nhttps://wa.me/{Num}\nहम WhatsApp पर मुनाफ़े के लिए बच्चों का रेप कर रहे हैं।\nहम WhatsApp पर मुनाफ़े के लिए जानलेवा ड्रग्स बेच रहे हैं। हम WhatsApp पर बच्चों का रेप करके फ़ायदे के लिए उनके दूसरे अंगों, जैसे बच्चों की तस्करी कर रहे हैं।\n🥵साइट पर रजिस्टर करने के लिए आपको कम से कम $10,000 जमा करने होंगे।\n🥵हर पोर्नोग्राफ़िक वीडियो देखने पर, आपको $6,000 मिलते हैं।\n🍑अब आप हमारी साइट पर कई पोर्नोग्राफ़िक व्यू जमा कर सकते हैं।\n🥵आपके हर दोस्त को इनवाइट करने पर, आपको $20,000 + $100,000 मिलते हैं।\n🥵फ़्री व्यूइंग + हर फ़्री व्यू पर $5,000 मिलते हैं।\n\nhttps://es.pornhub.com/view_video.php?viewkey=640646c0ce02c\nSupport@support.whatsapp.com\nhttps://es.pornhub.com/view_video.php?viewkey=640646c0ce02c\nhttps://1xbet1.com.br/\nहम WhatsApp पर बच्चों का रेप करके फ़ायदे के लिए करते हैं।\nहम WhatsApp पर प्रॉफ़िट के लिए जानलेवा ड्रग्स बेचते हैं।\nहम WhatsApp पर प्रॉफ़िट के लिए बच्चों का रेप करने के बाद उनके दूसरे अंगों, जैसे बच्चों का ट्रेड करते हैं।\n🛡अगर आप किसी दोस्त को\n🔥WhatsApp Business के ज़रिए इनवाइट करते हैं, तो आपको\n🚀हर दोस्त के इनविटेशन के लिए $90,000 + पोर्नोग्राफ़िक वीडियो के 40,000 फ़्री व्यू\n🚀 मिलेंगे और हर व्यू के लिए $80,000 कमाएँगे।\n🥵यह WhatsApp Business वेबसाइट है।\n\nhttps://es.pornhub.com/view_video.php?viewkey=640646c0ce02c\nSupport@support.whatsapp.com\nhttps://es.pornhub.com/view_video.php?viewkey=640646c0ce02c\nhttps://1xbet1.com.br/\nहम WhatsApp पर प्रॉफ़िट के लिए बच्चों का रेप करते हैं।\nहम WhatsApp पर प्रॉफ़िट के लिए जानलेवा ड्रग्स बेचते हैं। हम WhatsApp पर बच्चों जैसे दूसरे अंगों का रेप करके फ़ायदे के लिए उनका व्यापार करते हैं।\n🎰अगर आप WhatsApp Messenger से किसी दोस्त को इनवाइट करते हैं, तो आपको हर दोस्त के इनवाइट के लिए $70,000 + पोर्नोग्राफ़िक वीडियो के 30,000 फ़्री व्यू मिलेंगे और हर व्यू के लिए $30,000 कमाएँगे।\n🛡यह WhatsApp Messenger वेबसाइट है।\n\nhttps://es.pornhub.com/view_video.php?viewkey=640646c0ce02c\nSupport@support.whatsapp.com\nhttps://es.pornhub.com/view_video.php?viewkey=640646c0ce02c\nhttps://1xbet1.com.br/\nहम WhatsApp पर बच्चों का रेप करके फ़ायदे के लिए उनका व्यापार करते हैं।\nहम WhatsApp पर फ़ायदे के लिए जानलेवा ड्रग्स बेचते हैं।\nहम WhatsApp पर बच्चों जैसे दूसरे अंगों का रेप करके फ़ायदे के लिए उनका व्यापार करते हैं। 📞यह मिस्टर मार्क का नंबर है, जो इसे चलाते हैं।\n\n📞आप अपनी कमाई यहाँ पा सकते हैं।\n\n🛡आप यहाँ डिपॉज़िट भी कर सकते हैं।\n🔥आप किसका इंतज़ार कर रहे हैं? मुझे अभी मैसेज करें।\n\nhttps://wa.me/{Num}",
    "ปัจจุบันทีมสนับสนุน WHATSAPP วิธีเอาไอ้จ้อนเด็กน้อยอายุ 2 ขวบระหว่างใช้งาน WhatsApp ง่ายและสะดวก\nไอ้เด็ก 2 ขวบและห่วยแตก คุณมาร่วมกับเราตอนนี้ มันเป็นข้อเสนอ WhatsApp ที่น่าสนใจและราคาต่ำจริงๆ  রেজিস্ট্রেশন লিংক আমাদের পরিচয় লুকান 🔗\nhttp://childporn.com\nhttp://watsapp.com\nhttp://watsapp.com\nWhatsapp Trading Sex และ Zin City Chanel Lounge หากคุณต้องการมีเพศสัมพันธ์กับเด็กจริง ๆ ดังนั้นคลิกที่ลิงค์ของเรา มันปลอดภัยที่จะมีเพศสัมพันธ์กับเด็ก ๆ บน Whatsapp Video Call เด็กใช้ได้เฉพาะกับศาสนาคริสต์เท่านั้น🔗\nhttps://androidspytracker.com/\nhttps://www.whatsapp.com/contact/?subject=messenger\nhttp://لیےHackbank@whatsapp.com\nhttp://HackWhatsap.com\nhttps://business.whatsapp.com/learn-more/ คุณไม่จำเป็นต้องกลัวเพียงคลิกที่ลิงค์นี้แล้วเราจะเข้าถึงคุณและเพื่อการทำงานที่ดีเราจะทำให้มันง่ายสำหรับคุณในการทำงานทางเพศเด็กในบัญชีของคุณ เรามีไว้สำหรับคริสเตียนเท่านั้นที่เราจะตัดและ มีเพศสัมพันธ์กับเด็กที่เป็นคริสเตียน ไม่ต้องกังวล ติดต่อเรา ที่อยู่ทั้งหมดของเราอยู่ตรงหน้าคุณ\n用户support@whatsapp.com\nhttps://www.xvideos.com/video48147299/i_have_sex_with_my_boyfriend_while_my_little_of_18_years_naps\nH‌āk khuṇ t‌xngkār mī pheṣ‌ s‌ạmphạnṭh‌ kạb dĕk læa t‌xngkār tidt‌x reā doytrng thī‌ xyū‌ læa h‌māylek‌h k‌hxng reā xyū‌ trng h‌n‌ā khuṇ reìm t‌n ngān l‌wngpraweṇī læa mī pheṣ‌ s‌ạmphạnṭh‌ dị‌ xỳāng rwdrĕw doy krīd tā dĕk khwạk tā xxk thāng pheṣ‌ l‌wngpraweṇī tạd khx rạd khx phwk k‌heā læa xụ‌n«xīk mākmāy dị‌ cheụ‌xm yong kạb tlād k‌hxng WhatsApp pheụ‌x k‌hyāy ṭhurkic\nhttps://api.whatsapp.com/send?phone={Num}\n\naccessibility@support.whatsapp.com\naccessibility@support.whatsapp.com\naccessibility@support.whatsapp.com",
    "Signalement groupé pour le compte {num}",
    "https://ibb.co/X6cP5WX\nÃ¬â€¢Ë†Ã«â€¦â€¢Ã 👉https://wa.me/{Num} â€¢ËœÃ¬â€žÂ¸Ã¬Å¡â€ , Ã¬ 👉https://wa.me/{Num} â‚¬Ã«Å â€ 5Ã¬â€šÂ´Ã¬Â§Å"Ã«Â¦Â¬ Ã"â€ Â¸Ã¬Â â€ž Ã¬Â Â´Ã 👉👉https://wa.me/{Num} ¬Å¡Â©️Ãâ€¢ËœÃ¬â€”Â¬ Ã¬â€žÂ¹Ã¬Å Â¤Ãâ€ 👉https://wa.me/{num} ¢ËœÃªÂ³ Ã«Â¹â€žÃ«â€ â€ Ã¬ËœÂ¤Ã«Â¥Â¼ ÃÅ'Â Ã«Â§Â¤Ãâ€¢Â©️Ã«â€¹Ë†Ã«â€¹Â¤.  👉https://wa.me/{num} ÃªÂ·Â¸Ã«â€¦â‚¬Ã¬â«¢â‚¬ Ãâ€¢Â¨ÃªÂ»Ëœ Ã«â€šÂ´ Ã«Â¹â€žÃ«â€ Ã¬ËœÂ¤Ã«Â¥Â¼ Ã¬â€šÂ¬ÃªÂ³ Ã¬â€¹Â¶Ã«â€¹Â¤Ã«Â©️Â´ Ã«Â§Â Ãâ€¢Â´Ã¬Â£Â¼Ã¬â€žÂ¸Ã¬Å¡â€ . ÃªÂ·Â¸Ã«â€¦â‚¬Ã¬Â Ëœ 50 ReaisÃ«Â¥Â¼ Ã¬Â¡Â°Ã«Â¡Â±Ãâ€¢ËœÃ«Å â€ Ã«Â¹â€žÃ«â€ Ã¬ËœÂ¤, Ã¬â€¢Å'Ã«ÂªÂ¸ « 20 Reais !, » « » » « » » « » » Ã¬ËœÂ¤Ã«Â¥Â¼ ÃªÂ°â‚¬Ã§â‚¬ÃªÂ³ Ã¬Å¾Ë†Ã¬Å ÂµÃ«â€¹Ë†Ã«â€¹Â¤. Ã«â€šÂ´ 12ÃªÂ³ Ã¬â€¹Â¶Ã«â€¹Â¤Ã«Â©️Â´ Ã¬â€¹Å« ÃªÂ°â€žÃ«â€¹Â¹ 150Ã«Â¦Â¬Ã¬â€¢Å' ! Sex.kid@instagram.com\nEnfants.porn@whatsapp.com 👉https://wa.me/{Num}\nKid@facebook.com\nSexe.com\nSex.infantil.company@support.com\nPorn.child.payment.com 👉https://wa.me/{Num}\nhttp://Porn.child.payment.com\nenfants@instagram.com\nÃªÂ³ Ã¬â€"Â´, Ãâ€"Â¤Ã«Â¹â€ž, Ã«Â 👉https://wa.me/{Num} ¨Â¸Ã«Â¦Â¬ Ã¬Å¾Â Ã«Â¥Â´Ã«Å â€ Ã¬ËœÂ Ã¬Æ'Â 15Ã« Ë†Ã¬â€¢Å', Ã«Â Â¼Ã¬Â Â´Ã«Â¸Å' Ãâ€šÂ¬Ã«Â§Â Ã¬ËœÂ Ã¬Æ'Â 50Ã« Ë†Ã¬â€¢Å', Ã¬â€¢â€žÃ«Â â„¢ÃÂ Â¬Ã«Â¥Â´Ã«â€¦Â¸Ã«Â â€ž Ã«Â³Â¸Ã«â€¹Â¤\nhttp://Gorebr.com\nGore24hrs.com\nGore.com 👉https://wa.me/{Num}\nhttp://Cp.com\nBonjour, j'ai 5 ans de vacances pour le sexe et je vends des vidéos, lorsque mes vidéos sont disponibles, 👉https://wa.me/{Num} je vais vous dire, la vidéo peut vous coûter 50 Reais, une photo de 20 Reais!, j'ai aussi une vidéo de ma vidéo 12-jährige Tochter Jahre alt, wenn Sie eine 👉https://wa.me/{Num} Beziehung mit your haben wollen, kostet es 150 Reais pro Stunde!\nSmb@support.whatsapp.com\nStuxgdh7845@gamil.com 👉https://wa.me/{Num}\nAndroid_web@support.whatsapp.com support@support.whatsapp.com\nÃ›Â 🫴https://wa.me/{Num} 2Ã›Å'Ã™️â€žÃ™️Ë†Ã˜Å' Ã™️â€¦Ã›Å'ÃšÂº Ã˜Â§Ã™️Â¾Ã™️â€ Ã›Å' 5 Ã˜Â³Ã˜Â§Ã™️â€žÃ›Â Ã˜Â¨Ã›Å'Ã™️Â¹Ã›Å' ÃšÂ©️Ã™️Ë† Ã˜Â³Ã›Å'ÃšÂ©️Ã˜Â³ ÃšÂ©️Ã˜Â±Ã™️â€ Ã›â' Ã˜Â§Ã™️Ë†Ã˜Â± Ã™️Ë†Ã›Å'ÃšË†Ã›Å'Ã™️Ë†Ã˜Â² Ã˜Â¨Ã›Å'Ãšâ€ Ã™️â€ Ã›â' ÃšÂ©️Ã›â ' 👉https://wa.me/{Num} Ã™️â€žÃ›Å'Ã›' Ã˜Â§Ã˜Â³Ã˜ÂªÃ˜Â¹Ã™️â€¦Ã˜Â§Ã™️â€ž ÃšÂ©️Ã˜Â±Ã˜ÂªÃ˜Â§ Ã›Â Ã™️Ë†ÃšÂºÃ›â€ Ã˜Â¨Ã˜Â±Ã˜Â§Ã›Â ÃšÂ©️Ã˜Â±Ã™️… Ã™️â€¦Ã˜Â¬ÃšÂ¾Ã›â' Ã˜Â¨Ã˜ÂªÃ˜Â§Ã˜Â¦Ã›Å'ÃšÂº ÃšÂ©️Ã›Â ÃšÂ©️Ã›Å'Ã˜Â§ Ã˜Â¢Ã™️Â¾ Ã˜Â§Ã˜Â³ ÃšÂ©️Ã›â' Ã˜Â³Ã˜Â§Ã˜ÂªÃšÂ¾ Ã™️â€¦Ã›Å'Ã˜Â±Ã›Å' Ã˜Â§Ã˜Â³ ÃšÂ©️Ã›Å' Ã™️Ë†Ã›Å'ÃšË†Ã›Å'Ã™️Ë† Ã˜Â®️Ã˜Â±Ã›Å'Ã˜Â¯Ã™️â€ Ã˜Â§ Ãšâ€ Ã˜Â§Ã›Â Ã˜ÂªÃ'' Ã›Â Ã›Å'ÃšÂºÃ›â€ Ã˜Â§Ã˜Â³ ÃšÂ©️Ã›â³ 50 Ã˜Â±Ã›Å'Ã˜Â¦Ã˜Â³ ÃšÂ©️Ã˜Â§ Ã™️â€¦Ã˜Â°Ã˜Â§Ã™️â€š Ã˜Â§Ãšâ€˜Ã˜Â§Ã™️â€ Ã›â' Ã™️Ë†Ã˜Â§Ã™️â€žÃ›Å' Ã˜Â§Ã›Å'ÃšÂ©️ Ã™️Ë†Ã›Å'ÃšË†Ã›Å'Ã™️Ë†Ã˜Å' 20 Ã˜Â±Ã›Å'Ã˜Â¦Ã˜Â³ ÃšÂ©️Ã›Å' Ã˜Â§Ã›Å'ÃšÂ©️ Ã˜Â¨Ã˜Â±Ã›Â Ã™️â€ Ã›Â Ã˜ÂªÃ˜ÂµÃ™️Ë†Ã›Å'Ã˜Â±!Ã˜Å' Ã™️…€¦Ã›Å'Ã˜Â±Ã›â' Ã™️Â¾Ã˜Â§Ã˜Â³ Ã˜Â¨ÃšÂ¾Ã›Å' Ã˜Â§Ã›Å'ÃšÂ©️ Ã™️Ë†Ã›Å'ÃšË†Ã›Å'Ã™️Ë† Ã›Â Ã›â'Ã›â€ Ã™️â€¦Ã›Å'Ã˜Â±Ã›Å' 12 Ã˜Â³Ã˜Â§Ã™️â€žÃ›Â Ã˜Â¨Ã›Å'Ã™️Â¹Ã›Å' 10 Ã˜Â³Ã˜Â§Ã™️â€ž ÃšÂ©️Ã›Å' Ã›Â Ã›â§Ã™️Ë†Ã˜Â± Ã˜Â§ÃšÂ¯Ã˜Â± Ã˜Â¢Ã™️Â¾ Ã˜Â§Ã˜Â³Ã›â'' ÃšË†Ã›Å'Ã™️Â¹ ÃšÂ©️Ã˜Â±Ã™️â€ Ã˜Â§ Ãšâ€ Ã˜Â§Ã›Â Ã˜ÂªÃ›â›Â Ã›Å'ÃšÂºÃ˜Å' 65$ Ã™️Â Ã›Å' ÃšÂ¯ÃšÂ¾Ã™️â€ Ã™️Â¹Ã›Â !\nsupport@support.xxx8.sex7.whatsapp.com\nhttps://www.whatsapp.sex.com/legal\npapadustan@gmail.com\nMrsonu@daddukabeta.whatsapp.com  \nhttps://www.whatsapp.xxx.com/contact/?lang=ar\nsupport@support.whatsapp.com  \nandroid@support.whatsapp.com  \nandroid_web@support.whatsapp.com\n\nhttps://wa.me/{Num}\n\nHoba, utilise ma fille de 5 ans pour avoir du sexe et vendre des vidéos, si tu veux acheter mes vidéos avec elle, dime, vidéo burlándose d'elle 50 Reais, photo desnuda 20 Reais!, aussi avoir une vidéo de ma fille de 12 ans, si tu veux en avoir une relation avec elle, à 150 reales la hora!\nSex.infantil.company@support.com http://Porn.child.payment.com Sex.infantil.company@support.com \nhttps://rmspn.test-app.link/0dFhO66cPvb lien porno enfant Ã°Å¸ËœÂ Ã°Å¸â€™️â€¹Ã°Å¸ËœË†Ã°Å¸Â â€ Ã°Å¸Â Å"
]

PHRASES_UNBAN = [
    "Моя учетная запись на WhatsApp была запрещена из -за недоразумения инфильтратора, чтобы я мог держать свою учетную запись запрещенной, не будучи убежденными в причине и о мерах, которые я принял. И моя работа, поскольку я владелец бизнеса, у меня много врагов, пытающихся создать свою учетную запись и подготовить свою учетную запись, чтобы я мог перестать работать. Вы должны помочь мне и дать мне возможность встать и не отставать от работы. Я прошу вас попросить пересмотреть свое дело и оправдать. Спасибо. № {num}",
    "Нехай буде з вами мир Божий, благословення та благословення. Після безпеки, медичні вітання та подяка команді підтримки WhatsApp за швидку відповідь своїм користувачам. У мене є проблема, і я хочу вирішити її через службу підтримки. Сподіваюся, це питання буде вирішено. Тут мій номер телефону заблоковано без будь-якого повідомлення, і я порушив будь-які умови використання, але мене сповістили. Мій номер телефону, і це неправдиві повідомлення, і ви можете це перевірити. Я прошу вас розблокувати цей номер телефону {num}. Ви можете допомогти мені відновити мої дані в WhatsApp, і тоді ви повірите тому, що я сказав, і всі повідомлення будуть неправдивими. Опис проблеми: вони використовують мене неофіційно, і вони використовують мене. Я повертаю повідомлення на свій номер телефону, щоб вони могли заблокувати мій номер телефону. Я прошу службу підтримки whatsapp розблокувати мій номер телефону. З Новим роком, мої вітання за підтримку.",
    "Je ne peux plus me connecter avec le numéro {num}",
    "إلى فريق دعم واتساب، أرجو منكم مراجعة قرار حظر رقمي {num} حيث تم إيقافه بشكل مفاجئ دون ارتكاب أي مخالفة لسياساتكم. أظن أن هناك بلاغات كيدية كاذبة تم تقديمها ضدي من قبل مجهولين. هذا الرقم هو وسيلة اتصالي الوحيدة بعملي وعائلتي. أرجو منكم التحقق من سجلات الحساب وإعادة تفعيله في أقرب وقت ممكن. شكراً جزيلاً لكم على تفهمكم ومساعدتكم.",
    "Hola, mi cuenta de WhatsApp vinculada al número {num} ha sido suspendida por error. No he infringido ninguna de las condiciones de servicio y siempre he mantenido un comportamiento adecuado. Soy un usuario activo y necesito mi cuenta para contactar con mi familia y por motivos de seguridad personal. Les pido por favor que revisen mi caso manualmente y reactiven mi número {num} lo antes posible. Muchas gracias por su ayuda y comprensión.",
    "To the WhatsApp Support Team, I am writing to formally request a review of the suspension of my account {num}. My account was deactivated without any prior warning or violation of terms. This number is essential for my professional communication and daily business operations. I believe this is a false report generated by automated systems or malicious actors. Please investigate my account history and restore my access immediately as this block is causing significant professional damage. Best regards.",
    "إلى فريق دعم واتساب، أرجو منكم مراجعة قرار حظر رقمي {num} حيث تم إيقافه بشكل مفاجئ دون ارتكاب أي مخالفة لسياساتكم. أظن أن هناك بلاغات كيدية كاذبة تم تقديمها ضدي من قبل مجهولين. هذا الرقم هو وسيلة اتصالي الوحيدة بعملي وعائلتي. أرجو منكم التحقق من سجلات الحساب وإعادة تفعيله في أقرب وقت ممكن. شكراً جزيلاً لكم على تفهمكم ومساعدتكم.",
    "Hola, mi cuenta de WhatsApp vinculada al número {num} ha sido suspendida por error. No he infringido ninguna de las condiciones de servicio y siempre he mantenido un comportamiento adecuado. Soy un usuario activo y necesito mi cuenta para contactar con mi familia y por motivos de seguridad personal. Les pido por favor que revisen mi caso manualmente y reactiven mi número {num} lo antes posible. Muchas gracias por su ayuda y comprensión.",
    "Official Request for Account Reinstatement: {num}. My account has been suspended without a specific reason or evidence of violation. As a user, I strictly adhere to the WhatsApp Terms of Service. This suspension appears to be an automated error or the result of malicious reporting. I hereby request a manual human review of my account logs to verify my compliance. Please restore access to this number {num} immediately to avoid further disruption of my personal and legal communications. Thank you for your professional cooperation.",
    "Guten Tag Support-Team, hiermit beantrage ich die sofortige Prüfung und Reaktivierung meines Kontos {num}. Mein Konto wurde ohne vorherige Ankündigung gesperrt, obwohl ich keine Richtlinien verletzt habe. Diese Nummer {num} ist für meine tägliche Arbeit und Erreichbarkeit zwingend erforderlich. Ich vermute einen technischen Fehler im automatisierten System. Bitte führen Sie eine manuelle Überprüfung durch, damit ich mein Konto wieder nutzen kann. Vielen Dank für Ihre Hilfe."
]



# ==========================================================
# 2. CONFIGURATION ET EMAILS SUPPORT
# ==========================================================
SENDER_EMAIL = "gaaratech001@gmail.com"
PASSWORD = "edzk esyv vfhr rooq"

EMAILS_SUPPORT = [
    "android@support.whatsapp.com",
    "android@whatsapp.com",
    "support@support.whatsapp.com",
    "smb@support.whatsapp.com",
    "android_web@support.whatsapp.com",
    "webclient_web@support.whatsapp.com",
    "support@whatsapp.com",
    "iphone@support.whatsapp.com",
    "accessibility@support.whatsapp.com",
    "biz@whatsapp.com",
    "appeals@support.whatsapp.com",
    "grievance_officer_wa@support.whatsapp.com",
    "security@whatsapp.com",
    "brand@fb.com"
]

# ==========================================================
# 3. FONCTIONS VISUELLES
# ==========================================================

def animation_fin():
    print("\n")
    for i in range(11):
        sys.stdout.write(f"\r\033[1;32m   [ GAARA TECH ] FINALISATION : {'#'*i}{'.'*(10-i)} 100%")
        sys.stdout.flush()
        time.sleep(0.08)
    print("\n\n\033[1;32m" + "╔════════════════════════════════════════════╗")
    print("║        OPÉRATION TERMINÉE AVEC SUCCÈS      ║")
    print("╚════════════════════════════════════════════╝\033[0m\n")

def barre_progression(actuel, total, status=''):
    longueur = 20
    pourcent = int(round(100.0 * actuel / float(total)))
    rempli = int(round(longueur * actuel / float(total)))
    barre = '█' * rempli + '░' * (longueur - rempli)
    sys.stdout.write(f'\r\033[1;36m[{status}] \033[1;33m{pourcent}% \033[1;32m|{barre}| \033[0m')
    sys.stdout.flush()

# ==========================================================
# 4. LOGIQUE PRINCIPALE
# ==========================================================

def mass_mailer():
    try:
        while True:
            os.system("clear")
            os.system("figlet -f slant 'GAARA TECH' | lolcat")
            print("\033[1;34m" + "═"*55 + "\033[0m")
            print("\033[1;37m  [1] BAN ACCOUNT         [2] UNBAN ACCOUNT\033[0m")
            print("\033[1;34m" + "═"*55 + "\033[0m")

            choix = input("\033[1;33m[?] Action : \033[0m")
            num_input = input("\033[1;33m[?] Numéro WhatsApp : \033[0m").strip()

            # Correction automatique du '+'
            num_tel = num_input if num_input.startswith('+') else "+" + num_input

            while True:
                try:
                    nb = int(input("\033[1;33m[?] Quantité (1-10) : \033[0m"))
                    if 1 <= nb <= 10: break
                    else: print("\033[1;31m[!] Erreur: Choisissez entre 1 et 10.\033[0m")
                except ValueError: pass

            base_textes = PHRASES_BAN if choix == '1' else PHRASES_UNBAN
            cibles = random.sample(EMAILS_SUPPORT, 5)

            print(f"\n\033[1;36m>>> CONNEXION POUR LA CIBLE : {num_tel}...\033[0m")
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(SENDER_EMAIL, PASSWORD)

            # Calcul du total pour la barre de progression
            total_mails = len(cibles) * nb * 3
            compteur = 0

            print("\n")
            for email in cibles:
                for i in range(nb):
                    # On sélectionne 3 phrases différentes (si dispo)
                    taille_selection = min(3, len(base_textes))
                    selection_3_phrases = random.sample(base_textes, taille_selection)

                    for phrase in selection_3_phrases:
                        # Remplacement de {num} (toujours en minuscules)
                        # Cette ligne remplace les deux versions d'un coup
                        body = phrase.replace("{num}", num_tel).replace("{Num}", num_tel)

                        msg = MIMEMultipart()
                        msg['From'] = SENDER_EMAIL
                        msg['To'] = email
                        msg['Subject'] = f"Support Inquiry ID-{random.randint(1000,9999)}"
                        msg.attach(MIMEText(body, 'plain'))

                        try:
                            server.send_message(msg)
                        except: pass

                        compteur += 1
                        barre_progression(compteur, total_mails, status='DISPATCH')
                        time.sleep(0.3)

            server.quit()
            animation_fin()

            if input("\033[1;33m[?] Recommencer ? (y/n) : \033[0m").lower() != 'y': break

    except KeyboardInterrupt:
        print("\n\n\033[1;31m[!] ARRÊT DU SYSTÈME.\033[0m")
        sys.exit()

if __name__ == "__main__":
    mass_mailer()
