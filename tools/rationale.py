RAW = 'https://raw.githubusercontent.com/Akkhadat12/Anthropic-IPO/research-ipo-financials-models-2026/build-notes/prod-screens-v2/'
URL = 'https://anthropic-ipo-capacity-ledger.vercel.app'
SHA = '944a2d976ad2daec2d3806bba78282b0a6e5f301'

scenes = [
    ('cover', 'Cover — The capacity room',
     'ตั้งคำถามหลักด้วยภาพจริงของห้อง compute: ความต้องการใช้ Claude จะกลายเป็นเงินสดผ่านโครงสร้างพื้นฐานจริงได้หรือไม่ ภาพเป็นบริบท ไม่ใช่การวัดกำลังการผลิตของ Anthropic',
     'ภาพถ่ายจริง AWS Project Rainier (ภายในอาคาร) ให้ความลึก เส้นทาง demand แคบวิ่งเข้าหาแถบ capacity ที่กว้างกว่ามากที่ขอบฟ้า กรอบประตูคือจุดที่กล้องเดินผ่านเมื่อผู้นำเสนอกดเข้า',
     'กดประตู 3D หรือปุ่ม "Enter ledger" → demand (Space ก็ได้)',
     'Photo: Amazon Web Services, Project Rainier แสดงบนหน้าและใน Sources overlay ระบุว่าเป็นอาคาร AWS ที่ใช้กับงานของ Anthropic ไม่ใช่ของ Anthropic',
     'ไม่มีจาก proposal เดิมนอกจากขนาดกรอบประตูที่ลดลงหลังทดสอบภาพจริง'),
    ('demand', '1 — Demand accelerates',
     'แสดงตัวเลขรายได้สี่ชุดที่ "คนละนาฬิกา คนละฐาน": FY2025 ≈ $4.6B (Reuters จากร่างที่เห็น), Q1 2026 $4.73B (Bloomberg จากเอกสารนักลงทุน), Q2 2026 > $11.5B (Bloomberg เบื้องต้น) และ run-rate เดือนพฤษภาคม > $47B ต่อปี (Anthropic ระบุ) ไม่มีตัวใดเป็นรายได้ FY2026',
     'สี่แผ่นแยกกันในเชิงลึก ไม่ลากเส้นต่อเนื่องเพราะฐานเวลาไม่เหมือนกัน ป้ายสถานะแต่ละใบมีรูปทรงต่างกัน (ไม่พึ่งสีอย่างเดียว) และ Q1 ถูกแยกเป็น "Bloomberg · reported" ต่างจาก Q2 ที่ยัง "preliminary"',
     'กดแผ่น Q2 หรือปุ่ม "Trace revenue" → retained',
     'ไม่มีภาพจริง (กราฟที่ออกแบบเอง)',
     'หลัง QA (QA-04) แก้สถานะ Q1 จาก preliminary เป็น Bloomberg reported ให้ตรงกับ chart-data.csv'),
    ('retained', '2 — What is retained?',
     'รายได้ที่รายงานยังไม่เท่ากับมูลค่าที่บริษัทเก็บไว้ เพราะขายผ่านช่องทางตรงหรือคลาวด์พาร์ตเนอร์ได้ และลูกค้าสองรายคิดเป็นเกือบหนึ่งในสี่ของรายได้ FY2025 สัดส่วนช่องทางและส่วนแบ่งพาร์ตเนอร์ไม่เปิดเผย จึงไม่ใส่ตัวเลข',
     'เส้นรายได้แยกเป็นสองเส้น (Direct route และ Via cloud partners route) ผ่านประตู partner share ที่ระบุ "Not disclosed" แล้วรวมกันที่ประตู retained-value ซึ่งเส้นขาออกเป็นสีเทาโปร่งเพื่อบอกว่าไม่ทราบขนาด ลูกบาศก์สองก้อนคือลูกค้ารายใหญ่ ไม่ระบุชื่อ',
     'กดวงแหวน retained-value หรือปุ่ม "Follow retained value" → models',
     'ไม่มีภาพจริง',
     'ไม่มี ป้ายชื่อเส้นทางบนมือถือถูกทำให้มองเห็นหลัง QA (QA-03)'),
    ('models', '3 — Model edge meets task cost',
     'ความสามารถของโมเดลกับต้นทุนต่องานเป็นคนละแกน Opus 5.5 = 58 และ Sonnet 5.5 = 56 (Artificial Analysis, max effort) แต่ต้นทุนต่อโจทย์ Sonnet 5.5 $7.60 เทียบ Sonnet 5 $5.09 บนการทดสอบเดียวกัน ส่วนคำอ้างของ Anthropic เรื่องถูกลงเป็นอีกชั้นแยก (คนละฐาน) ไม่ใช่ต้นทุน serving หรือ margin ของบริษัท',
     'แท่งความสามารถซ้าย แท่งต้นทุนต่อโจทย์ขวา แผ่นโปร่งด้านหลังคือคำอ้างของบริษัท ป้ายแยกระบุว่า Fable 5.1 เปิดใช้ทั่วไป (generally available) ส่วน Mythos 5.1 เข้าถึงได้ผ่าน trusted access เท่านั้น (Haiku 5.5 ประกาศแล้วแต่ยังไม่เปิดใช้ อยู่ใน Sources) ลูกบาศก์กลางคือ "งานที่ทำเสร็จ" ปุ่มสลับ Opus / Sonnet เปลี่ยนรายละเอียดราคาและวันเปิดตัวโดยไม่เปลี่ยนฉาก',
     'กดลูกบาศก์งานเสร็จหรือ "Inspect task economics" → statements; ปุ่ม Opus/Sonnet อยู่ในฉากเดิม',
     'ไม่มีภาพจริง ไม่สร้างภาพโมเดลหรือบุคคล',
     'บนมือถือค่าตัวเลขทั้งสี่อยู่ในรายการซ้อนแทนป้ายลอย (QA-02) และเพิ่มป้ายสถานะ Fable/Mythos (QA-06)'),
    ('statements', '4 — Loss is not cash',
     'ขาดทุนจากการดำเนินงาน FY2025 > $8B, ขาดทุนสุทธิ ≈ $42B ซึ่งรวมรายการไม่ใช่เงินสดราว $34B และ Q2 adjusted operating income เป็นบวกแบบเบื้องต้น ทั้งหมดไม่เท่ากับกระแสเงินสดอิสระ ค่า compute $7.33B จากค่าใช้จ่ายรวม $12.65B ใช้เป็นบริบท ไม่ใช่ gross margin',
     'แผ่นบัญชีขนาดเท่ากันวางแยกกัน ไม่เรียงซ้อนให้ดูบวกกัน และไม่ให้ขนาดสื่อความสำคัญ แผ่นสุดท้ายคือ Cash flow เป็นกรอบเส้นประว่าง เขียนว่าไม่เปิดเผยในที่นี้',
     'กดแผ่นกรอบเส้นประ Cash flow หรือ "Look ahead" → capacity',
     'ไม่มีภาพจริง',
     'ไม่มี'),
    ('capacity', '5 — The capacity floor',
     'Reuters รายงานภาระโครงสร้างพื้นฐานอย่างน้อย $518B ในราวหนึ่งทศวรรษ ประมาณ 80% ยกเลิกไม่ได้หรือจ่ายแม้ใช้ไม่ครบ ไม่ใช่ค่าใช้จ่ายรายปี และไม่บวกกับข้อตกลง AWS > $100B ที่อาจทับซ้อนกัน',
     'ทางเดินยาวคือพื้น (floor) ที่คงอยู่ตลอด ริบบิ้นด้านบนคือ demand แบบไม่ระบุขนาด ประตูไกลคือจุดทดสอบ utilization ไม่มีแท่งรายปี',
     'กดประตู utilization หรือ "Test utilization" → scenarios',
     'ภาพถ่ายภายนอก AWS Project Rainier ขนาดเล็กด้านข้าง พร้อมเครดิต "Photo: Amazon Web Services … one partner site. Not the whole arrangement."',
     'ใช้ภาพภายนอกเป็นตัวเลือก (optional) ในขนาดเล็กเพื่อไม่ให้กลบพื้นที่แสดงหลักฐาน'),
    ('scenarios', '6 — Three conditional futures',
     'สามเส้นทางแบบมีเงื่อนไข ไม่ใช่การพยากรณ์ ไม่มีความน่าจะเป็นหรือราคาเป้าหมาย: Upside (retention และ utilization ดี ต้นทุนงานลด), Base (รายได้โตแต่ capacity และค่าช่องทางกลืนกำไร), Downside (utilization หรือราคาตามไม่ทันภาระ)',
     'สามเส้นออกจากจุดเริ่มเดียวกันเหนือพื้น capacity เดียวกัน เมื่อเลือกเส้นหนึ่ง อีกสองเส้นจางลงแต่พื้นยังเห็นครบ (ป้าย ≥ $518B floor อยู่นอกพื้นที่ปุ่ม)',
     'ปุ่ม Upside/Base/Downside หรือคลิกเส้นในฉาก อยู่ฉากเดิม; "What must be disclosed?" → filing',
     'ไม่มีภาพจริง',
     'ย้ายป้าย floor พ้นแถบปุ่มหลัง QA (QA-05)'),
    ('filing', '7 — IPO proof gates',
     'ยังไม่มี S-1 สาธารณะ ราคา จำนวนหุ้น หรือกำหนดเข้าตลาด ต้องดูห้าหมวด: cash flow และ reconciliation, นโยบายรายได้และส่วนแบ่งพาร์ตเนอร์, commitment และ maturity, ความเข้มข้นลูกค้าและ retention, โครงสร้างทุนและหุ้น',
     'ประตูห้าบาน เบื้องหลังยังเห็นเส้น demand และพื้น capacity เดิม ไม่มีเอกสารจำลองหรือโลโก้หน่วยงาน ไม่มีราคาหรือ ticker',
     'ปุ่มเลือกแต่ละประตูแสดงโน้ตสั้นในฉากเดิม; "Return to the question" → close',
     'ไม่มีภาพจริง',
     'ไม่มี'),
    ('close', 'Closing — The test',
     'ทวนคำถาม: demand เห็นแล้ว capacity ผูกไว้แล้ว การแปลงเป็นเงินสดยังต้องมีหลักฐาน',
     'เส้น demand ด้านบนและพื้น capacity ด้านล่าง ช่องว่างระหว่างสองอย่างเป็นกรอบเส้นประ "Unproven Cash conversion" ค้างไว้ ไม่ทำแอนิเมชันปิดช่องว่าง',
     '"Restart" → cover ไม่วนอัตโนมัติ และ Space ในฉากนี้ไม่ทำอะไร',
     'ไม่มีภาพจริง',
     'ไม่มี'),
]

