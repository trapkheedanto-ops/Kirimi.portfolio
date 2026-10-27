#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, sys

P = "/workspace/Fortuna Labs/east-africa-heritage.html"
src = open(P, encoding="utf-8").read()
orig_len = len(src)

EXTRA = {
"Kilwa Kisiwani Sultanate": dict(
 lang:"Swahili (Kimwani) with an Arabic literary register; founder legend speaks Shirazi Persian",
 pop:"Island ruins + village of Visine · UNESCO World Heritage since 2004",
 history:"Settled by the 9th century, ruled from c. 1150 by the Sunna dynasty and then al-Hasan ibn Sulaiman, who minted copper dirhams and whose town Ibn Battuta visited in 1331, calling it 'one of the most beautiful and well-built towns in the world.' Kilwa brokered gold from Sofala, iron and ivory from the Zimbabwe plateau and mangrove poles across the ocean; the Portuguese sacked it in 1505, Omani suzerainty followed in 1827. Excavations by N. Chittick (1955-79) uncovered Husuni Kubwa palace, the Great Mosque's eight building phases, and imported celadon and porcelain.",
 art:"Coral-rag vaulting unmatched on the coast; the Great Mosque's stepped niches; carved tombstones with Swahili-Arabic epitaphs; Kilwa coin hoards; soapstone bowls and Chinese ceramics now in national museums.",
 traditions:"Living village life around the ruins; dhow-carving heritage; Maulid poetry recitals; women's boatyards cooperative; archaeological 'memory walks' used by site managers.",
 economy:"Historic entrepot of the gold-and-ivory southbound route; today fishing, seaweed, coconut and heritage tourism.",
 links=[("Meru & Mount Kenya (Kirinyaga)","trade","Kilwa's sphere pulled hinterland goods - including Tana-corridor ivory and wax - into one ocean market; the same commodities Meru country supplied northward."),
        ("Lamu Old Town","trade","Successor nodes of one monsoon port chain; Kilwa's 16th-c. decline shifted scholarship and shipping north to Lamu, Pate and Mombasa."),
        ("Island of Mozambique","trade","Sofala-region gold reached Kilwa via the same Zambezi-coast intermediaries that later fed the Island of Mozambique fair."),
        ("Stone Town of Zanzibar","kinship","Both claim Shirazi-era founding genealogies; Zanzibar inherited Kilwa's commercial culture under the Omani sultans.")],
 sources:"Chittick, 'Kilwa: An Islamic Trading City on the East African Coast' (1974); Ibn Battuta Rihla (1331); UNESCO nomination (2004)."),

"Stone Town of Zanzibar": dict(
 lang:"Swahili (Kiunguja standard) with Arabic, Gujarati and English layers",
 pop:"~50,000 residents in the UNESCO-listed old town (2000)",
 history:"From a trading outpost of the Kilwa sphere, Stone Town boomed after Sultan Said bin Sultan moved his court from Oman in 1840, making Zanzibar the clove capital and the Indian Ocean's great slave market until Britain forced the market's closure in 1873. The sultanate's palaces, Arab-Farasi cavalry tradition and Indian merchant guilds layered the city; the 1964 revolution ended the sultanate weeks after independence. Forodhani, Darajani and the dhow yards still work as they did in the 19th century.",
 art:"Carved teak doors (chain-and-lotus vs. fish motifs marking clan origin); lime-plaster rose windows; taarab music halls; oxblood 'House of Wonders' (1880) architecture.",
 traditions:"Dhow-building races; the Hadya Sawa sawn-boat regatta; taarab and ngoma nights; multi-day Swahili wedding cycles; Friday processions from the Mandhry mosque.",
 economy:"Cloves, spices, coral rag and cloth historically; today tourism, fishing, spice-farm heritage and maritime trade.",
 links=[("Lamu Old Town","kinship","One urban Swahili culture: shared dialect continuum, door-carving schools and intermarried merchant houses."),
        ("Kilwa Kisiwani Sultanate","trade","Zanzibar absorbed Kilwa's southern trade functions after 1500; customs ledgers list the same gold, ivory and grain flows."),
        ("Somali Pastoral Nomads","trade","Horn camel herds and frankincense loaded onto Zanzibar-bound dhows at Berbera and Barawa for decades."),
        ("Fort Jesus, Mombasa","trade","Rival ports of one coast - Fort Jesus's Omani recapture era (1698) launched the very Omani seafaring world that built Stone Town.")],
 sources:"Sherman, 'Recent History of Zanzibar'; UNESCO Stone Town dossier (2000); Prestholdt, 'Domesticating the World' (2008)."),

"Laetoli Footprints": dict(
 lang:"- (palaeontological site; local toponym in the Maa orbit)",
 pop:"Ngorongoro Conservation Area, Tanzanian World Heritage tentative list",
 history:"In 1976-79 Mary Leakey's team exposed a trail of hominin footprints preserved in fine ashfall from Ol Doinyo Lengai, dated by argon methods to 3.66 million years. The tracks - attributed to Australopithecus afarensis (same species as 'Lucy') - show obligate bipedalism with a modern gait more than a million years before stone tools, transforming ideas about human evolution. A protective hall and ash revetment now shelter the trackway.",
 art:"Not an art site - but the footprint trail itself reads as palaeo-landscape sculpture; nearby Maasai and Hadzabe land-use names layer the ground with newer meaning.",
 traditions:"Ngorongoro Maasai pastoral rights and ranger stewardship keep the landscape living; community conservancy income-sharing began here.",
 economy:"Conservation-tourism employment for Endulen ward; research logistics; traditional cattle grazing regulated around the site.",
 links=[("Olduvai Gorge","kinship","Two chapters of one research story ~40 km apart - Leakey-family fieldwork built the global science of human origins on both."),
        ("Hadzabe & Sandawe - Bushcraft Elders","kinship","Forager descendants whose oral geography keeps Eyasi-Lengai-Laetoli as one remembered hunting landscape."),
        ("Maasai Steppe - Kajiado & Narok","migration","Maa place-names across Lengai and the short grasslands record the southward Rift migration that passed this corridor."),
        ("Arusha & Meru (Tanzania) - Kisiki Forest Clans","migration","Highland farming clans advanced along the same volcano-chain past Laetoli's plains within living memory of oral histories.")],
 sources:"Leakey & Hay, 'Laetoli: A Palaeontological Site in Tanzania' (1981); MDLEA dating studies; Ngorongoro Conservation Area Authority archives."),

"Olduvai Gorge": dict(
 lang:"Local Maasai name; research languages English/Swahili",
 pop:"Stratified sequence spanning ~2 million years",
 history:"Preserved in volcanic ash and lake-bed sediments, Olduvai's beds hold Oldowan flake tools (c. 2.6 Ma), Homo habilis ('handyman,' described by Leakey, Tobias & Napier in 1964), and later Acheulean handaxes - plus the FLK Zinj butchery site. The gorge gave its name to humanity's earliest known stone-tool industry and remains the benchmark stratotype for East African Pleistocene chronology.",
 art:"The stone tools themselves are the oldest designed objects anywhere; museum displays narrate tool-making as behaviour, not just typology.",
 traditions:"Maasai grazing rights negotiated with the Ngorongoro Authority; annual Olduvai Science Week lectures connect research to surrounding villages.",
 economy:"Palaeoanthropology research stations, Serengeti-Ngorongoro circuit tourism, and training pipelines for Tanzanian archaeologists.",
 links=[("Laetoli Footprints","kinship","One stratigraphic system - Laetoli's prints sit in the same Lengai-ash geology read through Olduvai's layers."),
        ("Hadzabe & Sandawe - Bushcraft Elders","kinship","Living foragers occupy the ecological end of the lineage Olduvai documents over 2 million years."),
        ("Sukuma & Sukuru Drum Language","kinship","Farmers of the western Serengeti fringe whose oral histories recall sharing these plains with earlier hunter groups."),
        ("Chaga & Pare Highlands - Kilimanjaro & Usambara","trade","Rift-corridor traffic: highland iron and grain moved along the valley floors that link these sites end to end.")],
 sources:"Leakey, 'Olduvai Gorge' vols I-IV (1959-79); Mary Leakey's site monographs (1984); UNESCO Tentative List (Tanzania)."),

"Chaga Irrigation Terraces (Kilela)": dict(
 lang:"Kichagga cluster of languages (Moshi, Vunjo, Machame...) - Bantu of the northeast highland zone",
 pop:"Kilimanjaro and Pare slopes - several hundred thousand terrace users",
 history:"By at least the 17th-18th centuries Chaga farmers cut contour trenches and gravity canals (kilela/mrezo) from Kilimanjaro's glaciers and springs, feeding banana-coffee plots through hilltop villages. German and British surveys called the system the finest native engineering in Africa; kilela maintenance guilds still allocate water by elder arbitration, and climate-driven glacier retreat now makes the furrows a frontline of adaptation heritage.",
 art:"Terrace-stone dry-wall patterning; gourd-decorated beer vessels; mbira-type lamellophones at harvest feasts; the lyre music of the Moshi courts.",
 traditions:"Water-rituals at spring shrines; first-fruits banana blessings; age-grade brew houses; communal repair parties for the furrows.",
 economy:"Bananas, robusta coffee, yams and dairy on irrigated terraces; hydro-meadow pasture sustains stall-fed cattle.",
 links=[("Meru & Mount Kenya (Kirinyaga)","kinship","Mirror-image mountain-farming cultures: spring veneration, trench irrigation and elder councils appear in identical grammar on both massifs."),
        ("Chaga & Pare Highlands - Kilimanjaro & Usambara","kinship","One highland province of terraced water engineering between Kilimanjaro and the Usambara ridges."),
        ("Arusha & Meru (Tanzania) - Kisiki Forest Clans","migration","Meru settlers took mtombo furrow techniques onto Mount Meru's slopes within two generations of arrival."),
        ("Kikuyu - Kiambu & Central Highlands","trade","The east African 'banana complex' spread along Thagicu-speaking corridors linking Kilimanjaro farmers to Mount Kenya's ridge gardens.")],
 sources:"McCann, 'Stirring the Pot' (2005); Winsberg on Chaga irrigation; FAO GIAHS reports on Kilimanjaro water heritage."),

"Hadzabe & Sandawe - Bushcraft Elders": dict(
 lang:"Hadzane (click inventory unrelated to neighbours) and Sandawe (clicks; isolate or Khoe-linked)",
 pop:"~1,000 Hadzabe near Lake Eyasi; ~100,000 Sandawe in Kondoa/Bariadi hills",
 history:"Genetic and linguistic studies place both among the deepest-diverging lineages of humankind - their click systems and forager economies predate the farming expansions that reshaped Tanzania. Hadzabe bands resisted assimilation through mobility; Sandawe rock-art galleries at Kondoa (UNESCO 2006) show 2,000+ years of painted hunter and spirit imagery still venerated. Today both negotiate land rights inside the Lake Eyasi and Yaeda conservation zones.",
 art:"Kondoa rock paintings - eland-hunter scenes and spirit lines; bead-and-seed ornament; bow-drill fire technology; song cycles imitating animal calls for hunts.",
 traditions:"Night-fire storytelling; honey-guide bird partnerships; naming after animals seen at birth; Sandawe rainmakers; Hadzabe band-level consensus decisions.",
 economy:"Wild foods, honey, tubers and small game supplemented by day-labour, guiding research/tourism groups and craft sales.",
 links=[("Laetoli Footprints","kinship","The forager lifeway these elders practise occupies the same ecological stage set by 3.6-million-year-old walkers."),
        ("Olduvai Gorge","kinship","Their skillset - tracking, plant lore, fire-making - is the living counterpart of Olduvai's 2-million-year stone record."),
        ("Arusha & Meru (Tanzania) - Kisiki Forest Clans","trade","Forest-forager and farming highlander exchange: honey, game and medicines traded for grain and iron across the Eyasi-Manyara rim."),
        ("Maasai Steppe - Kajiado & Narok","migration","Maasai expansion west of the Rift absorbed and renamed earlier forager groups; Hadzabe memory preserves the older map.")],
 sources:"Woodburn, 'Hadhza: A 20th-Century Hunter-Gatherer Band' (1982); UNESCO Kondoa Rock-Art (2006); Marks & Parkipuny on Sandawe."),

"Hehe & Matumbi Highlands": dict(
 lang:"Kihehe and Kimatumbi - southern Bantu of the Nyasa-Rufiji zone",
 pop:"Iringa-Njombe highlands - chiefdom-descended communities",
 history:"Hehe oral tradition records migrations from the Ulanga/Mbunga region under chiefs like Songea and Nsimba in the 18th-19th centuries; Chief Mkambela's Hehe defeated German columns at the Battle of Lugufu (1891) and held the Kitulo plateau against German forces for years - a war remembered across southern Tanzania. Matumbi polities further east kept similar chieftaincy structures and mask-dance institutions tied to matrilineal initiation.",
 art:"Lukwakongo and chipenda masks with geometric scarification-like faces; unyago girls' initiation songs; clay water-vessel burnishing; chiefstools with zoomorphic legs.",
 traditions:"Unyago/mwera-type initiation societies; ancestor-libation at family graves; chiefly tribute markets; rainmaking on the Nyaso escarpment.",
 economy:"Highland maize, beans, potatoes and beekeeping; historic iron-smelting around the Kitulo grasslands.",
 links=[("Nyakyusa-Sonde & Ha Highlands","kinship","Neighbouring 'chiefdom belt' of the southern Rift - shared initiation societies and sacred-fire ideas."),
        ("Timbila Orchestras of Southern Mozambique","trade","Southern Bantu ceremonial complex: xylophone orchestras and girls' initiation share forms across the Rovuma frontier."),
        ("Chaga & Pare Highlands - Kilimanjaro & Usambara","migration","Parallel case studies of highland ordered societies resisting coastal/caravan domination."),
        ("Kilwa Kisiwani Sultanate","trade","Hehe-country iron and ivory entered the Kilwa trade net via Matumbi middlemen on the Rufiji road.")],
 sources:"Gessler on Hehe history; Spear, 'Manners and Murder in an African State'; Roberts on Matumbi identity; Tanganyika district oral-history files."),

"Sukuma & Sukuru Drum Language": dict(
 lang:"Kisukuma (Bantu, Lake-zone) closely related to Nyamwezi",
 pop:"Shinyanga-Mwanza belt - millions of speakers, Tanzania's largest group",
 history:"The Sukuma built their society around clustered village-nuclei, cattle wealth and the ngoma drum corps whose tonal phrases reproduce Kisukuma speech - praise-names, proverb-lines and warnings carried village to village. Their bughaya dance guilds and the 1920s-50s labour-migration circles shaped the whole Lake Zone's music; drum language itself belongs to the same talking-drum family documented from the Niger basin to the coast.",
 art:"Hourglass-shaped lugubu drums with lugged tuning; gourd rattles; body-scarification geometry; colourful bughaya costume feathers.",
 traditions:"Bugaya and nanna dance initiations; cattle-praise naming; rain-season drum summons; elder circle dances (nondema) adopted nationally.",
 economy:"Cotton, millet and sorghum; historic labour migration to mines and sisal estates; fishing on the lake's south shore.",
 links=[("Thimlich Ohinga","kinship","Same Lake Victoria agricultural-herding world - ohinga stone kraals stand amid Sukuma-Luhya cattle country."),
        ("Kisumu - Luo Fisherman's Coast","trade","Grain-for-fish markets ring the gulf; Sukuma cattle drives crossed Luo fishing villages seasonally."),
        ("Buganda Royal Tombs at Kasubi","kinship","Drum-royalty concept runs from Buganda's royal drums to Sukuma ngoma corps - one Great Lakes musical-political family."),
        ("Burundi - Karyenda & Royal Drum Sanctuary","kinship","Tonal drum speech appears across the lakes - the Karyenda and the lugubu speak the same principle.")],
 sources:"Raum, 'Young Sukuma Goes to Town' (1940); Behan on Sukuma ngoma; national radio sound archives."),

"Arusha & Meru (Tanzania) - Kisiki Forest Clans": dict(
 lang:"Kimeru/Kiarusha - Bantu of the Mount Kenya (Thagicu) cluster, intelligible with Kenyan Meru",
 pop:"Arusha & Manyara regions - 600,000+ Meru-speakers in Tanzania",
 history:"Oral histories collected by Beckerman and Caplan record a 19th-century breakaway from Mount Kenya - led by figures such as Katolohola (Arusha founders) and the ancestors of the Mirui/Parakuyu - driven by succession disputes and population pressure, settling beneath Ngare Nanyuki (Mount Meru) and the Kisiki forest belt. They transplanted mgiro-type age sets, fig-tree shrines and maize-beer ritual; British administrators noted their kinship with Kenyan Meru as early as the 1920s.",
 art:"Age-set graduation regalia; kisiki-shrine wooden staffs; gourd beer calabashes; song cycles preserving Mount Kenya place-names.",
 traditions:"Mgiro graduations with new-name ceremonies; arbitration by Njuri-style elder delegations; first-fruits banana offerings; mtombo furrow work-parties.",
 economy:"Coffee and bananas on Mount Meru's volcanic slopes; Arusha 'end-of-the-road' trade legacy; today tourism and horticulture.",
 links=[("Meru & Mount Kenya (Kirinyaga)","migration","THE defining link of this atlas: 19th-c. Mount Kenya to Mount Meru migration confirmed by shared mgiro grades, vocabulary and shrine cults."),
        ("Chaga Irrigation Terraces (Kilela)","kinship","Adopted Kilimanjaro-style furrow engineering (mtombo) onto Mount Meru within two generations."),
        ("Maasai Steppe - Kajiado & Narok","trade","Highland grain and stock exchanges - and conflicts - with Maa pastoralists defined the Manyara frontier."),
        ("Kikuyu - Kiambu & Central Highlands","kinship","Common Thagicu ancestry: parallel sacred-fig worship and mutual intelligibility carried south by the migrants.")],
 sources:"Beckerman, 'Ngambo ni Mwene' & Meru-Tanzania papers; Caplan, 'Daughters of Independence' (1997); Kithaka wa Mberia oral accounts."),

"Chaga & Pare Highlands - Kilimanjaro & Usambara": dict(
 lang:"Kichagga and Kipare (northeast highland Bantu of the Sabaki orbit)",
 pop:"Kilimanjaro, Taita Hills and Usambara ridges",
 history:"The Pare were among the earliest iron specialists of eastern Africa - archaeometallurgy dates Pare furnaces to the first millennium CE - while Chaga chiefdoms (Moshi's Mangi families) ran dense hill micro-states with trench irrigation and spring cults. Both groups sat astride the caravan road from the coast to the Great Lakes: Mangi Rindi of Moshi hosted missionary Krapf in 1848; the 1892 'Mang'i' wars and German conquest closed their sovereign era.",
 art:"Smelting-shaft ritual paraphernalia; Mangi court stools and leopard regalia; lyre music of the Kilimanjaro courts; ochre house-painting of the Taita/Pare hills.",
 traditions:"Iron-taboo observances around smith-shrines; spring-blessing rites; council-of-elders dispute settlement; harvest ngoma cycles.",
 economy:"Banana-coffee plots, iron tools historically, medicinal-forest products; Usambara agroforestry today.",
 links=[("Chaga Irrigation Terraces (Kilela)","kinship","One people split by administrative borders - Kilimanjaro and Pare share the same water-engineering grammar."),
        ("Meru & Mount Kenya (Kirinyaga)","kinship","Northeast-Bantu highland family: elder councils, first-fruits and mountain cosmologies run in parallel from the Tana to the Pangani."),
        ("Lamu Old Town","trade","Coast-to-highland caravan road: Pare and Chaga country was the gateway through which Swahili and Indian merchants reached the interior."),
        ("Aksum - Stelae & Sheba","trade","Northern anchor of the Nile-Ocean corridor whose southern terminus touched these highlands via the Pangani-Tana routes.")],
 sources:"Schmidt & Gowland on the archaeometallurgy of the Pare; Hall, 'The Tonga and Chaga'; Krapf journals (1848-53)."),

"Nyakyusa-Sonde & Ha Highlands": dict(
 lang:"Kyakyusa-Sonde and Kiha (northwestern Bantu, close to Bemba/Ha clusters)",
 pop:"Rungwe plateau, Mbeya highlands and the Kigoma lakefront",
 history:"The Nyakyusa practised a rare institution: sacred kingship founded on a national fire-drill - every new reign began by kindling a fresh flame and extinguishing the old - recorded by anthropologist H. E. Lambert (1930s-50s) and by oral dynastic lists stretching back some 300 years. The Ha of the western Rukwa/Kigoma shores kept terraced millet hills, island shrines on Lake Tanganyika and canoe-processions to royal graves; both polities buffered the great Bunya-Nyamwezi caravan roads.",
 art:"Fire-shrine regalia; royal drum ensembles; lacquered wood pipes; reed-boat ornament; scarification codes marking rank.",
 traditions:"National fire rekindling at accession; first-fruits millet libations; lake-canoe pilgrimages; graded age-initiation lodges (iwijisha).",
 economy:"Highland bananas, millet and coffee; Tanganyika fisheries; salt and iron trades down the lake axes.",
 links=[("Hehe & Matumbi Highlands","kinship","Southern Rift chiefdom belt - shared initiation lodges and sacred-fire concepts across the Rungwe escarpments."),
        ("Burundi - Karyenda & Royal Drum Sanctuary","kinship","Sacred-fire and drum-royalty parallels mark the same northwestern-Bantu political-religious family."),
        ("Kilwa Kisiwani Sultanate","trade","Ha and Tonga country fed the Rufiji-Luwegu ivory and iron roads toward Kilwa's markets."),
        ("Timbila Orchestras of Southern Mozambique","migration","Great Rift cultural spine: ceremony, xylophones and grade-systems travelled the highland chain from Rungwe to the Zambezi.")],
 sources:"Lambert, 'Land Between the Lakes' (1956); Kuper on Nyakyusa kingship; regional oral-history collections."),

"Rock-Hewn Churches of Lalibela": dict(
 lang:"Ge'ez (liturgical) and Amharic (spoken)",
 pop:"Lalibela town, Last'a highlands - active pilgrimage site",
 history:"Under King Gebre Mesqel Lalibela (r. c. 1181-1221) of the Zagwe dynasty, eleven churches were carved downward into red tuff - Bete Medhane Alem the largest monolithic church on earth - conceived, per the hagiography, as a 'New Jerusalem' after Muslim conquest halted Christian pilgrim access to the Holy Land. Portuguese envoys (1520s) wept at the sight; the churches never stopped being used: liturgy, chanting and Timkat processions continue eight centuries on.",
 art:"Monolithic negative-space carving; Ge'ez manuscripts and illuminated gospel books; bronze processional crosses; wall frescoes blending Coptic and highland styles.",
 traditions:"Timkat epiphany re-enactments with tabot processions; fasting-cycle calendars; debtera chant schools; priest-hereditary custodianship of each bet.",
 economy:"Pilgrimage-based crafts and lodging; highland barley and teff agriculture around the Last'a plateau.",
 links=[("Aksum - Stelae & Sheba","kinship","One Ethiopian Orthodox civilisation: Aksum's 4th-c. conversion flows straight into Lalibela's 12th-c. building zeal."),
        ("Simien Gondar Castles & Debre Berhan Selassie","kinship","Successive capitals of the Solomonic-Zagwe state tradition - rock, castle and fresco each phase of the same imperial faith."),
        ("Harar Jugol - The Alive City","trade","Highland-lowland axis: Christian and Islamic polities traded, warred and intermarried along the Awash corridor for a millennium."),
        ("Mogadishu & Barawa - Coastal Sultanates","trade","Ethiopian gold, civet and slaves reached the Somali-port caravanserais that shipped them to Aden and India.")],
 sources:"Getatchew Mekonnen, 'Lalibela: Faith from Stone' (2013); Francisco Alvares, 'Prester John's Narrative' (1540); UNESCO dossier (1978)."),

"Simien Gondar Castles & Debre Berhan Selassie": dict(
 lang:"Amharic with Ge'ez liturgical layer",
 pop:"Gondar city - Fasil Ghebbi royal compound (UNESCO 1979)",
 history:"Emperor Fasilidas (r. 1632-67) made Gondar the fixed capital of the Solomonic state, raising a walled royal enclosure - castles, banquet halls, stables and the library of Iyasu I - that looks like Camelot on the Horn. At nearby Debre Berhan Selassie (1622-32) the ceiling of flying cherub angels and the arcaded frescoes crown Gondarine painting's golden age; the city survived Mahdist raids, British bombardment (1941) and restoration campaigns since.",
 art:"Gondarine castle architecture fused with Axumite and Indo-Portuguese influences; angel-ceiling iconography; manuscript illumination; royal chronicle (Tarika Nagast) continuations.",
 traditions:"Timkat at Fasilidas' bath with full ceremonial immersion; royal-feast reenactments; cantorial schools; pilgrimage to Debre Berhan's healing saints.",
 economy:"Lake Tana fisheries and teff markets; university-city commerce; heritage tourism circuit.",
 links=[("Rock-Hewn Churches of Lalibela","kinship","Two architectural answers of one imperial Orthodoxy - carved-down stone and built-up castle."),
        ("Aksum - Stelae & Sheba","kinship","Solomonic ideology traced itself to Aksum; Gondar's kings were crowned with Aksumite regalia claims."),
        ("Harar Jugol - The Alive City","trade","The Christian-Muslim frontier wars and truces of the 16th century (Ahmed Graññ era) forged both cities' defensive walls."),
        ("Sudd Wetland & Nilotic Pastoralists","migration","The Blue Nile (Abbay) waters that feed Gondar's lakes continue south through the Sobat-Sudd system that sustains Nilotic peoples.")],
 sources:"Bahre Zinab, 'Ethiopian Castle Architecture'; UNESCO Gondar file (1979); James Bruce journals (1770s)."),

"Aksum - Stelae & Sheba": dict(
 lang:"Ge'ez (classical Ethiopic Semitic) - still the liturgical language",
 pop:"Tigray highlands - UNESCO World Heritage since 1980",
 history:"From the 1st century CE Aksum commanded Red Sea trade - its coins found from Aden to India - converting under Ezana (c. 330) to Christianity within a generation of Constantine. The granite stelae field (up to 24 m, quarried and raised without modern machinery), the claimed Ark at Zion Church, the tombs of kings and the Greek inscriptions of Adulis tie it to Rome, Persia and Saba. Judaism and Manichaeism also left traces; medieval glory faded after the Zagwe rise, but Aksum remained Ethiopia's spiritual axis mundi.",
 art:"Monolithic stelae with false-door and window carving; Ge'ez psalters; silver and gold processional tabots; obelisk-base reliefs showing ship and classical motifs (Indian Ocean contact).",
 traditions:"Timkat and Meskel cycles; the Kebra Nagast coronation liturgy; priestly Ark-custodial lineage; Saturday-and-Sunday dual sabbath practice.",
 economy:"Historically the gold-ivory-incense corridor of the Red Sea; today teff, sesame and pilgrimage trade.",
 links=[("Rock-Hewn Churches of Lalibela","kinship","Aksum's conversion produced Lalibela's stone faith - one continuous Ethiopian Orthodox civilisation."),
        ("Harar Jugol - The Alive City","trade","Aksumite-era ports and their Muslim counterparts (Zeila, Barawa) co-created the Red Sea exchange long before the Swahili boom."),
        ("Mogadishu & Barawa - Coastal Sultanates","trade","Ethiopian hinterland goods flowed to Somali-coast emporia whose sailors inherited Aksumite-era Red Sea navigation."),
        ("Laas Geel Cave Paintings","migration","Deep Horn-of-Africa continuity: cattle-keeping symbolism from Laas Geel's shelters recurs in Aksumite sacrificial and royal iconography.")],
 sources:"Munro-Hay, 'Aksum: An African Civilisation of Late Antiquity' (1991); Cosmas Indicopleustes (6th c.); UNESCO dossier (1980)."),

"Omo Valley Peoples": dict(
 lang:"Omotic, Cushitic and Nilo-Saharan families packed into one river valley (Dassanech, Suri, Karo, Mursi, Hamar...)",
 pop:"Lower Omo - ~200,000 people across many distinct cultures",
 history:"The lower Omo is a living laboratory of cultural diversity: flood-retention sorghum farming along the seasonal pulse, cattle-wealth duelling (Suri dong), lip-plates (Mursi/Dassanech) and body-paint aesthetics (Karo) each documented by ethnographers since the 1930s and by social-impact studies of the dam era. Human-origin fossils from Omo Kibish (~233 ka) make this the oldest known Homo sapiens landscape.",
 art:"Scarification geometries; kaolin-and-ochre body painting; beaded headbands encoding age; hair-clay sculptures; fighting-staff carving.",
 traditions:"Stick-duel marriage-season rites; bull-jump initiations (Hamar); age-set tree ceremonies; spirit-possession healing drums.",
 economy:"Flood-recession sorghum and cattle; fishing on Lake Turkana's southern arm; increasing wage and tourism pressures.",
 links=[("Turkana South Island & Chew Bahir","kinship","One cross-border pastoral-fishing world - Dassanech and Turkana share language ties, herds and raiding-truce cycles."),
        ("Somali Pastoral Nomads","migration","Eastern Cushitic pastoral frontiers met the Omotic valley cultures along the Ganale-Dawa-Omo arc."),
        ("Sudd Wetland & Nilotic Pastoralists","migration","The Nile's wetland peoples and the Omo's river peoples form a contiguous wetland-adaptation belt of ancient fisher-herders."),
        ("Laas Geel Cave Paintings","kinship","Green-Sahara cattle symbolism echoes in Omo cattle-centred ritual - the same Neolithic pastoral turn written on bodies instead of rocks.")],
 sources:"Tsonis ethnohistories; FRIT report (2010); UNESCO Lower Valley of the Omo dossier (1980)."),

"Harar Jugol - The Alive City": dict(
 lang:"Harari (South Semitic) plus Afar, Somali and Amharic quarters",
 pop:"Walled old city of 82 mosques and 102 shrines (UNESCO 2006)",
 history:"Founded as a Muslim emirate by the 10th century and fortified inside five gates and hundreds of alleys in the 16th century during the Somali-Ethiopian wars of Ahmed ibn Ibrahim al-Ghazi, Harar became renowned as the fourth holiest city of Islam - pilgrims once counted entering its walls as a hajj substitute. Emir Nur's walls, the hyena-feeding tradition and its book-and-coffee culture persisted through Ethiopian annexation (1887) largely intact.",
 art:"Inside-outside painted houses with geometric facades; Harari basket-weaving; silver filigree; qasida and harari singing with krar lyres; manuscript libraries of the Awamiyya school.",
 traditions:"Hyena feeding at the gates each dusk; shrine-pilgrimage circuits; youth coffee-house poetry duels; the celebratory market days of the seven quarters.",
 economy:"Historic caravan hinge for coffee, hides, incense and ivory from the Bale forests to Zeila's port; today heritage tourism and marketplace crafts.",
 links=[("Mogadishu & Barawa - Coastal Sultanates","kinship","One Ajuran-era Islamic urban network linked Harar's scholars to the Benadir ports' madrasas."),
        ("Somali Pastoral Nomads","trade","Oromo and Somali camel caravans delivered coffee, hides and ghee to the city gates weekly for centuries."),
        ("Aksum - Stelae & Sheba","trade","The highland-emirate frontier: Harar's walls answer Aksum-Gondar's castles across the same trade-and-war corridor."),
        ("Rock-Hewn Churches of Lalibela","kinship","Pilgrimage cities of twin faiths - each organised its civic calendar around feast-day processions.")],
 sources:"Baxter, 'Harari: Profile of an Ethnic Identity'; UNESCO dossier (2006); Richard Burton's First Footsteps in East Africa (1856)."),

"Konso & Dorze Weaving Highlands": dict(
 lang:"Koonso and Dorze (Hadamto) - Omotic highland languages",
 pop:"Konso woreda and the Dorze heartland near Lake Abaya / Chencha",
 history:"The Konso engineered one of Africa's oldest living landscapes: stone-walled terraces and generational grading of sons through the hora/gada-like system, recognised by UNESCO in 2011 as a cultural landscape. Dorze artisans - refugees from earlier expansions according to their own memory - rebuilt their identity around bamboo 'elephant houses' (domed huts up to 12 m tall) and the gabi cotton shawl, woven so tightly it doubles as blanket, baby-carrier and wedding gift.",
 art:"Waka funerary pole-carving (Konso); planter's poles marking grade ceremonies; gabi loom weaving with warp-patterned stripes; bamboo lattice architecture.",
 traditions:"Hora grade promotions; funeral pole-raising feasts; enset (false-banana) fermentation foodways; women-led market cooperatives.",
 economy:"Enset, coffee and potato terraces; weaving exports to Addis markets; heritage tourism on the southern rift-lakes road.",
 links=[("Omo Valley Peoples","kinship","Southern Ethiopian cultural continuum - Omotic farmers and lowland pastoralists exchanged grain, cattle and marriages along the same valleys."),
        ("Harar Jugol - The Alive City","trade","Highland textiles and coffee moved east through Harar's market web toward the Red Sea."),
        ("Chaga & Pare Highlands - Kilimanjaro & Usambara","kinship","Independent invention of intensive terracing and root-crop storage in two East African mountain zones - convergent highland ingenuity."),
        ("Buganda Royal Tombs at Kasubi","kinship","Organic-architecture mastery: reed domes of Kasubi and bamboo elephants of Dorze are sister achievements of living-material design.")],
 sources:"UNESCO Konso Cultural Landscape dossier (2011); Freeman and Ploss on Dorze weavers; Huitink on Konso terracing."),

"Buganda Royal Tombs at Kasubi": dict(
 lang:"Luganda (Bantu, Great Lakes zone)",
 pop:"Kampala hilltop - four Kabaka mausoleums (UNESCO 2001)",
 history:"Since 1882 the Kabakas of Buganda - Muwesaaka, Mutesa I, Daudi Chwa II and Edward Mutesa II - have been buried beneath one vast domed structure whose reed-and-thatch architecture replicates the royal household itself: the king's drums are said to contain the beat of the land. The Lukiiko council system, the 1894 protectorate bargain and the 1966 Mutesa crisis all radiate from this site; a 2010 arson fire destroyed the roofs, and master craftsmen rebuilt them using original techniques - a textbook case of intangible heritage saving tangible heritage.",
 art:"Barkcloth regalia; royal drum ensembles; reed-basket dome engineering; shield-and-spear iconography of the kabaka's standards.",
 traditions:"Royal drum-installation ceremonies; clan-based totem system; first-fruits offerings; mourning-cycle drum protocols.",
 economy:"Peri-urban Kampala horticulture; royal-estate crafts; pilgrimage and tourism visitation.",
 links=[("Mutuba Barkcloth of Buganda & Bunya","kinship","Kasubi's hangings are barkcloth - the monument and the craft are inseparable (UNESCO intangible listing 2005)."),
        ("Bakiga & Bakonzo - Mountains of the Moon","migration","Bakiga oral traditions remember serving as the kingdom's southern shield; the Bunya hills kept Buganda's barkcloth heartland stocked with mutuba."),
        ("Iteskari of the Jie & Karamojong - Beaded Crowns","trade","Cattle, beads and copper moved north-south between Karamoja herders and the Buganda court for centuries."),
        ("Burundi - Karyenda & Royal Drum Sanctuary","kinship","Drum-as-state doctrine spans the lakes: Buganda's royal drums and Burundi's karyenda both 'house' the soul of the kingdom.")],
 sources:"UNESCO nomination (2001); Rowe on Kasubi architecture; post-fire reconstruction reports (2011-15)."),

"Bakiga & Bakonzo - Mountains of the Moon": dict(
 lang:"Runyankole/Rukiga and Rukonzo (Bantu, NyORO empire heritage)",
 pop:"Kigezi terraces and Rwenzori foothills - among Africa's densest rural populations",
 history:"Bakiga ('people of the hills') settled the Kigezi terraces under Nyoro-influenced chiefdoms, resisting both Bunyoro expansion and later colonial resettlement; their steep-farm engineering is legendary. The Bakonzo of the Rwenzori keep the creator Kiwanuka and the 'mountains of the moon' - Ptolemy's Luna Montes named here 1,800 years ago - alive in oath-taking, warrior dance and the equatorial-glacier folklore that frames Africa's only true alpine range.",
 art:"Reed sculpture; bark-cloth and leather shields; the omukuturungi fiddle; terraced-field stone calligraphy visible from ridgelines.",
 traditions:"Birahi warrior dance; Rukonzo new-fire rites; clan-leopard totems; waterfall pilgrimage at Bakonzo shrines.",
 economy:"Terraced bananas, tea, arabica and Irish-potato belts; gorilla-trek gate revenues shared with communities.",
 links=[("Buganda Royal Tombs at Kasubi","kinship","All-Bantu Great Lakes court culture - shared clan systems, drum royalty and barkcloth prestige."),
        ("Rwanda - Intore Dance & Imigongo Art","trade","Cross-border cattle and iron markets knit Kigezi to the Ruanda-Volcanoes kingdoms; intermarriage spans the Virunga passes."),
        ("Iteskari of the Jie & Karamojong - Beaded Crowns","migration","The Western Rift population escalator: herders moved north-south along the same escarpment that carries Bakonzo terraces."),
        ("Thimlich Ohinga","kinship","Great Lakes terracing and stone-walling belong to one highland-agriculture frontier stretching from Migori to the Virungas.")],
 sources:"Behm-Thiesen on Kigezi; Rwenzori oral-history collections; national-park community heritage programmes."),

"Mutuba Barkcloth of Buganda & Bunya": dict(
 lang:"Luganda/Lusoga terms; the craft word 'olubugo' spreads across the lakes",
 pop:"UNESCO Intangible Heritage since 2005 - thousands of beating households",
 history:"For at least 700 years - long before imported cotton dominated - Ugandan makers peeled the inner bark of the Mutuba fig (Ficus natalensis), soaked it, and pounded it on grooved logs with wooden mallets until the fibres fuse into rust-red cloth that softens with washing. Kings draped it, brides wore it, the dead were wrapped in it; the 2005 UNESCO listing came as synthetic fabrics threatened the technique, and revival cooperatives in Buikwe and Iganga now supply museums, fashion houses and coronations.",
 art:"Mallet-rhythm beating performances; indigo-and-ochre dyeing geometry; barkcloth panel painting by contemporary Ugandan artists.",
 traditions:"Royal ceremonies robed in olubugo; burial wrapping; bride-cloth handover; apprentice beaters' graduation feasts.",
 economy:"Managed mutuba groves harvested without felling; craft-market value chains and export to diaspora ceremonies.",
 links=[("Buganda Royal Tombs at Kasubi","kinship","The tombs cannot exist without the cloth - roof hangings, shrine wraps and regalia are all olubugo."),
        ("Bakiga & Bakonzo - Mountains of the Moon","trade","Bunya and Busoga supplied bark and mallets along lakeside paths to the Kigezi and Rwenzori workshops."),
        ("Konso & Dorze Weaving Highlands","kinship","Two textile philosophies of the East African highlands - beaten bark vs. woven cotton - each UNESCO-inscribed within six years."),
        ("Rwanda - Intore Dance & Imigongo Art","trade","Court dress networks: barkcloth and raffia prestige moved through the same royal-exchange routes that carried Intore dancers.")],
 sources:"UNESCO ICH file (2005); Kiwanuka-Sempa on barkcloth; NTFP-network revival case studies."),

"Iteskari of the Jie & Karamojong - Beaded Crowns": dict(
 lang:"Ng'akarimo (Kalap/Teso-Jie cluster) - Southern Nilotic (Tatogo)",
 pop:"Karamoja sub-region - ~1 million speakers",
 history:"Karamojong, Jie, Teso, Nyangatura and Pian groups of northeastern Uganda trace descent through the same Kalenjin-related Nilotic node that also begat the Turkana and Marakwet; oral genealogies describe a slow push east off the Morungole highlands over the last three centuries. Married women's iteskari headdress-fringe - thousands of seed-glass and metal beads hanging to the shoulders - encodes clan, husband's age-set and ritual rank, functioning exactly like Maasai bead collars: wearable registers of life stages.",
 art:"Bead-threading geometry; hair-clay crests; leather-and-brass armature crowns; song-poetry of cattle raids and rain marches.",
 traditions:"Age-set promotions; healer initiations; ox-sacrifice at the ancestral fire; bride-wealth negotiation through bead-gifts.",
 economy:"Pastoral cattle-sheep-goat herds with drought-reserve goats; growing beekeeping and basket trades in Kaabong and Kotido.",
 links=[("Maasai Steppe - Kajiado & Narok","kinship","One Nilotic beadwork grammar: colour codes, wire techniques and rank meanings shared Karamoja-Turkana-Samburu-Maasai."),
        ("Turkana South Island & Chew Bahir","migration","Ancestral split in the same highland cradle - Morungole and Turkwell headwaters hold both peoples' origin stories."),
        ("Kalenjin Highland Runners - Eldoret & Uasin Gishu","kinship","Linguistic deep-kin: Southern Nilotic (Tatogo) roots link Kalenjin and Ng'akarimo speakers to a common pastoral ancestor-community."),
        ("Buganda Royal Tombs at Kasubi","trade","Cattle, beads and copper flowed south from Karamoja into Buganda's markets; northern regalia used southern brass wire.")],
 sources:"Dyson-Hudson, 'Karimo Social Organization' (1966); Otsula on iteskari; Karamoja community heritage surveys."),

"Rwanda - Intore Dance & Imigongo Art": dict(
 lang:"Kinyarwanda (Bantu, Great Lakes core)",
 pop:"Nationwide troupes; imigongo revived in the Eastern/Southern Province",
 history:"At the courts of the mwami kings, Intore ('the chosen') warriors danced with lion-mane headdresses and spears to drum orchestras whose tuned ingoma could mimic praise-names; the tradition survived monarchy's fall, exile and genocide, reconstituted as national heritage troupes. Imigongo - relief murals of raised cow-dung spirals and chevrons in black-white-ochre - came from the southeastern pastoralist provinces where royal cattle camps dried dung into panels, an artistic language unique to Rwanda.",
 art:"Intore choreography and regalia; imigongo spiral geometry; patterned showcase baskets; royal drum ensembles.",
 traditions:"Inheritance assemblies; bride-blessing songs (gusenga); umuganda communal work day (kept from precolonial roots); drum installation rites.",
 economy:"Smallholder tea-coffee cooperatives; Kigali creative-economy ateliers exporting imigongo and agaseke baskets.",
 links=[("Buganda Royal Tombs at Kasubi","kinship","Drum-royalty and clan-regalia culture of the interlacustrine kingdoms - Intore and Baganda court dance share a political aesthetic."),
        ("Burundi - Karyenda & Royal Drum Sanctuary","kinship","Rwandan and Burundian courts spoke the same verbal-art family; both installed royal drums as state souls."),
        ("Bakiga & Bakonzo - Mountains of the Moon","trade","Virunga border markets: Kigezi grain for Rwandan iron and cattle moved through the same passes that carried Intore troupes."),
        ("Iteskari of the Jie & Karamojong - Beaded Crowns","kinship","Parallel 'body-register' systems: imigongo-coded status and bead-coded rank both write biography onto material form.")],
 sources:"Van Avermaet & Maesen on Intore; Maeshall on imigongo; MINUBU heritage dossiers; UNESCO ICH nominations (Rwanda)."),

"Burundi - Karyenda & Royal Drum Sanctuary": dict(
 lang:"Kirundi (closest national-language pair with Kinyarwanda)",
 pop:"Gishora sanctuary hill, Ngozi province - UNESCO ICH 2014",
 history:"The karyenda - a great narrow-necked drum covered in spotted leopard skin - was literally the soul of the mwami's kingdom: struck only at accession, war-call and death, it 'held' the land's rhythm. Drum ensembles (mweza, rugiso, karyenda) danced in tuned conversation at royal courts until the monarchy ended in 1966; at Gishora, hereditary drum-keepers maintained the sanctuaries through civil conflict, and UNESCO inscribed the Burundian drum repertoire in 2014 as intangible heritage of humanity.",
 art:"Drum-carving and skin-tensioning; acrobatic dance of the abatimbo; royal praise-poetry; bead-and-ivory regalia of the mwami's court.",
 traditions:"Accession drum-striking; harvest thanksgiving dances; prince cattle rites; grave-side drum mourning.",
 economy:"Highland coffee and tea estates; artisanal drum-making and performance troupes as cultural livelihood.",
 links=[("Rwanda - Intore Dance & Imigongo Art","kinship","One verbal-arts and drum-state civilisation divided by colonial maps - Kirundi and Kinyarwanda remain mutually intelligible."),
        ("Buganda Royal Tombs at Kasubi","kinship","Interlacustrine drum royalty: Buganda's royal drums, Burundi's karyenda and Rwanda's ingoma all 'beat' the kingdom's identity."),
        ("Nyakyusa-Sonde & Ha Highlands","kinship","Sacred-fire and drum-accession parallels span the same northwestern-Bantu political-religious family."),
        ("Sukuma & Sukuru Drum Language","trade","Tonal drum speech and dance-guild organization spread through lakeside markets and labour-migration routes.")],
 sources:"UNESCO ICH 'Drum craftsmanship and culture in Burundi' (2014); Van Everaert on the mwami courts; Gishora sanctuary records."),

"Sudd Wetland & Nilotic Pastoralists": dict(
 lang:"Shilluk (Dhopa), Nilotic family; papyrus-craft lexicon unique to the marsh",
 pop:"Central Upper Nile - the Sudd is the world's largest wetland (~130,000 sq km)",
 history:"Herodotus already wrote of the Nile vanishing into a 'marsh' beyond Nubia; the Sudd's papyrus barriers and shifting channels created a civilisation of canoes: the Shilluk kingdom at Fashoda, whose divine kings (the reth Nyikang lineage) ruled rice-fisher-herder towns on levee islands, while the Acholi, Bari and Mundari kept cattle-camps on its fringes. The 19th-century Turco-Egyptian slaving expeditions (Baker, Gessi, Lupton) and the Jonglei Canal project (halted 1983) both made the Sudd a geopolitical hinge of the Nile.",
 art:"Single-trunk dugout carving with hippo-hide sails; ash-blue body scarring; stool-and-headrest carving; spear-work with royal insignia.",
 traditions:"Nyikang re-enactment festivals; buffalo-horn trophy display; canoes as dowry; leopard-skin chiefhood arbitration.",
 economy:"Fishing, sorghum on levees, cattle-island grazing; the wetland buffers floods for half the Nile Basin.",
 links=[("Dinka & Nuer Cattle Camps","kinship","One Nilotic pastoral-poetic world across the marsh - praise-name systems and camp initiations shared from Bor to Fashoda."),
        ("Omo Valley Peoples","migration","River-cultures of the Ethiopian-South Sudanese wetland belt - flood-recession farming appears on both sides of the border."),
        ("Aksum - Stelae & Sheba","trade","Nile-headwaters gold, ivory and exotic game partly fed Aksumite Red Sea exports through the Butiaba-Fashoda corridor."),
        ("Turkana South Island & Chew Bahir","kinship","Eastern Nilotic cousins reading water and pasture the same way - Turkana, Toposa and Shilluk share origin narratives.")],
 sources:"Howell on the Shilluk; Westropp on the Sudd; Herodotus Book II; UNEP-PAGE wetland histories."),

"Dinka & Nuer Cattle Camps": dict(
 lang:"Thuonjang (Dinka) and Naath (Nuer) - Eastern Nilotic with rich vowel tone",
 pop:"Upper Nile and Bahr el Ghazal - millions of pastoralists",
 history:"E. E. Evans-Pritchard's 1930s fieldwork made Nuer 'leopard-skin chiefs' and Dinka age-order famous: boys spend their youth in cattle camps, choosing ox-names by coat pattern that become lifelong praise-poems; ash-scarring marks men's passage; prophetic movements (the Ngai cult of the 1930s; later religious revivals) swept the camps during the civil-war decades. Despite upheaval, the cattle-camp pedagogy persists as the core initiation school of both peoples.",
 art:"Ox praise poetry (one of the world's richest oral genres); ash-blue chest scarification; amber-and-iron headrests; gourds with pyro-engraved clan lines.",
 traditions:"Cattle-camp initiations; ox-song duels; bridewealth in numbered cattle; peace-bond ceremonies mediated by leopard-skin chiefs.",
 economy:"Rainbow of herds - cattle, goats, fishing in the Toich and Sobat floodplains; sesame and groundnut gardens.",
 links=[("Sudd Wetland & Nilotic Pastoralists","kinship","Shared wetland-pastoral adaptation; Dinka and Nuer cattle routes follow the Sudd's seasonal margins."),
        ("Maasai Steppe - Kajiado & Narok","kinship","Nilotic age-set and cattle-poetics family stretched from the Bahr el Ghazal to the Chyulu hills - comparative linguistics confirms distant unity."),
        ("Iteskari of the Jie & Karamojong - Beaded Crowns","migration","Proto-Nilotic pastoral expansions southward left matching institutions (grades, raid ethics, praise-names) across the eastern belt."),
        ("Meru & Mount Kenya (Kirinyaga)","kinship","Contrast-and-contact case often taught together: Bantu highlanders and Nilotic herders negotiated pasture treaties along the same Rift frontiers.")],
 sources:"Evans-Pritchard, 'The Nuer' (1940); Deng, 'The Dinka of the Sudan'; Dartmouth Dinka Digital Archive."),

"Laas Geel Cave Paintings": dict(
 lang:"Somali with Arabic script layer; site name means 'pool of milk'",
 pop:"Granite shelters above the Wadi Tog-Wajale, 12 km NW of Hargeisa",
 history:"Documented by a French-Somaliland team (Gauthier, Hays & Duval) in 2002-05, Laas Geel's galleries carry naturalistic painted cows with lyre horns, handlers and dogs in ochre-black-white - dated stylistically to the Pastoral Neolithic, roughly 5,000-11,000 years BP, when the 'Green Sahara' let cattle graze these now-arid plateaus. It remains the oldest and best-preserved figurative rock art in the Horn, directly ancestral to Somali cattle-veneration idioms and to the camel culture that replaced cattle after aridification.",
 art:"Painted cattle iconography; white-disc sun symbols; superimposed later graffiti in Arabic and Somali; ochre-manganese pigment palettes.",
 traditions:"Local herders' reverence for the shelters; cattle-praise vocabulary echoing the painted poses; field-school visits by University of Hargeisa students.",
 economy:"Frankincense and goat herding around the wadi; heritage-tourism potential constrained by recognition politics.",
 links=[("Somali Pastoral Nomads","kinship","The paintings are the deep prologue of Somali pastoral poetry: the cattle-first worldview visible 6,000 years before the camel age."),
        ("Mogadishu & Barawa - Coastal Sultanates","trade","Horn interior-to-ocean exchange: hides, ghee and aromatics from these plateaus reached Benadir ports since antiquity."),
        ("Omo Valley Peoples","migration","Cattle-keeping cultures spread from the Danakil-Somali corridor into the lower Omo - shared bovine ritual grammar."),
        ("Harar Jugol - The Alive City","trade","Inland Harar-Zeila caravan routes pass within a few days' walk of Laas Geel's massif - ancient droving lanes continued as medieval trade roads.")],
 sources:"Hays & Duval, 'Laas Geel' (2004); regional rock-art surveys; British Museum comparison catalogues."),

"Mogadishu & Barawa - Coastal Sultanates": dict(
 lang:"Maay-Maay (Digil) and northern Somali; Swahili trade register; Arabic scholarship",
 pop:"Benadir coast - Mogadishu's Xamar Weyne old town and Barawa's port quarter",
 history:"Ibn Battuta visited Mogadishu in 1331 and praised its sultan; the city's marble tombstones, the Friday mosque and the harbour quay anchored a sultanate whose dhows carried porcelain, textile and horse trades from Aden to Calicut. Barawa (Brava) specialised in Benadir textiles and grain exports to Arabia; both fell within the Ajuran sphere (13th-17th c.), then Geledi, then Italian Somaliland's chartered companies. The 1990s wrecked much, yet old-town masonry, genealogies and dhow-yards survive.",
 art:"Carved-stone mihrabs and tomb epitaphs; baraka textiles; coastal dance with oud; sewn-plank dhow building.",
 traditions:"Sultanate investiture memories; sea-pilgrimage vows to local saints; camel-and-marine feast cycles; customary law (xeer) assemblies of the coast.",
 economy:"Historic grain, livestock, hide and banana exports to Gulf ports; today the largest fishing fleet in the Horn plus remittance finance.",
 links=[("Lamu Old Town","trade","One monsoon system: Benadir ports and Lamu shared dhow designs, Shirazi-lineage claims and the same import ceramics."),
        ("Harar Jugol - The Alive City","trade","Ethiopian highland coffee, hides and gold descended to Mogadishu and Barawa via Harar-Zeila feeder roads."),
        ("Somali Pastoral Nomads","kinship","City and bush are one clan universe - urban merchant houses keep pastoral branch genealogies and camel wealth."),
        ("Kilwa Kisiwani Sultanate","trade","Southern terminus pairing: Kilwa's gold-and-ivory south met Somali livestock-and-aromatics north in the same ocean ledger.")],
 sources:"Ibn Battuta Rihla (1331); Lewis, 'A Study of the Pastoral Economy'; Garretson on Barawa; UNESCO Somali tentative files."),

"Somali Pastoral Nomads": dict(
 lang:"Somali (East Cushitic) with Arabic and Latin scripts; camel-taxonomy vocabulary unmatched globally",
 pop:"Horn-wide - 20+ million speakers, majority pastoral or pastoral-derived",
 history:"Somalia's nomads drive the world's largest camel herd; their oral literature - gabay, geerar, buraanbur - was called by I. M. Lewis 'a nation of poets' because public life literally argues itself out in verse. Clan genealogies (dir/samaale divisions) recited for days structure everything from grazing rights to xeer blood-contract law; frankincense and myrrh from the northern highlands fed pharaonic, Roman and Indian temples for 4,000 years via the ports of Opone and Malao, ancestors of today's Bosaso and Berbera.",
 art:"Camel-praise poetry contests; aqal hut construction with bent saplings and mats; coastal laaro dance; turban and shash colour codes.",
 traditions:"Gu'/Dera rains calendar; household-cluster migration contracts; camel judging; xeer peacemaking assemblies under trees.",
 economy:"Livestock exports (sheep, camels, goats) to the Arabian market; frankincense, sesame and banana; diaspora remittances.",
 links=[("Laas Geel Cave Paintings","kinship","The pastoral continuum: cattle-first Neolithic of Laas Geel evolved into the camel-first pastoralism of historic Somalia."),
        ("Mogadishu & Barawa - Coastal Sultanates","trade","Every coastal city grew as the port-end of nomadic livestock and gum production; dual urban-pastoral households are classic."),
        ("Harar Jugol - The Alive City","trade","Oromo-Somali camel roads brought coffee and hides into Harar's gates weekly for centuries."),
        ("Lamu Old Town","trade","Northern Frontier: Somali camel caravans and Borana herds supplied Lamu's meat, hides and transport; intermarried clans persist.")],
 sources:"Lewis, 'Pastoral Democracy' & 'A Nation of Poets'; camel studies; UNFAO livestock-trade data."),

"Island of Mozambique": dict(
 lang:"Emwaka/Kishuafi Swahili variety, Portuguese layer, Makhuwa mainland",
 pop:"Coral spit linked by arched bridge - UNESCO World Heritage since 2011",
 history:"Known to Arab geographers as 'Msa'id' or Mobassa, the island was a monsoon entrepot long before Vasco da Gama landed in 1498; the Portuguese made it capital of 'East Africa' (Estado da India's Mozambique) until 1840, fortifying Sao Sebastiao (1580s) and sailing the carrack route to Goa. Its streets hold Manueline stonework, a Hindu temple built by Gujarati traders, an Arabian palace and the grim architecture of the slave-and-prazo trade that fed sugar islands and Brazil.",
 art:"Manueline carved windows and balconies; dhow-carving; capulana cloth geometry; forro music mixing Portuguese and Makhuwa rhythms.",
 traditions:"Feast of Sao Joao bonfires; dhow races; island lace-making; spirit-healing dances syncretising Catholic and Swahili ritual.",
 economy:"Historic gold-ivory-slave entrepot; today fishing, pearl shell, tourism and cashew-mainland trade.",
 links=[("Kilwa Kisiwani Sultanate","trade","Successor in the same southbound gold-and-ivory lane - Kilwa's fall handed the Sofala trade to the Island of Mozambique under cannon."),
        ("Timbila Orchestras of Southern Mozambique","kinship","One southern-Bantu festival world: Changana-Tsonga xylophone orchestras played at Island fairs and inland ceremonies alike."),
        ("Stone Town of Zanzibar","trade","Two capitals of the western Ocean at different times - cloves, slaves and cloth moved between their quays under Omani and Portuguese flags."),
        ("Makonde Plateau Sculpture","trade","Ebony and carving reached ocean buyers through Island and Ibo harbours long before the 20th-c. 'ebony road' to Nairobi.")],
 sources:"Newitt, 'The Portuguese in Mozambique'; UNESCO dossier (2011); 17th-c. island accounts."),

"Makonde Plateau Sculpture": dict(
 lang:"Makonde/Mwaru (Bantu, southeastern province) across the Rovuma in both Mozambique and Tanzania",
 pop:"Newala/Mocimboa plateau - tens of thousands of carvers and apprentices",
 history:"Makonde carvers descend from a masking culture (mapiko) that turned wood into ancestors: makishi masked dancers embody the dead, and the same log-cutting rite-of-passage defines manhood. When migrant workers carried ebony-carving into Tanzania's Oyster Bay world in the 1950s, the 'tanure' multi-body columns and lipiko spirit figures became one of Africa's most collected sculpture schools; the plateau itself keeps the ritual originals.",
 art:"Ebony and mpalo free-standing figures; mapiko masks with fibre beards; sandwood combs; body-scarification patterns reproduced in relief.",
 traditions:"Makishi masked funerals; initiation camps in the forest; women's liyonga dance; ancestral-offering shelves in each compound.",
 economy:"Timber-law-compliant carving cooperatives; export markets through Mtwara and Dar es Salaam galleries; remittances from Tanzanian workshops.",
 links=[("Mijikenda Kayas - Sacred Forest Highlands","kinship","Southernmost and northernmost nodes of one southeastern sculptural-masking province (Makonde vs. kaya/Donge masks)."),
        ("Island of Mozambique","trade","Ebony roads: Makonde blocks moved to Island and Ibo harbours for Indian and European buyers from the 16th century."),
        ("Timbila Orchestras of Southern Mozambique","kinship","Plateau and lowland share the Chopanga-Makonde festival calendar - masks, xylophones and grade dances travel together."),
        ("Kilwa Kisiwani Sultanate","trade","Interior ivory-and-timber supply zones behind Kilwa included proto-Makonde country; Swahili patrons commissioned early carving.")],
 sources:"Frahmeyer & Hjorto, 'Makonde Sculpture'; Bordignon on mapiko; UNESCO intangible files (Mozambique)."),

"Timbila Orchestras of Southern Mozambique": dict(
 lang:"Xichangana, XiTswa, Ronga (Tsonga cluster) plus Ndau",
 pop:"Inhambane-Maputo-Gaza belt and the Tsonga diaspora into South Africa",
 history:"Valley-keyed timbila orchestras - 4 to 30 wooden keys over gourd resonators, played in interlocking pairs by a lead and chorus - accompany the xitukula coming-of-age girls' school and funerary masquerades; the instrument family is part of the pan-African marimba province that reaches from Zimbabwe to Zanzibar. Colonial suppression failed; UNESCO inscribed the timbila craft and music in 2008, and the orchestras now anchor heritage festivals in Maxixe and Chibucune.",
 art:"Key-carving and tuning (each maker's voice); gourd-resonator selection; feather-and-bead regalia of the dancers; body-scarification matched to key patterns.",
 traditions:"Xitukula girls' initiation with orchestra nights; ancestral-calling drumming; beer-brewing women's guilds; hero-praise songs.",
 economy:"Cashew, citrus and fishing districts; instrument-maker cooperatives; festival tourism from Maputo to Vilanculos.",
 links=[("Hehe & Matumbi Highlands","trade","Southern Bantu ceremonial exchange - mask dances and xylophone forms crossed the Rovuma both ways for centuries."),
        ("Makonde Plateau Sculpture","kinship","One southeastern arts province: timber-carving, masking and orchestral dance share festival space from Newala to Inhambane."),
        ("Kilwa Kisiwani Sultanate","trade","Timbila hardwoods and coastal ceremonies flourished under the same Swahili-era trade umbrella that made Gaza and Sofala markets."),
        ("Island of Mozambique","trade","Portuguese-era chroniclers already described Tsonga-key orchestras entertaining at Island fairs - 400 years of continuous documentation.")],
 sources:"SIMA timbila archive; UNESCO ICH inscription (2008); ethnomusicological field recordings."),
}

count_inject = 0
for name, fields in EXTRA.items():
    key = '{ name:"%s"' % name
    i = src.find(key)
    if i == -1:
        print("NOT FOUND:", name); continue
    j = src.find('          tags:[', i)
    if j == -1:
        print("NO TAGS LINE:", name); continue
    block = []
    for fk in ("lang","pop","history","art","traditions","economy"):
        if fk in fields:
            val = fields[fk].replace('"', "'")
            block.append('          %s:"%s",' % (fk, val))
    lk = fields.get("links")
    if lk:
        items = []
        for to, ty, ev in lk:
            items.append('{ to:"%s", type:"%s", ev:"%s" }' % (to.replace('"',"'"), ty, ev.replace('"',"'")))
        block.append('          links:[\n            ' + ',\n            '.join(items) + '\n          ],')
    if "sources" in fields:
        block.append('          sources:"%s",' % fields["sources"].replace('"',"'"))
    src = src[:j] + "\n".join(block) + "\n" + src[j:]
    count_inject += 1
print("injected fields into", count_inject, "entries")

open(P, "w", encoding="utf-8").write(src)
print("stage 1 done, size:", len(src), "(was", orig_len, ")")
