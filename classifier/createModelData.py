import os

from classifier.models import plantInformation
from classifier.CNNkNN import constants as c
# RUN THIS
# python manage.py shell
# exec(open('classifier/createModelData.py').read())



    
plantInformation.objects.create(
    scientificName = 'Basella Alba',
    localName = ' Alugbati or Alabati',
    description = '"Glabrous annual or shortly lived perennial, succulent tangled twiner; stems much branched, 2-10 m long, sometimes almost leafless, greenish or reddish.  Leaf-lamina ovate to suborbicular, (2-) 5-15 cm long, (1.25-) 5-13.5 cm broad, acute or acuminate (less commonly obtuse), usually widely cordate at the base; lateral nerves 4-5 on either side; petiole (1-) 2.5-6.5 cm long.  Flowers white, rose or purplish, (3-) 4-5 mm long, in long-peduncled spikes, 2.5-15 (-25) cm long, usually unbranched (in African specimens at least) but branched in some cultivated forms.  Perianth fleshy, urceolate, somewhat saccate at bhe base; lobes short, ovate, about one-third the length of the tube, not opening.  Fruits ± 0.5 cm in diameter (4-7 x 5-10) mm (according to van Steenis), red, white or black; surface crinkly in the dry state" (Verdcourt, 1968; p. 2).',
    habitat = 'In Africa, "in thickets, forest edges, margins of cultivated land and swampy ground, frequently by rivers or streams; 0 (cultivated)-2450 m" (Verdcourt, 1968; p. 2).',
    propagation = 'Seed and locally by underground rhizomes  (Staples & Herbst, 2005; p. 173).',
    nativeRange = '"Precise native range not known, but is presumed to be Africa or somewhere in Asia.  Today it is cultivated as a food plant throughout warm regions of the world"  (Staples & Herbst, 2005; p. 173).',
    comments = 
    '''
    The growth of B. alba is limited by low temperatures, altitudes higher than 500 m and day/night temperature variations (PIER, 2017). Although it is cultivated worldwide up to 2600 m elevation and in tropical, subtropical and temperate areas, the species will grow best in hot, dry to humid climates and in areas below 500 m elevation (PROTA; 2017; ZipcodeZoo, 2017). The optimum mean annual temperatures for B. alba are 23 to 27°C, but it can tolerate a temperature range of 10 to 35°C. It does not tolerate frost and requires a minimum daytime temperature of 15°C. It does not do well if night temperature drops below 14°C, but will tolerate night temperatures occasionally falling below 10°C. It prefers an annual precipitation range of 2000 to 2500 mm, but will tolerate 700 to 4200 mm. The species prefers well-drained fertile sandy loam soils and full sun to light shade situations. It can grow in soils with a pH range of 5.5 – 7, but can tolerate 4.3 - 7.5. It tolerates poor soils and short periods of drought (Useful Tropical Plants, 2017). It is intolerant to salinity and standing water (PROTA, 2017).
    
    ''',
    control = 
    '''
    Cultural Control and Sanitary Measures
    <br>
    <br>
    Basella alba is a fast-growing vine that can be harvested about once a week by removing leaves and young stems. This will both encourage the production of more stems to harvest, keep the plants from taking over large areas (Useful Tropical Plants, 2017).
    <br>
    <br>
    Biological Control
    <br>
    <br>
    Plectonycha correntina has been proposed as the biological control of Anredera cordifolia in Argentina (Cagnotti et al., 2007). Since the plant hosts of this insect are restricted to the Basellaceae family, its use as a biological control for B. alba should be studied.
    ''',      
    icon = '',
)
plantInformation.objects.create(
    scientificName = 'Broussonetia papyrifera',
    localName = 'Lapnis',
    description = '''
    B. papyrifera is a medium to large deciduous tree. The crown is round and spreading. It is a hardy, fast-growing tree and under favourable conditions in a hot, moist climate can attain a height of 21 m and a diameter of 70 cm (Luna, 1996). Its stout, grey-brown, spreading branches are brittle and susceptible to wind damage. The branches are marked with stipular scars. Young branchlets are subtomentose and shoots are pubescent when young. The bark is light-grey, smooth, with shallow fissures or ridges. The stem, branches and petioles contain a milky latex (Luna, 1996).
    <br>
    <br>
    B. papyrifera has variable mulberry-like papery leaves. Some leaves are distinctly deep lobed, while others are unlobed. Several different shapes of leaves may appear on the same shoot. The leaves are alternate/subopposite, ovate, acuminate, dentate-crenate, their bases often oblique, scabrous above, with a woolly surface on the lower side. The leaves are 9.7 x 6.6 cm in size. The petioles are 3-10 cm long and the stipules 1.6-2.0 cm long (Parker, 1956).
    <br>
    <br>
    B. papyrifera is unisexual and dioecious. The male flower is 3.5-7.5 cm long, yellowish-white, with pendulous catkin-like spikes. The perianth is campanulate, hairy, 4-fid, and its segments are valvate. The female flowers are in rounded clusters in globose pedunculate heads about 1.3 cm in diameter. Persistent, hairy, clavate bracts subtend flowers. The fruit is shiny-reddish, fleshy, globose and compound with the achenes hanging on long fleshy stalks. The achenes are 1-2 cm long and wide.
        
    ''',
    habitat = '''
    B. papyrifera is native to East Asia with its warm and humid climate, with a temperature range of 0-40°C and with an annual rainfall of up to 2500 mm (Sheikh, 1993). It prefers a sub-humid warm, sub-tropical monsoon climate. The tree is remarkable for the variety of climates in which it can be grown, being hardy enough to survive in Europe. However its growth in cool climates is not as vigorous as in a warm, moist climate (Parker, 1956).
    <br>
    <br>
    B. papyrifera requires moist, well-drained soil and has been unsuccessful when tried on poor soil. It prefers sandy loams and light soils. Stiff clay and hard laterite soils prevent penetration of the roots to the sub-soil, resulting in stunted growth (Luna, 1996).
    
    ''',
    propagation = '''
    B. papyrifera is insect- and wind-pollinated, and can be grown from seed (sown and self-sown), stem cuttings, coppice and root suckers. Most plantations of this species in India and Pakistan are from self-sown seed, coppice or root suckers. It regenerates freely from seed in moist places where there is not already heavy plant cover, and seedlings can become a problem around mature trees. It can also be readily grown from cuttings, even in December (Parker, 1956). Intensive planting is avoided, however, because the wood is no longer commonly used on a commercial scale (Bokhari, 1973).
    <br>
    <br>
    Seeds are light and small, with about 540,000 seeds per kilogram. The germination rate of seeds is 50% and the seedling survival rate is 25-30% (Luna, 1996). Seed germination starts three weeks after sowing and is completed within four months. Green immature fruits treated with ethylene at 0.1% concentration for 48 hours at 18°C become ripe and can then be sown in nursery beds. Seeds collected in June usually show a tendency to be dormant for about one month after sowing, indicating a period of after-ripening. Seed dispersed by birds has been observed to germinate readily.
    
    ''',
    nativeRange = '',
    comments = '''
    B. papyrifera is a highly invasive species, becoming weedy and difficult to remove after its introduction. Its timber does not have high commercial value. Due to its excessive growth, it has become an agent of change in the whole ecosystem affecting native flora, human beings and causing economic losses.''',
    control = '''Plans to manually eradicate B. papyrifera have met with limited success because of gregarious vegetative reproduction and its invasive nature through seeds. Newly sprouted shoots from tree stumps and suckers are cut and burnt, being replaced by higher quality native timber trees, however this is not an effective method. The most common techniques are manual control methods, by hand pulling, hand picking, cutting, etc., but are not enough for complete management of the tree. Biological control has not yet been used for control of B. papyrifera, it may be the most appropriate way through selection and introduction of a suitable biological control agent.
    <br>
    <br>
    B. papyrifera has the capability of massive water consumption, a reason why they are more often seen around water, but also slowing the flow of water in channels and suppressing the growth of other plants. These channels not only provide water but also work as a dispersal source for the seeds. The huge canopy of the tree besides covering the outsized area provides shade over the closely growing trees and local shrubs, which creates competition for light, space and water.
    
    ''',      
    icon = '--',
)
plantInformation.objects.create(
    scientificName = 'Chromolaena odorata',
    localName = 'agonoi, huluhagonoi',
    description = '"Big bushy herb or subshrub with long rambling (but not twining) branches; stems terete, pubescent; leaves opposite, flaccid-membranous, velvety-pubescent, deltoid-ovate, acute, 3-nerved, very coarsely toothed, each margin with 1-5 teeth, or entire in youngest leaves; base obtuse or subtruncate but shortly decurrent; petiole slender, 1-1.5 cm long; blade mostly 5-12 cm long, 3-6 cm wide, capitula in sub-corymbose axillary and terminal clusters; peduncles 1-3 cm long, bracteate; bracts slender, 10-12 mm long; involucre of about 4-5 series of bracts, pale with green nerves, acute, the lowest ones about 2 mm long, upper ones 8-9 mm long, all acute, distally ciliate, flat, appressed except the extreme divergent tip; florets all alike (disc-florets), pale purple to dull off-white, the styles extending about 4 mm beyond the apex of the involucre, spreading radiately; receptacle very narrow; florets about 20-30 or a few more, 10-12 mm long; ovarian portion 4 mm long; corolla slender trumpet form; pappus of dull white hairs 5 mm long; achenes glabrous or nearly so"  (Stone, 1970; p. 581).',
    habitat = '''
    It grows in many soil types but prefers well-drained soils. It does not tolerate shade and thrives well in open areas (Ecoport).  Forms dense stands which prevent establishment of other species, both due to competition and allelopathic effects.  Requires disturbance to become established.  When dry, is a flashy fuel which promotes wildland fires. 
    <br>
    <br>
    "An opportunistic weed generally confined to forest edges and clearings.  It can form dense thickets in disturbed areas and may prevent recruitment of native plant species, thereby delaying successional processes.  Dense infestations can increase the intensity and frequency of fire, leading to further changes in the structure and composition of native plant communities.  C. odorata has the potential to colonise tropical and sub-tropical areas where annual rainfall exceeds 1000 mm per annum.  In its native habitat, the plant trives in tropical rainforest clarings and river flats, appearing early in the successional stage, rapidly establishing dense thickets and then gradually disappearing as the rainforest canopy closes over.  C. odorata can grow on most soils but prefers well-drained sites and will not grow in water-logged or saline soils.  Tree clearing for agriculture and other development appears to facilitate spread of the plant, which is quick to colonise roadsides, forest edges, plantations and pastures.  Agricultural districts, where original rainforest cover has been fragmented into small reserves and corridors, is particularly vulnerable to invasion."  (Csurhes & Edwards, 1998; p. 31-32).
    <br>
    <br>
    C. odorata can be considered as a major weed in all perennial crops of the humid tropics as well as in forestry. It also invades pastures. Its aggressiveness is much more serious in the Old World tropics where it is an exotic, rather than in its native Americas. C. odorata is found mainly in the humid part of the inter-tropical zone at elevations below 2000 m, in open secondary habitats such as cultivated lands, abandoned or neglected fields, forest clearings, wastelands, along forest trails, fence rows, roadsides and forest margins. Gils et al. (2006) found significant differences in four habitats invaded in KwaZulu-Natal, South Africa, concluding that spread along paths and lack of control in state forest mean that it is most abundant there, followed by eucalyptus plantations, and a low abundance in sugar cane fields and communal grasslands is thought to be due to fires and ground cover.
    
    ''',
    propagation = 'Wind-dispersed seeds. Seeds also cling to hair, clothing and shoes. The tiny seeds can occur as a contaminant in imported seed or on vehicles and machinery. Vehicle traffic can spread the seed along roads. Can propagate vegetatively from stem and root fragments. (Waterhouse & Mitchell, 1998; pp. 23-24).',
    nativeRange = '"Native from Florida through the West Indies and from Texas through Central and South America to Argentina (Howard 1989, Liogier 1997). It has been accidentally or deliberately introduced and has naturalized throughout much of the tropics"',
    comments = '''
    The aggressive nature and competitiveness of C. odorata in the Palaeotropics can be explained by the lack of host-specific natural enemies. In its native range in the Neotropics, it is attacked by a large number of arthropods (Crutwell, 1974; Gagne, 1977) and diseases (Elango et al., 1993; Barreto and Evans, 1994), reviewed by Crutwell McFadyen (1991). The most damaging and those that are promising potential biological control agents are given in the List of Natural Enemies, which includes successful introductions that have already been made. These natural enemies are either host-specific or only attack a narrow range of species related to C. odorata.
    
    ''',
    control = '''
    Physical: "Manual slashing, use of bush-cutter or tractor-drawn implements are commonly used methods of control. Slashing causes rapid regeneration unless followed by other methods to suppress this weed for an extended period. Manual weeding is labour intensive. Use of tractor drawn equipment is limited to areas that are accessible." (Ecoport)
    <br>
    <br>
    Chemical:  Chemical control using herbicides applied at the seedling stage or on early regrowth has given encouraging results. Triclopyr has proven to be the most effective. However, problems in herbicide use include (a) the high cost of the chemicals and their application, (b) ecological concerns and, (c) non-compatibility in many cropping and other environmental situations." (Ecoport)
    <br>
    <br>
    "Remove all seed and flower heads the, leaving the rest of the plants intact, spray with a herbicide, probably 2,4-D Amine plus Picloram (sold as Tordon in Australia). The 2,4-D will kill off the top growth and the picloram will move through the soil, killing the root system."  (Rod Randall, communication to Aliens list server, 30 October 2000).
    <br>
    <br>
    Biological: "Four insects have been released for biological control, the weevil Apion brunneonigrum, the fly Melanagromyza eupatoriella and two moths, Mescinia parvula and Pareuchaetes pseudoinsulata.  Of these, only the last has become established, fairly readily in Sri Lanka, Guam and other Micronesian islands, but with some difficulty in India and Sabah (Malaysia) and it has since spread unaided to the Philippines and Brunei.  It failed to become established in Thailand, Ghana, Nigeria and South Africa.  It has produced spectacular defoliation and death of many plants in Guam and striking but sporadic defoliation in Sri Lanka.  In India, populations have built up but damage has seldom been great.  Where established, it is heavily attacked by a range of predators and these are believed to have prevented successful establishment in several countries. 
    <br>
    <br>
    "The eriophyid mite Acalitus adoratus causes abnormal growth of the epidermal hairs on young leaves and stems of C. odorata.  Although it was never purposely introduced, it was observed in Thailand in 1984 and the Philippines in 1987, but had probably been present for some years.  It is also widespread in Java and Sumatra, but there is no information from other Indonesian islands.  It is present in Yap and Palau in the Caroline Islands and was observed on Guam in November 1993 (R. Muniappan pers. comm.)"  (Waterhouse, 1994; pp. 39, 41).  Waterhouse (1994, pp. 37-53) also lists natural enemies of the species, the biology of the more promising ones, and the status of biological control in individual countries.
    <br>
    <br>
    The biological control agent Pareuchaetes pseudoinsulata has been introduced into Guam, where it effectively defoliates pure stands. It is less successful in scattered plants and patches. It has also been introduced into Rota, Tinian, Aguijan, Palau, Kosrae, Pohnpei and Yap, but its present status on these islands is unknown. It has been introduced to Saipan where it seems to have been effective in reducing the problem to an occasional nuisance.
    <br>
    <br>
    "Another natural enemy, Cecidochares connexa (Tephritidae) has been established in Palau and Guam" (Muniappan and Nandwani, 2002; p. 15).
    
    ''',      
    icon = '---',
)
plantInformation.objects.create(
    scientificName = '''Leucaena leucocephala ''',
    localName = '''Ipil-Ipil''',
    description = '''"Shrub or small tree, up to 5 (rarely 10) m tall; leaves bipinnate, to 25 cm long; pinnae about 5 (4-9) pairs, up to 8-10 cm long; leaflets about 12 (11-17) pairs, about (7-) 9-12 mm long, 2-3.5 (-4) mm wide, opposite, lanceolate, acute; somewhat dull, grayish-green; flowers in globose, pedunculate heads, to nearly 3 cm thick; peduncles to 5-6 cm long; corolla and stamens white; calyx 2.5 mm long; petals linear; stamens 10, nearly 1 cm long, anthers hairy; ovary faintly pubescent at apex; pods clustered, linear, flat, 10-15 (-20) cm long, 1.8-2 cm wide, dark brown, beaked at apex, with about 20 (1825) seeds, these glossy brown, oval-oblong, flat, 6 mm long" (Stone, 1970; pp. 299-300).

    ''',
    habitat = ''' "Coastal heath- and scrubland.  This palnt is evergreen unless moisture is limited seasonally.  The shrub forms extensive and dense thickets displacing the original vegetation and reducing species richness.  The tree is deep-rooted and the taproot may grow rapidly, e.g. more than 2 m in 1-year-old plants.  It is a nitrogen-fixing species that increases soil fertility levels"  (Weber, 2003; p. 234).  "This thornless tree forms dense thickets, excluding all plants. It is grown for fodder, but unless severely grazed or controlled, it spreads rampantly throughout adjacent areas" (C.W. Smith, 1985; p. 193).  Generally favors limestone soils (although seems to do well on volcanic soils on Tahiti) and disturbed areas and is found in dry to mesic habitats up to 700 m.  It was deliberately broadcast on several war-disturbed islands after World War II. It also grows in severely disturbed wet areas but not as a dominant species. 
    <br>
    <br>
    In Fiji, "abundantly naturalized from near sea level to about 800 m along roadsides, in cultivated areas and in pastures, on dry river banks or open gravel banks in forest, often forming dense thickets"  (A.C. Smith, 1985; pp. 63-65).  In Hawai‘i, "naturalized and very common, sometimes forming the dominant element of the vegetation, in low elevation, dry, disturbed habitats, 0-350m" (Wagner et al., 1999; pp. 679-680). ''',
    propagation = ''' "Coastal heath- and scrubland.  This palnt is evergreen unless moisture is limited seasonally.  The shrub forms extensive and dense thickets displacing the original vegetation and reducing species richness.  The tree is deep-rooted and the taproot may grow rapidly, e.g. more than 2 m in 1-year-old plants.  It is a nitrogen-fixing species that increases soil fertility levels"  (Weber, 2003; p. 234).  "This thornless tree forms dense thickets, excluding all plants. It is grown for fodder, but unless severely grazed or controlled, it spreads rampantly throughout adjacent areas" (C.W. Smith, 1985; p. 193).  Generally favors limestone soils (although seems to do well on volcanic soils on Tahiti) and disturbed areas and is found in dry to mesic habitats up to 700 m.  It was deliberately broadcast on several war-disturbed islands after World War II. It also grows in severely disturbed wet areas but not as a dominant species. 
    <br>
    <br>
    In Fiji, "abundantly naturalized from near sea level to about 800 m along roadsides, in cultivated areas and in pastures, on dry river banks or open gravel banks in forest, often forming dense thickets"  (A.C. Smith, 1985; pp. 63-65).  In Hawai‘i, "naturalized and very common, sometimes forming the dominant element of the vegetation, in low elevation, dry, disturbed habitats, 0-350m" (Wagner et al., 1999; pp. 679-680). ''',
    nativeRange = ''' Belize, Guatemala and Mexico; cultivated and naturalized (GRIN). Through introductions now virtually pan-tropical. Widely planted and seeded in the Pacific region.''',
    comments = ''' Leucaena has been widely planted and seeded throughout the Pacific and is among the most prevalent invasive species. A serious problem in Tonga.
    <br>
    <br>
    Planting of this species is prohibited in Miami-Dade County, Florida (U.S.) (Hunsberger, 2001).
    <br>
    <br>
    Eradication project planned for the island of Santa Cruz, Galápagos Islands (Chris Buddenhagen, pers. com.). ''',
    control = '''
    Physical:  "Good forage in dry pastures but its toxicity is somewhat of a problem and it grows out of reach of livestock and shades out the understory.  Goats will control koa haole (An Peischel)" (Motooka et al., 2003).  "Difficult to control mechanically because the roots break when pulled"  (Englberger, 2009; p. 26).
    <br>
    <br>
    "La lutte mécanique est possible sur de grandes surfaces planes (gyrobroyage)" (Meyer, 2008; p. 24).
    <br>
    <br>
    Chemical: "Sensitive to foliar-applied triclopyr. Susceptible to soil applied tebuthiuron at 2 lb/acre and to cut-surface applications of picloram. Dicamba ineffective in cut-surface applications. Triclopyr ester applied basal bark and stump bark effective, 2,4-D in diesel and sometimes diesel alone effective in basal bark treatments" (Motooka et al., 2003).
    <br>
    <br> 
    "Triclopyr (Garlon 4) can be used as foliar application on young plants.  For older plants undiluted Garlon 4 can be applied to the cut stem"  (Englberger, 2009; p. 26).
    <br>
    <br>
    "La lutte manuelle (arrachage des plantules) associée à un traitement chimique (triclopyr ou dicamba) sur souches d’arbres coupés ou par injection dans les troncs est réalisable sur de petites surfaces" (Meyer, 2008; p. 24).
    <br>
    <br>
    Biological: An insect, the leucaena psyllid (Heterophylla cubana), damages but does not eliminate the plant. For a list of pests of leucaena, see the Ecoport web site.
    <br>
    <br>
    "Heteropsylla cubana, the leucaena psyllid was discovered in Hawaii in 1984. This psyllid was causing extensive defoliation of Leucaena leucocephala. Ranchers who relied on leucaena as fodder in marginal lands were concerned, and the Hawaii Department of Agriculture initiated a search for natural enemies of the psyllid in Trinidad and Tobago. Conservationists who considered leucaena a pest initially objected to efforts to control the psyllid, but as leucaena stands opened up, broomsedge (Andropogon virginicus) invaded the understory. Broomsedge provided fuel for more intense and extensive wildfires which threatened remaining pockets of native vegetation in lowland mesic areas. Eventually, opposition to control of the leucaena psyllid weakened, and Psyllaephagus yaseeni, a nymphal parasite of the psyllid, was released in Hawaii in 1987 and 1988"  (Smith et al., 2002).
    ''',      
    icon = ''' ---''',
)



