"""Builds home.html (繁體中文) and index.html (English) from one template.

Text is written as L(中文, English). Run:  python3 _build/build.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class L:
    def __init__(self, zh, en):
        self.zh, self.en = zh, en


PHONE = "0121 643 9266"
PHONE_TEL = "+441216439266"
MOBILE = "07505 388 911"
MOBILE_TEL = "+447505388911"
EMAIL = "maggiewong@maggiewong.co.uk"
SRA_NO = "564108"
COMPANY_NO = "7769257"
OFFICIAL = "http://maggiewong.co.uk/"
MAP = "https://www.google.com/maps/search/?api=1&query=17+Cannon+Street+Birmingham+B2+5EN"

ICONS = {
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/>',
    "check": '<circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/>',
    "briefcase": '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2M2 13h20"/>',
    "cap": '<path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 2 9 2 12 0v-5"/>',
    "family": '<circle cx="9" cy="7" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 21v-2a5 5 0 0 1 5-5h2a5 5 0 0 1 5 5v2M15 21v-1.5a4 4 0 0 1 6-3.4"/>',
    "passport": '<rect x="4" y="2" width="16" height="20" rx="2"/><circle cx="12" cy="10" r="3.5"/><path d="M8.5 10h7M12 6.5c1.2 1 1.2 6 0 7M12 6.5c-1.2 1-1.2 6 0 7M9 17h6"/>',
    "scale": '<path d="M12 3v18M7 21h10M5 7h14M5 7l-3 7a3 3 0 0 0 6 0L5 7zM19 7l-3 7a3 3 0 0 0 6 0l-3-7z"/>',
    "plane": '<path d="M17.8 19.2 16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z"/>',
    "home": '<path d="M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
    "doc": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "arrow": '<path d="M7 17 17 7M9 7h8v8"/>',
    "send": '<path d="m22 2-7 20-4-9-9-4z"/><path d="M22 2 11 13"/>',
}


def icon(name, sw="1.8"):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


SERVICES = [
    ("briefcase",
     L("商業及投資移民", "Business & investor immigration"),
     L("為創業者、投資者及海外公司駐英代表規劃簽證路線，由首次申請、續簽到永居一手包辦。",
       "Visa strategy for entrepreneurs, investors and overseas businesses sending a representative to the UK — from first application to settlement."),
     [L("創業及投資類簽證", "Entrepreneur and investor routes"),
      L("海外公司駐英代表", "Sole representatives of overseas businesses"),
      L("續簽及永久居留", "Extensions and settlement")]),
    ("passport",
     L("工作簽證及擔保牌照", "Work visas & sponsor licences"),
     L("協助僱員申請工作簽證，並為僱主申請及維持擔保牌照（Sponsor Licence）。",
       "Work visas for employees, and sponsor licence applications and compliance for employers."),
     [L("技術工作簽證", "Skilled worker visas"),
      L("公司內部調派", "Intra-company transfers"),
      L("僱主擔保牌照申請", "Sponsor licence applications")]),
    ("cap",
     L("學生簽證", "Student visas"),
     L("為來英升學的學生及兒童學生準備申請，並安排畢業後的簽證出路。",
       "Applications for students and child students, and planning what comes after graduation."),
     [L("學生及兒童學生簽證", "Student and child student visas"),
      L("續簽及轉換簽證", "Extensions and switching"),
      L("準學生簽證", "Prospective student visas")]),
    ("family",
     L("家庭團聚", "Family & partners"),
     L("讓家人在英國團聚：配偶、未婚夫妻、同居伴侶、民事伴侶，以及受養子女及長者。",
       "Bringing families together: spouses, fiancé(e)s, unmarried and civil partners, dependent children and elderly relatives."),
     [L("配偶及伴侶簽證", "Spouse and partner visas"),
      L("未婚夫妻簽證", "Fiancé(e) visas"),
      L("子女及長者受養人簽證", "Child and elderly dependant visas")]),
    ("plane",
     L("探親及訪問簽證", "Visitor visas"),
     L("旅遊、探親、商務及短期學習的訪問簽證，以及其他各類入境簽證。",
       "Tourist, family, business and short-study visitor visas, and other entry clearance."),
     [L("旅遊及探親", "Tourist and family visits"),
      L("商務訪問", "Business visits"),
      L("各類入境簽證", "Other entry clearance")]),
    ("shield",
     L("永久居留及入籍", "Settlement & citizenship"),
     L("各類永久居留（ILR）申請、十年長居、酌情居留及複雜人權申請，以至入籍及護照。",
       "All kinds of indefinite leave to remain, the ten-year long residence route, discretionary leave and complex human rights claims, through to naturalisation and passports."),
     [L("永久居留 ILR", "Indefinite leave to remain"),
      L("十年長居", "Long residence (10 years)"),
      L("入籍及英國護照", "British citizenship and passports")]),
]

WIDE = (
    "scale",
    L("上訴、司法覆核及庇護", "Appeals, judicial review & asylum"),
    L("申請被拒並非終點。我們會分析拒簽理由，代表你向移民審裁處及更高級法院上訴，或提出司法覆核。",
      "A refusal is not the end of the road. We analyse the reasons, represent you at the Immigration Tribunal and higher courts, or bring a judicial review."),
    [L("移民審裁處上訴", "Immigration Tribunal appeals"),
     L("司法覆核", "Judicial review"),
     L("庇護及人權申請", "Asylum and human rights claims")],
    [L("與資深大律師合作處理", "Working with leading counsel"),
     L("一審上訴 £3,000 起", "First-tier appeals from £3,000"),
     L("全程由律師親自代表", "Represented by your solicitor throughout")],
)

OTHER = [
    ("home",
     L("商業及住宅物業", "Commercial & residential property"),
     L("房屋買賣、商舖新租約、分租及轉讓租約，以及生意買賣。",
       "Residential conveyancing, new commercial leases, subletting, assignments and sale of businesses."),
     [L("住宅物業買賣", "Residential conveyancing"),
      L("商業租約及轉讓", "Commercial leases and assignments"),
      L("生意買賣", "Sale of businesses")]),
    ("doc",
     L("宣誓、改名及牌照", "Declarations & licensing"),
     L("單身證明、改名契（Deed Poll）、各類宣誓書，以及處所牌照和個人牌照申請。",
       "Single status declarations, change of name deeds, statutory declarations, and premises and personal licences."),
     [L("單身證明及宣誓書", "Single status and statutory declarations"),
      L("改名契 Deed Poll", "Change of name (deed poll)"),
      L("處所及個人酒牌", "Premises and personal licences")]),
]

PROMISES = [
    (L("認識你這個人，而不是一個檔案編號", "Knowing you as a person, not a file number"),
     L("我們會先了解你的工作及家庭狀況，再給你合適的意見。", "We start with your work and family situation, then advise on what fits.")),
    (L("為你、你的公司和家人找出有效的方案", "Efficient solutions for you, your company and family"),
     L("安排申請時間、準備表格，並提醒你申請後需要注意的事項。", "We plan the timing, prepare the forms and tell you what to watch for afterwards.")),
    (L("長遠的簽證規劃，而非一次性申請", "Long-term planning, not a one-off application"),
     L("從第一個簽證開始，就為續簽、永居及入籍鋪路。", "From the first visa, we plan for extensions, settlement and citizenship.")),
    (L("不放過任何細節", "Leaving no stone unturned"),
     L("申請不獲批時，我們會據理力爭，直至上訴及司法覆核。", "If an application is refused, we fight on — through appeals and judicial review.")),
    (L("以合理收費提供高水平服務", "High standards of care at fair fees"),
     L("開案前先與你議定固定收費，讓你清楚知道費用。", "We usually agree a fixed fee before we start, so you know the cost.")),
]

STEPS = [
    (L("預約諮詢", "Book a consultation"),
     L("致電或電郵預約。本行只接受預約，不設即場諮詢。", "Call or email to book. We see clients by appointment only — no walk-ins.")),
    (L("評估個案及報價", "Case review and quote"),
     L("審閱你的情況及文件後，提供準確的費用估算。", "We review your circumstances and documents, then give an accurate estimate of costs.")),
    (L("準備及遞交申請", "Prepare and submit"),
     L("準備表格及證明文件，確保申請準時遞交，避免被拒。", "We prepare the forms and evidence and submit on time to avoid refusal.")),
    (L("跟進直至結果", "Through to the decision"),
     L("代表你與內政部聯絡；如有需要，可就決定提出上訴。", "We represent you to the Home Office and can challenge a decision at tribunal if needed.")),
]

FEES = [
    (L("配偶 / 伴侶 / 未婚夫妻簽證", "Spouse, partner or fiancé(e) visa"), L("首次申請，主申請人", "Initial application, main applicant"), "£900 – £1,500"),
    (L("技術工作或學生簽證", "Skilled worker or student visa"), L("首次申請，主申請人", "Initial application, main applicant"), "£750 – £1,500"),
    (L("十年長居永久居留", "Long residence settlement (10 years)"), L("主申請人", "Main applicant"), "£900 – £1,800"),
    (L("探親 / 商務訪問簽證", "Family or business visitor visa"), L("主申請人", "Main applicant"), "£600 – £1,500"),
    (L("入籍申請", "Naturalisation"), L("主申請人", "Main applicant"), "£600 – £1,500"),
    (L("一審移民上訴", "First-tier immigration appeal"), L("視乎個案複雜程度", "Depending on complexity"), L("£3,000 起", "From £3,000")),
]

T = {
    "lang": L("zh-Hant", "en-GB"),
    "file": L("home.html", "index.html"),
    "other_file": L("index.html", "home.html"),
    "other_label": L("English", "中文"),
    "other_lang": L("en-GB", "zh-Hant"),
    "title": L("黃艷彤律師行 Maggie Wong & Co｜伯明翰移民律師", "Maggie Wong & Co Solicitors | Immigration solicitors in Birmingham"),
    "desc": L("黃艷彤律師行位於伯明翰市中心，提供英國移民、人權、上訴、物業買賣、宣誓及牌照等法律服務。受律師規管局（SRA 564108）認可及規管。",
              "Maggie Wong & Co is a Birmingham city centre law firm offering UK immigration, human rights, appeals, property, declarations and licensing services. Authorised and regulated by the SRA (564108)."),
    "skip": L("跳至主要內容", "Skip to main content"),
    "concept_tag": L("概念", "Concept"),
    "concept": L("概念設計展示，非 <a href=\"%s\" target=\"_blank\" rel=\"noopener\">黃艷彤律師行官方網站</a>。" % OFFICIAL,
                 "A design concept — not the <a href=\"%s\" target=\"_blank\" rel=\"noopener\">official Maggie Wong &amp; Co website</a>." % OFFICIAL),
    "concept_by": L("設計：", "Design by "),
    "brand_name": L("黃艷彤律師行", "Maggie Wong &amp; Co"),
    "brand_sub": L("Maggie Wong &amp; Co Solicitors", "黃艷彤律師行 · Solicitors"),
    "nav": [(L("服務範圍", "Services"), "#services"), (L("服務流程", "How we work"), "#approach"),
            (L("關於律師", "About Maggie"), "#about"), (L("收費", "Fees"), "#fees"), (L("聯絡我們", "Contact"), "#contact")],
    "menu": L("選單", "Menu"),
    "book": L("預約諮詢", "Book a consultation"),
    "hero_eyebrow": L("伯明翰市中心 · 移民及人權法律", "Birmingham city centre · Immigration &amp; human rights"),
    "hero_h1": L("<span class=\"nw\">在英國生活、</span><span class=\"nw\">工作、團聚，</span><br><em><span class=\"nw\">由律師親自</span><span class=\"nw\">為你處理</span></em>", "Live, work and be with family in the UK — <em>handled by your solicitor</em>"),
    "hero_lead": L("簽證、永居、入籍及上訴，為個人、家庭及企業度身處理。",
                   "Visas, settlement, citizenship and appeals for individuals, families and businesses."),
    "call": L("致電", "Call"),
    "hero_meta": [("pin", L("近唐人街，步行約十分鐘", "About ten minutes' walk from Chinatown")),
                  ("calendar", L("只接受預約", "By appointment only")),
                  ("shield", L("受 SRA 規管（%s）" % SRA_NO, "SRA regulated (%s)" % SRA_NO))],
    "portrait_name": L("黃艷彤律師", "Maggie Wong"),
    "portrait_role": L("英格蘭及威爾斯執業律師 · 英國華威大學法律系畢業", "Solicitor, England &amp; Wales · Law graduate, University of Warwick"),
    "portrait_alt": L("黃艷彤律師在辦公室", "Maggie Wong at her desk"),
    "trust": [(L("律師親自處理", "Handled by a solicitor"), L("由黃艷彤律師跟進你的個案", "Maggie Wong works on your case")),
              (L("固定收費", "Fixed fees"), L("開案前先與你議定費用", "Usually agreed before we start")),
              (L("專注移民及人權法", "Immigration specialists"), L("曾於倫敦著名移民律師行執業", "Trained at a leading London immigration firm")),
              (L("服務華人社區", "Part of the community"), L("英國華文教育基金會法律顧問", "Legal adviser, UK Chinese Education Foundation"))],
    "svc_eyebrow": L("服務範圍", "What we do"),
    "svc_h2": L("由第一個簽證到入籍，每一步都有清晰方向", "Clear advice at every step, from your first visa to citizenship"),
    "svc_lead": L("英國移民法例複雜多變。我們會針對你的工作及家庭狀況，找出最合適的申請路線，並為日後的續簽、永居及入籍作好準備。",
                  "UK immigration law is complex and changes often. We find the route that fits your work and family, and plan ahead for extensions, settlement and citizenship."),
    "approach_eyebrow": L("我們的承諾", "Our approach"),
    "approach_h2": L("沒有兩個個案是一樣的", "No two cases are the same"),
    "approach_lead": L("我們以全面的角度處理每一個個案，讓你可以安心工作和生活。", "We take a broad view of every case, so you can get on with your work and family life."),
    "steps_title": L("服務流程", "How it works"),
    "about_eyebrow": L("關於律師", "About Maggie"),
    "about_h2": L("黃艷彤律師", "Maggie Wong"),
    "about_role": L("主管律師 · 英格蘭及威爾斯執業律師", "Principal solicitor · Solicitor of England &amp; Wales"),
    "about_p": [
        L("黃艷彤律師於英國華威大學法律學院畢業，其後加入倫敦一間著名移民律師行，專門處理移民及人權法。她熟悉英國移民法例、上訴程序及人權法，竭誠為客戶爭取居留及上訴權利。",
          "Maggie Wong graduated in law from the University of Warwick and joined one of London's leading immigration law firms, specialising in immigration and human rights law. She knows UK immigration law, appeal procedure and human rights law in depth, and fights hard for her clients' right to stay and to appeal."),
        L("她曾代表不同背景、文化及種族的客戶，處理投資者、創業者、學生、家庭及工作相關的移民個案，並與移民及人權領域的資深大律師合作。除移民事務外，她亦提供商業及住宅物業買賣服務。",
          "She has represented clients from many backgrounds and cultures — investors, entrepreneurs, students, families and workers — and has worked with leading counsel in the immigration and human rights field. Alongside immigration, she also handles commercial and residential conveyancing."),
    ],
    "about_quote": L("「舉家移居、轉換工作、出國留學，都是人生重要而令人緊張的決定。我的工作，是讓整個過程既快捷又安心。」",
                     "“Relocating a family, changing jobs or studying abroad are vital and daunting decisions. My job is to make the process swift and stress-free.”"),
    "about_p2": L("工作以外，黃律師積極參與華人社區，是英國華文教育基金會（<a href=\"http://www.ukcef.org.uk\" target=\"_blank\" rel=\"noopener\">UKCEF</a>）法律顧問之一，亦是伯明翰中文學校校董，鼓勵英國華人青年學習中文及認識中華文化。",
                  "Outside work, Maggie is closely involved in the Chinese community: she is a legal adviser to the UK Chinese Education Foundation (<a href=\"http://www.ukcef.org.uk\" target=\"_blank\" rel=\"noopener\">UKCEF</a>) and a governor of the Birmingham Chinese School, encouraging young people in the UK to learn Chinese and its traditions."),
    "facts": [(L("學歷", "Education"), L("英國華威大學法律學士", "Law degree, University of Warwick")),
              (L("規管機構", "Regulator"), L("律師規管局 SRA %s" % SRA_NO, "Solicitors Regulation Authority, %s" % SRA_NO)),
              (L("專業範疇", "Specialism"), L("移民、人權及上訴", "Immigration, human rights and appeals")),
              (L("社區服務", "Community"), L("UKCEF 法律顧問 · 伯明翰中文學校校董", "UKCEF legal adviser · Birmingham Chinese School governor"))],
    "fees_eyebrow": L("收費參考", "Fees"),
    "fees_h2": L("透明收費，開案前先講清楚", "Clear fees, agreed before we start"),
    "fees_lead": L("以下收費只供參考。每個個案都會獨立評估，我們會在審閱你的情況及文件後，提供準確的費用估算，通常會議定固定收費。",
                   "These fees are a guide only. Every case is assessed individually: once we have reviewed your circumstances and documents we give you an accurate estimate, and usually agree a fixed fee."),
    "consult_h": L("初步諮詢", "Consultation"),
    "consult_unit": L("/ 每小時", "/ hour"),
    "consult_p": L("需預先預約，不設即場諮詢。", "By appointment only — we do not offer walk-in consultations."),
    "fee_notes": [L("本行未有登記增值稅，法律費用不另收 VAT", "We are not VAT registered, so no VAT on our legal fees"),
                  L("不包括內政部申請費、醫療附加費及其他雜費", "Excludes Home Office fees, the health surcharge and disbursements"),
                  L("加入配偶或子女另計", "Adding a spouse or child is charged separately")],
    "fees_full": L("查看完整收費表", "See the full price list"),
    "contact_eyebrow": L("聯絡我們", "Contact"),
    "contact_h2": L("預約與黃律師見面", "Book an appointment with Maggie"),
    "contact_lead": L("請致電、電郵或填寫表格，告訴我們你的情況。我們會盡快回覆，安排合適的諮詢時間。",
                      "Call, email or use the form to tell us about your situation. We'll come back to you to arrange a consultation."),
    "l_address": L("地址", "Address"),
    "address": L("Room 14, Second Floor, 17 Cannon Street<br>Birmingham B2 5EN", "Room 14, Second Floor, 17 Cannon Street<br>Birmingham B2 5EN"),
    "map": L("在 Google 地圖開啟", "Open in Google Maps"),
    "l_phone": L("電話", "Telephone"),
    "l_email": L("電郵", "Email"),
    "l_hours": L("辦公時間", "Opening hours"),
    "hours": [(L("星期一至五", "Monday – Friday"), L("上午 9:00 – 下午 5:30", "9:00am – 5:30pm"), False),
              (L("星期六", "Saturday"), L("上午 9:00 – 中午 12:00", "9:00am – 12:00 noon"), False),
              (L("星期日及公眾假期", "Sunday &amp; bank holidays"), L("休息", "Closed"), True)],
    "appt": L("只接受預約", "By appointment only"),
    "directions": L("本行位於伯明翰市中心，由 New Street、Moor Street 及 Snow Hill 火車站步行約十分鐘，鄰近唐人街。",
                    "We are in the heart of Birmingham city centre, about ten minutes' walk from New Street, Moor Street and Snow Hill stations."),
    "form_h": L("查詢表格", "Send an enquiry"),
    "form_p": L("填寫後會開啟你的電郵程式，把資料傳送給我們。", "This opens your email app with the details filled in, ready to send."),
    "f_name": L("姓名", "Name"),
    "f_phone": L("電話", "Telephone"),
    "f_email": L("電郵", "Email"),
    "f_topic": L("查詢事項", "Enquiry about"),
    "f_topics": [L("工作或商業簽證", "Work or business visa"), L("學生簽證", "Student visa"), L("家庭或伴侶簽證", "Family or partner visa"),
                 L("永久居留或入籍", "Settlement or citizenship"), L("上訴或拒簽", "Appeal or refusal"), L("物業買賣", "Property"),
                 L("宣誓、改名或牌照", "Declarations or licensing"), L("其他", "Something else")],
    "f_msg": L("你的情況", "Your situation"),
    "f_send": L("發送查詢", "Send enquiry"),
    "f_subject": L("網上查詢", "Website enquiry"),
    "f_note": L("請勿在表格中提供護照號碼等敏感資料，我們會在預約時再向你索取。", "Please don't include passport numbers or other sensitive details — we'll ask for those when we meet."),
    "foot_about": L("位於伯明翰市中心的律師行，為各界人士提供專業及高效率的法律諮詢服務。", "A Birmingham city centre law firm providing professional, efficient legal advice."),
    "foot_explore": L("網站內容", "On this page"),
    "foot_legal": L("法律資訊", "Legal information"),
    "foot_links": [(L("私隱及資料保護", "Privacy &amp; data protection"), OFFICIAL + "Newsletter_ICU.html"),
                   (L("法律資訊及投訴程序", "Legal info &amp; complaints"), OFFICIAL + "Legal_Information_.html"),
                   (L("完整收費表", "Prices"), OFFICIAL + "Prices.html"),
                   (L("社區活動", "Community events"), OFFICIAL + "Event.html")],
    "sra": L("受律師規管局認可及規管<br><strong>SRA %s</strong>" % SRA_NO, "Authorised and regulated by the SRA<br><strong>No. %s</strong>" % SRA_NO),
    "reg": L("Maggie Wong &amp; Co Solicitors Limited，於英格蘭及威爾斯註冊之公司（編號 %s）。註冊辦事處：Room 14, Second Floor, 17 Cannon Street, Birmingham B2 5EN。本行受律師規管局（Solicitors Regulation Authority）認可及規管，並由 AXIS Speciality Europe 提供 £300 萬專業彌償保險，承保範圍為英格蘭及威爾斯。" % COMPANY_NO,
             "Maggie Wong &amp; Co Solicitors Limited, registered in England and Wales (No. %s). Registered office: Room 14, Second Floor, 17 Cannon Street, Birmingham B2 5EN. Authorised and regulated by the Solicitors Regulation Authority. Professional indemnity insurance of £3 million provided by AXIS Speciality Europe, covering work in England and Wales." % COMPANY_NO),
    "copy": L("非官方概念設計，由 <a href=\"https://ux-circles.com/web\" target=\"_blank\" rel=\"noopener\">UX CIRCLES</a> 設計", "Unofficial design concept by <a href=\"https://ux-circles.com/web\" target=\"_blank\" rel=\"noopener\">UX CIRCLES</a>"),
}


def page(lg):
    def t(v):
        if isinstance(v, L):
            return getattr(v, lg)
        return v

    def g(key):
        return t(T[key])

    def service_card(ic, title, text, items, extra=""):
        lis = "".join(f"<li>{t(i)}</li>" for i in items)
        return (f'<article class="service reveal{extra}"><div class="service-icon">{icon(ic)}</div>'
                f'<h3>{t(title)}</h3><p>{t(text)}</p><ul>{lis}</ul></article>')

    nav = "".join(f'<a href="{h}">{t(n)}</a>' for n, h in T["nav"])
    meta = "".join(f"<li>{icon(i)}{t(x)}</li>" for i, x in T["hero_meta"])
    trust = "".join(f'<div class="trust-item"><strong>{t(a)}</strong><span>{t(b)}</span></div>' for a, b in T["trust"])
    cards = "".join(service_card(*s) for s in SERVICES)
    w_ic, w_title, w_text, w_a, w_b = WIDE
    wide = (f'<article class="service service-wide reveal"><div class="service-icon">{icon(w_ic)}</div>'
            f'<div><h3>{t(w_title)}</h3><p>{t(w_text)}</p></div>'
            f'<div><ul>{"".join(f"<li>{t(i)}</li>" for i in w_a)}{"".join(f"<li>{t(i)}</li>" for i in w_b)}</ul></div></article>')
    others = "".join(service_card(*s) for s in OTHER)
    promises = "".join(f"<li>{icon('check')}<div><strong>{t(a)}</strong><span>{t(b)}</span></div></li>" for a, b in PROMISES)
    steps = "".join(f"<li><h3>{t(a)}</h3><p>{t(b)}</p></li>" for a, b in STEPS)
    about_p = "".join(f"<p>{t(p)}</p>" for p in T["about_p"])
    facts = "".join(f'<div class="fact"><strong>{t(a)}</strong><span>{t(b)}</span></div>' for a, b in T["facts"])
    fees = "".join(f'<div class="fee-row"><span>{t(a)}<small>{t(b)}</small></span><strong>{t(c)}</strong></div>' for a, b, c in FEES)
    fee_notes = "".join(f"<li>{t(n)}</li>" for n in T["fee_notes"])
    hours = "".join(f'<tr{" class=\"closed\"" if c else ""}><td>{t(d)}</td><td>{t(h)}</td></tr>' for d, h, c in T["hours"])
    topics = "".join(f"<option>{t(o)}</option>" for o in T["f_topics"])
    foot_nav = "".join(f'<li><a href="{h}">{t(n)}</a></li>' for n, h in T["nav"])
    foot_links = "".join(f'<li><a href="{h}" target="_blank" rel="noopener">{t(n)}</a></li>' for n, h in T["foot_links"])
    other = g("other_file")

    return f"""<!doctype html>
