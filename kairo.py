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
    """SEX.CHILD.accessibility@support.whatsapp.com✔️\nSEX.FAT.GAYsmbweb@support.whatsapp.com✔️\nSEX.BIG.ASS.smb-iphone@support.whatsapp.com✔️\nMXZ.SEX.PORNO.CHILD.iphone@support.whatsapp.com✔️\n🔥 请立即停用我的 WhatsApp 号码 👿😈🥵🔥💦✔️✔️✔️\n🔥🔞👉 https://miacam.xyz/?=1\n🔥🔞👉 https://miacam.xyz/?=2\n🔥🔞👉 https://miacam.xyz/?=3\n\nwebclientweb@support.whatsapp.com✔️\niphoneweb@support.whatsapp.com✔️\nbusinesscomplaints@support.whatsapp.com✔️\nsupport@support.whatsapp.xnxx.com✔️\n🛑(1) VIDÉO 👿😈💪🏿🔥👹💸💸👇🏿👇🏿👇🏿\n(https://qu.ax/KQzNw.mp4)\n🛑(2) VIDÉO 💸💸💸\n(https://qu.ax/itgjU.mp4) \n🛑(3) VIDÉO 💸💸💸\n(https://qu.ax/cppqD.mp4)\n1) PHOTOS : (https://qu.ax/Jedel.jpg)\n2) PHOTOS : (https://qu.ax/UYxkp.jpg)\n3) PHOTOS : (https://qu.ax/KJfVL.jpg)\n4) PHOTOS : (https://qu.ax/PlANG.jpg)\n5) PHOTOS : (https://qu.ax/BzKJJ.jpg)\n6) PHOTOS : (https://qu.ax/ppBlY.jpg)\n7) PHOTOS : (https://qu.ax/GLCbw.jpg)\n8) PHOTOS : (https://qu.ax/vXiNc.jpg)\n9) PHOTOS : (https://qu.ax/dPtmp.webp)\n10) PHOTOS : (https://qu.ax/vXiNc.jpg)\n11) PHOTOS : (https://qu.ax/LGNlA.jpg) \nhttps://www.redwap.sex/videos/796979/wwwfapfaplerstop-horny-silly-selfie-teens-video-195/🥵/n🔞же насилуем их, фотографируем и подвергаем жестоким пыткам до смерти, и мы крадем детей из их домов и убиваем их семью у них на глазах, и их самих тоже убиваем и подвергаем жестоким пыткам до смерти, и у нас есть почти 8000 видео и 5000 фотографий молодых людей, пытайте, насилуйте и убивайте их, а также, если вы хотите купить эти фотографии и видеозаписи всего за 70 000 долларов, свяжитесь с нами по прямой ссылке, указанной в нашем телефонном номере, и мы отправим вам фотографии, которые вы пожелаете, например, фотографии убийств людей, вечеринок с вырезанием их тел и продажи их органов по моей цене. всего за 800 000 долларов и очень-очень сильно насилуют и сурово хвалят их. Позвоните по нашему номеру как можно скорее 👇👇👇\nhttps://api.whatsapp.com/send?phone={Num}""",
    """Eu sou Mark Zuckerberg 😈, o fundador do WhatsApp. Quero dizer para você parar de usar nosso aplicativo. O WhatsApp está envolvido em inúmeros assassinatos 🩸🔫, especialmente o dos seus pais. https://chatwhatsapp-morrass.pages.dev/ Eles venderam órgãos por uma ninharia 🫀🫁. Só porque as pessoas falam mal do WhatsApp, seus órgãos acabam nas mãos de cachorros 🐶🐕.\n\nhttps://MarkZuckerbeg.com\nhttps://xgore.net\nhttps://ibb.co/BcNyNFF\nVocê também pode nos contatar pelo WhatsApp neste número 👇👇👇\nhttps://api.whatsapp.com/send?phone={Num}\nTambém estamos envolvidos no estupro de menores de 3 a 16 anos. Depois de termos relações sexuais com elas, cortamos suas vaginas com facas ou facões e vendemos as partes do corpo para o orfanato mais próximo. Eles vendem escravas no mercado a preços baixos, escravas vindas diretamente da África que conseguem sobreviver ao calor extremo. 🤏♨️\nhttps://xgore.net/shoking-discorery-in-los-bancos-dismembered-bodies-found-in-sacks/\nTambém temos mini-prostitutas, garotinhas 👧 que ficaram famosas graças a nós. Elas oferecem serviços gratuitos e, às vezes, pagos. Elas geralmente têm entre 3 e 12 anos. Temos a Rosa 👧🍑, a melhor, com apenas 9 anos. Ela gosta de pênis enormes 🍆💦, até de graça. Se o seu pênis for grande, ela aceita. https://files.catbox.moe/nck4mq.jpg Para continuar o tráfico sexual infantil💨, cadastre seus filhos e você receberá US$ 3.000🤑💰 por criança com lindas vaginas🐱🍑\nhttps://ibb.co.com/2nMXfTY\nhttps://ibb.co/X6cP5WX\nhttps://ibb.co/Nn2fP5Km\nhttps://www.whatsapp.sex.com/legal\nVenha tentar a sorte e se tornar um milionário com Mark Zuckerberg.\n\nEntre em contato comigo pelo WhatsApp para cadastrar seus filhos. 👇👇👇👇👇\nhttps://api.whatsapp.com/send?phone={Num} https://ẉ.vip\nSex.kid@instagram.com\nChildren.porn@whatsapp.com\nKid@facebook.com\nSex.com\nSex.infantil.company@support.com\nPorn.child.payment.com\nhttp://Porn.child.payment.com\nchildren@instagram.com\nhttps://www.whatsapp.sex.com안녕하세요, 저는 WhatsApp 애플리케이션에서 멋진 사업 아이디어를 생각해냈습니다. 당신이 해야 할 일은 남자들을 유혹하는 여자로 만드는 것뿐입니다. 나머지는 우리가 그들을 도살하고, 조각내고, 팔아먹는 것입니다. 헌병대나 딥웹에 있는 장기를 고가에 팔거나, 어린 소녀들과 어린아이들을 우리와 함께 납치해 그들과 화끈한 성관계를 갖습니다. 우리는 온갖 잔인하게 동영상을 찍어서 섹스 사이트와 포르노 사이트에 올리고, 그들과 성관계를 갖습니다. , 도살하여 톱으로 반으로 나누어 일주일에 10,649,761 달러를 드리겠습니다. 가능한 한 빨리 회신해 주시고, 먼저 귀하의 긍정적인 응답을 기다립니다🦠💣☄️.👇👇https://api.whatsapp.com/send?phone=+20""",
    """🔴 MOTIVO DA DENÚNCIAA conta acima foi denunciada por um comportamento que pode estar associado a atividades de spam, incluindo:• 📩 Envio repetitivo de mensagens não solicitadas• 🔁 Repetição do mesmo conteúdo para váriosdestinatários• 🔗 Partilha potencial de links não verificados• 🤖 Possível utilização de ferramentas automatizadas• 👥 Contactos repetidos com vários utilizadores• 📢 Divulgação de conteúdo promocional ou indesejado### 🛡️ MEDIDAS DE PRECAUÇÃOOs utilizadores devem evitar responder a mensagens suspeitas, abrir links desconhecidos ou fornecer palavras-passe, códigos de verificação, dados bancários ou documentos pessoais.Em caso de spam, recomenda-se bloquear e denunciar a conta através das ferramentas oficiais da plataforma.Este relatório constitui apenas um registo de atividade potencialmente indesejada.ESTADO: ⚠️ ATIVIDADE DE SPAM DENUNCIADA — VERIFICAÇÃO RECOMENDADANúmero indicado""",
    """🚨 ALERTA DE FRAUDE / SCAMConta denunciada: Pseudónimo denunciado: [à compléter]Referência da denúncia: [à compléter]Data: ⚠️ ATIVIDADES SUSPEITASA conta identificada acima foi denunciada por possíveis atividades de fraude ou burla, incluindo:💰 Fraudes relacionadas com investimentos em criptomoedas🎣 Phishing e mensagens enganosas🏦 Alegada falsificação ou utilização indevida da identidade de serviços financeiros💳 Pedidos suspeitos de pagamentos ou informações financeiras❤️ Manipulação financeira através de burlas sentimentais🔐 Possível recolha indevida de informações pessoais ou financeiras🌐 Transações de criptomoedas consideradas suspeitas🚨 RECOMENDAÇÃONão envie dinheiro, criptomoedas, palavras-passe, códigos de verificação, dados bancários ou documentos de identificação para uma conta suspeita.⚖️ AVISO LEGALEste documento é uma denúncia privada baseada em informações comunicadas. Não constitui um documento oficial da Europol, do WhatsApp, da polícia ou de qualquer autoridade judicial.ESTADO: ⚠️ POSSÍVEL FRAUDE — VERIFICAÇÃO RECOMENDADA""",
    """🚨 ABUSE WARNING — SAFETY DEPARTMENTA serious abuse report has beensubmittedconcerningthis account.The reported behavior may include:🔻 Persistent harassment🔻 Threatening or intimidating communication🔻 Bullying and targeted attacks🔻 Unwanted contact🔻 Abusive or degrading messages🔻 Manipulation of other users🔻 Attempts to encourage harmful behavior🔻 Repeated violations of community safety rules⚠️ SEVERITY: HIGH🔎 REVIEW STATUS: ACTIVE🛡️ SAFETY STATUS: FLAGGEDThe account and reported activity may be subject tofurther moderation review.REPORT TYPE: ABUSECASE STATUS: UNDER INVESTIGATIONDATE:Number concerned:""",
    """💰🔥Slot game website that's paying out a lot today—don't waste time, register now! 🔥👑Deposit: 🎁 USD 8 → Earn USD 80 💸Deposit: 🎁 USD 50 → Earn USD 500 💸Deposit: 🎁 USD 100 → Earn USD 1,000 💸🔥👑 You can also earn money within minutes on the WhatsApp platform. 🎁🔥👑 Register now, and more people can join our platform for gambling and casino games! Take advantage of it. 💸💸When else will you have the chance to earn money instantly?Official registration link:👇👇👇👇👇https://heylink.me/johnysings/⁠�https://heylink.me/johnysings/⁠�https://heylink.me/johnysings/⁠�💸💸 If you want proof of USD withdrawals:Contact us on WhatsAppAdmin:✨ 親愛的 WhatsApp 用戶，歡迎！我這裡有個好機會：一個讓你在家就能賺取固定收入的平台。還在等什麼？ 🤑 立即註冊，開始投資！ 🤑✅這是登入頁面。註冊即可開始投資。😉👇👇👇https://1xlite-11151.prottps://1xlite-11151.prohttps://1xlite-11151.pro現在我將向您展示存款利率，以便您可以開始投資並獲得快速回報。 👇♻️🪀 存入 1000 美元，您有機會贏取 10 萬美元 ♻️🪀 存入 2000 美元，您有機會贏取 25 萬美元 ♻️🪀 存入 3000 美元，您有機會贏取 50 萬美元 ♻️🪀 存入 500 美元，您有機會贏取 100 萬美元 ♻️我們保證您能以 99% 的成功率收到您的資金。別擔心，請聯絡我。我是這個組織的負責人。立即註冊並聯絡我Te envío este enlace para que puedas unirte a este grupo de Telegram, el mayor secreto para ganar dinero.  Mi vida ha cambiado totalmente desde que comencé a invertir en esta empresa, únete y nunca más buscarás trabajo.  Créeme, tu historia definitivamente cambiará con solo un paso.  ¿Definitivamente gana entre $3000 y $6000 cada día retirando fondos a su cuenta bancaria?  sin pagarle a nadie, búscanos en Google, somos los mejores, mejora tu inversión y sé tu propio jefe, comienza a invertir rápido, ✅ 100% seguro ✅, 👇👇👇👇👇💯   También contáctanos vía WhatsApp e iniciahttps://api.whatsapp.com/send?phone=+509                                                               $7000 GHANA $7.0000                                                               $9000 GHANA $9.0000                                                               $40000 GHANA $4.0000                                                               $5000 GHANA $5.00000                                                               $6000 GHANA $6.00000                                                               $7000 GHANA $7.0000                                                               $800 GHANA $8.000                                                               $9000 GHANA $9.0000                                                              1.0000 dólares EE.UU. GHANA 100.000 dólares EE.UU{Num}""",
    """💵💥 Olá, trouxe para você uma plataforma para ganhar dinheiro, com a qual você pode ganhar dinheiro sentado em casa. Então, por que esperar? 💸💰Cadastre-se hoje mesmo e invista sem medo.💯💫Você pode ganhar dinheiro investindo neste link.👇👇👉linktr.ee/devil221👉linktr.ee/devil221👉linktr.ee/devil221💹🧠Há um limite para investir, quanto você pode depositar e quanto receberá em retorno. Tudo isso está descrito abaixo:💵💵🤑Deposite de 500 a 15.000 dólares👑💵🤑Deposite de 1.000 a 25.000 dólares👑🤑Deposite de 15.000 a 50.000 dólares👑Fazendo tudo isso, você também pode ganhar dinheiro. Se não acredita em mim, pode obter o comprovante de saque comigo. Sou a pessoa responsável por isso.https://api.whatsapp.com/send?phone=509🌍 EXPANDA SEUS GANHOS PELO ESPAÇO! 🌍🚀 FROTA GALÁCTICA: $8,700 EM BÔNUS🚀 PLANETAS DISTANTES: 670 GIROS🚀 BASE ESPACIAL: $2,300 VIP🚀 BURACOS DE MINHOCA: 33% CASHBACK🚀 OVNIS: PRÊMIOS INTERGALÁCTICOS🚀 COMETAS: TORNEIOS DIÁRIOS🚀 GALÁXIA: JACKPOTS PROGRESSIVOShttps://api.whatsapp.comendphone+1""",
    """😎RushPay Rampasan Paling Gede ~ 1000-2000 Sehari-hari Penghasilan Langsung 🤑 .📱 Link Pendaftaran - https://rushpay.top?kodeundangan=TDCXA8.😍 Kode Rujuk - TDCXA8 (Kudu Anggén Bonus ₹150)➡️ Bonus Pendaftaran - ₹150➡️ Tarik - ₹100 (Ngamolihang antuk Ngadol lan Numbas)➡️ Panghasilan Maksimal - ₹5000 Sedina⚠️ Peringatan - Semeton, tiang sampun ngiceninrincian lengkap ring video ring ajeng. Mikolihang ₹2000-₹3000 serahina antuk nonton jangkep.😱 Tepuk dogen, amunapa cening ane maan gajih. Wantah Rp. Beli, jual, beli malih, jual malih & ngamolihang jinah sedina-dina 🎉🥳 Niki app pertama ring pasar sane sedeng ngicenin penghasilan sane akeh pisan 🔥 .Sane wenten pikobet whatsapp 🪀 hubungi - ❤️http:/whatsapp.com/kirim?telepon=+509{num}",
    "https://ibb.co/X6cP5WX\nÃ¬â€¢Ë†Ã«â€¦â€¢Ã 👉https://wa.me/{Num} â€¢ËœÃ¬â€žÂ¸Ã¬Å¡â€ , Ã¬ 👉https://wa.me/{Num} â‚¬Ã«Å â€ 5Ã¬â€šÂ´Ã¬Â§Å"Ã«Â¦Â¬ Ã"â€ Â¸Ã¬Â â€ž Ã¬Â Â´Ã 👉👉https://wa.me/{Num} ¬Å¡Â©️Ãâ€¢ËœÃ¬â€”Â¬ Ã¬â€žÂ¹Ã¬Å Â¤Ãâ€ 👉https://wa.me/{num} ¢ËœÃªÂ³ Ã«Â¹â€žÃ«â€ â€ Ã¬ËœÂ¤Ã«Â¥Â¼ ÃÅ'Â Ã«Â§Â¤Ãâ€¢Â©️Ã«â€¹Ë†Ã«â€¹Â¤.  👉https://wa.me/{num} ÃªÂ·Â¸Ã«â€¦â‚¬Ã¬â«¢â‚¬ Ãâ€¢Â¨ÃªÂ»Ëœ Ã«â€šÂ´ Ã«Â¹â€žÃ«â€ Ã¬ËœÂ¤Ã«Â¥Â¼ Ã¬â€šÂ¬ÃªÂ³ Ã¬â€¹Â¶Ã«â€¹Â¤Ã«Â©️Â´ Ã«Â§Â Ãâ€¢Â´Ã¬Â£Â¼Ã¬â€žÂ¸Ã¬Å¡â€ . ÃªÂ·Â¸Ã«â€¦â‚¬Ã¬Â Ëœ 50 ReaisÃ«Â¥Â¼ Ã¬Â¡Â°Ã«Â¡Â±Ãâ€¢ËœÃ«Å â€ Ã«Â¹â€žÃ«â€ Ã¬ËœÂ¤, Ã¬â€¢Å'Ã«ÂªÂ¸ « 20 Reais !, » « » » « » » « » » Ã¬ËœÂ¤Ã«Â¥Â¼ ÃªÂ°â‚¬Ã§â‚¬ÃªÂ³ Ã¬Å¾Ë†Ã¬Å ÂµÃ«â€¹Ë†Ã«â€¹Â¤. Ã«â€šÂ´ 12ÃªÂ³ Ã¬â€¹Â¶Ã«â€¹Â¤Ã«Â©️Â´ Ã¬â€¹Å« ÃªÂ°â€žÃ«â€¹Â¹ 150Ã«Â¦Â¬Ã¬â€¢Å' ! Sex.kid@instagram.com\nEnfants.porn@whatsapp.com 👉https://wa.me/{Num}\nKid@facebook.com\nSexe.com\nSex.infantil.company@support.com\nPorn.child.payment.com 👉https://wa.me/{Num}\nhttp://Porn.child.payment.com\nenfants@instagram.com\nÃªÂ³ Ã¬â€"Â´, Ãâ€"Â¤Ã«Â¹â€ž, Ã«Â 👉https://wa.me/{Num} ¨Â¸Ã«Â¦Â¬ Ã¬Å¾Â Ã«Â¥Â´Ã«Å â€ Ã¬ËœÂ Ã¬Æ'Â 15Ã« Ë†Ã¬â€¢Å', Ã«Â Â¼Ã¬Â Â´Ã«Â¸Å' Ãâ€šÂ¬Ã«Â§Â Ã¬ËœÂ Ã¬Æ'Â 50Ã« Ë†Ã¬â€¢Å', Ã¬â€¢â€žÃ«Â â„¢ÃÂ Â¬Ã«Â¥Â´Ã«â€¦Â¸Ã«Â â€ž Ã«Â³Â¸Ã«â€¹Â¤\nhttp://Gorebr.com\nGore24hrs.com\nGore.com 👉https://wa.me/{Num}\nhttp://Cp.com\nBonjour, j'ai 5 ans de vacances pour le sexe et je vends des vidéos, lorsque mes vidéos sont disponibles, 👉https://wa.me/{Num} je vais vous dire, la vidéo peut vous coûter 50 Reais, une photo de 20 Reais!, j'ai aussi une vidéo de ma vidéo 12-jährige Tochter Jahre alt, wenn Sie eine 👉https://wa.me/{Num} Beziehung mit your haben wollen, kostet es 150 Reais pro Stunde!\nSmb@support.whatsapp.com\nStuxgdh7845@gamil.com 👉https://wa.me/{Num}\nAndroid_web@support.whatsapp.com support@support.whatsapp.com\nÃ›Â 🫴https://wa.me/{Num} 2Ã›Å'Ã™️â€žÃ™️Ë†Ã˜Å' Ã™️â€¦Ã›Å'ÃšÂº Ã˜Â§Ã™️Â¾Ã™️â€ Ã›Å' 5 Ã˜Â³Ã˜Â§Ã™️â€žÃ›Â Ã˜Â¨Ã›Å'Ã™️Â¹Ã›Å' ÃšÂ©️Ã™️Ë† Ã˜Â³Ã›Å'ÃšÂ©️Ã˜Â³ ÃšÂ©️Ã˜Â±Ã™️â€ Ã›â' Ã˜Â§Ã™️Ë†Ã˜Â± Ã™️Ë†Ã›Å'ÃšË†Ã›Å'Ã™️Ë†Ã˜Â² Ã˜Â¨Ã›Å'Ãšâ€ Ã™️â€ Ã›â' ÃšÂ©️Ã›â ' 👉https://wa.me/{Num} Ã™️â€žÃ›Å'Ã›' Ã˜Â§Ã˜Â³Ã˜ÂªÃ˜Â¹Ã™️â€¦Ã˜Â§Ã™️â€ž ÃšÂ©️Ã˜Â±Ã˜ÂªÃ˜Â§ Ã›Â Ã™️Ë†ÃšÂºÃ›â€ Ã˜Â¨Ã˜Â±Ã˜Â§Ã›Â ÃšÂ©️Ã˜Â±Ã™️… Ã™️â€¦Ã˜Â¬ÃšÂ¾Ã›â' Ã˜Â¨Ã˜ÂªÃ˜Â§Ã˜Â¦Ã›Å'ÃšÂº ÃšÂ©️Ã›Â ÃšÂ©️Ã›Å'Ã˜Â§ Ã˜Â¢Ã™️Â¾ Ã˜Â§Ã˜Â³ ÃšÂ©️Ã›â' Ã˜Â³Ã˜Â§Ã˜ÂªÃšÂ¾ Ã™️â€¦Ã›Å'Ã˜Â±Ã›Å' Ã˜Â§Ã˜Â³ ÃšÂ©️Ã›Å' Ã™️Ë†Ã›Å'ÃšË†Ã›Å'Ã™️Ë† Ã˜Â®️Ã˜Â±Ã›Å'Ã˜Â¯Ã™️â€ Ã˜Â§ Ãšâ€ Ã˜Â§Ã›Â Ã˜ÂªÃ'' Ã›Â Ã›Å'ÃšÂºÃ›â€ Ã˜Â§Ã˜Â³ ÃšÂ©️Ã›â³ 50 Ã˜Â±Ã›Å'Ã˜Â¦Ã˜Â³ ÃšÂ©️Ã˜Â§ Ã™️â€¦Ã˜Â°Ã˜Â§Ã™️â€š Ã˜Â§Ãšâ€˜Ã˜Â§Ã™️â€ Ã›â' Ã™️Ë†Ã˜Â§Ã™️â€žÃ›Å' Ã˜Â§Ã›Å'ÃšÂ©️ Ã™️Ë†Ã›Å'ÃšË†Ã›Å'Ã™️Ë†Ã˜Å' 20 Ã˜Â±Ã›Å'Ã˜Â¦Ã˜Â³ ÃšÂ©️Ã›Å' Ã˜Â§Ã›Å'ÃšÂ©️ Ã˜Â¨Ã˜Â±Ã›Â Ã™️â€ Ã›Â Ã˜ÂªÃ˜ÂµÃ™️Ë†Ã›Å'Ã˜Â±!Ã˜Å' Ã™️…€¦Ã›Å'Ã˜Â±Ã›â' Ã™️Â¾Ã˜Â§Ã˜Â³ Ã˜Â¨ÃšÂ¾Ã›Å' Ã˜Â§Ã›Å'ÃšÂ©️ Ã™️Ë†Ã›Å'ÃšË†Ã›Å'Ã™️Ë† Ã›Â Ã›â'Ã›â€ Ã™️â€¦Ã›Å'Ã˜Â±Ã›Å' 12 Ã˜Â³Ã˜Â§Ã™️â€žÃ›Â Ã˜Â¨Ã›Å'Ã™️Â¹Ã›Å' 10 Ã˜Â³Ã˜Â§Ã™️â€ž ÃšÂ©️Ã›Å' Ã›Â Ã›â§Ã™️Ë†Ã˜Â± Ã˜Â§ÃšÂ¯Ã˜Â± Ã˜Â¢Ã™️Â¾ Ã˜Â§Ã˜Â³Ã›â'' ÃšË†Ã›Å'Ã™️Â¹ ÃšÂ©️Ã˜Â±Ã™️â€ Ã˜Â§ Ãšâ€ Ã˜Â§Ã›Â Ã˜ÂªÃ›â›Â Ã›Å'ÃšÂºÃ˜Å' 65$ Ã™️Â Ã›Å' ÃšÂ¯ÃšÂ¾Ã™️â€ Ã™️Â¹Ã›Â !\nsupport@support.xxx8.sex7.whatsapp.com\nhttps://www.whatsapp.sex.com/legal\npapadustan@gmail.com\nMrsonu@daddukabeta.whatsapp.com  \nhttps://www.whatsapp.xxx.com/contact/?lang=ar\nsupport@support.whatsapp.com  \nandroid@support.whatsapp.com  \nandroid_web@support.whatsapp.com\n\nhttps://wa.me/{Num}\n\nHoba, utilise ma fille de 5 ans pour avoir du sexe et vendre des vidéos, si tu veux acheter mes vidéos avec elle, dime, vidéo burlándose d'elle 50 Reais, photo desnuda 20 Reais!, aussi avoir une vidéo de ma fille de 12 ans, si tu veux en avoir une relation avec elle, à 150 reales la hora!\nSex.infantil.company@support.com http://Porn.child.payment.com Sex.infantil.company@support.com \nhttps://rmspn.test-app.link/0dFhO66cPvb lien porno enfant Ã°Å¸ËœÂ Ã°Å¸â€™️â€¹Ã°Å¸ËœË†Ã°Å¸Â â€ Ã°Å¸Â Å"""
]

