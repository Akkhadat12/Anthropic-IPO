# Current assignment specification

The shared v1.6 master instructions below are retained verbatim. Placeholder examples in the master are illustrative, not live assignment values. This Current assignment specification and the committed WORKFLOW_STATUS.md carry the live values. No downstream Design/Visual/Build work has been performed.

```yaml
PROJECT_ID: anthropic-ipo-20261001-0426
PROJECT_TITLE: "ก่อน IPO: Anthropic โตแรง แต่กำไรยั่งยืนหรือยัง?"
BOOTSTRAP_MODE: FRESH
AUDIENCE: Thai general audience; no accounting background required
OWNER: UNSET
NARRATION_LANGUAGE: Thai
TARGET_DURATION: 8–10 minutes; editorial scene budgets total 560 seconds; measured read-through NOT_RUN
FORMAT: narration-led local web presentation
DELIVERY_MODE: LOCAL_ZIP
TARGET_OS: Windows
OFFLINE_AFTER_SETUP: true
SCOPE: enterprise demand; revenue/profit/cash distinctions; compute obligations; conditional sustainability tests
OUT_OF_SCOPE: personalized buy/sell advice; price targets; invented audited financials; guessed current segment mix; market-timing forecast
THESIS: "Anthropic เติบโตเร็วและมีสัญญาณ adjusted operating profit ที่ดีขึ้น แต่ความยั่งยืนต้องพิสูจน์ด้วยกำไรสุทธิและเงินสดที่รองรับภาระ compute ตามเวลา"
AUDIENCE_TAKEAWAY: Read financial periods and definitions before treating growth or a single profit/loss headline as sustainable economics.
OWNER_SCOPE_DECISION: APPROVED general audience8–10minutes, ownerreplyดีครับผม
OWNER_THESIS_DECISION: APPROVED title/question above
RESEARCH_AS_OF: 2026-10-01T04:24:00Z
COVER_SCENE_ID: S01
COVER_IMAGE_SUBJECT: authentic official Anthropic or Claude logo from company source
COVER_ASSET_REQUIREMENT: authentic_original_required
COVER_PROVENANCE_CANDIDATE: https://www.anthropic.com/news/confidential-draft-s1-sec
COVER_RIGHTS: Trademark/company-owned; no license assumed. Visual must verify official downloadable asset/usage terms, record provenance/crop/offline path and fallback before READY_FOR_BUILD.
COVER_FALLBACK: Another verified authentic company/product image with usable rights; never generated/reconstructed logo. If none, block Visual readiness.
```

## Evidence architecture

Canonical source register: references/source-register.md. Canonical claim register: references/claim-register.md. Reading editions are generated from the knowledge and analysis sections below; narration is canonical here and mirrored in references/narration.json for reproducibility. All research boundaries remain explicit.

## Story logic

S01 asks the sustainability question → S02 establishes what is confirmed → S03 separates clocks/metrics → S04 asks why customers pay → S05 separates loss from cash → S06 credits newer profit signals and limits → S07 examines capacity obligations → S08 tests conditional scenarios → S09 closes with evidence to watch.

## Owner knowledge edition content

# ทำความเข้าใจ Anthropic ก่อน IPO

ชุดความรู้สำหรับผู้เล่าและผู้ชมทั่วไป

Anthropic ผู้สร้าง Claude มีหลักฐานการเติบโตเร็วและสัญญาณกำไรดำเนินงานแบบปรับปรุงแล้วที่ดีขึ้น แต่ข้อมูลที่เข้าถึงยังไม่พอให้ยืนยันกำไรสุทธิและเงินสดอย่างยั่งยืน ชุดอ่านนี้ช่วยแยกตัวเลขต่างนิยามและต่างช่วงเวลา ก่อนตีความข่าว IPO

## สถานะ IPO ที่ยืนยันได้

Anthropic ประกาศยื่นร่าง S-1 แบบ confidential ต่อ SEC เมื่อ 1 มิถุนายน 2026 โดยจำนวนหุ้นและราคาเสนอขายยังไม่กำหนดในประกาศนั้น การยื่นร่างเป็นขั้นตอนเตรียมเสนอขาย ไม่ใช่หลักฐานว่าการเข้าตลาดเสร็จแล้ว [SRC01]

ข้อมูลที่ Reuters เปิดเผยปลายกันยายนมาจาก prospectus ที่ผู้สื่อข่าวได้อ่าน จึงมีน้ำหนักกว่าเพียงข่าวลือ แต่ทีมยังหาเอกสาร S-1 ฉบับสาธารณะเพื่ออ่านงบและหมายเหตุเต็มโดยตรงไม่พบ ณ วันตัดข้อมูล ข้อจำกัดนี้ไม่ได้แปลว่าไม่มีข้อมูลการเงินเผยแพร่เลย [SRC02, SRC05]

## ข่าวใหม่อาจเป็นข้อมูลของงวดเก่า

FY2025: Reuters รายงานเมื่อ 28–29 กันยายนว่ารายได้เกือบ 4,600 ล้านดอลลาร์ และผลขาดทุนสุทธิราว 42,000 ล้านดอลลาร์ ซึ่งรวมรายการบัญชีไม่ใช่เงินสดราว 34,000 ล้านดอลลาร์ ตัวเลขเหล่านี้เป็นข้อมูลปี 2025 ที่เพิ่งเป็นข่าว [SRC02]

Q2 2026: Bloomberg รายงานเมื่อ 14 สิงหาคมว่ารายได้เบื้องต้นมากกว่า 11,500 ล้านดอลลาร์ และ adjusted operating income เป็นบวก เป็นงวดธุรกิจใหม่กว่า FY2025 แม้ข่าวเผยแพร่ก่อน และตัวเลขยังอาจเปลี่ยน [SRC03]

สิ้นกรกฎาคม 2026: Reuters รายงาน annual revenue run-rate มากกว่า 65,000 ล้านดอลลาร์ คือการปรับจังหวะรายได้ระยะสั้นให้เป็นภาพรายปี ไม่ใช่รายได้ที่รับรู้ครบทั้งปีแล้ว [SRC06]

Q3 2026: ข่าว 13 กันยายนอ้าง FT ว่าบริษัทคาด adjusted operating profit ต่อเนื่องอีกไตรมาส ข่าวก่อนปิดงวดนี้ต้องเรียกว่า outlook ไม่ใช่ผล Q3 ที่ประกาศแล้ว [SRC04]

## คำศัพท์ที่ต้องแยกให้ออก

Revenue คือรายได้ของช่วงเวลาที่ระบุ ส่วน run-rate คือภาพรายปีที่คำนวณจากจังหวะช่วงสั้น การเติบโตของสองชุดนี้ห้ามนำมาเทียบข้ามฐานแล้วเรียก growth ของรายได้ทั้งปี

Adjusted operating income คือกำไรจากการดำเนินงานตามนิยามที่ปรับบางรายการ ต้องเห็นรายการปรับจึงจะเชื่อมกับกำไรตามมาตรฐานบัญชีได้ ส่วน net income ยังรวมรายการนอกการดำเนินงาน ภาษี และผลบัญชีอื่น

Cash flow แสดงการรับและจ่ายเงินจริง ขาดทุนสุทธิไม่เท่ากับ cash burn และหักรายการ non-cash เพียงรายการเดียวก็ยังไม่ใช่งบกระแสเงินสด

Commitment คือข้อผูกพันในอนาคตตามสัญญา ต้องอ่านเงื่อนไข วันครบกำหนด และวิธีรับรู้บัญชี ไม่เท่ากับหนี้ที่ต้องชำระทั้งหมดวันนี้

Private post-money valuation คือมูลค่าบริษัทตามรอบระดมทุนเอกชน ไม่ใช่ราคาเสนอขายหุ้น IPO หรือมูลค่าหุ้นในตลาด และเงินระดมทุนไม่ใช่รายได้จากลูกค้า [SRC09]

## ธุรกิจขายอะไรและข้อจำกัดของข้อมูล

Claude มีบริการผู้ใช้โดยตรง เครื่องมือนักพัฒนา และช่องทางคลาวด์ ในกุมภาพันธ์บริษัทระบุ Claude Code run-rate มากกว่า 2,500 ล้านดอลลาร์ โดย enterprise use มากกว่าครึ่งของรายได้ Claude Code ตัวเลขนี้ยืนยันความสำคัญในเวลานั้น แต่ไม่ใช่ product mix เดือนตุลาคม [SRC07]

Reuters ระบุลูกค้าสองรายคิดเป็นรายได้เกือบหนึ่งในสี่ใน FY2025 ต้องติดป้ายปี 2025 และไม่สมมติว่าความกระจุกตัวปี 2026 เท่าเดิม ยังไม่มี current mix, retention/NRR และข้อมูลรายได้หลังส่วนแบ่งช่องทางเพียงพอในหลักฐานที่ตรวจ [SRC02]

## Compute เป็นโอกาสและความเสี่ยงพร้อมกัน

Compute คือกำลังประมวลผลสำหรับฝึกและให้บริการโมเดล การจองล่วงหน้าอาจช่วยรองรับความต้องการและลดความเสี่ยงขาดกำลังผลิต แต่ถ้าลูกค้าโตช้ากว่าคาด ภาระขั้นต่ำก็อาจกดดันธุรกิจ

Reuters รายงาน commitments อย่างน้อย 518,000 ล้านดอลลาร์ในราวหนึ่งทศวรรษ ประมาณ 80% ยกเลิกไม่ได้หรือจ่ายแม้ไม่ใช้ ตัวเลขนี้ไม่ใช่ค่าใช้จ่ายปีเดียว และยังไม่มีตารางจ่ายรายปีครบพอที่จะหารเฉลี่ยแทนกระแสเงินสดจริง [SRC05]

## อ่านข่าวถัดไปด้วยคำถามสามชุด

หนึ่ง ลูกค้าเดิมยังอยู่และใช้จ่ายเพิ่มไหม บริษัทเหลือรายได้หลังจ่ายช่องทางเท่าไร

สอง กำไรแบบปรับปรุงแล้วต่างจากกำไรสุทธิอย่างไร และการดำเนินงานสร้างหรือใช้เงินสดเท่าไร

สาม ภาระ compute ต้องจ่ายเมื่อไร ปรับลดได้แค่ไหน และใช้กำลังที่จองไว้คุ้มหรือไม่

รายงานนี้เป็นความรู้และการวิเคราะห์ธุรกิจ ไม่ใช่คำแนะนำซื้อขายหรือราคาเป้าหมายหุ้น

## Owner analysis edition content

# วิเคราะห์การเติบโตและความยั่งยืนของ Anthropic

ชุดวิเคราะห์หลักฐาน ข้อโต้แย้ง และเงื่อนไขที่เปลี่ยนข้อสรุป

แกนที่เจ้าของอนุมัติคือ ก่อน IPO Anthropic โตแรง แต่กำไรยั่งยืนหรือยัง สำหรับคนทั่วไปและบทเล่า 8–10 นาที ข้อสรุปที่เหมาะกับหลักฐานคือรายได้โตเร็วและมีสัญญาณ adjusted operating profit แต่ยังต้องตรวจการแปลงเป็นกำไรสุทธิและเงินสด โดยไม่ใช้ผลขาดทุนปีเก่าฟันธงธุรกิจปัจจุบัน

## ระดับหลักฐานและวันตัดข้อมูล

ตัดข้อมูล 1 ตุลาคม 2026 ข้อมูลหลักมาจากประกาศบริษัท Reuters ที่อ่าน confidential prospectus และ Bloomberg ที่อ่านเอกสารนักลงทุน ข่าว Q3 margin เป็น Bloomberg/Reuters อ้าง FT จึงเป็นสายข้อมูลเดียวกัน ไม่ใช่การตรวจงบอิสระหลายชุด [SRC01–SRC07, SRC12]

ทีมอ่านข่าว Bloomberg ฉบับเต็มผ่านบัญชีที่เข้าถึงได้แล้ว แต่ยังไม่มีงบ Anthropic เต็มพร้อมหมายเหตุและความเห็นผู้สอบบัญชี จึงไม่เรียกตัวเลขในข่าวว่า audited ด้วยตัวเอง ผล SEC ที่เป็นเอกสารคู่ค้าและกองทุนไม่ใช่งบ Anthropic [SRC03, SRC04, SRC08]

## แยกแกนเวลา ก่อนตัดสินการเติบโต

FY2025 revenue เกือบ 4,600 ล้านดอลลาร์เป็นผลทั้งปีที่ Reuters เพิ่งรายงานปลายกันยายน ส่วน Q2 2026 revenue เบื้องต้นมากกว่า 11,500 ล้านดอลลาร์เป็นผลช่วงสามเดือนที่ Bloomberg รายงานในสิงหาคม ข่าวล่าสุดกับงวดล่าสุดจึงต้องแยก [SRC02, SRC03]