plantInformation.objects.create(
    scientificName = '''Swietenia Macrophylla''',
    localName = '''Mahogany''',
    description = '''"Large tree; leaves 15-35 cm long; leaflets in 6-12 pairs, lanceolate, 7-15 cm long, 2.5-7 cm wide, inequilateral at base, acuminate at apex, petioluled, entire, coriaceous, glabrous; panicles 9-20 cm long; bracts and bracteoles orbicular or nearly so, deciduous; calyx cup 2-2.5 mm wide, lobes rounded; petals obovate to spatulate, 5-6 mm long, 2-3 mm wide; capsule ovoid, 12-15 cm long, 7-7.5 cm wide, acute to acuminate apically; seeds 7.5-8.5 cm long, the wing about twice as long as body, reddish brown."

    ''',
    habitat = ''' "Forests and forest edges.  A fast growing and shade tolerant tree that withstands pronounced periods of dry weather.  It establishes well in disturbed sites and in secondary forests, becoming the dominant species and will suppress native plants" 
    <br>
    <br>
    In Hawai'i (West Maui), widely naturalized in disturbed lowland mesic forest (Meidell et al., 1998; pp. 6-7). Moist forests (Wiggins & Porter, 1971; pp. 699-700). ''',
    propagation = ''' "Seed production is prolific and seeds are dispersed by wind.  The tree has some ability to sprout after cutting"  (Weber, 2003; p. 423).

    ''',
    nativeRange = ''' Southern Mexico to Peru and Brazil (Wiggins & Porter, 1971; pp. 699-700).''',
    comments = '''  Reported as possibly an invasive plant in the Galápagos Islands per Charles Darwin Research Station.''',
    control = '''
    Physical:  Hand pull or dig out seedlings and young plants.
    <br>
    <br>
    Chemical: Cut large plants and treat the stumps with herbicide (Weber, 2003; p. 423).
    ''',      
    icon = ''' ---''',
)
plantInformation.objects.create(
    scientificName = '''Muntingia Calabura''',
    localName = '''Jamaica Cherry-Gasagase''',
    description = '''" "Small tree with tiered slightly drooping branches with crowded distichous simple alternate strongly asymmetrical sticky-pubescent oblong acuminate obliquely subcordate thin serrulate leaves, soon wilting, 2.5-15 cm long, 1-6.5 cm wide; stipules linear, about 5 mm long, caducous, flowers bisexual, 1 or few in axils, on pedicels about 2-3 cm long; sepals 5 (rarely 6 or 7), each about 1 cm long, lanceolate-caudate, tomentose-hirsute; petals white, [or pink], broadly spathulate-deltoid, about 12-13 mm long, rotate, stamens about 75; filaments slender, distinct, 6 mm long, white; anthers small yellow; disc annular, around the ovary; hirsute; ovary stipitate, glabrous, 5-celled; stigma capitate, 5-riged; fruit 5-celled baccate, sub-globose, light red, 1-1.5 cm wide, sweet-juicy, with many small (1/2 mm) elliptic grayish yellow seeds, stigma persistent" (Stone, 1970; pp. 404-405).

    ''',
    habitat = ''' A pioneer species favoring disturbed areas. Seeds germinate only with light; plants can be shaded out by overtopping vegetation. In French Polynesia (Raiatea) naturalizing to 300 m (Welsh, 1998; p. 281). In New Caledonia, "est parfois planté dans les jardins" (MacKee, 1994; p. 49). 
    ''',
    propagation = ''' Fruits contain hundreds of tiny seeds. "The seeds are spread by birds and fruit bats, may build up to large seed banks under rainforest, and require filtered light for germination.  Seedlings are very delicate but grow rapidly, soon forming thickets the shade of which prevents further...germination." (Swarbrick, 1997; pp. 51-52).''',
    nativeRange = ''' Tropical Americas; also cultivated (GRIN).''',
    comments = ''' Reported to be moderately invasive on Nauru (Meyer, 2000; p. 99).''',
    control = '''
    Chemical: Stem injection with 50% Roundup in water. Possibly may be controlled by cut stump treatment with 50% Roundup® or by basal bark treatment with 10% Garlon® 600 in diesel oil. (Swarbrick, 1997; pp. 51-52).
    ''',      
    icon = ''' ---''',
)
plantInformation.objects.create(
    scientificName = '''Plectranthus Amboinicus''',
    localName = '''Mexican Mint''',
    description = '''"Sprawling and somewhat succulent herb to 1 m high, sometimes subligneous and prostrate at base, the branchlets ascending, densely spreading-hirsute; leaves petiolate, the petioles 1-4.5 cm long, densely pubescent, the blades fleshy, broadly ovate to suborbicular, rhombic, or reniform, 4-10 x 3-9 cm, rounded to truncate and then often long-attenuate at base, obtuse to rounded at apex, coarsely crenate to dentate at margin or entire toward base, densely appressed-pubescent above and beneath; vericils 10-20 (or more)-flowered, subglobose, arranged in terminal, spicate, densely pubescent inflorescences 10-20 cm long, the bracts 3-4 mm long, the pedicels slender, hirsute, to 5 mm long; calyx campanulate, 1.5-4 mm long, hirsute and glandular, the upper lip erect, broadly ovate-oblong, the other teeth narrow, acute; corolla pale blue or mauve to pink, 8-12 mm long, the tube declinate, 3-4 mm long, expanding distally, pubescent without, the upper lip to 4.5 x 3 mm, erect, puberulent, the lower lip to 5-6 x 4 mm, concave; filaments of stamens mostly fused into a tube around style; nutlets smooth, pale brown, about 0.7 x 0.5 mm"  (Smith, 1991; pp. 226-227).
    
    ''',
    habitat = ''' In Fiji, "from near sea level to about 250 m, cultivated and naturalized in rocky and sandy areas in woods and thickets" (Smith, 1991; pp. 226-227). In Tonga, "frequent as a waste-area and roadside weed" (Yuncker, 1959; p. 235).''',
    propagation = ''' Seed, rooting of stems. ''',
    nativeRange = ''' Not known but possibly southern tropical Africa, now widely cultivated (Smith, 1991; pp. 226-227).''',
    comments = ''' Invasive in the Virgin Islands where it forms dense carpets in shaded dry forest. (Fred Kraus, communication to Aliens listserver)''',
    control = '''If you know of control methods for Plectranthus amboinicus, please let us know.''',      
    icon = ''' ---''',
)
plantInformation.objects.create(
    scientificName = '''Pongamia Pinnata''',
    localName = '''Indian Beech''',
    description = '''"[Millettia pinnata] is a 25-75' tree with smooth bark and drooping branchlets. The leaves are odd-pinnately compound, with 3-7 ovate, broadly elliptic, or obovate leaflets, each 2.5-6.25" long and 1.5-3.5" wide, ther terminal one the largest. Pendent racemes of fragrant, 0.75" long, pinkish to lavender, pea-type flowers are produced [in Hawaii] mainly between October and January, though a few flowers may be present any time of the year. The woody, flat, elliptic-oval pods are indehiscent, 1.5-2" long and 0.75-1" wide, and usually contain a single seed." (A Tropical Garden Flora, p. 333)
    ''',
    habitat = ''' "Widespread in coastal areas and tidal streams from India across Asia to western Polynesia, as well as inland in northern Australia and New Guinea. . . ." (A Tropical Garden Flora, p. 333) 
    <br>
    <br>
    "It is rare in Samoa in littoral forest on 'Upolu (south coast) and Tutuila (south coast), and in coastal forest on the north side [sic] Ta'umacron;, reported from near sea level to about 100 m elevation." (Rainforest Trees of Samoa, p. 76)''',
    propagation = ''' (no propagation information known by PIER)''',
    nativeRange = ''' "Widespread in coastal areas and tidal streams from India across Asia to western Polynesia, as well as inland in northern Australia and New Guinea. . . ." (A Tropical Garden Flora, p. 333)
    <br>
    <br>
    native to China, Japan (Kyushu, Ryukyu Islands), Taiwan, Bangladesh, India, Sri Lanka, Andaman and Nicobar, Myanmar, Thailand, Vietnam, Brunei, Christmas Island, Indonesia (Java, Kalimantan, Lesser Sunda Islands, Sumatra), Malaysia, Philippines, Singapore, Indonesia (Irian Jaya, Papua New Guinea), Australia (Northern Territory, Queensland), Guam, Micronesia, Northern Mariana Islands (Tinian), Palau, Fiji, Samoa (GRIN accessed 20171018)
    ''',
    comments = ''' "One species [of Millettia], Millettia pinnata, is native to Polynesia. It was formerly considered to be in the genus Pongamia, which consisted only of this one species." (Rainforest Trees of Samoa, p. 74)
    <br>
    <br>
    cultivated in Hawaii (implied by inclusion in A Tropical Garden Flora, p. 333)
    <br>
    <br>
    "It is considered to be a useful timber tree in Fiji, where it is more common [PIER ed.: than in Samoa], but has no Samoan name or reported uses." (Rainforest Trees of Samoa, p. 76)''',
    control = '''If you know of control methods for Millettia pinnata, please let us know.''',      
    icon = ''' ---''',
)
plantInformation.objects.create(
    scientificName = '''Psidium Guajava''',
    localName = '''Guava''',
    description = '''"A shrub or small tree; bark smooth, light reddish-brown, with pubescent 4-angled young branches; leaves opposite, ovate-elliptic or oblong-elliptic, acute-acuminate, pubescent beneath, often rather brittle, prominently nerved, lateral nerves 10-20 pairs; blades mostly 7-15 cm long and 3-5 cm wide, rounded at base, dull green; flowers solitary or 2-4 together in leaf axils, rather large (2.5 cm wide); peduncle about 1-2 cm long, pubescent; calyx 4-5-lobed (anthesis, not before) about 6-8 mm long, petals white, 10-15 mm long, fugacious, usually 4 or 5, obovate, slightly concave, stamens numerous (c. 200-250), white, about as long as petals; style 10-12 mm long, stigma peltate, fruit globose, ovoid, or pyriform, whitish-yellow or faintly pink, sweet-sour pulpy, many-seeded, 2.5-10 cm long; pulp granular-juicy; seeds yellowish, reniform" (Stone, 1970; pp. 454-455).
    ''',
    habitat = '''"Guava grows on soils of all textures derived from most parent materials. Well-drained and poorly drained soils, soils with pH's from 4.5 to 9.4, mildly salty soils, and soils both rich and poor in basic cations are tolerated. Guava grows at near sea level in coastal environments up to 2,300 m in elevation in Ecuador (Morton 1987). It grows naturally in areas of Puerto Rico that receive from about 1000 to 3000 mm of mean annual precipitation. Guava withstands drought very well. The species is moderately intolerant of shade. It develops a broad, low crown if open grown, grows a more vertical crown with side shade, and becomes tall and spindly in intermediate crown positions. Saplings can endure a few years in the understory of low basal-area secondary forests. Guava survives the competition of weeds, grass, and brush well. Growth is benefited by root association with arbuscular mycorrhizal fungi (Samarao and Martins 1999).  This thin-barked species is easily top-killed by fire and is sensitive to frost (von Carlowitz 1991)"  (Wildland shrubs of the United States and its territories). 
    <br>
    <br>
    This evergreen tree reaches heights of 8 m. It invades disturbed sites and forms dense thickets. Cultivated in gardens but often escaped and naturalized where introduced.  Common on abandoned fields (C. W. Smith, 1985; p. 200). " A major problem in pastures, roadsides and forest planting, and is also common in plantations, but not in cultivation"  (Swarbrick, 1997; p. 18).  In Hawai‘i, "naturalized and often forming dense stands in disturbed dry, mesic, and wet forest, 15-1,220 m"  (Wagner et al., 1999; p. 972).  In Fiji, "An abundantly naturalized tree or shrub 1-10 m high from near sea level to about 800 m, often forming dense thickets in waste places, along roadsides, and in pastoral, arable, and plantation land"  (A. C. Smith, 1985; pp. 307-308).  In Niue, "a common or very common species in scrub and open secondary forest in most areas"  (Sykes, 1970; p. 131). In New Caledonia, "est vite devenu un fléau dans les pâturages. Planté à Lifou par Deplance (1864) et aujourd'hui souvent spontané aux îles Loyauté, où il est moins envahissant que sur la Grande-Terre" (MacKee, 1994; p. 106). In the Galápagos Islands, "common in the more mesic forests of the larger islands" (Wiggins & Porter, 1971; p. 708).''',
    propagation = ''' The seeds are dispersed by frugivorous birds as well as rats and feral pigs.  "The seeds are spread by birds and fruit bats and the plants regrow from stumps and buds along damaged roots."  (Swarbrick, 1997; p. 18) ''',
    nativeRange = ''' Tropical America, introduced early to Guam by the Spanish, thence to the Philippines and throughout Asia (Stone, 1970; pp. 454-455).''',
    comments = ''' A major invasive species in the Galápagos Islands.
    <br>
    <br>
    A problem in Hawai'i, the Marquesas (French Polynesia), New Caledonia and Fiji.
    <br>
    <br>
    Very invasive in Tonga, especially on 'Eua (Space & Flynn, 2001).
    <br>
    <br>
    Common, and in the future may well become even more widespread in the Cook Islands (Space & Flynn, 2002)
    <br>
    <br>
    The fruit is a host to fruit flies (Motooka et al., 2003).''',
    control = '''
    Physical:  " "Cattle tend to ignore the leaves except when they are under intensive grazing management and grazing very succulent forage; then they develop a craving for roughage.  Goats and sheep graze the leaves and strip the bark. Goats have been used to control guava at Kapapala Ranch on Hawai‘i (An Peischel)."  (Motooka et al., 2003).  "Controlled by cultivation.  Tolerant to fire and unpalatable to stock.  Small plants suppressed, but not killed, by slashing" (Swarbrick, 1997; pp. 28-29).
    <br>
    <br>
    Chemical: "Probably susceptible to: 1) foliar application of arboricides such as picloram, metsulfuorn-methyl, glyphosate, and triclopyr at standard rates and dilutions; 2) stem injections and cut stump application of the same herbicides; 3) soil applications of hexazinone, karbutilate, fluroxypyr and bromacil at standard rates" (Swarbrick, 1997; pp. 28-29). 
    <br>
    <br> 
    "Guava is sensitive to foliar applications of triclopyr, dicamba and 2,4-D at 1 lb/acre and to cut surface applications of concentrates of these herbicides; very sensitive to basal bark treatments of triclopyr ester and 2,4-D ester at 2% and 4% of product, respectively, in diesel or crop oil; very sensitive to soil-applied tebuthiuron at 2 lb/acre. Very sensitive to very-low volume basal bark applications of 20% triclopyr ester product in oil. A small-leafed shrubby form of guava appears to be tolerant of foliar applied herbicides but sensitive to tebuthiuron." (Motooka et al., 2003).
    ''',      
    icon = ''' ---'''
)