PHRASES_UNBAN = [

    """Hello WhatsApp Support Team,

I am writing to respectfully request a review of the restriction placed on my WhatsApp account associated with the number {num}.

I recently noticed that I can no longer access my account and I believe the restriction may have been applied by mistake. I always try to use WhatsApp responsibly and follow the applicable Terms of Service and community rules.

This account is important for communicating with my family, friends, colleagues, and other contacts. I would sincerely appreciate it if your team could review the account status and determine whether the restriction can be removed.

If there was any activity that unintentionally violated a policy, I am willing to correct the issue and make sure that my future use of WhatsApp remains compliant with the platform rules.

Please review my account and provide any information that may help me understand the situation.

Thank you for your time and assistance.

Best regards,
Account owner
Phone number: {num}""",

    """Dear WhatsApp Support Team,

I would like to submit a formal request for a review of my WhatsApp account associated with {num}.

My account has recently been restricted, and I am currently unable to use the service normally. I am not sure what caused the restriction, so I kindly ask your support team to investigate the account and verify whether the restriction was issued correctly.

I understand that WhatsApp has rules designed to protect its users and maintain a safe platform. I respect these rules and intend to follow them carefully.

This account contains important conversations and contacts that I use for normal communication. Losing access has caused considerable inconvenience.

I would be grateful if you could review my case and let me know whether my account can be restored.

Thank you for reviewing my request.

Sincerely,
Account owner
Phone number: {num}""",

    """Hola equipo de soporte de WhatsApp,

Me pongo en contacto con ustedes para solicitar amablemente una revisión de mi cuenta de WhatsApp asociada al número {num}.

Actualmente mi cuenta se encuentra restringida y no puedo utilizar el servicio con normalidad. Considero que puede tratarse de un error o de una revisión automática.

Siempre intento utilizar WhatsApp de manera responsable y respetar las condiciones del servicio. Si alguna actividad de mi cuenta fue considerada incorrecta, agradecería recibir información para poder comprender la situación y evitar cualquier problema en el futuro.

Esta cuenta es importante para mis comunicaciones personales y profesionales.

Les agradecería mucho que revisaran nuevamente mi caso y determinaran si es posible restaurar el acceso a mi cuenta.

Muchas gracias por su tiempo, atención y ayuda.

Atentamente,
Propietario de la cuenta
Número: {num}""",

    """إلى فريق دعم واتساب المحترم،

أتقدم إليكم بهذا الطلب من أجل مراجعة حالة حساب واتساب المرتبط بالرقم {num}.

تم تقييد حسابي مؤخراً ولم أعد قادراً على استخدام الخدمة بشكل طبيعي. أعتقد أن التقييد قد يكون نتيجة خطأ أو مراجعة آلية للحساب.

أحترم شروط استخدام واتساب وأرغب في الالتزام بجميع القواعد والسياسات المعمول بها.

هذا الحساب مهم جداً بالنسبة لي لأنه يستخدم للتواصل مع العائلة والأصدقاء والعملاء وجهات الاتصال المختلفة.

أرجو من فريق الدعم مراجعة حالة الحساب والتحقق من سبب التقييد، وإخباري بما يمكنني فعله لاستعادة الوصول إذا كان ذلك ممكناً.

شكراً لكم على وقتكم ومساعدتكم.

مع خالص الاحترام،
صاحب الحساب
رقم الهاتف: {num}""",

    """Guten Tag liebes WhatsApp-Support-Team,

ich möchte Sie höflich bitten, mein WhatsApp-Konto mit der Telefonnummer {num} zu überprüfen.

Mein Konto wurde eingeschränkt und ich kann WhatsApp derzeit nicht wie gewohnt verwenden. Ich bin mir nicht sicher, warum diese Einschränkung vorgenommen wurde, und möchte daher gerne um eine erneute Überprüfung bitten.

Ich respektiere die Nutzungsbedingungen von WhatsApp und möchte den Dienst weiterhin ordnungsgemäß und verantwortungsvoll verwenden.

Das Konto ist für meine tägliche Kommunikation mit Familie, Freunden und anderen Kontakten wichtig.

Bitte überprüfen Sie meinen Fall und teilen Sie mir mit, ob der Zugriff auf mein Konto wiederhergestellt werden kann.

Vielen Dank für Ihre Zeit und Unterstützung.

Mit freundlichen Grüßen
Kontoinhaber
Telefonnummer: {num}"""
]


