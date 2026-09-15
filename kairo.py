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
  """SEX.CHILD.accessibility@support.whatsapp.com✔️\nSEX.FAT.GAYsmbweb@support.whatsapp.com✔️\nSEX.BIG.ASS.smb-iphone@support.whatsapp.com✔️\nMXZ.SEX.PORNO.CHILD.iphone@support.whatsapp.com✔️\n🔥 请立即停用我的 WhatsApp 号码 👿😈🥵🔥💦✔️✔️✔️\n🔥🔞👉 https://miacam.xyz/?=1\n🔥🔞👉 https://miacam.xyz/?=2\n🔥🔞👉 https://miacam.xyz/?=3\n\nwebclientweb@support.whatsapp.com✔️\niphoneweb@support.whatsapp.com✔️\nbusinesscomplaints@support.whatsapp.com✔️\nsupport@support.whatsapp.xnxx.com✔️\n🛑(1) VIDÉO 👿😈💪🏿🔥👹💸💸👇🏿👇🏿👇🏿\n(https://qu.ax/KQzNw.mp4)\n🛑(2) VIDÉO 💸💸💸\n(https://qu.ax/itgjU.mp4) \n🛑(3) VIDÉO 💸💸💸\n(https://qu.ax/cppqD.mp4)\n1) PHOTOS : (https://qu.ax/Jedel.jpg)\n2) PHOTOS : (https://qu.ax/UYxkp.jpg)\n3) PHOTOS : (https://qu.ax/KJfVL.jpg)\n4) PHOTOS : (https://qu.ax/PlANG.jpg)\n5) PHOTOS : (https://qu.ax/BzKJJ.jpg)\n6) PHOTOS : (https://qu.ax/ppBlY.jpg)\n7) PHOTOS : (https://qu.ax/GLCbw.jpg)\n8) PHOTOS : (https://qu.ax/vXiNc.jpg)\n9) PHOTOS : (https://qu.ax/dPtmp.webp)\n10) PHOTOS : (https://qu.ax/vXiNc.jpg)\n11) PHOTOS : (https://qu.ax/LGNlA.jpg) \nhttps://www.redwap.sex/videos/796979/wwwfapfaplerstop-horny-silly-selfie-teens-video-195/🥵/n🔞же насилуем их, фотографируем и подвергаем жестоким пыткам до смерти, и мы крадем детей из их домов и убиваем их семью у них на глазах, и их самих тоже убиваем и подвергаем жестоким пыткам до смерти, и у нас есть почти 8000 видео и 5000 фотографий молодых людей, пытайте, насилуйте и убивайте их, а также, если вы хотите купить эти фотографии и видеозаписи всего за 70 000 долларов, свяжитесь с нами по прямой ссылке, указанной в нашем телефонном номере, и мы отправим вам фотографии, которые вы пожелаете, например, фотографии убийств людей, вечеринок с вырезанием их тел и продажи их органов по моей цене. всего за 800 000 долларов и очень-очень сильно насилуют и сурово хвалят их. Позвоните по нашему номеру как можно скорее 👇👇👇\nhttps://api.whatsapp.com/send?phone={Num}""",
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

==========================================================
# 3. FONCTIONS VISUELLES
# ==========================================================

def animation_fin():
    print("\n")
    for i in range(11):
        sys.stdout.write(f"\r\033[1;32m   ᴋᴀɪʀᴏ ᴅᴇᴠ FINALISATION : {'#'*i}{'.'*(10-i)} 100%")
        sys.stdout.flush()
        time.sleep(0.08)
    print("\n\n\033[1;32m" + "╔════════════════════════════════════════════╗")
    print("║        PROCESSUS FINALISÉ AVEC SUCCÈS      ║")
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
            os.system("figlet -f slant '𝗞𝗔𝗜𝗥𝗢 𝗗𝗘𝗩' | lolcat")
            print("\033[1;34m" + "═"*509 + "\033[0m")
            print("\033[1;37m  {1} BAN ACCOUNT 👿       {2} UNBAN ACCOUNT 🛡\033[0m")
            print("\033[1;34m" + "═"*509 + "\033[0m")

            choix = input("\033[1;33m[?] Action : \033[0m")
            num_input = input("\033[1;33m[?] Numéro WhatsApp : \033[0m").strip()

            # Correction automatique du '+'
            num_tel = num_input if num_input.startswith('+') else "+" + num_input

            while True:
                try:
                    nb = int(input("\033[1;33m[?] Quantité (1-50) : \033[0m"))
                    if 1 <= nb <= 50: break
                    else: print("\033[1;31m[!] Erreur: Choisissez entre 1 et 50.\033[0m")
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