Run-rate มากกว่า 65,000 ล้านดอลลาร์ ณ สิ้นกรกฎาคมเป็นอัตรารายได้ปรับเป็นรายปี ไม่ใช่ยอด FY2026 ที่รับรู้แล้ว และไม่ใช่ backlog รับประกัน ภาพที่สมเหตุผลคือธุรกิจโตเร็ว ไม่ใช่การสร้าง growth rate ข้ามนิยาม [SRC06]

Series H เดือนพฤษภาคมระดมทุน 65,000 ล้านดอลลาร์ที่ post-money valuation 965,000 ล้านดอลลาร์ เป็นการเงินทุนและมูลค่าเอกชน ไม่ควรนำไปเทียบกับรายได้เดือนอื่นเพื่อฟันธงราคาหุ้น IPO ว่าถูกหรือแพง [SRC09]

## ความต้องการจริงยังต้องผ่านการทดสอบคุณภาพรายได้

Claude Code เป็นหลักฐานเชิงผลิตภัณฑ์ที่มีน้ำหนัก บริษัทประกาศเดือนกุมภาพันธ์ว่า run-rate มากกว่า 2,500 ล้านดอลลาร์ และ enterprise use มากกว่าครึ่งของรายได้ผลิตภัณฑ์ แต่เราไม่ทราบสัดส่วนล่าสุด API, Code, subscriptions และ partner channel แยกกัน [SRC07]

ข้อวิเคราะห์คือเครื่องมือที่ช่วยให้งานสำเร็จและเข้าไปอยู่ในกระบวนการประจำอาจมีโอกาสให้ลูกค้าจ่ายซ้ำ อย่างไรก็ตามยังต้องทดสอบด้วย retention, cohort spending, ความง่ายในการย้ายโมเดล และราคาต่อผลงานที่ใช้ได้จริง ไม่ใช้ความเก่งของ benchmark แทนหลักฐานกำไร

Reuters รายงาน FY2025 ลูกค้าสองรายสร้างรายได้เกือบหนึ่งในสี่และหลายรายไม่มีข้อผูกมัดใช้ต่อระยะยาว นี่เป็นเหตุให้ถามถึงความกระจุกตัว ไม่ใช่หลักฐานว่าลูกค้าจะหายหรือ concentration ปีปัจจุบันเหมือนเดิม [SRC02]

Revenue presentation ผ่านพาร์ตเนอร์อาจต่างกันระหว่างบริษัท ดังนั้น headline revenue ไม่พอสำหรับเปรียบเทียบ economics [SRC10]

## ขาดทุนสุทธิไม่ใช่เงินสดที่ใช้เท่ากัน

Reuters รายงาน net loss FY2025 ราว 42,000 ล้านดอลลาร์ รวมรายการ non-cash ราว 34,000 ล้านดอลลาร์จากการเพิ่มมูลค่าตราสาร financing ที่อาจแปลงเป็นหุ้น Operating loss มากกว่า 8,000 ล้านดอลลาร์มีฐานที่ผู้สื่อข่าวอธิบายแยกต่างหาก [SRC02]

ห้ามใช้ 42,000 ล้านเป็น cash burn หรือเอา 42,000 ลบ 34,000 แล้วตั้งชื่อผลต่างว่า operating cash flow เพราะยังมีเงินทุนหมุนเวียน ค่าเสื่อม หุ้นพนักงาน การจ่ายล่วงหน้า และรายการอื่นซึ่งเราไม่มีข้อมูลครบ

Non-cash ไม่ได้แปลว่าไม่มีความหมายต่อผู้ถือหุ้น รายละเอียดสิทธิแปลงสภาพและ dilution ต้องตรวจจากเอกสารจริงก่อนตีความ ส่วนยอดเงินสดและเงินลงทุนระยะสั้น 20,280 ล้านดอลลาร์ ณ สิ้นปี 2025 ไม่ใช่ยอดเงินคงเหลือเดือนตุลาคม หลังระดมทุนและใช้จ่ายเพิ่มแล้ว [SRC02]

## หลักฐานกำไรใหม่ต้องให้เครดิตและอ่านนิยาม

Bloomberg ระบุ Q2 2026 adjusted operating income เป็นบวก จากเอกสารที่ยังเป็นเบื้องต้น ต่อมา 13 กันยายน Bloomberg อ้าง FT ว่าบริษัทคาด Q3 จะเป็นบวกต่อเนื่อง นี่คือหลักฐานที่ขัดกับการเล่าเรื่องว่าบริษัทยังขาดทุนแบบเดิมในทุกนิยาม [SRC03, SRC04]

แต่ยังไม่มีจำนวน adjusted profit และ reconciliation ทุกรายการไปสู่ GAAP net income หรือ cash flow ข่าว Q3 ก่อนสิ้นงวดจึงเป็น outlook ไม่ใช่ผลจริงที่ยืนยันแล้ว ไม่ควรพูดว่าได้กำไรสองไตรมาสแล้วโดยไม่มี caveat

ข่าวเดียวกันระบุ gross margin มากกว่า 80% ก่อน partner revenue-sharing และ model training costs ห้ามเรียกว่ากำไรหลังต้นทุนทุกอย่าง และห้ามอนุมานว่า adjusted operating income ตัดค่าใช้จ่ายสองกลุ่มนี้ด้วย เพราะนิยาม gross margin ไม่เท่ากับนิยาม operating income [SRC04]

## ภาระกำลังผลิตมีทั้งขนาด ระยะเวลา และเงื่อนไข

Reuters ระบุภาระอย่างน้อย 518,000 ล้านดอลลาร์ในราวสิบปี ประมาณ 80% ยกเลิกไม่ได้หรือจ่ายแม้ไม่ใช้ ช่วงสัญญา Google เม.ย. 2026–ก.ค. 2033, Amazon พ.ค. 2026–เม.ย. 2036 และ Microsoft พ.ย. 2026–พ.ค. 2033 ยังไม่ใช่ cash-maturity schedule รายปี [SRC05]

บทวิเคราะห์ต้องเห็นทั้งสองด้าน การจองกำลังผลิตอาจเป็นข้อได้เปรียบถ้าความต้องการสูงและ compute ขาดแคลน แต่ทำให้ความผิดพลาดในการคาด demand มีต้นทุน ภาระ xAI ที่รายงานว่าส่วนใหญ่ยกเลิกได้ด้วย notice 90 วันก็ไม่แข็งตัวเท่าก้อนอื่น [SRC05]

หลักฐานสาธารณะจาก Akamai 8-K วันที่ 24 กันยายนระบุ commitment 11,600 ล้านดอลลาร์ ระยะเริ่มต้นเจ็ดปีนับจากวันเริ่มบริการ โดยขึ้นกับการส่งมอบและ availability พร้อมสิทธิยกเลิกตามเหตุผิดสัญญา/ระบบขัดข้องบางกรณี ไม่ใช่การรับประกันว่าปรับลดได้ตามใจ [SRC08]

ยัง reconcile ก้อน Akamai กับยอดรวม Reuters ไม่ได้ จึงไม่บวกยอดใหม่เอง ประกาศ AWS เดิมมากกว่า 100,000 ล้านดอลลาร์ก็อาจทับกับก้อน Amazon ในยอดรวม ไม่ใช่ภาระเพิ่มอีกก้อน ส่วน capex ของผู้ขายเป็นต้นทุนผู้ขาย ไม่ใช่ commitment เพิ่มของ Anthropic [SRC08, SRC11]

## สามสถานการณ์เพื่อทดสอบ ไม่ใช่การพยากรณ์

เติบโตพร้อมสร้างเงินสด หากลูกค้าใช้ซ้ำ รายได้สุทธิหลังช่องทางโต ต้นทุนต่องานลด และ capacity ถูกใช้งานคุ้ม จะสนับสนุนความยั่งยืน ต้องเห็น reconciliation และ cash flow ดีขึ้นจริง

โตดีแต่ยังต้องเติมทุน หากรายได้เพิ่มแต่ต้องลงทุน training และ capacity ต่อเนื่อง adjusted profit อาจดีขึ้นขณะที่ free cash flow ยังติดลบ เราไม่ถือความต้องการทุนต่อเป็นความล้มเหลวโดยอัตโนมัติ

Demand หรือราคาขายต่ำกว่าที่วางแผน หากลูกค้าหลักลดใช้ คู่แข่งกดราคา หรือ capacity ใช้ไม่เต็ม ภาระขั้นต่ำอาจกดดันเงินสด ต้องทดสอบด้วย utilization, concentration และ maturity schedule

สถานการณ์เหล่านี้เป็นข้อวิเคราะห์ ไม่ใส่ความน่าจะเป็น ราคาเป้าหมาย หรือเส้น forecast ที่ไม่มีแหล่ง

## อะไรจะเปลี่ยนข้อสรุป

ข้อสรุปจะแข็งแรงขึ้นถ้าเอกสารเปิดเผยแสดงรายได้ที่รักษาลูกค้าได้ รายได้หลังส่วนแบ่งช่องทางที่โต พร้อม GAAP profit และ cash generation ที่สอดคล้องกับ commitments ตามกำหนด

ข้อสรุปจะอ่อนลงถ้า concentration เพิ่ม ต้นทุนขั้นต่ำและเงินจ่ายล่วงหน้าโตเร็วกว่ารายได้สุทธิ หรือ margin ที่ปรับรายการไว้ไม่แปลงเป็น cash flow

รายการที่ยังไม่ทราบอย่างชัดเจนคือ current product/channel mix, current concentration, NRR/churn, full adjusted-to-GAAP bridge, cash-flow statement งวดล่าสุด, commitment annual maturities และเงื่อนไขเสนอขายสุดท้าย ข้อมูลที่ขาดไม่ใช่หลักฐานว่าธุรกิจไม่ดี แต่เป็นขอบเขตความเชื่อมั่นของการวิเคราะห์

ข้อสรุปของเรื่องคือมีสัญญาณการเติบโตและ adjusted operating profit ที่ดีขึ้น แต่ความยั่งยืนยังต้องพิสูจน์ด้วยกำไรและเงินสดหลังต้นทุนที่เกี่ยวข้องทั้งหมด

## Complete narration and content scene specifications

Spacebar is the full forward route: reveal/settle/hold/advance. Each beat holds indefinitely for narration; no auto timing. R returns to S01 initial state with authentic cover visible. Cues here are semantic intentions only; Design/Visual decide the presentation without changing claims.

## S01 คำถามเปิดเรื่อง

SCENE_PURPOSE: ทำให้ผู้ชมเข้าใจตั้งแต่ต้นว่าเราจะตรวจความสัมพันธ์ระหว่างการเติบโตกับความยั่งยืนของธุรกิจ ใช้โลโก้หรือ wordmark ของ Anthropic หรือ Claude จากแหล่งทางการอย่างแท้จริงเพื่อระบุเจ้าของเรื่อง ไม่วาดเลียนแบบและไม่สื่อถึงการรับรองคลิปโดยบริษัท หากใช้ wordmark หนึ่งชื่อ ต้องนับเพิ่มในงบข้อความภาพอนาคตจาก 7 เป็น 8 หน่วย; อย่าเพิ่มทั้งสองชื่อโดยไม่ปรับข้อความอื่น
CLAIM_IDS: [C02, C03, C04, C05]
ESTIMATED_SPOKEN_SECONDS: 30 (editorial budget; no audio measured)
PRESENTER_CUES: เว้นสั้น ๆ หลังคำถามแรก,ไม่เน้นคำว่าขาดทุนจนกลบข่าวด้านบวก
VISUAL_JOB: ทำให้ผู้ชมเข้าใจตั้งแต่ต้นว่าเราจะตรวจความสัมพันธ์ระหว่างการเติบโตกับความยั่งยืนของธุรกิจ ใช้โลโก้หรือ wordmark ของ Anthropic หรือ Claude จากแหล่งทางการอย่างแท้จริงเพื่อระบุเจ้าของเรื่อง ไม่วาดเลียนแบบและไม่สื่อถึงการรับรองคลิปโดยบริษัท หากใช้ wordmark หนึ่งชื่อ ต้องนับเพิ่มในงบข้อความภาพอนาคตจาก 7 เป็น 8 หน่วย; อย่าเพิ่มทั้งสองชื่อโดยไม่ปรับข้อความอื่น
VISIBLE_COPY_PROPOSAL: โตแรง แต่ กำไร ยั่งยืน หรือยัง?
VISIBLE_WORD_COUNT: 7
COUNT_METHOD: โต,แรง,แต่,กำไร,ยั่งยืน,หรือ,ยัง
ESSENTIAL_DATA_LABELS: NONE proposed at Content stage. If Visual uses data, its minimum value/unit/period labels must map to the claims and be justified, not disguised prose.
ESSENTIAL_LABEL_REASON: NOT_APPLICABLE until a data visual is chosen.
TOTAL_VISIBLE_WORD_COUNT: 7 ordinary copy + 1 official wordmark = 8 maximum; if logo wordmark longer reduce ordinary copy
FACTUAL_BOUNDARIES: wordmark ที่เพิ่มภายหลังต้องนับในงบข้อความบนภาพ,ใช้โลโก้จากแหล่งทางการ ไม่สร้างเครื่องหมายเลียนแบบ
TRANSITION_REASON: Next audience question: ก่อน IPO เรารู้อะไรจริง

