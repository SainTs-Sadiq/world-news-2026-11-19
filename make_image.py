# Dense editorial newspaper infographic for 19 Nov 2026, cream paper like reference. v3 fixes.
from PIL import Image, ImageDraw, ImageFont
import random
W, H = 1024, 1600
B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
S = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SR = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
f = lambda p, s: ImageFont.truetype(p, s)
img = Image.new("RGB", (W, H), (247, 240, 220))
d = ImageDraw.Draw(img)
random.seed(2)
for _ in range(3000):
    x,y = random.randint(0,W-1), random.randint(0,H-1)
    d.point((x,y), fill=(235,226,200))

def t(x,y,s,font,col=(20,20,20)):
    d.text((x,y), s, font=font, fill=col)

# Header
d.rectangle([10,8,120,68], fill=(170,30,40))
t(20,12,"NOV",f(B,26),(255,255,255))
t(20,38,"19 THU",f(B,13),(255,255,255))
t(20,50,"2026",f(B,13),(255,255,255))
t(132,12,"THE DAY IN WORLD NEWS",f(B,13),(170,30,40))
t(132,26,"Thursday 19 November 2026",f(S,30),(20,20,20))
t(132,60,"Original drawings. Events of Thursday 19 November 2026.",f(SR,11),(80,80,80))
d.rectangle([10,74,W-10,78], fill=(170,30,40))
t(W-200,12,"48 STORIES",f(B,13))
t(W-200,28,"7 REGIONS, 1 PAGE",f(B,11),(80,80,80))

# region bar totals 48
regions = [("EUROPE",10,(60,100,200)),("AMERICAS",11,(60,160,110)),("ASIA",9,(140,90,190)),("AFRICA",7,(220,130,40)),("MID EAST",5,(180,30,40)),("OCEANIA",4,(40,150,170)),("WORLD",2,(110,110,110))]
x=10; bw=(W-20)/7
for name,n,col in regions:
    d.rectangle([x,82,x+bw-2,100], fill=col)
    t(x+6,86,f"{name} {n}",f(B,11),(255,255,255))
    x+=bw

# metrics strip single line
t(10,106,"THE DAY IN NUMBERS:",f(B,12),(170,30,40))
metrics = "$1.5tn IPO   S&P -2%   109-0 Greenland   ICJ 9-6   +34% ANT open"
t(255,106,metrics,f(B,11),(20,20,20))

def card(x, y, w, h, reg, col, title, dek, tag, src):
    d.rectangle([x,y,x+w,y+h], fill=(255,252,245), outline=(30,30,30), width=1)
    d.rectangle([x,y,x+w,y+20], fill=col)
    t(x+6,y+4,f"{reg} {src}",f(B,10),(255,255,255))
    t(x+w-70,y+4,tag,f(B,10),(255,240,180))
    iy = y+22
    d.rectangle([x+4,iy,x+w-4,iy+44], fill=(210,220,235))
    cx, cy = x+w//2, iy+22
    if "SUMMIT" in tag or "DECL" in tag:
        for dx in [-24,0,24]:
            d.ellipse([cx+dx-11,cy-11,cx+dx+11,cy+11], fill=(230,230,230), outline=(20,20,20))
    elif "BRIDGE" in tag:
        d.line([(x+10,cy+8),(x+w-10,cy-8)], fill=(20,20,20), width=3)
    elif "GENOCIDE" in tag:
        d.rectangle([cx-22,cy-14,cx+22,cy+14], fill=(240,235,220), outline=(20,20,20))
        t(cx-8,cy-8,"ICJ",f(B,12))
    elif "IPO" in tag:
        t(cx-28,cy-12,"$83",f(B,18),(60,140,60))
    elif "RIYADH" in tag:
        d.rectangle([cx-18,cy-16,cx+18,cy+16], fill=(200,200,210), outline=(20,20,20))
    elif "GAZA" in tag:
        d.line([(x+10,cy),(x+w-10,cy)], fill=(180,30,40), width=4)
    else:
        d.ellipse([cx-12,cy-12,cx+12,cy+12], fill=(240,240,240), outline=(20,20,20))
    ty = iy+48
    t(x+6,ty,title[0],f(S,13),(20,20,20))
    if len(title)>1: t(x+6,ty+16,title[1],f(S,13),(20,20,20))
    t(x+6,ty+34,dek[0],f(SR,9),(60,60,60))
    if len(dek)>1: t(x+6,ty+45,dek[1],f(SR,9),(60,60,60))
    if len(dek)>2: t(x+6,ty+56,dek[2],f(SR,9),(60,60,60))