h = []
h.append('<html><head><meta charset="utf-8"><title>06_SCENE_RATIONALE</title></head><body>')
h.append('<h1>06_SCENE_RATIONALE — Anthropic IPO: Capacity Ledger</h1>')
h.append(f'<p><b>เว็บที่ deploy:</b> <a href="{URL}">{URL}</a><br><b>Commit:</b> {SHA}<br><b>Branch:</b> research-ipo-financials-models-2026<br><b>ทิศทางภาพที่เลือก:</b> B "Night blueprint" (เหตุผลและภาพเทียบอยู่ใน BUILD_NOTES.md)<br><b>ข้อมูลถึงวันที่:</b> 29 กันยายน 2026 เวลาไทย ยังไม่มี S-1 สาธารณะ ไม่ใช่คำแนะนำลงทุน</p>')
h.append('<p>เอกสารนี้อธิบาย "สิ่งที่สร้างจริง" ทีละฉาก: จุดประสงค์เชิงแหล่งข้อมูล ความหมายเชิงภาพ การโต้ตอบ เครดิตภาพจริง และสิ่งที่ต่างจากข้อเสนอใน 04_BUILD_WEB.md ภาพหน้าจอ desktop ทุกฉากถ่ายจาก production URL ข้างต้น (ตัว build ที่ระบุ commit) ภาพมือถือแนบเป็นลิงก์ใต้แต่ละฉาก ไฟล์อยู่ที่ build-notes/prod-screens-v2/ บน branch ข้อความบนเว็บเป็นภาษาอังกฤษล้วน ตามที่กำหนด</p>')
h.append('<h2>ภาพรวมการโต้ตอบ</h2><ul><li>Space = ไปฉากถัดไปหนึ่งฉาก (ระหว่างเปลี่ยนฉากจะไม่รับเพิ่ม กันข้ามหรือซ้อนกัน) ที่ฉากสุดท้าย Space ไม่ทำอะไร</li><li>R = กลับ cover จากทุกที่ (รวมระหว่างเปลี่ยนฉากและตอนเปิด overlay) Esc = ปิด overlay</li><li>ปุ่ม Sources / caveats เปิดรายการแหล่งของฉากนั้น พร้อมประเภทหลักฐาน ลิงก์ตรง และข้อควรระวัง</li><li>ตามข้อเสนอแนะของ owner ไม่มีแถบควบคุมถาวรด้านล่างหรือจุดบอกฉากแล้ว: ปุ่มหลักเป็น pill เล็กที่มุมขวาล่าง, ตัวเลือกในฉากเป็นแผงเล็กมุมซ้ายล่าง, ปุ่ม "Scenes" มุมขวาบนเปิดเมนูกระโดดฉากสำหรับซ้อม เส้นทางหลักยังเป็นการกดทีละขั้นโดยผู้นำเสนอ</li><li>โหมด reduced-motion: จุดหมายและสถานะสุดท้ายเหมือนเดิม กล้องเคลื่อนทันที ไม่มีการเต้นของวงแหวน</li></ul>')
h.append('<h2>รายฉาก</h2>')
for sid, title, purpose, visual, inter, asset, dep in scenes:
    h.append(f'<h3>{title} (<code>{sid}</code>)</h3>')
    h.append(f'<p><b>จุดประสงค์เชิงแหล่งข้อมูล:</b> {purpose}</p>')
    h.append(f'<p><b>ความหมายเชิงภาพ:</b> {visual}</p>')
    h.append(f'<p><b>การโต้ตอบ:</b> {inter}</p>')
    h.append(f'<p><b>ภาพจริง/เครดิต:</b> {asset}</p>')
    h.append(f'<p><b>ต่างจาก proposal:</b> {dep}</p>')
    h.append(f'<p><img src="{RAW}b-desk-{sid}.jpg" width="620" alt="{sid} desktop"></p>')
    h.append(f'<p>ภาพมือถือ: <a href="{RAW}b-phone-{sid}.jpg">phone 390×844</a></p>')