plantInformation.objects.create(
    scientificName = '''Syzygium Jambos ''',
    localName = '''Rose Apple''',
    description = '''"Trees 6-15 m tall, bark grayish brown, smooth, glabrous throughout.  Leaves thin, coriaceous, somewhat pendent, narrowly lanceolate, 10-23 cm long, 2.5-5 cm wide, principal lateral veins 10-20 pairs, 5-15 mm apart, submarginal vein irregular, apex long-acuminate, base cuneate, petioles 0.5-1 cm long.  Flowers in terminal, once-branched cymes ca. 2 cm long, peduncles 0.7-1.5 cm long, bracts 0.8-1 mm long; hypanthium funnelform, 7-10 mm long, narrowing into a short pseudostipe 3-4 mm long; sepals 4, fleshy, unequal, one pair 6-8 mm long, the other pair 4-6  mm long, glabrous or sparsely puberulent, persistent; petals 4, white to greenish white, orbicular to ovate-orbicular, concave, 12-20 mm long, caducous; stamens ca. 200, filaments creamy white, 10-50 mm long.  Berries whitish yellow to pinkish yellow, subglobose, 2-4 cm long, pericarp fleshy, 10-15 mm thick.  Seed usually 1, subglobose, 2-2.5 cm in diameter, testa closely coherent to cotyledons"  (Wagner et al., 1999; p. 975)
    <br>
    <br>
    "A tropical fruit tree up to 10 m tall.  The terminal inflorescence is showy and usually carries four whitish-green flowers on the outside of the crown.  Flowering can occur two or three times per year.  The fruits are whitish-green, rose scented, about 5 cm long and ripen over an extended period.  The dry, crisp fresh fruit is used to make jellies.  Fruit/seed can be produced following self-pollination" (Csurhes & Edwards, 1998; p. 58).
    ''',
    habitat = ''' This medium-sized deciduous tree forms dense thickets which shade out native species. It invades undisturbed forest.  The tree thrives under a variety of edaphic conditions but is most commonly found in wet lowland habitats up to about 500 m elevation in Hawai‘i (C. W. Smith, 1985; p. 186), to 100 m in French Polynesia.  In Fiji, "cultivated and occasionally naturalized in thickets and waste places from near sea level to an elevation of about 850 m"  (A. C. Smith, 1985; pp. 356-357). In New Caledonia, "cultivé à Koé en 1883, se rencontre aujourd'hui surtout à l'état spontané" (MacKee, 1994; p. 106). Moist uplands in the Galápagos Islands (McMullen, 1999; p. 85).
    <br>
    <br>
    "On the island of La Reunion in the Indian Ocean, S. jambos is considered to be the most ecologically important weed in the riverine areas of semi-dry riparian forest, where it has formed dense, tall, almost monospecific stands in the absence of human disturbance.  The plant is capable of invading undisturbed ecosystems and reducing their conservation values.  It readily invades disturbed rainforest." (Csurhes & Edwards, 1998; p. 58).''',
    propagation = ''' The fruit is dispersed by humans and perhaps feral pigs. 
    ''',
    nativeRange = '''Southeast Asia.''',
    comments = ''' A major invasive species in French Polynesia and other locations in the Pacific, the Galápagos Islands and the islands of Mauritius and La Réunion in the Indian Ocean.
    <br>
    <br>
    "Not widespread in Tahiti where it forms very dense but localized stands. However, the rose-apple has become highly invasive in the island of Nuku Hiva in the Marquesas in cloud forests up to 1000 m elevation. the rose-apple produces large fruits with are only dispersed by gravity (short-distance) in Tahiti in places where trees have been planted (usually at low elevation) and as the species needs a high humidity to grow it is only found near rivers. In Nuku Hiva, the fruits are eaten and actively dispersed by a giant endemic pigeon (Ducula galeata) over long-distances and up in the montane rainforests where the habitat seems more favorable" (Jean-Yves Meyer, pers. com).
    ''',
    control = '''
    Chemical: "Sensitive to picloram applied cut-surface and to glyphosate applied to drilled holes.  Good control with triclopyr applied basal bark and cut-surface"  (Motooka et al., 2003).
    ''',      
    icon = ''' ---'''
)





# plantInformation.objects.create(
#     scientificName = ''' ''',
#     localName = ''' ''',
#     description = ''' ''',
#     habitat = ''' ''',
#     propagation = ''' ''',
#     nativeRange = ''' ''',
#     comments = ''' ''',
#     control = ''' ''',      
#     icon = ''' ''',
# )




print('done')