NARRATION:

ถ้าบริษัท AI มีรายได้โตเร็วมาก แต่ขณะเดียวกันก็ต้องจองกำลังประมวลผลล่วงหน้าเป็นเวลาหลายปี เราควรมองว่านี่คือธุรกิจที่กำลังแข็งแรงขึ้น หรือกำลังรับความเสี่ยงมากขึ้น?

Anthropic บริษัทผู้สร้าง Claude ทำให้คำถามนี้น่าสนใจ เพราะตัวเลขที่เป็นข่าวมีทั้งรายได้พุ่ง ขาดทุนก้อนใหญ่ และกำไรจากการดำเนินงานแบบปรับปรุงแล้ว

วันนี้เราจะค่อย ๆ แยกว่าตัวเลขเหล่านี้บอกอะไร ก่อนตอบคำถามว่า Anthropic โตแรงแล้ว แต่กำไรยั่งยืนหรือยัง


## S02 ก่อน IPO เรารู้อะไรจริง

SCENE_PURPOSE: แยกเหตุการณ์ที่บริษัทยืนยันแล้วออกจากเงื่อนไข IPO ที่ยังไม่ยืนยัน และแสดงขอบเขตของเอกสารที่เราเข้าถึง
CLAIM_IDS: [C01, C02, C10]
ESTIMATED_SPOKEN_SECONDS: 55 (editorial budget; no audio measured)
PRESENTER_CUES: เน้นความต่างระหว่างยื่นร่างกับราคาเสนอขาย,ไม่เปลี่ยนเป็นบทสอนขั้นตอน IPO ยาว ๆ
VISUAL_JOB: แยกเหตุการณ์ที่บริษัทยืนยันแล้วออกจากเงื่อนไข IPO ที่ยังไม่ยืนยัน และแสดงขอบเขตของเอกสารที่เราเข้าถึง
VISIBLE_COPY_PROPOSAL: ยื่นร่างแล้ว ยังไม่รู้ราคาขาย
VISIBLE_WORD_COUNT: 8
COUNT_METHOD: ยื่น,ร่าง,แล้ว,ยัง,ไม่,รู้,ราคา,ขาย
ESSENTIAL_DATA_LABELS: NONE proposed at Content stage. If Visual uses data, its minimum value/unit/period labels must map to the claims and be justified, not disguised prose.
ESSENTIAL_LABEL_REASON: NOT_APPLICABLE until a data visual is chosen.
TOTAL_VISIBLE_WORD_COUNT: 8
FACTUAL_BOUNDARIES: กล่าวว่ายังหาเอกสารสาธารณะฉบับเต็มไม่พบ ไม่สรุปว่าไม่มีข้อมูลการเงินสาธารณะ,ไม่ยืนยันวัน IPO หรือ offer terms
TRANSITION_REASON: Next audience question: ตัวเลขสามแบบ อย่าอ่านแทนกัน

NARRATION:

เริ่มจากสถานะ IPO ก่อน วันที่ 1 มิถุนายน 2026 Anthropic ประกาศว่าได้ยื่นร่างเอกสาร S-1 ต่อหน่วยงานกำกับหลักทรัพย์สหรัฐฯ แบบเป็นความลับแล้ว

พูดง่าย ๆ คือบริษัทเริ่มขั้นตอนเตรียมเข้าตลาดหุ้น แต่ยังไม่ได้แปลว่ามีวันขายหุ้น จำนวนหุ้น หรือราคาเสนอขายที่ยืนยันเรียบร้อย

ส่วนข้อมูลการเงินที่เป็นข่าวปลายเดือนกันยายน มาจาก Reuters ซึ่งรายงานว่าได้อ่านเอกสารเสนอขายของบริษัท นี่จึงมีน้ำหนักมากกว่าข่าวลือทั่วไป

แต่ต้องรักษาเส้นแบ่งไว้ด้วยว่า ณ วันที่ 1 ตุลาคม เรายังหาเอกสาร S-1 ฉบับสาธารณะที่เปิดอ่านงบเต็มและหมายเหตุด้วยตัวเองไม่พบ

ดังนั้น ในคลิปนี้เราจะระบุให้ชัดว่าอะไรเป็นประกาศจากบริษัท อะไรเป็นข้อมูลที่สื่อรายงานจากเอกสาร และอะไรยังเป็นความคาดหมาย

เพราะสำหรับธุรกิจที่เปลี่ยนเร็วมาก การรู้ว่าตัวเลขมาจากไหน และเป็นของช่วงเวลาไหน สำคัญพอ ๆ กับขนาดของตัวเลขเลย


## S03 ตัวเลขสามแบบ อย่าอ่านแทนกัน

SCENE_PURPOSE: อธิบายช่วงเวลาที่ตัวเลขแต่ละชนิดครอบคลุม เพื่อป้องกันการนำยอดรายปี รายไตรมาส และ run-rate มาเทียบตรง ๆ
CLAIM_IDS: [C02, C03, C06]
ESTIMATED_SPOKEN_SECONDS: 75 (editorial budget; no audio measured)
PRESENTER_CUES: หยุดสั้นหลังตัวเลขแต่ละชุด,อ่าน run-rate แล้วอธิบายภาษาไทยทันที
VISUAL_JOB: อธิบายช่วงเวลาที่ตัวเลขแต่ละชนิดครอบคลุม เพื่อป้องกันการนำยอดรายปี รายไตรมาส และ run-rate มาเทียบตรง ๆ
VISIBLE_COPY_PROPOSAL: คนละช่วงเวลา คนละความหมาย
VISIBLE_WORD_COUNT: 5
COUNT_METHOD: คนละ,ช่วง,เวลา,คนละ,ความหมาย
ESSENTIAL_DATA_LABELS: NONE proposed at Content stage. If Visual uses data, its minimum value/unit/period labels must map to the claims and be justified, not disguised prose.
ESSENTIAL_LABEL_REASON: NOT_APPLICABLE until a data visual is chosen.
TOTAL_VISIBLE_WORD_COUNT: 5
FACTUAL_BOUNDARIES: ไม่คำนวณ growth rate ข้ามฐานเวลา,ไม่ annualize Q2 เพิ่มเอง,ข้อความตัวเลขหรือวันที่ที่จะเพิ่มบนภาพต้องนับรวมในงบซีน
TRANSITION_REASON: Next audience question: ลูกค้าจ่ายเงินให้ Claude เพราะอะไร

NARRATION:

ลองดูตัวเลขสามชุดที่อาจทำให้เรารู้สึกเหมือนกำลังอ่านคนละบริษัท

ชุดแรก Reuters รายงานปลายเดือนกันยายนว่า Anthropic มีรายได้ปี 2025 เกือบ 4,600 ล้านดอลลาร์ นี่เป็นรายได้ของปีที่จบไปแล้ว

ชุดที่สอง Bloomberg รายงานเมื่อวันที่ 14 สิงหาคมว่า รายได้เบื้องต้นของไตรมาสสองปี 2026 สูงกว่า 11,500 ล้านดอลลาร์ โดยตัวเลขยังอาจเปลี่ยนได้

แปลว่า แม้ข่าวรายได้ปี 2025 จะเพิ่งออก แต่ตัวเลขไตรมาสสองเป็นข้อมูลของงวดธุรกิจที่ใหม่กว่า ข่าวล่าสุดกับงวดล่าสุดจึงไม่ใช่อย่างเดียวกัน

ส่วนชุดที่สาม Reuters รายงานวันที่ 17 สิงหาคมว่า ณ สิ้นเดือนกรกฎาคม รายได้แบบ annual run-rate สูงกว่า 65,000 ล้านดอลลาร์แล้ว

Run-rate คือการนำจังหวะรายได้ในช่วงหนึ่งมาปรับให้เป็นภาพรายปี ไม่ใช่รายได้ที่บริษัทรับรู้ครบทั้งปีไปแล้ว และไม่ใช่คำรับประกันว่าทั้งปีจะทำได้เท่านั้น

ทั้งสามตัวเลขสะท้อนภาพการเติบโต แต่ใช้ตอบคำถามต่างกัน

ถ้าเรานำ run-rate ไปหารรายได้ของปีก่อน แล้วเล่าว่าเป็นการเติบโตของรายได้ทั้งปี ก็จะทำให้ภาพดูแน่นอนกว่าหลักฐานที่มี

สิ่งที่ควรเห็นตอนนี้คือ ธุรกิจขยายตัวเร็วมาก และเราต้องติดป้ายช่วงเวลาให้ถูกก่อนวิเคราะห์ว่าการเติบโตนั้นมีคุณภาพแค่ไหน


## S04 ลูกค้าจ่ายเงินให้ Claude เพราะอะไร

SCENE_PURPOSE: เชื่อมการใช้งานกับเหตุผลที่องค์กรยอมจ่าย พร้อมแยกหลักฐานการยอมรับผลิตภัณฑ์ออกจากหลักฐานการรักษาลูกค้า
CLAIM_IDS: [C07, C08, C11]
ESTIMATED_SPOKEN_SECONDS: 65 (editorial budget; no audio measured)
PRESENTER_CUES: ใช้ภาพตัวอย่างงานเพื่อช่วยความเข้าใจ แต่ไม่อ้างว่าเป็นลูกค้าจริงหรือผลสำเร็จที่วัดแล้ว
VISUAL_JOB: เชื่อมการใช้งานกับเหตุผลที่องค์กรยอมจ่าย พร้อมแยกหลักฐานการยอมรับผลิตภัณฑ์ออกจากหลักฐานการรักษาลูกค้า
VISIBLE_COPY_PROPOSAL: ลูกค้า จ่ายซ้ำ เพราะอะไร?
VISIBLE_WORD_COUNT: 5
COUNT_METHOD: ลูกค้า,จ่าย,ซ้ำ,เพราะ,อะไร
ESSENTIAL_DATA_LABELS: NONE proposed at Content stage. If Visual uses data, its minimum value/unit/period labels must map to the claims and be justified, not disguised prose.
ESSENTIAL_LABEL_REASON: NOT_APPLICABLE until a data visual is chosen.
TOTAL_VISIBLE_WORD_COUNT: 5
FACTUAL_BOUNDARIES: ไม่สร้าง pie chart current revenue mix,ไม่ถือ enterprise use เป็นบริษัทลูกค้าใหม่ทั้งหมด,ไม่ยืด customer concentration ปี 2025 ไปปี 2026
TRANSITION_REASON: Next audience question: ขาดทุนก้อนใหญ่ ไม่ใช่เงินสดที่หายไปเท่ากัน

NARRATION:

แล้วรายได้ที่โตขึ้นมาจากอะไร?

Claude มีทั้งบริการให้คนใช้งานโดยตรง เครื่องมือสำหรับนักพัฒนา และการเข้าถึงผ่านช่องทางคลาวด์ แต่ข้อมูลที่มีตอนนี้ยังไม่พอให้เราแบ่งสัดส่วนรายได้ล่าสุดของแต่ละส่วนอย่างมั่นใจ

หลักฐานชิ้นหนึ่งที่น่าสนใจคือ ในเดือนกุมภาพันธ์ 2026 บริษัทประกาศว่า Claude Code มีรายได้แบบ run-rate มากกว่า 2,500 ล้านดอลลาร์ และมากกว่าครึ่งของรายได้ Claude Code มาจากการใช้งานระดับองค์กร

ตัวเลขนี้บอกว่าเครื่องมือช่วยเขียนโค้ดมีบทบาทสำคัญ แต่ต้องจำว่าเป็นภาพ ณ เดือนกุมภาพันธ์ ไม่ใช่สัดส่วนล่าสุดของเดือนตุลาคม

ในทางธุรกิจ เหตุผลที่องค์กรอาจยอมจ่ายต่อเนื่อง คือเครื่องมือช่วยให้งานเสร็จเร็วขึ้น ลดงานซ้ำ หรือเข้าไปเป็นส่วนหนึ่งของกระบวนการทำงานจริง

แต่คำว่า ‘อาจ’ ยังสำคัญ เราต้องดูต่อว่าลูกค้าเดิมอยู่ต่อแค่ไหน ใช้จ่ายเพิ่มหรือเปล่า และย้ายไปใช้คู่แข่งได้ง่ายเพียงใด

อีกด้าน Reuters รายงานว่าปี 2025 ลูกค้าเพียงสองรายสร้างรายได้เกือบหนึ่งในสี่ของบริษัท

นี่คือความกระจุกตัวที่ควรติดตาม แต่ยังไม่ควรสมมติว่าสัดส่วนของปี 2026 เหมือนเดิม

