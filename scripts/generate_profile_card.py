from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, os

W, H = 760, 291
OUT = "dist/profile-card.gif"
os.makedirs("dist", exist_ok=True)

mono = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
sans = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
f_big = ImageFont.truetype(sans, 24)
f_title = ImageFont.truetype(sans, 17)
f_mono = ImageFont.truetype(mono, 9)
f_small = ImageFont.truetype(mono, 8)
frames = []

for k in range(10):
    im = Image.new("RGB", (W, H), "#050816")
    d = ImageDraw.Draw(im, "RGBA")
    for x in range(0, W, 24): d.line((x, 0, x, H), fill=(51,65,85,22), width=1)
    for y in range(0, H, 24): d.line((0, y, W, y), fill=(51,65,85,22), width=1)
    d.rounded_rectangle((5,5,W-5,H-5), radius=20, fill=(7,11,28,245), outline=(34,211,238,150), width=2)
    d.rounded_rectangle((13,13,W-13,H-13), radius=16, outline=(124,58,237,90), width=1)
    seg_x = 18 + ((k * 75) % (W-55)); d.line((seg_x,14,min(seg_x+55,W-14),14), fill=(34,211,238,255), width=3)
    for i,c in enumerate([(239,68,68,255),(245,158,11,255),(52,211,153,255)]): d.ellipse((27+i*14,28,35+i*14,36), fill=c)
    d.text((78,26), "durgesh@profile:~$ ./digital_id", font=f_mono, fill=(100,116,139,255))
    d.text((650,27), "ONLINE", font=f_small, fill=(52,211,153,255))

    # left identity panel
    d.rounded_rectangle((25,55,260,270), radius=16, fill=(2,6,23,230), outline=(51,65,85,180))
    d.text((42,72), "[ DATA CORE ]", font=f_small, fill=(34,211,238,255))
    d.text((42,92), "DURGESH", font=f_big, fill=(248,250,252,255))
    d.text((43,121), "AI & DATA SCIENCE", font=f_small, fill=(148,163,184,255))
    cx, cy = 142, 187
    for rr, al in [(39,75),(52,50),(65,35)]: d.ellipse((cx-rr,cy-rr,cx+rr,cy+rr), outline=(34,211,238,al), width=2)
    for j in range(8):
        a = 2*math.pi*j/8 + k*math.pi/8; px=cx+39*math.cos(a); py=cy+39*math.sin(a)
        d.ellipse((px-3,py-3,px+3,py+3), fill=(103,232,249,255))
    d.ellipse((cx-22,cy-22,cx+22,cy+22), fill=(15,23,42,255), outline=(167,139,250,220), width=2)
    d.text((cx-9,cy-6), "AI", font=f_small, fill=(103,232,249,255))
    for i,v in enumerate([0.58,0.82,0.68,0.9]):
        y=236+i*6; d.rounded_rectangle((42,y,215,y+3),radius=2,fill=(30,41,59,255)); w=int(173*max(.12,min(1,v+0.08*math.sin(k/2+i)))); d.rounded_rectangle((42,y,42+w,y+3),radius=2,fill=(34,211,238,210))

    # right information panel
    d.text((282,57), "PROFILE / SYSTEM.INFO", font=f_small, fill=(34,211,238,255))
    d.text((282,78), "Data Analytics  •  Data Science", font=f_title, fill=(248,250,252,255))
    d.text((282,99), "B.Tech Artificial Intelligence & Data Science", font=f_mono, fill=(148,163,184,255))
    d.line((282,118,735,118), fill=(51,65,85,180), width=1)
    rows=[("ROLE","Student • Builder • Data/AI Learner"),("FOCUS","Python • SQL • Statistics • Machine Learning"),("FLAGSHIP","BizGuard AI"),("LIVE","bizguard.streamlit.app"),("PROJECT","HoteliQ • Streamlit Analytics")]

    y=136
    for label,val in rows:
        d.text((282,y),label,font=f_small,fill=(34,211,238,255)); d.text((354,y),val,font=f_mono,fill=(226,232,240,255)); y+=22
    d.text((282,248),"STATUS",font=f_small,fill=(34,211,238,255)); d.text((354,248),"BUILDING / LEARNING / SHIPPING",font=f_mono,fill=(52,211,153,255))
    d.rectangle((282,267,735,270),fill=(30,41,59,255)); sx=282+int(453*(k/9)); d.rectangle((282,267,max(283,sx),270),fill=(34,211,238,220))
    frames.append(im)

frames[0].save(OUT, save_all=True, append_images=frames[1:], duration=160, loop=0, disposal=2, optimize=True)
print(OUT)