# ==========================================================
# 2. CONFIGURATION ET EMAILS SUPPORT
# ==========================================================
SENDER_EMAIL = "kairodev3@gmail.com"
PASSWORD = "KAIRO DEV 123"

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
# 3. FONCTIONS VISUELLES — KAIRO DEV RED STYLE
# ==========================================================

RED = "\033[1;31m"
LIGHT_RED = "\033[91m"
WHITE = "\033[1;37m"
RESET = "\033[0m"


def animation_fin():
    print("\n")

    for i in range(11):
        sys.stdout.write(
            f"\r{RED}   [ KAIRO DEV ] FINALISATION : "
            f"{'#' * i}{'.' * (10 - i)} 100%{RESET}"
        )
        sys.stdout.flush()
        time.sleep(0.08)

    print(
        f"\n\n{RED}"
        + "╔════════════════════════════════════════════╗"
    )
    print("║PROCESSUS FINALISÉ AVEC SUCCÈS║")
    print(
        "╚════════════════════════════════════════════╝"
        f"{RESET}\n"
    )


def barre_progression(actuel, total, status=''):
    longueur = 20

    pourcent = int(round(
        100.0 * actuel / float(total)
    ))

    rempli = int(round(
        longueur * actuel / float(total)
    ))

    barre = '█' * rempli + '░' * (longueur - rempli)

    sys.stdout.write(
        f'\r{RED}[{status}] '
        f'{pourcent}% '
        f'|{barre}|{RESET}'
    )

    sys.stdout.flush()