รายได้โตจึงเป็นจุดเริ่มต้น คำถามถัดไปคือ ลูกค้ากลุ่มไหนจะจ่ายซ้ำ และจ่ายต่อเนื่องได้นานแค่ไหน


## S05 ขาดทุนก้อนใหญ่ ไม่ใช่เงินสดที่หายไปเท่ากัน

SCENE_PURPOSE: แยกผลขาดทุนทางบัญชีออกจากเงินสด โดยไม่ทำให้ผู้ชมเข้าใจว่ารายการ non-cash ไม่มีความสำคัญ
CLAIM_IDS: [C02, C12]
ESTIMATED_SPOKEN_SECONDS: 65 (editorial budget; no audio measured)
PRESENTER_CUES: อ่านตัวเลขชัดแต่ไม่เร่ง,เว้นหลังคำว่าไม่ใช่เงินสดเพื่อให้ผู้ชมแยกแนวคิดทัน
VISUAL_JOB: แยกผลขาดทุนทางบัญชีออกจากเงินสด โดยไม่ทำให้ผู้ชมเข้าใจว่ารายการ non-cash ไม่มีความสำคัญ
VISIBLE_COPY_PROPOSAL: ขาดทุน ไม่เท่ากับ เงินสดที่ใช้
VISIBLE_WORD_COUNT: 6
COUNT_METHOD: ขาดทุน,ไม่,เท่ากับ,เงินสด,ที่,ใช้
ESSENTIAL_DATA_LABELS: NONE proposed at Content stage. If Visual uses data, its minimum value/unit/period labels must map to the claims and be justified, not disguised prose.
ESSENTIAL_LABEL_REASON: NOT_APPLICABLE until a data visual is chosen.
TOTAL_VISIBLE_WORD_COUNT: 6
FACTUAL_BOUNDARIES: ไม่เรียกผลต่างว่า cash burn, operating loss หรือ adjusted loss ที่คำนวณยืนยันแล้ว,ไม่ใช้ผลปี 2025 สรุปสถานะปัจจุบันทุกนิยาม
TRANSITION_REASON: Next audience question: ต้องให้เครดิตข่าวกำไรด้วย

NARRATION:

ทีนี้มาถึงตัวเลขที่สะดุดตาที่สุด คือผลขาดทุนสุทธิปี 2025 ราว 42,000 ล้านดอลลาร์ ตามรายงานของ Reuters

ถ้าอ่านแค่พาดหัว เราอาจนึกว่าบริษัทใช้เงินสดไปเท่านั้นในปีเดียว แต่รายละเอียดสำคัญมาก

Reuters ระบุว่าตัวเลขนี้รวมค่าใช้จ่ายทางบัญชีที่ไม่ใช่เงินสดราว 34,000 ล้านดอลลาร์ ซึ่งเกี่ยวข้องกับการเพิ่มมูลค่าของตราสารจัดหาเงินทุนที่อาจแปลงเป็นหุ้น

หมายความว่า ผลขาดทุนก้อนใหญ่นี้ส่วนหนึ่งเกิดจากวิธีบันทึกมูลค่าทางบัญชี ไม่ใช่เงินสดที่ไหลออกไปซื้อกำลังประมวลผลทั้งหมดในปีนั้น

แต่ก็ไม่ควรสรุปกลับด้านว่า ถ้าไม่ใช่เงินสดก็ไม่ต้องสนใจ เพราะรายละเอียดของเงินทุนและการแปลงเป็นหุ้นอาจมีความหมายต่อผู้ถือหุ้นได้

และเราไม่ควรหยิบ 42,000 ลบ 34,000 แล้วเรียกส่วนที่เหลือว่า cash burn เพราะกำไรขาดทุนกับกระแสเงินสดยังมีรายการต่างกันอีก

สิ่งที่ต้องการจริง ๆ คืองบกระแสเงินสด และคำอธิบายว่าผลขาดทุนทางบัญชีเชื่อมไปถึงเงินสดที่ใช้จริงอย่างไร

ตัวเลขปี 2025 จึงบอกว่ามีต้นทุนและประเด็นบัญชีขนาดใหญ่ แต่ยังใช้ตอบไม่ได้ว่าธุรกิจปัจจุบันใช้เงินสดเท่าไร หรือทำกำไรแล้วหรือยัง


## S06 ต้องให้เครดิตข่าวกำไรด้วย

SCENE_PURPOSE: แสดงระยะห่างของหลักฐานระหว่าง adjusted operating income, net income และ cash flow โดยไม่สมมติจำนวนเงินหรือรายการ reconciliation
CLAIM_IDS: [C03, C04, C09, C12]
ESTIMATED_SPOKEN_SECONDS: 75 (editorial budget; no audio measured)
PRESENTER_CUES: น้ำเสียงเป็นบวกจริงในครึ่งแรก,ไม่ใช้ประโยคแต่ลบล้างข่าวกำไรทั้งหมด
VISUAL_JOB: แสดงระยะห่างของหลักฐานระหว่าง adjusted operating income, net income และ cash flow โดยไม่สมมติจำนวนเงินหรือรายการ reconciliation
VISIBLE_COPY_PROPOSAL: กำไรปรับปรุงแล้ว ถึง เงินสด หรือยัง?
VISIBLE_WORD_COUNT: 7
COUNT_METHOD: กำไร,ปรับปรุง,แล้ว,ถึง,เงินสด,หรือ,ยัง
ESSENTIAL_DATA_LABELS: NONE proposed at Content stage. If Visual uses data, its minimum value/unit/period labels must map to the claims and be justified, not disguised prose.
ESSENTIAL_LABEL_REASON: NOT_APPLICABLE until a data visual is chosen.
TOTAL_VISIBLE_WORD_COUNT: 7
FACTUAL_BOUNDARIES: Q2 เป็น preliminary,Q3 เป็น outlook,ไม่อ้างว่า reported >80% เป็น all-in margin หรือ adjusted operating margin,ไม่อนุมาน exclusions ของ gross margin ไปยัง adjusted operating income
TRANSITION_REASON: Next audience question: Compute เป็นทั้งกำลังผลิตและภาระล่วงหน้า

NARRATION:

ถ้าเล่าเฉพาะขาดทุนปี 2025 เรื่องนี้ก็จะไม่ครบ เพราะมีข้อมูลด้านบวกที่ใหม่กว่านั้น

Bloomberg รายงานวันที่ 14 สิงหาคมว่า ไตรมาสสองปี 2026 Anthropic มีกำไรจากการดำเนินงานแบบปรับปรุงแล้วเป็นบวก แม้ตัวเลขในเอกสารขณะนั้นยังเป็นข้อมูลเบื้องต้น

และวันที่ 13 กันยายน มีรายงานอ้าง Financial Times ว่าบริษัทบอกผู้ถือหุ้นว่า คาดว่าจะทำกำไรในนิยามนี้ต่อเนื่องเป็นไตรมาสที่สองในไตรมาสสาม

นี่เป็นสัญญาณที่ควรให้เครดิต เพราะชี้ว่าภาพธุรกิจอาจเปลี่ยนไปมากจากปีก่อน

แต่คำสำคัญมีสองคำ คือ ‘ปรับปรุงแล้ว’ และ ‘คาดว่า’

กำไรแบบปรับปรุงแล้วอาจช่วยให้เห็นการดำเนินงานตามมุมมองที่บริษัทใช้ แต่เรายังต้องรู้ว่าปรับรายการอะไรออก และมีจำนวนเท่าไร จึงจะเชื่อมไปถึงกำไรสุทธิตามมาตรฐานบัญชีได้

ส่วนข่าวไตรมาสสามเป็นความคาดหมายที่รายงานก่อนปิดงวด เราจึงยังไม่ควรพูดเหมือนเป็นผลประกอบการที่ประกาศแล้ว

ข่าวเดียวกันยังกล่าวถึงอัตรากำไรขั้นต้นสูงกว่า 80 เปอร์เซ็นต์ แต่ตัวเลขนั้นไม่รวมส่วนแบ่งรายได้ให้พาร์ตเนอร์และต้นทุนฝึกโมเดล จึงไม่ใช่อัตรากำไรหลังต้นทุนทุกอย่าง

และต้องระวังอีกชั้นว่า การตัดรายการออกจากอัตรากำไรขั้นต้น ไม่ได้พิสูจน์ว่ารายการเดียวกันถูกตัดออกจากกำไรดำเนินงานด้วย

ข้อสรุปที่พอดีกับหลักฐานคือ มีสัญญาณดีขึ้น แต่เรายังต้องเห็นสะพานจากกำไรแบบปรับปรุงแล้ว ไปถึงกำไรสุทธิและเงินสดจริง


## S07 Compute เป็นทั้งกำลังผลิตและภาระล่วงหน้า

SCENE_PURPOSE: ทำให้เห็นว่ากำลังประมวลผลรองรับรายได้ในอนาคต แต่มีภาระหลายปีและเงื่อนไขความยืดหยุ่นไม่เท่ากัน
CLAIM_IDS: [C05, C13]
ESTIMATED_SPOKEN_SECONDS: 75 (editorial budget; no audio measured)
PRESENTER_CUES: เน้นหลายปีและเงื่อนไขต่างกัน,ให้พื้นที่กับประโยชน์ของ capacity ก่อนพูดความเสี่ยง
VISUAL_JOB: ทำให้เห็นว่ากำลังประมวลผลรองรับรายได้ในอนาคต แต่มีภาระหลายปีและเงื่อนไขความยืดหยุ่นไม่เท่ากัน
VISIBLE_COPY_PROPOSAL: จองกำลังผลิต รับภาระล่วงหน้า
VISIBLE_WORD_COUNT: 6
COUNT_METHOD: จอง,กำลัง,ผลิต,รับ,ภาระ,ล่วงหน้า
ESSENTIAL_DATA_LABELS: NONE proposed at Content stage. If Visual uses data, its minimum value/unit/period labels must map to the claims and be justified, not disguised prose.
ESSENTIAL_LABEL_REASON: NOT_APPLICABLE until a data visual is chosen.
TOTAL_VISIBLE_WORD_COUNT: 6
FACTUAL_BOUNDARIES: ไม่บวก partnership announcements ซ้ำ,ไม่สร้าง annual payment schedule,ไม่ตีความ commitments ทั้งหมดเป็นหนี้ทางบัญชี
TRANSITION_REASON: Next audience question: สองด้านของโอกาสเดียวกัน

NARRATION:

ต่อให้มีคนอยากใช้ Claude เพิ่มขึ้น บริษัทก็ต้องมีกำลังประมวลผลเพียงพอ ทั้งเพื่อให้บริการและพัฒนาโมเดลต่อไป

การจอง compute ล่วงหน้าจึงมีเหตุผลทางธุรกิจ ถ้าความต้องการโตจริงและกำลังประมวลผลมีจำกัด บริษัทที่มีความพร้อมอาจรับลูกค้าได้มากกว่า

แต่อีกด้านหนึ่งคือภาระที่ต้องรับไว้ก่อน

Reuters รายงานวันที่ 29 กันยายนว่า Anthropic มี commitments อย่างน้อย 518,000 ล้านดอลลาร์ในช่วงราวหนึ่งทศวรรษ และประมาณ 80 เปอร์เซ็นต์มีลักษณะยกเลิกไม่ได้ หรืออาจต้องจ่ายแม้ไม่ได้ใช้

ตัวเลขนี้ใหญ่ แต่ต้องอ่านให้ถูกว่าเป็นภาระในอนาคตหลายปี ไม่ใช่ค่าใช้จ่ายหรือเงินสดที่ใช้ในปีเดียว และเราไม่ควรหารสิบแล้วสมมติว่าจ่ายเท่ากันทุกปี

สัญญาแต่ละก้อนก็มีความยืดหยุ่นต่างกัน ตัวอย่างเช่น Reuters รายงานว่าสัญญากับ xAI ส่วนใหญ่สามารถยกเลิกได้ด้วยการแจ้งล่วงหน้า 90 วัน จึงไม่ควรรวมทุกก้อนแล้วมองว่าแข็งตัวเท่ากันหมด

คำถามที่สำคัญกว่าขนาดยอดรวม คือเมื่อถึงเวลาต้องจ่าย บริษัทจะมีรายได้และเงินสดรองรับแค่ไหน ใช้กำลังที่จองไว้คุ้มเพียงใด และปรับลดภาระได้มากน้อยเท่าไร

ถ้าความต้องการโตทัน นี่อาจเป็นความพร้อมที่มีค่า แต่ถ้าโตช้ากว่าที่วางไว้ ภาระล่วงหน้าก็อาจกดดันบริษัทได้


## S08 สองด้านของโอกาสเดียวกัน