<html lang="{g('lang')}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{g('title')}</title>
<meta name="description" content="{g('desc')}">
<meta property="og:title" content="{g('title')}">
<meta property="og:description" content="{g('desc')}">
<meta property="og:image" content="assets/img/maggie-wong.jpg">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#133029">
<link rel="alternate" hreflang="{g('lang')}" href="{g('file')}">
<link rel="alternate" hreflang="{g('other_lang')}" href="{other}">
<link rel="icon" href="assets/img/logo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Source+Serif+4:opsz,wght@8..60,500;8..60,600;8..60,700&family=Noto+Sans+TC:wght@400;500;700&family=Noto+Serif+TC:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<a class="skip" href="#main">{g('skip')}</a>
<div class="concept-bar" role="note">
  <div class="container concept-inner">
    <p><span class="concept-tag">{g('concept_tag')}</span><span class="concept-long">{g('concept')}</span></p>
    <a href="https://ux-circles.com/web" target="_blank" rel="noopener"><span class="concept-by">{g('concept_by')}</span><strong>UX CIRCLES</strong> {icon('arrow', '2')}</a>
  </div>
</div>
<header class="site-header">
  <div class="container">
    <a class="brand" href="{g('file')}">
      <img src="assets/img/logo.svg" alt="" width="42" height="42">
      <span class="brand-text"><span class="brand-name">{g('brand_name')}</span><span class="brand-sub">{g('brand_sub')}</span></span>
    </a>
    <nav class="nav" id="nav" aria-label="{g('menu')}">{nav}</nav>
    <div class="header-actions">
      <a class="lang" href="{other}" hreflang="{g('other_lang')}" lang="{g('other_lang')}">{g('other_label')}</a>
      <a class="btn btn-primary btn-sm" href="#contact">{g('book')}</a>
      <button class="menu-toggle" type="button" aria-controls="nav" aria-expanded="false" aria-label="{g('menu')}">{icon('menu', '2')}</button>
    </div>
  </div>