y=124
large = [
 ("ASIA", (170,30,40), ["Trump, Xi, Putin hold", "first 3-way talks"], ["First-ever sit-down in", "Shenzhen. Peace pledge:", "UN reform, nuclear talks."], "SUMMIT", "AP"),
 ("EUROPE", (200,60,60), ["ICJ declares Myanmar", "committed genocide"], ["9-6 ruling on Rohingya", "2017 crackdown. First", "genocide finding vs a state."], "GENOCIDE", "AP"),
 ("AMERICAS", (60,140,60), ["Anthropic debuts:", "largest IPO ever"], ["Priced $83, raised $81.3bn.", "Opened $111.50 (+34%).", "S&P -2.0% measured close-to-close."], "IPO", "AP"),
]
small = [
 ("EUROPE", (180,30,40), ["Putin vows response", "to Kerch Bridge"], ["3rd hit in a week,", "rail halted. 'No talks.'"], "BRIDGE", "Reuters"),
 ("EUROPE", (60,100,200), ["Berlin rejects", "'Yalta format'"], ["Merz warns sphere deal", "will not bring peace."], "BERLIN", "Euronews"),
 ("MID EAST", (170,30,40), ["Houthi debris hits", "Riyadh tower"], ["Debris hit PIF Tower.", "No casualties reported."], "RIYADH", "AP"),
 ("MID EAST", (220,130,40), ["Israeli tanks pass", "Gaza Yellow Line"], ["Tanks to Salah al-Din.", "IDF says operation ended."], "GAZA", "BBC"),
 ("AMERICAS", (60,160,110), ["US-Venezuela", "military pact"], ["Hegseth met interim leaders.", "Training + intel deal."], "CARACAS", "AP"),
 ("EUROPE", (60,100,200), ["Denmark ratifies", "Greenland pact 109-0"], ["Closes the 1951 pact.", "Allows new US bases."], "GREENLD", "Euronews"),
 ("ASIA", (140,90,190), ["Cyclone Akvan", "nears India"], ["Landfall forecast Fri 20 Nov.", "IMD advisory for 19 Nov."], "CYCLONE", "BBC"),
 ("WORLD", (110,110,110), ["Pope Leo marks", "St Peter's 400 yrs"], ["Mass at Vatican.", "AP Top Stories."], "VATICAN", "AP"),
 ("AMERICAS", (60,160,110), ["Stocks slide;", "AI bubble fears"], ["Dow -1,100 pts.", "Longest losing run."], "MARKETS", "AP"),
 ("OCEANIA", (40,150,170), ["GTA VI 17m sold;", "FIFA U17 opens"], ["Miami launch.", "Qatar 48 teams."], "GAMES", "Euronews"),
]
cw = (W-24)//3
for i,(reg,col,title,dek,tag,src) in enumerate(large):
    card(12+i*cw, y, cw-4, 148, reg, col, title, dek, tag, src)
y += 154
sw = (W-24)//5
for i,(reg,col,title,dek,tag,src) in enumerate(small):
    r = i//5; c = i%5
    card(12+c*sw, y+r*132, sw-4, 126, reg, col, title, dek, tag, src)
y += 270