SCENE_PURPOSE: เปรียบเทียบสถานการณ์เชิงเงื่อนไขโดยไม่ให้น้ำหนักความน่าจะเป็นหรือ forecast ตัวเลขที่ไม่มีหลักฐาน
CLAIM_IDS: [A01]
ESTIMATED_SPOKEN_SECONDS: 60 (editorial budget; no audio measured)
PRESENTER_CUES: แต่ละสถานการณ์ใช้น้ำหนักเสียงใกล้เคียงกัน,ไม่ทำฝั่งใดเป็นข้อสรุป
VISUAL_JOB: เปรียบเทียบสถานการณ์เชิงเงื่อนไขโดยไม่ให้น้ำหนักความน่าจะเป็นหรือ forecast ตัวเลขที่ไม่มีหลักฐาน
VISIBLE_COPY_PROPOSAL: โตทันต้นทุน หรือ ต้องเติมทุน?
VISIBLE_WORD_COUNT: 7
COUNT_METHOD: โต,ทัน,ต้นทุน,หรือ,ต้อง,เติม,ทุน
ESSENTIAL_DATA_LABELS: NONE proposed at Content stage. If Visual uses data, its minimum value/unit/period labels must map to the claims and be justified, not disguised prose.
ESSENTIAL_LABEL_REASON: NOT_APPLICABLE until a data visual is chosen.
TOTAL_VISIBLE_WORD_COUNT: 7
FACTUAL_BOUNDARIES: เป็น analysis/scenario only,ไม่ใส่ bull/base/bear probabilities, valuation หรือผลตอบแทนคาดการณ์
TRANSITION_REASON: Next audience question: หลักฐานที่จะตอบคำถามนี้

NARRATION:

พอมาถึงตรงนี้ เราจะเห็นว่าเรื่องของ Anthropic ไม่ได้มีคำตอบง่าย ๆ จากตัวเลขตัวเดียว

ด้านที่เป็นโอกาสคือ ถ้า Claude เข้าไปอยู่ในงานที่ลูกค้าใช้ทุกวัน ลูกค้าอยู่ต่อ และต้นทุนต่อการทำงานหนึ่งชิ้นลดลง บริษัทก็อาจสร้างรายได้เพิ่มโดยไม่ต้องให้ต้นทุนเพิ่มในอัตราเดียวกัน

กำลังประมวลผลที่จองไว้ก็อาจช่วยให้รับความต้องการนั้นได้ทัน

แต่ภาพนี้ต้องเกิดขึ้นจริง ไม่ใช่แค่มีโมเดลที่เก่งขึ้น เพราะความเก่งต้องแปลงเป็นงานที่ลูกค้ายอมจ่าย และเหลือรายได้หลังต้นทุนกับส่วนแบ่งของช่องทาง

อีกด้านคือ ถ้าคู่แข่งกดราคา ลูกค้าสลับใช้หลายโมเดล หรือความต้องการโตช้ากว่าที่บริษัทจองกำลังไว้ รายได้อาจยังโต แต่เงินสดที่เหลืออาจไม่มากพอรองรับภาระ

ระหว่างสองด้านนี้ยังมีอีกกรณี คือธุรกิจเติบโตดี แต่ต้องระดมทุนต่อเพื่อรองรับการขยายตัว

ทั้งหมดเป็นสถานการณ์ที่ใช้ตั้งคำถาม ไม่ใช่คำทำนายว่าแบบไหนจะเกิดขึ้น

สิ่งที่เราอยากรู้จึงไม่ใช่แค่ Claude จะได้รับความนิยมต่อไหม แต่คือความนิยมจะเปลี่ยนเป็นธุรกิจที่เลี้ยงการเติบโตของตัวเองได้มากขึ้นหรือเปล่า


## S09 หลักฐานที่จะตอบคำถามนี้

SCENE_PURPOSE: ให้ผู้ชมจบด้วยเกณฑ์ตรวจหลักฐานสามชุด และข้อสรุปที่แยกสิ่งที่รู้จากสิ่งที่ยังพิสูจน์ไม่ได้
CLAIM_IDS: [C10, C11, C12, A01]
ESTIMATED_SPOKEN_SECONDS: 60 (editorial budget; no audio measured)
PRESENTER_CUES: เว้นระหว่างหลักฐานสามชุด,จบเป็นคำถามชวนประเมิน ไม่เชิญชวนซื้อหุ้น
VISUAL_JOB: ให้ผู้ชมจบด้วยเกณฑ์ตรวจหลักฐานสามชุด และข้อสรุปที่แยกสิ่งที่รู้จากสิ่งที่ยังพิสูจน์ไม่ได้
VISIBLE_COPY_PROPOSAL: ลูกค้า กำไร เงินสด ภาระจ่าย
VISIBLE_WORD_COUNT: 5
COUNT_METHOD: ลูกค้า,กำไร,เงินสด,ภาระ,จ่าย
ESSENTIAL_DATA_LABELS: NONE proposed at Content stage. If Visual uses data, its minimum value/unit/period labels must map to the claims and be justified, not disguised prose.
ESSENTIAL_LABEL_REASON: NOT_APPLICABLE until a data visual is chosen.
TOTAL_VISIBLE_WORD_COUNT: 5
FACTUAL_BOUNDARIES: ไม่ยกระดับยังไม่มีหลักฐานเพียงพอให้กลายเป็นบริษัททำกำไรไม่ได้,ไม่แนะนำซื้อขายเฉพาะบุคคล
TRANSITION_REASON: Close with evidence tests; no investment instruction.

NARRATION:

ถ้าจะติดตาม Anthropic ต่อจากนี้ มีหลักฐานสามชุดที่น่าดู

ชุดแรกคือคุณภาพของรายได้ ลูกค้าเดิมอยู่ต่อและใช้จ่ายเพิ่มแค่ไหน รายได้กระจุกตัวเพียงใด และหลังแบ่งให้ช่องทางแล้ว บริษัทเหลือรายได้เท่าไร

ชุดที่สองคือสะพานจากกำไรไปสู่เงินสด กำไรแบบปรับปรุงแล้วต่างจากกำไรสุทธิอย่างไร และการดำเนินงานสร้างหรือใช้เงินสดเท่าไร

ชุดที่สามคือภาระตามเวลา ต้องจ่าย commitments เมื่อไร มีเงื่อนไขปรับหรือยกเลิกอย่างไร และกำลังประมวลผลที่จองไว้ถูกใช้งานมากน้อยแค่ไหน

ดังนั้น คำตอบ ณ วันที่ 1 ตุลาคม 2026 คือ หลักฐานที่รายงานสนับสนุนว่า Anthropic เติบโตเร็วมาก และมีสัญญาณด้านกำไรดำเนินงานแบบปรับปรุงแล้วที่ดีขึ้น

แต่ยังไม่เพียงพอจะยืนยันว่าบริษัทมีกำไรสุทธิและสร้างเงินสดได้อย่างยั่งยืน

ส่วนหุ้นจะน่าสนใจหรือไม่ ยังเป็นอีกคำถามหนึ่ง เพราะต้องรู้ทั้งเงื่อนไขเสนอขายและราคาที่เราจะจ่าย

ก่อนถึงวันนั้น คำถามที่มีประโยชน์ที่สุดอาจเป็นว่า ทุกครั้งที่ Claude ทำงานให้ลูกค้ามากขึ้น Anthropic เหลือเงินไว้สร้างอนาคตของตัวเองมากขึ้นด้วยหรือยัง


## Pacing and rehearsal

ผลรวม scene budgets = 560 วินาที หรือ 9:20 เป็น editorial target ยังไม่ใช่ measured narration ต้องใช้ read-through หรือไฟล์เสียงจริงตรวจ 8–10 นาที เผื่อหยุดหลังตัวเลขและคำศัพท์บัญชี ไม่อ่าน URL, claim IDs, headings หรือ production notes การนับคำไทยจากช่องว่างคลาดเคลื่อนสูง จึงไม่ใช้ whitespace word count เพื่อยืนยันความยาว หากเกิน 10 นาทีให้ตัดตัวอย่างเงื่อนไข xAI ใน S07 และย่อสถานการณ์ที่สามใน S08 ก่อน โดยคง distinctions ใน S03/S05/S06 หากสั้นกว่า 8 นาทีให้เพิ่มช่องว่างทำความเข้าใจโดยไม่เพิ่ม fact ใหม่ Visible copy เป็นข้อความธรรมดาที่เสนอทั้งหมดต่อซีน; labels ตัวเลข วันที่ หรือ wordmark เพิ่มเติมต้องนับในงบอนาคต Visual JOB ยังไม่กำหนด design

No audio or owner delivery speed measured. Scene budgets are an editorial 9:20 estimate, not stopwatch evidence. Preserve core metric/accounting distinctions if trimming; trim optional contract example or scenario prose first. Owner rehearsal remains pending separately from Content completion.

## Pronunciation notes

Anthropic: แอนโทรปิก; Claude: คลอด; IPO: ไอพีโอ; S-1: เอสวัน; SEC: เอสอีซี; run-rate: รันเรต (อัตรารายได้ปรับเป็นรายปี); compute: คอมพิวต์ (กำลังประมวลผล); GAAP: แกป (หลักบัญชีสหรัฐฯ); adjusted operating income: กำไรจากการดำเนินงานแบบปรับปรุงแล้ว; xAI: เอ็กซ์เอไอ. Read dollar numbers in millions consistently; do not read source IDs aloud.

---

# Master instructions retained from v1.6

# 01_CONTENT.md — Agent 1: Content and Research

Content defines truth and narration. This file is an executable stage brief plus a fillable project specification.

## Shared contract — mandatory for every agent

This is one of five reusable workflow templates, version 1.6, dated 2026-10-01. The master copies live in 00_WORKFLOW, the reusable template library:
https://drive.google.com/drive/folders/1WcszSRTyebajZj1FuLE-wCuKehyInE8n

For a topic, Agent 1 copies all five templates into the chosen GitHub repository and fills their project sections. The five master templates remain reusable. Topic-specific technical files are maintained in GitHub; do not mirror them back into Drive.

### Drive organization — templates and project outputs

~~~yaml
WORKFLOW_FOLDER: https://drive.google.com/drive/folders/1WcszSRTyebajZj1FuLE-wCuKehyInE8n
WORKFLOW_FOLDER_ID: 1WcszSRTyebajZj1FuLE-wCuKehyInE8n
TEMPLATE_LIBRARY_URL: https://drive.google.com/drive/folders/1WcszSRTyebajZj1FuLE-wCuKehyInE8n
TOPIC_DRIVE_PARENT: https://drive.google.com/drive/folders/153uw4BMBT78VS6TQgGelanIzXPomkzZt
TOPIC_DRIVE_PARENT_ID: 153uw4BMBT78VS6TQgGelanIzXPomkzZt
~~~

00_WORKFLOW contains only START_HERE.md and the five reusable workflow specifications. Agent 1 reads all six here before bootstrap. Do not create topic folders or owner outputs in 00_WORKFLOW.

01_PROJECTS is the only default parent for future owner folders. Agent 1 creates <Topic Name> - <PROJECT_ID> under this exact parent, then records the returned OWNER_DRIVE_FOLDER URL/ID in README.md and WORKFLOW_STATUS.md. The parent and topic-folder identity are different fields.

Later agents reuse that exact recorded owner folder and ID; never create new/final/v2/replacement/duplicate topic folders. Keep the same four owner-facing documents and the current runnable ZIP package there; technical workspace files stay in GitHub and are not mirrored into each project folder. Do not recreate or relocate an existing run's folder merely because the library was reorganized.

### FRESH bootstrap and continuation are distinct