</header>

<main id="main">
<section class="hero">
  <div class="container">
    <div>
      <p class="eyebrow">{g('hero_eyebrow')}</p>
      <h1>{g('hero_h1')}</h1>
      <p class="hero-lead">{g('hero_lead')}</p>
      <div class="hero-cta">
        <a class="btn btn-primary" href="#contact">{icon('calendar')}{g('book')}</a>
        <a class="btn btn-ghost" href="tel:{PHONE_TEL}">{icon('phone')}{g('call')} {PHONE}</a>
      </div>
      <ul class="hero-meta">{meta}</ul>
    </div>
    <figure class="portrait" style="margin:0">
      <div class="portrait-frame"><img src="assets/img/maggie-wong.jpg" alt="{g('portrait_alt')}" width="403" height="480"></div>
      <figcaption class="portrait-card"><strong>{g('portrait_name')}</strong><span>{g('portrait_role')}</span></figcaption>
    </figure>
  </div>
</section>

<section class="trust" aria-label="{g('approach_eyebrow')}">
  <div class="container">{trust}</div>
</section>

<section class="section" id="services">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">{g('svc_eyebrow')}</p>
      <h2>{g('svc_h2')}</h2>
      <p>{g('svc_lead')}</p>
    </div>
    <div class="services">{cards}{wide}{others}
      <article class="service reveal" style="display:flex;flex-direction:column;justify-content:center;background:var(--paper-2)">
        <h3>{g('contact_h2')}</h3>
        <p>{g('contact_lead')}</p>
        <div><a class="btn btn-outline btn-sm" href="#contact">{g('book')}</a></div>
      </article>
    </div>
  </div>