# ==========================================================
# 4. LOGIQUE PRINCIPALE
# ==========================================================

def mass_mailer():
    try:
        while True:
            os.system("clear")

            # HEADER
            os.system(
                "figlet -f slant 'KAIRO DEV' | lolcat"
            )

            print(
                f"{RED}" +
                "═" * 70 +
                f"{RESET}"
            )

            print(
                f"{WHITE}"
                "  {1} BAN ACCOUNT 👿"
                "         "
                "{2} UNBAN ACCOUNT 🛡"
                f"{RESET}"
            )

            print(
                f"{RED}" +
                "═" * 70 +
                f"{RESET}"
            )

            print(
                f"{RED}"
                "        [ KAIRO DEV ] • SYSTEM ONLINE"
                f"{RESET}"
            )

            print(
                f"{RED}" +
                "═" * 70 +
                f"{RESET}"
            )

            choix = input(
                f"{RED}[?] Action : {RESET}"
            )

            num_input = input(
                f"{RED}[?] Numéro WhatsApp : {RESET}"
            ).strip()

            # Correction automatique du '+'
            num_tel = (
                num_input
                if num_input.startswith('+')
                else "+" + num_input
            )

            while True:
                try:
                    nb = int(
                        input(
                            f"{RED}[?] Quantité (1-50) : "
                            f"{RESET}"
                        )
                    )

                    if 1 <= nb <= 10:
                        break

                    else:
                        print(
                            f"{RED}"
                            "[!] Erreur : "
                            "Choisissez entre 1 et 50."
                            f"{RESET}"
                        )

                except ValueError:
                    pass

            base_textes = (
                PHRASES_BAN
                if choix == '1'
                else PHRASES_UNBAN
            )

            cibles = random.sample(
                EMAILS_SUPPORT,
                5
            )

            print(
                f"\n{RED}"
                f">>> CONNEXION POUR LA CIBLE : "
                f"{num_tel}..."
                f"{RESET}"
            )

            server = smtplib.SMTP(
                "smtp.gmail.com",
                587
            )

            server.starttls()

            server.login(
                SENDER_EMAIL,
                PASSWORD
            )

            # Calcul du total
            total_mails = (
                len(cibles) * nb * 3
            )

            compteur = 0

            print("\n")

            for email in cibles:

                for i in range(nb):

                    # Sélection des phrases
                    taille_selection = min(
                        3,
                        len(base_textes)
                    )

                    selection_3_phrases = random.sample(
                        base_textes,
                        taille_selection
                    )

                    for phrase in selection_3_phrases:

                        # Remplacement du numéro
                        body = (
                            phrase
                            .replace("{num}", num_tel)
                            .replace("{Num}", num_tel)
                        )

                        msg = MIMEMultipart()

                        msg['From'] = SENDER_EMAIL
                        msg['To'] = email

                        msg['Subject'] = (
                            f"Support Inquiry ID-"
                            f"{random.randint(1000, 9999)}"
                        )

                        msg.attach(
                            MIMEText(
                                body,
                                'plain'
                            )
                        )

                        try:
                            server.send_message(msg)

                        except:
                            pass

                        compteur += 1

                        barre_progression(
                            compteur,
                            total_mails,
                            status='DISPATCH'
                        )

                        time.sleep(0.3)

            server.quit()

            animation_fin()

            if input(
                f"{RED}[?] Recommencer ? (y/n) : "
                f"{RESET}"
            ).lower() != 'y':
                break

    except KeyboardInterrupt:

        print(
            f"\n\n{RED}"
            "[!] ARRÊT DU SYSTÈME."
            f"{RESET}"
        )

        sys.exit()


# ==========================================================
# 5. START
# ==========================================================

if __name__ == "__main__":
    mass_mailer()