- Entry through START_HERE.md is always BOOTSTRAP_MODE=FRESH. Agent 1 receives the workflow folder, TOPIC and GITHUB_REPOSITORY and starts a new assignment even in an old repo. Old README/status is historical context, never current state or an instruction to resume.
- Inspect the actual default branch and existing branches first. Generate a unique PROJECT_ID and create a new uniquely named normal Git branch from an appropriate existing base, preserving repository history and compatible infrastructure. Record DEFAULT_BRANCH, the chosen base/commit, BRANCH and exact BRANCH_URL. A name such as project/<topic>-<date-or-project-id> is recommended, not mandatory. Never automatically reuse an old assignment branch.
- Main/default branch is READ-ONLY BY DEFAULT for FRESH work; write there only on an explicit owner instruction. Never reset, delete, rename, overwrite or force-push an old branch; never delete Git history or the repository. All agents work only on this assignment's exact branch unless the workflow explicitly changes it. An interrupted bootstrap retries its already created branch; a later branch-URL continuation never creates another assignment.
- On the new branch initialize fresh README.md, WORKFLOW_STATUS.md and the five current specifications. Start PLANNING/Content with no inherited thesis, scenes, narration, Drive folder, workflow stage, QA findings/pass, build/deployment identity, production verification, blockers or NEXT_ACTOR/NEXT_ACTION. Reuse compatible tooling/configuration, not stale assignment values. Consult old content only as historical/reference material when explicitly useful and revalidate it.
- Cleanup is limited to files clearly belonging to the previous assignment and only on the new branch. Preserve .gitignore, package-manager setup, reusable tooling, repository settings, compatible framework/deployment configuration and CI/CD as appropriate. Never change old branches or main/default during cleanup. If ownership or compatibility is unclear, preserve the file and document the ambiguity and handling in references/bootstrap-notes.md; do not delete blindly. Record the chosen base and scoped cleanup there.
- Persist/push this run's PROJECT_ID and branch in seed README/status before cloud creation. Agent 1 creates one owner folder per PROJECT_ID under 01_PROJECTS, named <Topic Name> - <PROJECT_ID> for recovery; another FRESH run is separate. Retries recover the same recorded folder. Later agents reuse the exact OWNER_DRIVE_FOLDER and OWNER_DRIVE_FOLDER_ID and cannot create replacements.
- Initialize DELIVERY_MODE=LOCAL_ZIP, PUBLIC_DEPLOYMENT_REQUIRED=false, PACKAGE_STATE=NOT_BUILT, PACKAGE_IDENTITY=NOT_VERIFIED, OPEN_FINDINGS=[] and QA_RESULT=NOT_RUN. Vercel/hosting credentials are not required. Preserve old deployments and provider configuration; do not deploy or change them for a local assignment.
- An old public URL, deployed build, archive or QA pass is not evidence for this assignment. Builder creates a versioned prebuilt ZIP, records BUILD_COMMIT, package SHA-256, manifest and verified download identity. All fix cycles replace the current package with a new identified version while preserving finding history.
- An exact BRANCH_URL plus “Continue this project from the current workflow state.” always continues its recorded PROJECT_ID. Later agents discover roles from README/status and follow REQUIRED_INPUTS. BOOTSTRAP_MODE=FRESH describes how the run began; it never tells later agents to restart, reset findings, create another branch or create a new folder.

### Start, identity, and scope

1. For continuation of an initialized run, open README.md first on the supplied GitHub branch, then open the latest committed WORKFLOW_STATUS.md immediately after. Read NEXT_ACTOR and NEXT_ACTION and infer your workflow role from repository state before doing any work. Verify PROJECT, REPOSITORY, BRANCH, BRANCH_URL, PROJECT_ID, STAGE, required inputs, OPEN_FINDINGS, BLOCKERS, OWNER_DRIVE_FOLDER, DELIVERY_MODE, PACKAGE_DOWNLOAD_URL, PACKAGE_SHA256, and LOCAL_RUNTIME. The owner supplies only the current branch URL and “Continue this project from the current workflow state.”; the owner does not assign later agents their roles.
2. After FRESH bootstrap has chosen its new branch, or for a continuation request, clone or locate that exact repo and check out that exact branch. A local checkout path is machine-specific; all durable file references are relative to the repo root. Never depend on chat memory, another agent's temporary directory, or an owner's machine path.
3. Read all project files required by the discovered stage and its REQUIRED_INPUTS, plus upstream specifications and the acceptance criteria in 05_QA.md, before work. Perform the recorded stage. Do not silently change the thesis, content, design rules, branch, Drive folder, or package/runtime identity.
4. Respect recorded owner decisions. Raise a reasoned objection when evidence contradicts a proposed claim. Do not agree merely to please the owner. Never ask the owner to repeat the role, instructions, thesis, project paths, Drive folder, package link, findings, scene numbers, or build status already recorded in the repository. The owner acts as dispatcher and decision-maker, not as a relay between agents. Ask only for essential missing decisions or access that the repo cannot supply; continue independent work.
5. Record unresolved values as UNSET, NOT_CREATED_YET, NOT_BUILT, or NOT_VERIFIED, with the next action. Never invent repo URLs, folder IDs, commit hashes, source evidence, access, package or QA success.
6. Work sequentially on the active branch. Detect upstream changes before committing; preserve others' changes, avoid force-pushes, and resolve conflicts explicitly. An agent handoff is durable only after the commits are pushed and their files are readable on the remote branch.

### Local ↔ Cloud execution and capability-aware handoff

- Roles are independent of execution location. Content, Design, Visual, Builder and QA may run locally or in cloud environments. Choose an executor with the capabilities needed for the current task; do not force Cloud=Research or Local=Build.
- Builder and QA remain independent reviewers even if both use the same type of environment or the same Windows machine. Changing location alone does not make Builder's self-check independent QA.
- Before a switch, save work, commit/push durable source/specifications/reports and update status with exact artifact identity, actual execution environment, unfinished tasks and next action. Verify the remote branch is readable. Uncommitted files, another machine's checkout, cloud session memory and localhost URLs are not a handoff.
- On receipt, read remote README/status on the exact assignment branch; fetch and check out/update from the latest remote state before edits. Inspect dirty local work first and preserve it; never reset, overwrite or blindly pull over it. Resolve divergent work explicitly. Work sequentially on the branch, and recheck remote changes before committing/pushing.
- All portable references use repo-relative paths or observed persistent artifact URLs. Record package source/version/SHA-256. Local absolute paths may appear only in environment-specific run evidence or command examples, never as the next executor's required file location.
- Record EXECUTION_MODE=LOCAL/CLOUD/UNKNOWN and actual OS/runtime/browser where observed. Unknown values stay NOT_VERIFIED. Record what was executed separately from code inspection, assumptions and owner reports; do not invent installed tools, credentials or test results.
- Check only services needed by the current subtask using safe reads or already authorized operations. Record READ_VERIFIED, WRITE_VERIFIED, READ_ONLY, BLOCKED, NOT_VERIFIED or NOT_REQUIRED with scope/evidence. A successful read does not establish write access. Do not create/delete test resources or broaden permissions just to probe access.
- Missing Drive access does not prevent independent source work or package tests. Record the pending publication/document subtask and route it to a capable executor on the same branch with the same folder/file IDs. It does not make required owner artifacts optional: do not advance a stage gate or mark delivery complete until its required artifacts are verified.
- An intermediate handoff is allowed with the current unfinished stage preserved (for example BUILDING), explicit PENDING_SERVICE_TASKS and NEXT_ACTOR/NEXT_ACTION. Do not mark that stage complete merely to switch agents. If the core task cannot proceed, set BLOCKED and retain BLOCKED_FROM_STAGE.
- A Windows local agent may execute START.bat/STOP.bat and target-browser checks against the exact delivered archive. A cloud agent with actual Windows access may do the same; a Linux/macOS cloud run cannot certify Windows execution. Record actual Windows evidence and archive hash, not execution location as a proxy for OS.
- Resume existing verified work when source/package bytes are unchanged. Complete the pending environment-specific checks and affected regressions; do not rebuild/restart the assignment solely because the executor changes. Changed runtime/assets/launchers require a new package identity and independent affected QA.
- If a Windows check fails after a scoped cloud pass, record a stable finding and route Builder → independent QA retest. Preserve the previous evidence, but invalidate affected readiness/pass claims for that package. Keep owner acceptance separate from technical test evidence.

### Drive ownership and storage

- Only Agent 1 (Content/Research) may create the per-topic owner folder for a FRESH assignment. Create at most one folder per PROJECT_ID directly under the recorded TOPIC_DRIVE_PARENT=01_PROJECTS, named <Topic Name> - <PROJECT_ID>. Never create it in WORKFLOW_FOLDER=00_WORKFLOW. Reuse a folder only when verified as this same run during continuation/bootstrap recovery; never import an older run's folder. Commit/push its returned URL/ID before owner-document writes.
- Record the real OWNER_DRIVE_FOLDER URL and OWNER_DRIVE_FOLDER_ID immediately in README.md and WORKFLOW_STATUS.md. The library/root folder and the per-topic folder are different fields.
- Agents 2–5 must reuse the exact topic folder recorded in the latest committed WORKFLOW_STATUS.md. They must never create a second assignment folder, including a “new”, “final”, “v2”, duplicate, or replacement folder.
- Before every Drive write, read the latest committed folder ID/URL and verify folder access. Missing, conflicting, or inaccessible folder records are a blocker; later agents request Agent 1 to repair the record rather than guessing or creating a replacement.
- Preserve existing sharing and ownership. “Folder owner” here identifies the workflow creator; it does not instruct agents to transfer Google Drive ownership or broaden permissions.
- GitHub owns README.md, WORKFLOW_STATUS.md, 01–05 specifications, BUILD_NOTES.md, references/, assets/, src/, dependency lockfiles, and qa/ evidence. Use repo-relative paths.
- Drive owns the owner's reading, rehearsal, and rationale deliverables: 01_KNOWLEDGE_SUMMARY.pdf, 02_RESEARCH_AND_ANALYSIS.pdf, 03A_NARRATION_SCRIPT (editable Thai Google Doc), 06_SCENE_RATIONALE (final Thai Google Doc), and the current <PROJECT_ID>-<PACKAGE_VERSION>-local.zip package. Other Drive documents require an explicitly owner-facing purpose.
- Research notes and narration in 01_CONTENT.md are canonical authoring inputs. Drive reading documents are owner-facing editions generated from those inputs; log their source commit and refresh them when the inputs change. Owner edits in Drive must be reconciled into GitHub before downstream work continues.
- Before creating a Drive deliverable, consult its recorded file ID. Update the existing file when possible, preserving its identity. If replacement is necessary, record the superseded ID and current ID; do not leave several files ambiguously marked current.
- Every Drive artifact record includes file ID, observed URL, MIME/type, responsible agent, state, source commit, and last verification time. In-progress or failed writes cannot be marked READY.
- Secrets and credential values never belong in Markdown, Git, Drive, screenshots, or logs. Record environment variable names and configuration state only.

### Handoff and evidence

Deliverables and status must agree. Use this procedure:

1. Finish the stage's artifacts; verify its exit criteria. Commit and push the artifacts. Let the real resulting SHA be D.
2. Update WORKFLOW_STATUS.md with ARTIFACT_COMMIT=D, what was checked, evidence paths, Drive IDs/URLs, blockers, next actor, explicit next action, and exact required files. Preserve unrelated records.
3. Commit and push the status update as a separate handoff commit H. Do not put H's own hash inside H: that creates a self-referential hash problem. Record D in status and report the remote branch URL and H to the owner.
4. LAST_VERIFIED_COMMIT means the exact commit actually inspected. BUILD_COMMIT, PACKAGE_SHA256 and QA_TESTED_COMMIT have separate meanings; record only observed identities. Documentation-only status changes do not invalidate a tested package. Changed runtime source/assets/dependencies/launchers require a newly built package and affected QA.
5. Read back the remote status and verify recorded Drive artifacts. A failed push, upload, package build, or check stays PENDING/FAILED/BLOCKED with the reason and recovery action. Never advance a stage merely because a file exists.

Transitions:
PLANNING → READY_FOR_DESIGN → READY_FOR_VISUAL → READY_FOR_BUILD → BUILDING → READY_FOR_QA → QA.
If checks pass with no unresolved material findings: QA → QA_PASS.
If checks fail: QA → QA_FAIL → FIXING → READY_FOR_QA → QA. Repeat the fix/retest loop until QA_PASS.
Agent 4 publishes BUILDING or FIXING before implementation; Agent 5 publishes QA before testing. Only Agent 5 may set QA_PASS after independent retesting. QA never changes runtime code or builds fixes to close its own findings. Builder never marks its own build QA_PASS.
For access/missing decisions: set STAGE=BLOCKED and retain BLOCKED_FROM_STAGE; after resolution resume that stage.
After QA_PASS: owner final review/rehearsal and Windows smoke check → COMPLETE when agreed delivery is verified and decisions are recorded. A cloud/browser pass is scoped to its actual environment, not proof that START.bat/STOP.bat worked on Windows. Preserve useful work if owner-machine verification is pending; report it explicitly.

Upstream changes invalidate affected downstream artifacts. Record INVALIDATED_BY_COMMIT, reset their status to STALE, and route NEXT_ACTOR to the earliest affected stage. Do not build from stale content or claim QA on an earlier package.

### Formal findings and local package contract