</section>

<section class="section section-alt" id="approach">
  <div class="container approach">
    <div class="reveal">
      <div class="section-head" style="margin-bottom:32px">
        <p class="eyebrow">{g('approach_eyebrow')}</p>
        <h2>{g('approach_h2')}</h2>
        <p>{g('approach_lead')}</p>
      </div>
      <ul class="promises">{promises}</ul>
    </div>
    <div class="reveal">
      <p class="steps-title">{g('steps_title')}</p>
      <ol class="steps">{steps}</ol>
    </div>
  </div>
</section>

<section class="section" id="about">
  <div class="container about">
    <figure class="about-photo reveal" style="margin:0">
      <img src="assets/img/maggie-wong.jpg" alt="{g('portrait_alt')}" width="403" height="480" loading="lazy">
      <figcaption>{g('portrait_role')}</figcaption>
    </figure>
    <div class="about-body reveal">
      <p class="eyebrow" style="color:var(--accent)">{g('about_eyebrow')}</p>
      <h2>{g('about_h2')}</h2>
      <p class="role">{g('about_role')}</p>
      {about_p}
      <blockquote class="quote">{g('about_quote')}</blockquote>
      <p>{g('about_p2')}</p>
      <div class="facts">{facts}</div>
    </div>
  </div>
</section>