h.append('<h2>ภาพเพิ่มเติมจาก production</h2><p>สามสถานะของ scenarios, Sources overlay และเฟรมกลางการเปลี่ยนฉาก (desktop และ phone): ไฟล์ qa-*.jpg ใน <a href=\"https://github.com/Akkhadat12/Anthropic-IPO/tree/research-ipo-financials-models-2026/build-notes/prod-screens-v2\">build-notes/prod-screens-v2</a></p>')
h.append('<h2>ความต่างสำคัญจาก proposal ใน 04_BUILD_WEB.md</h2><ol><li>เป้าหมายหลักของแต่ละฉากมีสองทาง: วัตถุ 3D ที่กดได้ และปุ่มข้อความสำรองเป็น pill เล็กมุมขวาล่าง (เพื่อ accessibility) ไม่มีแถบล่างหรือจุดบอกฉากตามที่ owner สั่ง มีเมนู Scenes เล็ก ๆ ไว้ซ้อมแทน</li><li>ป้ายตัวเลขเป็น HTML ที่ฉายตามตำแหน่ง 3D ไม่ใช่ข้อความในโมเดล 3D เพื่อความคมชัดและให้โปรแกรมอ่านหน้าจออ่านได้</li><li>บนมือถือ (จอแคบ) ป้ายทั้งหมดเปลี่ยนเป็นรายการซ้อนเหนือปุ่ม ส่วน 3D เป็นฉากประกอบ ตามแนวทางเรียบง่ายของ brief</li><li>แยกสถานะ "Bloomberg · reported" (Q1) ออกจาก "Bloomberg · preliminary" (Q2) หลัง QA</li><li>ใช้ภาพภายนอก Project Rainier เป็นตัวเลือกขนาดเล็กใน capacity เท่านั้น</li><li>แหล่ง AWS Project Rainier ใน Sources ใช้ป้าย "Source: AWS" ไม่ใช่ "Anthropic stated" (QA-07)</li></ol>')
h.append('<h2>ข้อจำกัดที่ทราบ</h2><ul><li>ภาพมือถือเป็นลิงก์ ไม่ได้ฝังในเอกสาร</li><li>ถ้อยคำ Fable/Mythos ใน 03_STORY_STRUCTURE.md เป็นหน้าที่ของเจ้าของงานวิจัยแก้ (เว็บระบุตาม QA-06 แล้ว)</li><li>ทดสอบด้วย Edge/Chrome เท่านั้น ยังไม่ได้ทดสอบมือถือจริง Safari Firefox หรือ GPU จริง</li><li>ลิงก์ Reuters (MarketScreener) สองรายการยังต้องให้ QA เปิดยืนยันซ้ำ</li><li>หากมี S-1 สาธารณะก่อนใช้งาน ต้องปรับงานวิจัย ข้อมูลและเว็บทั้งชุด</li></ul>')
h.append('</body></html>')
open('tools/06_SCENE_RATIONALE.html', 'w', encoding='utf-8').write('\n'.join(h))
print(len('\n'.join(h)))