- Every material QA finding has a stable project-wide ID QA-001, QA-002, etc.; allocate monotonically and never renumber or reuse it. Each record includes scope, severity, expected/observed behavior, evidence, correction, tested source/package identity and state.
- Finding states: OPEN, FIX_IN_PROGRESS, FIXED_PENDING_RETEST, REOPENED, CLOSED. Only independent QA closes a finding after retest; keep all unresolved material IDs in OPEN_FINDINGS.
- Builder owns code, launchers, build notes, package assembly and identity. At QA_FAIL it publishes FIXING, records per-ID fix commits/responses, builds a new version of the same assignment's ZIP, verifies its SHA-256 and refreshes affected owner documents.
- QA independently downloads/extracts the exact identified package into a clean directory, verifies its SHA-256/manifest, runs the prebuilt payload through loopback HTTP, and tests that package rather than the developer checkout. It records actual source identity, archive hash, environment, commands and evidence. A prior package's pass cannot transfer to changed runtime bytes.
- Cloud QA uses its own localhost. Its localhost URL is temporary and is not an owner-download link or a portable handoff reference. The owner runs the downloaded package on their own Windows computer.
- The required delivery is a prebuilt static Webapp ZIP with START.bat, STOP.bat, a Thai quick-start guide, packaged assets, a standard-library local server helper, and a manifest. Choose one tested runtime (Python 3 by default, or a documented compatible Node.js launcher); disclose the one-time prerequisite. Ordinary launches must not require npm install, a build, credentials, Vercel or network downloads.
- Bind the server only to 127.0.0.1. Support paths with spaces and Thai characters, occupied ports, repeat starts, missing runtime, readiness before opening a browser, and stopping only the package-owned process. Do not terminate unrelated processes or weaken browser security.
- Default OFFLINE_AFTER_SETUP=true: images, fonts, media, scripts and data needed for presentation are packaged. Test with external requests unavailable after initial runtime setup. Never substitute a generated image for authentic factual material.
- Store the current ZIP as the fifth owner-facing deliverable in the exact recorded topic Drive folder. Update its recorded file ID where possible and verify a usable observed download/file URL. If Drive delivery is blocked, preserve the repo and package; report the delivery blocker rather than claiming completion.
- Record DELIVERY_MODE, TARGET_OS, LOCAL_RUNTIME, BUILD_COMMIT, PACKAGE_VERSION, PACKAGE_PATH, PACKAGE_MANIFEST_PATH, PACKAGE_FILE_ID, PACKAGE_DOWNLOAD_URL, PACKAGE_SHA256, PACKAGE_STATE, QA_TESTED_COMMIT, QA_TESTED_PACKAGE_SHA256, QA_RESULT, OWNER_WINDOWS_SMOKE_RESULT and NEXT_ACTION. Never fabricate hashes, links or Windows test results.
- Public hosting is optional only upon a separate explicit owner request. It is not an entry/exit criterion for LOCAL_ZIP Build or QA; unavailable Vercel access must not block this route. Preserve historical cloud deployments.
- Presentation pointer and first cover are required: the pointer uses a theme-appropriate high-contrast color; S01 is the first cover and uses a verified authentic relevant image/official logo/character asset. These are detailed in Design/Visual/QA; the pointer is the explicit narrow exception to the otherwise clean canvas.

### Universal continuation prompt

~~~text
Continue this project from the current workflow state:
<the actual BRANCH_URL>

Open README.md first, then immediately open WORKFLOW_STATUS.md from that branch.
Verify the repo/branch, follow NEXT_ACTOR and NEXT_ACTION, and read the recorded required inputs and 05_QA.md.
Use repo-relative paths. Reuse the exact OWNER_DRIVE_FOLDER and package identity in status.
Fetch the latest branch, preserve local uncommitted work, inspect recorded environment/capabilities and finish pending subtask checks without restarting the assignment.
Discover your role from NEXT_ACTOR and NEXT_ACTION; do not ask me to assign it.
Do not ask me to repeat instructions, role, paths, thesis, Drive/package URLs, QA findings, or build status already recorded.
Complete the stage, verify its exit criteria, push its artifacts, and push an updated WORKFLOW_STATUS.md.
Return the branch URL, handoff commit, next action, and any real blocker.
~~~

The prompt is sufficient only when the agent has access to the repo and the services required by its stage. Missing credentials are reported precisely; they are never assumed.

## Mission and inputs

Turn the topic into an evidence-supported story that the owner can narrate naturally. Define what the audience should understand before choosing visual techniques.

Minimum bootstrap inputs: the workflow folder, TOPIC, and GITHUB_REPOSITORY. Follow START_HERE.md's mandatory FRESH policy. Inspect old repository state only to avoid collisions and protect existing work; it cannot select this run's role or supply completed outputs. Propose assumptions for unspecified audience, duration and scope, respecting the decision gates below. Owner-facing narration and final scene rationale must be editable Thai Google Docs. Use Thai narration by default; honor an explicit owner language override and record it. Do not infer a language from folder names.

Use the supplied existing repository; Agent 1 creates a new normal uniquely named branch from an appropriate existing base for each FRESH PROJECT_ID, records DEFAULT_BRANCH/base/BRANCH_URL, and preserves history and compatible infrastructure. Never create a replacement repository or resume an old branch automatically. If access prevents bootstrap, record a precise blocker and preserve existing work.

## Bootstrap a new topic

1. Inspect the actual DEFAULT_BRANCH and existing branches; generate a unique PROJECT_ID and record BOOTSTRAP_MODE=FRESH. Create a new normal unique assignment branch from an appropriate existing base and record its name/URL and base commit. Keep main/default read-only unless explicitly instructed otherwise. Start PLANNING/Content with fresh README/status and copies of these five current templates; keep Build specifications and QA criteria from the start. Preserve old branches/history and compatible infrastructure; clean only clearly stale assignment files on the new branch and document ambiguity in references/bootstrap-notes.md.
2. Verify WORKFLOW_FOLDER=00_WORKFLOW and TOPIC_DRIVE_PARENT=01_PROJECTS using the exact URLs/IDs above. Read START_HERE.md and all five specifications from 00_WORKFLOW. Agent 1 creates exactly one <Topic Name> - <PROJECT_ID> folder directly under 01_PROJECTS and persists the returned OWNER_DRIVE_FOLDER URL/ID in README/status. Never create a topic folder inside 00_WORKFLOW. Retries recover this same run's recorded folder; a matching topic name from an older run does not justify reuse.
3. Create the repo structure below. Store only necessary, legally usable reference excerpts/assets and source metadata; do not indiscriminately copy copyrighted material.
4. Produce content and the three owner reading/narration deliverables. Mark 06_SCENE_RATIONALE=PENDING_BUILD.
5. Verify and publish the repository handoff using the shared commit procedure.

~~~text
repo/
├─ README.md
├─ WORKFLOW_STATUS.md
├─ 01_CONTENT.md
├─ 02_DESIGN_SYSTEM.md
├─ 03_VISUAL_PLAN.md
├─ 04_BUILD.md
├─ 05_QA.md
├─ BUILD_NOTES.md              # created/filled by Builder
├─ references/                # source register, permitted reference material
├─ assets/                    # runtime assets and provenance
├─ src/                       # implementation when built
└─ qa/                        # reports and evidence
~~~

Existing deployment caches are historical and never required for LOCAL_ZIP. Ignore credentials, build caches and launcher process files. Record runtime prerequisites and package identity in status.

## Research and story procedure

- Separate knowledge summary (what is known), research and analysis (evidence, interpretation, counterarguments), narration (spoken story), and visual purpose (what must become understandable).
- Verify time-sensitive claims against dated primary sources. Record publication/event date, access date, and scope. Distinguish fact, estimate, inference, analogy, and opinion.
- Build a claim register. Every material factual assertion or numerical comparison in narration or visuals must map to a claim ID and supporting source. Record uncertainty, limitations, contrary evidence, units, denominator, period, geography, and rounding.
- Develop an evidence-supported thesis. Explain the strongest counterargument and what would change the conclusion. Unsupported certainty must be removed or qualified.
- Obtain essential scope/thesis choices if they are genuinely unresolved. Reuse decisions the owner already made; routine scene, style, and implementation decisions belong to the agents.
- Write a hook, context, explanation, evidence, implications, and a closing takeaway appropriate to the topic. Avoid rigid scene counts or padding to reach a duration.
- Require an authentic cover image: identify a relevant official logo, original character artwork, or real photograph from a verifiable source. Record source and rights; do not generate/reconstruct the required authentic image. The packaged image must be visible in the initial S01 state and after R reset. The owner may choose a subject; Content defines the relevance and Visual selects the actual asset.
- Divide narration into stable scene IDs S01, S02, etc. Define S01 as the cover so that R has an unambiguous destination; the cover is part of the story and follows the same clean-canvas and copy rules. One scene has one audience takeaway, but may contain multiple reveal beats. IDs are internal metadata, never visible page numbers.
- Narration carries explanation and nuance. Visuals carry relationships, scale, mechanisms, or evidence. Do not write slides as paragraphs or repeat the spoken script onscreen.
- Supply proposed ordinary visible copy targeting 0–8 words per scene, excluding essential chart/data labels. Separate indispensable labels/units/numbers from ordinary copy; justify the minimum data labels needed for truthful reading and do not use the exception for prose. A scene may be entirely text-free. For Thai, count meaningful linguistic words rather than whitespace chunks; document segmentation where ambiguous.
- Estimate pacing from an actual read-through where possible. A presenter can hold longer than the estimate; avoid assuming narration audio or automatic timing exists.
- Do not select 3D merely for appearance. State the understanding needed; Agent 3 chooses the appropriate visual medium.

## Fillable project specification

Replace placeholders with real values; maintain these sections alongside the instructions.

~~~yaml
BOOTSTRAP_MODE: FRESH
PROJECT_ID: <unique identifier for this fresh assignment>
PROJECT_TITLE: <title>
AUDIENCE: <who and prior knowledge>
OWNER: <provided name or UNSET>
NARRATION_LANGUAGE: <language>
TARGET_DURATION: <range and read-through estimate>
FORMAT: narration-led local web presentation
DELIVERY_MODE: LOCAL_ZIP
TARGET_OS: Windows
OFFLINE_AFTER_SETUP: true
COVER_SCENE_ID: S01
COVER_IMAGE_SUBJECT: <authentic relevant image/official logo/character subject>
COVER_ASSET_REQUIREMENT: authentic_original_required
SCOPE: <included questions>
OUT_OF_SCOPE: <excluded questions>
THESIS: <one defensible sentence>
AUDIENCE_TAKEAWAY: <what changes in understanding>
OWNER_SCOPE_DECISION: <decision/evidence or PENDING>
OWNER_THESIS_DECISION: <decision/evidence or PENDING>
RESEARCH_AS_OF: <ISO date/time with timezone>
~~~

### Source register

| Source ID | Title / publisher | Direct URL | Published / event date | Accessed | Supports | Limits / reliability |
|---|---|---|---|---|---|---|
| SRC01 | <source> | <verified URL> | <dates> | <date> | <claim IDs> | <limits> |

### Claim register

| Claim ID | Exact claim | Type | Source IDs and location | Unit / period / denominator | Uncertainty / opposing evidence | Allowed visual interpretation |
|---|---|---|---|---|---|---|
| C01 | <claim> | FACT/INFERENCE/ESTIMATE/ANALOGY | <sources and page/section> | <scope> | <limits> | <what may be shown> |

### Story outline

| Beat | Audience question | Takeaway | Evidence / claim IDs | Why this beat follows |
|---|---|---|---|---|
| <beat> | <question> | <takeaway> | <IDs> | <logic> |

### Repeat for every scene

~~~yaml
SCENE_ID: S01
SCENE_PURPOSE: <one audience takeaway>
NARRATION: |
  <complete natural spoken text; not abbreviated slide bullets>
CLAIM_IDS: [<IDs>]
ESTIMATED_SPOKEN_SECONDS: <number and measurement basis>
PRESENTER_CUES: <when to reveal, settle, hold, and advance>
VISUAL_JOB: <understanding the visual must supply>
VISIBLE_COPY_PROPOSAL: <ordinary copy, target 0–8 words or empty>
VISIBLE_WORD_COUNT: <ordinary copy count; Thai segmentation if relevant>
ESSENTIAL_DATA_LABELS: <exact indispensable chart/data labels; or NONE>
ESSENTIAL_LABEL_REASON: <why each excluded label is necessary>
TOTAL_VISIBLE_WORD_COUNT: <ordinary copy plus excluded labels>
FACTUAL_BOUNDARIES: <what the visual must not imply>
TRANSITION_REASON: <how the next idea follows>
~~~

## Owner-facing Drive deliverables

Write these into the exact OWNER_DRIVE_FOLDER:

| Name | Format | Contents | Responsible |
|---|---|---|---|
| 01_KNOWLEDGE_SUMMARY.pdf | PDF | Concise knowledge map, definitions, key facts, uncertainties, source links | Agent 1 |
| 02_RESEARCH_AND_ANALYSIS.pdf | PDF | Claim/evidence analysis, thesis, counterarguments, limitations, dated references | Agent 1 |
| 03A_NARRATION_SCRIPT | Google Doc | Editable Thai rehearsal-ready script with scene IDs, pacing/cues, pronunciation notes if needed; no code | Agent 1 |
| 06_SCENE_RATIONALE | Google Doc | Final Thai explanation of the actual built visuals and pointer; created after build | Agent 4 |
| <PROJECT_ID>-<PACKAGE_VERSION>-local.zip | ZIP | Prebuilt Webapp, START.bat/STOP.bat, runtime helper, packaged authentic cover/assets, manifest and Thai quick-start | Agent 4 |

Include project/version and source commit in each owner edition. Owner documents can contain full explanations, source citations, and cue labels; the 0–8-word ordinary-copy target applies to the audience scene canvas, with a justified exception for essential chart/data labels, not these documents. Verify PDF readability and all document links.

## README.md starter — create in the topic repo