<section class="section section-alt" id="fees">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">{g('fees_eyebrow')}</p>
      <h2>{g('fees_h2')}</h2>
      <p>{g('fees_lead')}</p>
    </div>
    <div class="fees-wrap">
      <div class="fee-table reveal">{fees}</div>
      <aside class="fee-note reveal">
        <h3>{g('consult_h')}</h3>
        <div class="price">£220 <small>{g('consult_unit')}</small></div>
        <p>{g('consult_p')}</p>
        <ul>{fee_notes}</ul>
        <a class="btn btn-ghost" href="{OFFICIAL}Prices.html" target="_blank" rel="noopener">{g('fees_full')} {icon('arrow', '2')}</a>
      </aside>
    </div>
  </div>
</section>

<section class="section" id="contact">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">{g('contact_eyebrow')}</p>
      <h2>{g('contact_h2')}</h2>
      <p>{g('contact_lead')}</p>
    </div>
    <div class="contact">
      <div class="contact-info reveal">
        <span class="appt">{icon('calendar')}{g('appt')}</span>
        <div class="contact-line"><span class="ic">{icon('pin')}</span><div><strong>{g('l_address')}</strong><span>{g('address')}</span><br><a href="{MAP}" target="_blank" rel="noopener" style="font-size:.9rem;color:var(--pine-600)">{g('map')}</a></div></div>
        <div class="contact-line"><span class="ic">{icon('phone')}</span><div><strong>{g('l_phone')}</strong><a href="tel:{PHONE_TEL}">{PHONE}</a> · <a href="tel:{MOBILE_TEL}">{MOBILE}</a></div></div>
        <div class="contact-line"><span class="ic">{icon('mail')}</span><div><strong>{g('l_email')}</strong><a href="mailto:{EMAIL}">{EMAIL}</a></div></div>
        <div class="contact-line"><span class="ic">{icon('clock')}</span><div><strong>{g('l_hours')}</strong><table class="hours">{hours}</table></div></div>
        <p class="directions">{g('directions')}</p>
      </div>
      <form class="form reveal" id="enquiry" data-subject="{g('f_subject')}" data-l-name="{g('f_name')}" data-l-phone="{g('f_phone')}" data-l-email="{g('f_email')}" data-l-topic="{g('f_topic')}">
        <h3>{g('form_h')}</h3>
        <p>{g('form_p')}</p>
        <div class="field"><label for="f-name">{g('f_name')}</label><input id="f-name" name="name" autocomplete="name" required></div>
        <div class="field-row">
          <div class="field"><label for="f-phone">{g('f_phone')}</label><input id="f-phone" name="phone" type="tel" autocomplete="tel"></div>
          <div class="field"><label for="f-email">{g('f_email')}</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
        </div>
        <div class="field"><label for="f-topic">{g('f_topic')}</label><select id="f-topic" name="topic">{topics}</select></div>
        <div class="field"><label for="f-msg">{g('f_msg')}</label><textarea id="f-msg" name="message"></textarea></div>
        <button class="btn btn-primary" type="submit">{icon('send')}{g('f_send')}</button>
        <p class="form-note">{g('f_note')}</p>
      </form>
    </div>
  </div>