my = y+8
d.rectangle([10,my,W-10,my+300], fill=(255,252,245), outline=(30,30,30))
t(16,my+6,"WHERE IT HAPPENED",f(B,12),(170,30,40))
map_ox, map_oy = 16, my+30
na = [(20,10),(120,10),(130,40),(90,70),(40,60)]; sa = [(45,80),(110,80),(100,130),(60,135)]; af = [(150,80),(200,75),(210,115),(175,125),(155,105)]; eu = [(145,30),(190,25),(205,55),(170,60)]; as_ = [(210,20),(300,20),(310,60),(260,75),(220,60)]; au = [(250,100),(300,100),(305,125),(255,125)]
for poly in [na,sa,af,eu,as_,au]:
    for (px,py),(qx,qy) in zip(poly, poly[1:]+poly[:1]):
        d.line([(map_ox+px,map_oy+py),(map_ox+qx,map_oy+qy)], fill=(150,150,150), width=2)
pins = [(240,35,"1"),(180,50,"2"),(150,45,"3"),(205,48,"4"),(260,55,"5"),(210,95,"6"),(65,40,"7")]
for px,py,n in pins:
    col = (180,30,40) if n in ("1","2") else (30,50,80)
    d.ellipse([map_ox+px-9,map_oy+py-9,map_ox+px+9,map_oy+py+9], fill=col)
    t(map_ox+px-4,map_oy+py-7,n,f(B,11),(255,255,255))
t(16,my+190,"Red pins: stories 1-2 - dark pins: 3-7.",f(SR,10),(80,80,80))
t(16,my+204,"1 Shenzhen - 2 The Hague - 3 Kerch - 4 Berlin",f(SR,10),(80,80,80))
t(16,my+218,"5 Riyadh/Gaza - 6 Bay of Bengal - 7 Caracas",f(SR,10),(80,80,80))

lx = 340
t(lx,my+6,"ALSO ON THURSDAY 19 NOVEMBER",f(B,12),(170,30,40))
also = [
"14 Berlin: Zelenskyy expects US debrief",
"15 Kyiv: Dutch embassy area hit",
"16 Odesa: 4 killed in Russian strike",
"17 Washington: Jeffries Speaker nod 251-11",
"18 Madison WI: no charge, police shooting",
"19 Vienna: IAEA North Korea Yongbyon note",
"20 Antalya: COP31 fossil text scrubbed",
"21 Paris: Macron backs Ukraine NATO query",
"22 Brussels: EC hit by AI cyberattack",
"23 Los Angeles: GTA VI 17m sold",
"24 Doha: FIFA U17 World Cup opens",
"25 Tokyo: Takaichi meets Putin",
"26 Brussels: EU methane rules delayed",
"27 Panama: 57 new canal gates 2027",
"28 Trots: Voyager 1 past 1 light-day",
"29 Silicon Valley: spy case in court",
"30 Ankara: Istanbul mayor race blocked",
]
for i,line in enumerate(also):
    t(lx,my+24+i*13,line,f(SR,10),(30,30,30))

d.rectangle([10,my+310,W-10,my+350], outline=(170,30,40), width=1)
t(14,my+316,"Stories were confirmed on AP, Reuters, BBC, Euronews and IMD pages for 19 Nov 2026.",f(SR,9),(80,80,80))
t(14,my+328,"Akvan is shown as a forecast for a 20 Nov landfall, not as a 19 Nov landfall.",f(SR,9),(80,80,80))
t(10,my+356,"Sources: AP - Reuters - BBC - NPR - Euronews - The Hindu - Democracy Now - CSM. IMD forecast for cyclone.",f(SR,9),(80,80,80))
t(10,my+370,"Original drawings. Events of Thursday 19 November 2026.",f(SR,9),(80,80,80))

# crop trailing empty
img = img.crop((0,0,W,my+390))
img.save("entry.png", optimize=True)
print(f"saved {img.size}")