~~~markdown
# <PROJECT_TITLE>

PROJECT: <real topic/project name>
BOOTSTRAP_MODE: FRESH
PROJECT_ID: <unique ID for this fresh assignment>
REPOSITORY: <actual GitHub repo URL>
DEFAULT_BRANCH: <verified repository default branch; read-only by default>
BRANCH: <actual active branch>
BRANCH_URL: <actual branch URL>
WORKFLOW_STATE: WORKFLOW_STATUS.md

WORKFLOW_FOLDER: https://drive.google.com/drive/folders/1WcszSRTyebajZj1FuLE-wCuKehyInE8n
WORKFLOW_FOLDER_ID: 1WcszSRTyebajZj1FuLE-wCuKehyInE8n
TEMPLATE_LIBRARY_URL: https://drive.google.com/drive/folders/1WcszSRTyebajZj1FuLE-wCuKehyInE8n
TOPIC_DRIVE_PARENT: https://drive.google.com/drive/folders/153uw4BMBT78VS6TQgGelanIzXPomkzZt
TOPIC_DRIVE_PARENT_ID: 153uw4BMBT78VS6TQgGelanIzXPomkzZt
OWNER_DRIVE_FOLDER: <actual per-topic folder URL>
OWNER_DRIVE_FOLDER_ID: <actual per-topic folder ID>

Open this README.md first, then WORKFLOW_STATUS.md immediately after.
Infer your role from NEXT_ACTOR and NEXT_ACTION before doing any work.
The owner supplies only the current GitHub branch URL and “Continue this project from the current workflow state.”.
Read the stage's REQUIRED_INPUTS before work; discover Drive/package metadata and open QA findings from status.
Never ask the owner to repeat any role, thesis, instruction, URL, path, finding, scene number, or build state already recorded.
Use the five specifications on this branch and repo-relative paths.
GitHub is the canonical agent workspace. Drive contains owner-facing editions.
Only Agent 1 creates this run's topic folder; later agents reuse its exact recorded ID.
BOOTSTRAP_MODE=FRESH records this assignment's origin. A branch-URL continuation never creates a new run or restarts this one.
Setup/build/run instructions: <repo-relative path, added by Builder>
Presentation keyboard guide: <repo-relative path, added by Builder>
~~~

## WORKFLOW_STATUS.md starter — create in the topic repo

This is a status schema, not a sixth master-template deliverable. Agent 1 creates the live file from it; every later agent updates the same file. YAML blocks keep values explicit; use ISO 8601 timestamps with offset, for example +07:00 for Bangkok when appropriate.

~~~~markdown
# WORKFLOW_STATUS

## Identity and storage
~~~yaml
SCHEMA_VERSION: 7
PROJECT: <real topic/project name>
BOOTSTRAP_MODE: FRESH
PROJECT_ID: <unique ID for this fresh assignment>
PROJECT_TITLE: <real title>
REPOSITORY: <actual repo URL>
DEFAULT_BRANCH: <verified repository default branch>
BRANCH: <actual new normal assignment branch>
BRANCH_URL: <actual branch URL>
TEMPLATE_VERSION: "1.6"
WORKFLOW_FOLDER: https://drive.google.com/drive/folders/1WcszSRTyebajZj1FuLE-wCuKehyInE8n
WORKFLOW_FOLDER_ID: 1WcszSRTyebajZj1FuLE-wCuKehyInE8n
TEMPLATE_LIBRARY_URL: https://drive.google.com/drive/folders/1WcszSRTyebajZj1FuLE-wCuKehyInE8n
TOPIC_DRIVE_PARENT: https://drive.google.com/drive/folders/153uw4BMBT78VS6TQgGelanIzXPomkzZt
TOPIC_DRIVE_PARENT_ID: 153uw4BMBT78VS6TQgGelanIzXPomkzZt
OWNER_DRIVE_FOLDER: <actual topic folder URL>
OWNER_DRIVE_FOLDER_ID: <actual topic folder ID>
DRIVE_FOLDER_CREATED_BY: Agent 1
DRIVE_FOLDER_VERIFIED_AT: <timestamp>
~~~

## Current workflow
~~~yaml
STAGE: PLANNING
BLOCKED_FROM_STAGE: null
ACTIVE_ACTOR: Agent 1 — Content/Research
UPDATED_AT: <timestamp>
ARTIFACT_COMMIT: NOT_VERIFIED
LAST_VERIFIED_COMMIT: NOT_VERIFIED
LAST_VERIFIED_SCOPE: <exact files/checks inspected>
NEXT_ACTOR: Agent 1 — Content/Research
NEXT_ACTION: <concrete task, output paths, finding IDs/regressions if relevant, and exit criteria>
REQUIRED_INPUTS: [01_CONTENT.md, 05_QA.md]
OPEN_FINDINGS: [] # stable QA-001-style IDs; empty means None
QA_FINDINGS_REPORT_PATH: UNSET
BLOCKERS: [] # empty means None
OWNER_ACTION_REQUIRED: null
OWNER_DECISIONS:
  SCOPE: <decision plus evidence, or PENDING>
  THESIS: <decision plus evidence, or PENDING>
  FINAL_REVIEW: PENDING
  DELIVERY: LOCAL_ZIP
  PUBLICATION: NOT_REQUESTED
~~~

## Execution environment and pending service tasks
~~~yaml
EXECUTION_MODE: UNKNOWN # LOCAL/CLOUD/UNKNOWN; record actual context
EXECUTION_OS: NOT_VERIFIED
EXECUTION_RUNTIME: NOT_VERIFIED
EXECUTION_BROWSER: NOT_VERIFIED
EXECUTION_VERIFIED_AT: UNSET
EXECUTION_EVIDENCE: UNSET # repo-relative report; distinguish executed/inspected/reported
REQUIRED_SERVICES_FOR_NEXT_ACTION: []
SERVICE_CAPABILITIES: {} # service -> state, scope, evidence, verified_at; no credentials
PENDING_SERVICE_TASKS: [] # task ID, role, required capability, artifact path/ID, state, next action
NEXT_EXECUTION_PREFERENCE: ANY_CAPABLE # preference only, not role assignment
WINDOWS_VERIFICATION_ACTOR: UNSET
WINDOWS_VERIFICATION_PACKAGE_SHA256: NOT_VERIFIED
~~~

Capability states: READ_VERIFIED, WRITE_VERIFIED, READ_ONLY, BLOCKED, NOT_VERIFIED, NOT_REQUIRED. Pending service tasks retain their identity until verified complete. Record evidence rather than assuming a connector exists in the next environment.

## Repository deliverables
| Path | Actor | State | Source/artifact commit | Verified evidence | Invalidated by |
|---|---|---|---|---|---|
| 01_CONTENT.md | Agent 1 | PENDING | NOT_VERIFIED | <path> | null |
| 02_DESIGN_SYSTEM.md | Agent 2 | PENDING | NOT_VERIFIED | <path> | null |
| 03_VISUAL_PLAN.md | Agent 3 | PENDING | NOT_VERIFIED | <path> | null |
| 04_BUILD.md | Agent 4 | TEMPLATE_READY | NOT_VERIFIED | <path> | null |
| 05_QA.md | Agent 5 | CRITERIA_READY | NOT_VERIFIED | <path> | null |
| BUILD_NOTES.md | Agent 4 | PENDING | NOT_VERIFIED | <path> | null |
| src/ and assets/ | Agent 4 | PENDING | NOT_VERIFIED | <paths> | null |
| qa/ | Agent 5 | PENDING | NOT_VERIFIED | <paths> | null |
| delivery/ launchers, helper and manifest | Agent 4 | PENDING | NOT_VERIFIED | <paths> | null |

## Owner-facing Drive deliverables
| Name | Type | Actor | State | File ID | Observed URL | Source commit | Verified at |
|---|---|---|---|---|---|---|---|
| 01_KNOWLEDGE_SUMMARY.pdf | PDF | Agent 1 | PENDING | UNSET | UNSET | NOT_VERIFIED | UNSET |
| 02_RESEARCH_AND_ANALYSIS.pdf | PDF | Agent 1 | PENDING | UNSET | UNSET | NOT_VERIFIED | UNSET |
| 03A_NARRATION_SCRIPT | Google Doc | Agent 1 | PENDING | UNSET | UNSET | NOT_VERIFIED | UNSET |
| 06_SCENE_RATIONALE | Google Doc | Agent 4 | PENDING_BUILD | UNSET | UNSET | NOT_VERIFIED | UNSET |
| <PROJECT_ID>-<PACKAGE_VERSION>-local.zip | ZIP | Agent 4 | PENDING_BUILD | UNSET | UNSET | NOT_VERIFIED | UNSET |

## Local package and build identity
~~~yaml
DELIVERY_MODE: LOCAL_ZIP
TARGET_OS: Windows
PUBLIC_DEPLOYMENT_REQUIRED: false
OFFLINE_AFTER_SETUP: true
LOCAL_RUNTIME: UNSET # choose Python 3 by default or a documented Node.js alternative
LOCAL_RUNTIME_TESTED_VERSION: UNSET
WINDOWS_RUNTIME_PREREQUISITE: UNSET
FRAMEWORK: UNSET
INSTALL_COMMAND: UNSET # Builder setup only
BUILD_COMMAND: UNSET # Builder setup only
OUTPUT_DIRECTORY: UNSET
BUILD_COMMIT: NOT_VERIFIED
FIX_COMMITS_BY_FINDING: {}
PACKAGE_VERSION: UNSET
PACKAGE_PATH: UNSET # repo-relative assembly/output path
PACKAGE_MANIFEST_PATH: UNSET
PACKAGE_FILE_ID: UNSET
PACKAGE_DOWNLOAD_URL: NOT_DELIVERED_YET # observed persistent owner link
PACKAGE_SHA256: NOT_VERIFIED
PACKAGE_STATE: NOT_BUILT # NOT_BUILT/IN_PROGRESS/READY/STALE/FAILED/BLOCKED
PACKAGE_IDENTITY_EVIDENCE: UNSET
LAST_PACKAGE_VERIFIED_AT: UNSET
POINTER_MODE: theme_adaptive_presenter_dot
POINTER_SPEC_PATH: 02_DESIGN_SYSTEM.md
COVER_SCENE_ID: S01
COVER_ASSET_ID: UNSET
~~~

## QA identity and owner verification
~~~yaml
QA_TESTED_COMMIT: NOT_VERIFIED
QA_TESTED_PACKAGE_SHA256: NOT_VERIFIED
QA_PACKAGE_VERSION: UNSET
QA_ENVIRONMENT: UNSET
QA_TARGET: extracted_package_on_loopback
QA_TARGET_URL: UNSET # local run observation only; never an owner handoff link
QA_REPORT_PATH: UNSET
QA_RESULT: NOT_RUN
QA_VERIFIED_AT: UNSET
QA_FINDING_STATES: {}
WINDOWS_LAUNCHER_TEST_RESULT: NOT_RUN
WINDOWS_LAUNCHER_TEST_EVIDENCE: UNSET
OWNER_WINDOWS_SMOKE_RESULT: NOT_RUN
OWNER_WINDOWS_SMOKE_EVIDENCE: UNSET
~~~

## Current handoff
~~~yaml
LAST_HANDOFF_ARTIFACT_COMMIT: <real SHA or NOT_VERIFIED>
LAST_HANDOFF_EVIDENCE: <repo-relative report paths>
BOOTSTRAP_NOTES_PATH: references/bootstrap-notes.md # chosen base/commit, scoped cleanup, preserved ambiguities
WORKFLOW_HISTORY_PATH: references/workflow-history.md
~~~
Keep one current-state summary here. Append historical handoffs in WORKFLOW_HISTORY_PATH and detailed QA runs in qa/; do not append chat transcripts.
~~~~

When copying this nested Markdown example, use the section text as a normal file, removing the outer example fence only. Preserve the inner YAML fences.

Allowed artifact states: PENDING, TEMPLATE_READY, CRITERIA_READY, IN_PROGRESS, READY, STALE, FAILED, BLOCKED. A template is not a completed stage. Update the skeleton with real metadata as work happens.

## Exit criteria and handoff

- Scope/thesis decisions are recorded or essential unresolved decisions are explicitly blocked.
- Claims are traceable; narration is complete; each scene has purpose, cues, and text budget.
- All five templates, README.md, and live WORKFLOW_STATUS.md exist in the remote topic repo.
- The exact topic folder and the three reading/narration artifacts are verified and recorded; narration is editable Thai and rationale is scheduled as final Thai.
- Commit/push content artifacts and then status. Set STAGE=READY_FOR_DESIGN, NEXT_ACTOR=Agent 2 — Design.
- NEXT_ACTION: “Read README.md, WORKFLOW_STATUS.md, 01_CONTENT.md, and 05_QA.md. Fill 02_DESIGN_SYSTEM.md for this topic, preserving the narration-first, visual-first, 16:9 and clean-canvas constraints. Do not build yet.”