</section>
</main>

<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <a class="brand" href="{g('file')}"><img src="assets/img/logo.svg" alt="" width="42" height="42"><span class="brand-text"><span class="brand-name">{g('brand_name')}</span><span class="brand-sub">{g('brand_sub')}</span></span></a>
        <p>{g('foot_about')}</p>
        <p><a href="tel:{PHONE_TEL}">{PHONE}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
      <div><h4>{g('foot_explore')}</h4><ul>{foot_nav}</ul></div>
      <div><h4>{g('foot_legal')}</h4><ul>{foot_links}</ul></div>
    </div>
    <div class="reg">
      <p>{g('reg')}<br>© <span id="year">2026</span> Maggie Wong &amp; Co Solicitors Limited · {g('copy')}</p>
      <span class="sra">{icon('shield')}<span>{g('sra')}</span></span>
    </div>
  </div>
</footer>

<div class="callbar">
  <a class="btn btn-outline" href="tel:{PHONE_TEL}">{icon('phone')}{g('call')}</a>
  <a class="btn btn-primary" href="#contact">{g('book')}</a>
</div>
<script src="assets/js/main.js"></script>
</body>
</html>
"""


if __name__ == "__main__":
    for lg, name in (("zh", "home.html"), ("en", "index.html")):
        (ROOT / name).write_text(page(lg), encoding="utf-8")
        print("wrote", name)
